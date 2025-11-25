#           __                   __                          __
#      ____/ /___ ______   ___  / /__  ____ ___  ___  ____  / /_
#     / __  / __ `/ ___/  / _ \/ / _ \/ __ `__ \/ _ \/ __ \/ __/
#    / /_/ / /_/ (__  )  /  __/ /  __/ / / / / /  __/ / / / /_
#    \__,_/\__,_/____/   \___/_/\___/_/ /_/ /_/\___/_/ /_/\__/
#
#                  Copyright (c) 2025 das element
'''
Documentation for the API for das element
Make sure to link the correct executable 'das-element-cli' in the manager.py
'''

import json
import os
import shutil
import subprocess
import sys

# Suppress traceback printing for cleaner CLI error messages
sys.tracebacklimit = 0

# This feature is available since version 1.1.6

# EXECUTABLE_CLI = '/path/to/das-element-cli_2.0.3_lin'
# EXECUTABLE_CLI = '/path/to/das-element-cli_2.0.3_mac'
# EXECUTABLE_CLI = '/path/to/das-element-cli_2.0.3_win.exe'
EXECUTABLE_CLI = os.getenv('DASELEMENT_CLI')

# EXECUTABLE_CLI_FULL = '/path/to/das-element-cli-full_2.0.3_lin'
# EXECUTABLE_CLI_FULL = '/path/to/das-element-cli-full_2.0.3_mac'
# EXECUTABLE_CLI_FULL = '/path/to/das-element-cli-full_2.0.3_win.exe'
EXECUTABLE_CLI_FULL = os.getenv('DASELEMENT_CLI_FULL')


def as_quoted_string(value):
    # wraps string into double quotes string
    return '"{}"'.format(str(value).strip(' "'))


def as_quoted_dict(value):
    return json.dumps(value)


def execute_command(arguments, cli_full=False):
    executable = EXECUTABLE_CLI_FULL if cli_full else EXECUTABLE_CLI
    command = [executable] + [str(argument) for argument in arguments]

    if not executable or not shutil.which(executable):
        raise Exception(
            'Please define path to Das Element CLI executable by setting the environment variables DASELEMENT_CLI and DASELEMENT_CLI_FULL'
        )

    if sys.version_info <= (3, 4):
        process = subprocess.Popen(command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        output, error = process.communicate()
        output = output.strip('\n')
        error = error.strip('\n')
    else:
        process = subprocess.run(command,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=False,
                                 check=False)
        output = process.stdout.decode('utf8', 'ignore').strip('\n')
        error = process.stderr.decode('utf8', 'ignore').strip('\n')

    returncode = process.returncode

    if returncode != 0:
        print('Argument: {}'.format(' '.join(command)))
        print('Returncode: {}'.format(returncode))
        print('Error:')
        print(output)
        print(error)
        print()
        raise Exception('Oh no ... something went wrong!')

    return json.loads(output)
