#!/bin/sh

export FLASK_APP=kept_you_waiting_huh/server/server.py
pipenv run python -m flask run
