#!/bin/bash

python -m pytest -q 2>&1 | tee explanations/pytest_error_log.txt

