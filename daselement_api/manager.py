#           __                   __                          __
#      ____/ /___ ______   ___  / /__  ____ ___  ___  ____  / /_
#     / __  / __ `/ ___/  / _ \/ / _ \/ __ `__ \/ _ \/ __ \/ __/
#    / /_/ / /_/ (__  )  /  __/ /  __/ / / / / /  __/ / / / /_
#    \__,_/\__,_/____/   \___/_/\___/_/ /_/ /_/\___/_/ /_/\__/
#
#                  Copyright (c) 2022 das element
'''
Documentation for the API for das element
Make sure to link the correct executable 'das-element-cli' in the manager.py
'''

import subprocess
import json
import sys

# This feature will be availabel in version 1.1.6
# For testing please use Daily Builds from May 23th onwards

EXECUTABLE = '/path/to/das-element-cli_1.1.6_lin'
# EXECUTABLE = '/path/to/das-element-cli_1.1.6_mac'
# EXECUTABLE = '/path/to/das-element-cli_1.1.6_win.exe'


def as_quoted_string(value):
    # wraps string into double quotes string
    return '"{}"'.format(value.strip(' "'))


def execute_command(arguments):
    command = [EXECUTABLE] + [str(argument) for argument in arguments]

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
        raise Exception("Oh no ... something went wrong!")

    return json.loads(output)
