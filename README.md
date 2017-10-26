```
@dmarcoux/grc

GitHub Release Checker
```

# Setup

*Docker (TODO)*

*Native*

1. Install [pyenv](https://github.com/pyenv/pyenv): `pacaur -S pyenv` (This is on Arch Linux. Others, refer to [pyenv's README](https://github.com/pyenv/pyenv/blob/master/README.md))
2. Install Python: `pyenv install $(cat .python-version)`
3. Install [pipenv](https://github.com/kennethreitz/pipenv): `pip install pipenv`
4. Install all dependencies of the project (including dev): `pipenv install --dev`
5. Work in the virtual environment: `pipenv shell`
