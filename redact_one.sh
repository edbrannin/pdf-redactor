#!/bin/bash
FILENAME=$(basename $1)
mkdir input output
cp $1 input/
python redact.py < input/$FILENAME > output/$FILENAME
open output/$FILENAME
cowsay Done
