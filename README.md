# GitHub Actions Tryout

Experimenting with trying to get some things working in GitHub Actions.

Tests should fail with Django 5.1, but succeed in 4.2 and 5.0.

### Running tests locally

Install `uv`. Then:

```shell
uv tool install tox --with-uv
```

Run tests across all environments:

```shell
tox
```

Or only one:

```shell
tox -e py312-django51
```
