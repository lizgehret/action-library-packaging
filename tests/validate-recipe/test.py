#!/usr/bin/env python

import unittest
import os.path
import subprocess
import sys
from pathlib import Path

def run(filepath):
    results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py', filepath])
    return results.returncode

class TestValidateRecipe(unittest.TestCase):

    # def test_basic(self):
    #     filepath = 'data/recipe.yaml'
    #     obs_exit_code = run(filepath)
    #     self.assertEqual(obs_exit_code, 0)

    def test_file_exists(self):
        filepath = sys.argv[0]
        file = Path(filepath)
        assert file.exists()

    def test_filepath_not_provided(self):
        results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py'])
        obs_exit_code = results.returncode
        self.assertNotEqual(obs_exit_code, 0)

    # def test_version_provided(self):
    #     pass

    # def test_name_provided(self):
    #     pass

if __name__ == '__main__':
        unittest.main()
