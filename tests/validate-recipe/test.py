#!/usr/bin/env python

import unittest
import subprocess

def run(filepath):
    results = subprocess.run(['bash', '../../bin/alp-1c8c84a3-validate-recipe.py'])
    return results.returncode

class TestValidateRecipe(unittest.TestCase):

    def test_basic(self):
        filepath = 'data/recipe.yaml'
        obs_exit_code = run(filepath)
        self.assertEqual(obs_exit_code, 0)

if __name__ == '__main__':
        unittest.main()
