#!/usr/bin/env python
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LANGUAGES = ['de']
EXCLUDE = ['env']


def get_command(language):
    command = ['python', 'develop.py', 'makemessages', '-l', language, '--no-location', '--no-wrap']
    for exclude in EXCLUDE:
        command.extend(['-i', exclude])
    return command


def run():
    for language in LANGUAGES:
        subprocess.call(get_command(language))


if __name__ == '__main__':
    run()