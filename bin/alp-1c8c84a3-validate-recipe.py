#!/usr/bin/env python

# TODO: validate that file exists
# TODO: Validate that filepath exists (?) -no b/c if filepath exists
# then it's assumed that the filepath exists as well...
# TODO: validate that file contains version & name

# import os.path
import sys
import pathlib

if __name__ == '__main__':
    filename = sys.argv[0]
    filepath = sys.argv[1]
    # os.path.exists(filepath)

    # Does the file exist
    file = pathlib.Path(filename)
    if file.exists():
        print(f'This is the name of the file: ${filename}')
    else:
        raise ValueError
    
    # Does the filepath exist
    path = pathlib.Path(filepath)
    if path.exists():
        print(f'This is the location of the file: ${filepath}')
    else:
        raise ValueError
