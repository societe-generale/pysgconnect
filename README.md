# pysgconnect
Python package to interact with SGConnect

## Install

You can install this package by using Pypi:

     ```shell
     pip install pysgconnect
     ```

## Usage

### Protect HTTP requests
```python
from pysgconnect import SGConnectAuth
from requests import Session

s = Session()
# Do not hardcode your credential directly in your scripts, use a secure Vault solution instead
client_id = 
client_secret =
s.auth = SGConnectAuth(client_id, client_secret, scopes=['myscope'], env='PRD')

r = s.get('https://api.foo.socgen')
```
