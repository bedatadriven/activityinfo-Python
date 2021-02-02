import csv
import os
import shutil
import time
import requests


class ExportDatabaseFormsResult:
    """Class to store data exported from ActivityInfo"""

    def __init__(self, header, records, job_id, database_id, resource_id=None):
        self.jobId = job_id
        self.databaseId = database_id,
        self.resourceId = resource_id,
        self.header = header
        self.records = records

    def to_dict(self):
        """Convert exported results to a list of dictionaries

        :return: A list of dictionaries. The keys are the column/field names.
        """
        return [dict(zip(self.header, record)) for record in self.records]

    def to_csv(self, filename, delimiter=',', quotechar='"'):
        """Write exported results to a CSV file

        :param filename: Full path of the file to be written to.
        :param delimiter: Character to use as the delimiter.
        :param quotechar: Character to use to quote non-numeric values.
        :return: The ``filename``.
        """
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(self.header)
            writer.writerows(self.records)

        return filename

    def __str__(self):
        msg = 'ExportDatabaseFormsResult object with {ncol} columns and {nrow} records'
        return msg.format(ncol=len(self.header), nrow=len(self.records))


def get_quantity_table(client, database_id, resource_id=None, record_filter=None, delete=True):
    """Export a database, folder, or form in long format.

    :param client: A :class:`Client` object.
    :param database_id: Database identifier (required).
    :param resource_id: Form or folder identifier (optional).
    :param record_filter: A formula that is applied to each form to filter the resulting records.
    :param delete: If True, then the temporary file on the local file system is deleted before the function returns.
    :return: A :class:`ExportDatabaseFormsResult` object.
    """
    if resource_id is None:
        parent_id = database_id
    else:
        parent_id = resource_id

    payload = {'type': 'exportDatabaseForms',
               'descriptor': {
                   'databaseId': database_id,
                   'folderId': parent_id,
                   'format': 'LONG',
                   'fileFormat': 'TEXT'
               }}

    if record_filter is not None:
        payload['descriptor']['filter'] = record_filter

    job_status = client.post_resource('resources/jobs', body=payload)

    while True:
        job_status = client.get_resource('resources/jobs/{job_id}'.format(job_id=job_status['id']))
        if job_status['state'] == 'completed':
            break
        if job_status['state'] != 'started':
            raise ValueError('Error exporting quantity table')
        time.sleep(2)

    download_url = '{0}/{1}'.format(client.base_url, job_status['result']['downloadUrl'])

    local_filename = download_file(client, download_url, job_status['result']['filename'])

    records = []
    with open(local_filename, encoding='utf-8') as f:
        header = f.readline().strip('\n').split(sep=u'\u001F')
        for line in f:
            records.append(line.strip('\n').split(sep=u'\u001F'))

    if delete is True:
        os.remove(local_filename)

    return ExportDatabaseFormsResult(
        header=header,
        records=records,
        job_id=job_status['id'],
        database_id=database_id,
        resource_id=resource_id
    )


def download_file(client, url, filename=None):
    """Download a file at a given URL

    Code inspired by https://stackoverflow.com/a/39217788.

    :param client: A :class:`activityinfo.client.Client` object.
    :param url: The URL where the file is located.
    :param filename: The name to be given to the file when written to the local file system. If this is not provided,
    then the name is taken from the end of ``url``.
    :return: The name of the file on the local file system.
    """
    if filename is None:
        local_filename = url.split('/')[-1]
    else:
        local_filename = filename

    with requests.get(url, auth=client.auth, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename
