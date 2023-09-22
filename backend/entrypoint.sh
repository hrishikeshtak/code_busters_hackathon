#!/usr/bin/env bash

echo "*************************************************"
python3 --version
echo "*************************************************"

export PYTHONPATH=$PWD:$PYTHONPATH
echo "PYTHONPATH=$PYTHONPATH"

echo "Starting API Server !!!"
echo python3 run-api.py
python3 run-api.py
