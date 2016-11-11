#!/usr/bin/env bash

# example of the run script for running the fraud detection algorithm with a python file,
# but could be replaced with similar files from any major language

# I'll execute my programs, with the input directory paymo_input and output the files in the directory paymo_output

pip install 'pandas>=.0.18.1,<0.18.2'
pip install networkx

python ./src/antifraud.py
