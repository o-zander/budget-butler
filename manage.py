#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budgetbutler.settings.production')
    os.environ['PATH'] += os.pathsep + os.path.join('app', 'vendor', 'node', 'bin')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
