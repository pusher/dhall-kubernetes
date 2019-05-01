#!/usr/bin/env python3
#
# Typecheck and resolve all Dhall files in the ./default directory.
#
# Exit with 1 if at least one file fails to check.
#
# Some files are ingnored because they have existing errors.

import sys
from glob import glob
from subprocess import run, DEVNULL, PIPE

# We skip tests for the following set of files
ignored_failures = {
}

default_files = glob('./defaults/*.dhall')
failure_files = set()
for default_file in default_files:
    if default_file in ignored_failures:
        print('Skipping {}'.format(default_file))
        continue
    print('Checking {}'.format(default_file))
    cmd = 'dhall resolve <<< {file}'.format(file=default_file)
    result = run(cmd, shell=True, executable='bash', stdout=DEVNULL, stderr=PIPE)
    if result.returncode != 0:
        print(result.stderr.decode('utf-8'))
        failure_files.add(default_file)

if len(failure_files) > 0:
    print('The following files failed to check:')
    for failure_file in failure_files:
        print('  ' + failure_file)
    sys.exit(1)
