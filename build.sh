#!/usr/bin/env bash

set -o errexit # exit on error

python pip install -r requirements

python manage.py collectstatic --no-input
python manage.py migrate
