#!/usr/bin/env python

# TODO: validate that file exists
# TODO: Validate that filepath exists
# TODO: validate that file contains version & name

# import os.path
import sys
import pathlib
import yaml

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

    # YAML file parsing
    recipe = open('../tests/validate-recipe/data/recipe.yml')
    parsed_recipe = yaml.load(recipe, Loader=yaml.FullLoader)

    # Does the file contain a version
    if parsed_recipe.get('version') == None:
        raise ValueError
    else:
        print(parsed_recipe.get('version'))
    
    # Does the file contain a name
    if parsed_recipe.get('name') == None:
        raise ValueError
    else:
        print(parsed_recipe.get('name'))
