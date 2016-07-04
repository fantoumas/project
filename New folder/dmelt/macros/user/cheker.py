#!/usr/bin/env python

"""This program does a syntax check on Python files.

use -r or --recursive to delve into subdirectories
(default is to only examine current dir)

use -c or --continue to keep going after an error has been found.

Copyright 1999 Preston Landers <planders@deja.com>"""

import os, sys, string, traceback, commands, getopt

def get_files_to_examine(recursive = None):
    """returns a list of paths to Python files to be checked.  If
       recursive is set, then will delve into subdirs."""

    if recursive:
        find_cmd = 'find . -name \*.py'
    else:
        find_cmd = 'find . -maxdepth 1 -name \*.py'

    status, output = commands.getstatusoutput(find_cmd)
    if status:
        print output
        print "Find failed...?"
        raise SystemExit(1)

    files = string.split(output, "\n")

    return files

def examine_files(python_files, err_continue = None):
    ### do the test
    for python_file in python_files:
        file = open(python_file).read()

        ### this whole try: except: block is neccesary if
        ### you want to be able to continue after errors
        try:
            compile(file, python_file, "exec")
        except:
            exception, msg, tb = sys.exc_info()
            print "%s:  %s: %s" % (python_file, exception, msg)
            traceback.print_tb(tb)
            if not err_continue:
                print "ABORTING"
                raise SystemExit(1)
        else:
            print "%s: GOOD" % python_file

        ### this is what I would use if I wanted to see exactly
        ### where the error occured (each error will halt program)
        # compile(file, python_file, "exec")

if __name__ == "__main__":
    recursive = None  # assume not recursive
    err_continue = None  # assume break on error
    try:
        options, args = getopt.getopt(sys.argv[1:], 'hrc',
        ["help", "recursive", "continue"])
    except:
        print "Unrecognized option."
        print __doc__
        raise SystemExit(1)

    for option_name, option_value in options:

        if option_name in ["-h", "--help"]:
            print __doc__
            raise SystemExit(0)

        elif option_name in ["-r", "--recursive"]:
            recursive = 1

        elif option_name in ["-c", "--continue"]:
            err_continue = 1

    files_to_examine = get_files_to_examine(recursive)

    examine_files(files_to_examine, err_continue)

    raise SystemExit(0) # success
