# activityinfo-Python
A Python package with an API client for [ActivityInfo](https://www.activityinfo.org) version 4.

## Usage

Create a Python virtual environment in the project root:

```commandline
python3 -m venv venv
```

Activate the virtual environment:

```commandline
source venv/bin/activate
```

Install the module's requirements using `pip`:
```commandline
python3 -m pip install -r requirements.txt 
```

Start the Python 3 shell:

```commandline
python3
```

Load the module and get a JSON of the databases in your account:
```python
from activityinfo import Client
client = Client("<your API token>")
dbs = client.get("databases")
# 'dbs' is a JSON object with the list of databases in your account
```

See also the 
[help article on API tokens](http://help.activityinfo.org/m/84880/l/1333305-using-an-api-token-to-authenticate-with-activityinfo) 
in the ActivityInfo user manual.

When you're done, deactivate the virtual environment:
```commandline
deactivate
```

## License

The code in this Python package is released under the MIT license.
See the [LICENSE](LICENSE) file for the full license.
