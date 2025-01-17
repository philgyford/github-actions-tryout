# GitHub Actions Tryout

Experimenting with trying to get some things working in GitHub Actions.


### Running tests locally

Install `uv`. Then:

```shell
uv tool install tox --with-uv
```

Run tests across all environments:

```shell
tox
```

### Results

Tests should fail with Django 5.1, but succeed in 4.2 and 5.0:

```
  py311-django42: OK (1.74=setup[1.44]+cmd[0.29] seconds)
  py311-django50: OK (0.84=setup[0.56]+cmd[0.28] seconds)
  py311-django51: FAIL code 1 (0.83=setup[0.55]+cmd[0.28] seconds)
  py312-django42: OK (0.93=setup[0.62]+cmd[0.30] seconds)
  py312-django50: OK (0.85=setup[0.57]+cmd[0.28] seconds)
  py312-django51: FAIL code 1 (0.87=setup[0.58]+cmd[0.29] seconds)
  evaluation failed :( (6.10 seconds)
```

However, running via GitHub Actions, it marks all environments as failing.

It seems that each environment is running tests across all three Django,
versions and, because one of them fails, it marks the environment as having
failed.

I think this is because there's no way to configure
[tox-gh-actions](https://github.com/ymyzk/tox-gh-actions) to set the
`DJANGO` environment variable for GH Actions using `pyproject.toml` natively.

If we comment out all the tox stuff from `pyproject.toml`, and move
`tox_unused.ini` to `tox.ini` then the GH Actions tests work as expected.

So, giving up on tox + GH Actions configuration using `pyproject.toml` for now.
Maybe it will work with future updates to tox-gh-actions.

I did also look at [tox-gh](https://github.com/tox-dev/tox-gh) but couldn't see
how to set env vars how we want using that either.
