#!/usr/bin/env python

import sys
import pathlib
import yaml

if __name__ == '__main__':
    filepath = sys.argv[1]
    
    # Does the filepath exist
    path = pathlib.Path(filepath)
    if not path.exists():
        raise ValueError('filepath not found')

    # YAML file parsing
    with open(filepath) as recipe:
        parsed_recipe = yaml.load(recipe, Loader=yaml.FullLoader)

    # Does the file contain the version key
    if parsed_recipe['version'] == None:
        raise ValueError('version value not added')
    
    # Does the file contain the name key
    if parsed_recipe['name'] == None:
        raise ValueError('name value not added')
