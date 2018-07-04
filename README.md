# bcio

A project towards blockchain interoperability.

## Dependencies

This project is built with:

- [Python](https://www.python.org/)
- [Sqlite3](https://www.sqlite.org/index.html)
- [Web3.py](https://web3py.readthedocs.io/en/stable/) for Ethereum support
- [mcrpc](https://github.com/coblo/mcrpc) for MultiChain support
- [python-bitcoinrpc](https://github.com/jgarzik/python-bitcoinrpc) for Bitcoin support

## Setup

### General dependencies

Install dependencies using your favourite package manager:

```
# pacman -S python sqlite
```

> Note: The project is built with `python` version `3.6.5` and `sqlite` version `3.24.0`.

### Python dependencies

#### With virtual environment

Create a virtual environment within the project (for `python >= 3.3`):

```
$ python -m venv venv
```

Activate virtual environment:

```
$ source venv/bin/activate
```

Install dependencies:

```
(venv) $ pip install web3 mcrpc python-bitcoinrpc
```

Deactivate virtual environment:

```
(venv) $ deactivate
```

#### Without virtual environment

Install dependencies:

```
$ pip install --user web3 mcrpc python-bitcoinrpc
```
