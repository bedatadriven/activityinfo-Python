# activityinfo-Python
A Python package with a API client for [ActivityInfo](https://www.activityinfo.org) version 4.

## Usage

Create a Python virtual environment in the project root:

```commandline
python3 -m venv venv
```

Activate the virtual environment:

```commandline
source venv/bin/activate
```

Start the Python 3 shell:

```commandline
python3
```

Load the module and get a JSON of the databases in your account:
```python
from activityinfo import Client
client = Client("you@example.com", "your password or API token")
dbs = client.get("databases")
# 'dbs' is a JSON object with the list of databases in your account
```
