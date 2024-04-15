# pysgconnect

Python package to interact with SGConnect

## Install

You can install this package by using Pypi:

```sh
pip install pysgconnect
```

## Usage

### Protect HTTP requests

```python
from pysgconnect import SGConnectAuth
from requests import Session

session = Session()
# Do not hardcode your credential directly in your scripts, use a secure Vault solution instead
client_id = 
client_secret =

session.auth = SGConnectAuth(client_id, client_secret, scopes=['myscope'], env='PRD')

request = session.get('https://api.foo.socgen')
```

### Development

```sh
pip install -e .
```
