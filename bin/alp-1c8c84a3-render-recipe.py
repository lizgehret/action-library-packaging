#!/usr/bin/env python

import pathlib
import sys


def parse_inputs(inputs):
    if len(inputs) != 3:
        raise Exception('todo')

    q2_recipe_fp, conda_recipe_fp = inputs[1:]
    q2_recipe_path = pathlib.Path(q2_recipe_fp)
    conda_recipe_path = pathlib.Path(conda_recipe_fp)

    if not q2_recipe_path.exists():
        raise Exception('todo')

    if not conda_recipe_path.parent.exists():
        raise Exception('todo')

    return (q2_recipe_path, conda_recipe_path)


def main(q2_recipe_fp, conda_recipe_fp):
    # TODO: do something with the q2_recipe_fp!
    with open(conda_recipe_fp, 'w') as fh:
        fh.write('')


if __name__ == '__main__':
    q2_recipe_fp, conda_recipe_fp = parse_inputs(sys.argv)

    main(q2_recipe_fp, conda_recipe_fp)
