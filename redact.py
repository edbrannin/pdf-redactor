#;encoding=utf-8
# Example file to redact Social Security Numbers from the
# text layer of a PDF and to demonstrate metadata filtering.

import re
from datetime import datetime

import pdf_redactor

## Set options.

options = pdf_redactor.RedactorOptions()

# Redact things that look like social security numbers, replacing the
# text with X's.
options.content_filters = [
        (re.compile(r'.*'), lambda m: '')
]

# Perform the redaction using PDF on standard input and writing to standard output.
pdf_redactor.redactor(options)
