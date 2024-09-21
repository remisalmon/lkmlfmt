#!/usr/bin/env bash

python -m venv venv

source venv/bin/activate

python -m pip install -U pip setuptools build
python -m build
