# infcommon documentation

[![CI](https://github.com/aleasoluciones/infcommon/actions/workflows/ci.yml/badge.svg)](https://github.com/aleasoluciones/infcommon/actions/workflows/ci.yml)
![Python versions supported](https://img.shields.io/badge/supports%20python-2.7-blue.svg)



## How to set up your local development environment

1. Run `source dev/env_develop`
2. Run `dev/setup_venv.sh`

## How to run the tests
Run `dev/all-tests.sh`

## Logger documentation
* **VERY IMPORTANT**: If you want, you can set SENTRY_DNS environment variable to use Sentry as logger handler.
* For disabling the logs, set the environment variable TEST_MODE (e.g. when executing the tests we don't want logs to be printed or breaking the execution). This is currently done in env_develop.
