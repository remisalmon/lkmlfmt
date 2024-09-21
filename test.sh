#!/usr/bin/env bash

python -m venv venv

source venv/bin/activate

python -m pip install -U pip setuptools
python -m pip install .
python -m unittest discover tests/
