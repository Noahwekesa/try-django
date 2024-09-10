#!/usr/bin/env bash

set -o errexit # exit on error

python3 pip install -r requirements

python3 manage.py collectstatic --no-input
python3 manage.py migrate
