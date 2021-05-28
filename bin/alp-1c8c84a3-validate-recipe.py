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

    # Does the file contain any disallowed keys
    allowed_keys = ['version', 'name', 'type', 'build_cmd', 'requirements', 'test']
    for key in parsed_recipe.keys():
        if key not in allowed_keys:
            raise ValueError(f'invalid key added. allowed keys are: {allowed_keys}')

    # Does the file contain the version key and a value
    if parsed_recipe['version'] == None:
        raise ValueError('version value not added')
    
    # Does the file contain the name key and a value
    if parsed_recipe['name'] == None:
        raise ValueError('name value not added')

    # Does the file contain the type key and a valid value
    allowed_types = ['plugin', 'interface', 'utility']
    if parsed_recipe['type'] not in allowed_types:
        raise ValueError(f'valid type value not added. allowed values are: {allowed_types}')
