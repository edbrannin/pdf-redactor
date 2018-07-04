#!/usr/bin/env bash

mkdir input output
[ -d _env ] || virtualenv _env
. _env/bin/activate
pip install -r requirements.txt

for input in $(ls input/); do
    echo $input
    python redact.py < input/$input > output/$input
done

cowsay "Done"
