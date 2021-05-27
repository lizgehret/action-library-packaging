#!/usr/bin/env python

import unittest
import subprocess

def run(filepath):
    results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py', filepath])
    return results.returncode

class TestValidateRecipe(unittest.TestCase):

    def test_basic(self):
        filepath = '../../tests/validate-recipe/data/recipe-basic.yml'
        obs_exit_code = run(filepath)
        self.assertEqual(obs_exit_code, 0)

    def test_version_not_provided(self):
        # No version key present
        obs_exit_code = run('../../tests/validate-recipe/data/recipe-noversion-key.yml')
        self.assertNotEqual(obs_exit_code, 0)        

        # Version key present, no value
        obs_exit_code = run('../../tests/validate-recipe/data/recipe-noversion-value.yml')
        self.assertNotEqual(obs_exit_code, 0)

    def test_name_not_provided(self):
        # No name key present
        obs_exit_code = run('../../tests/validate-recipe/data/recipe-noname-key.yml')
        self.assertNotEqual(obs_exit_code, 0)

        # Name key present, no value
        obs_exit_code = run('../../tests/validate-recipe/data/recipe-noname-value.yml')
        self.assertNotEqual(obs_exit_code, 0)

    def test_type_not_valid(self):
        # No type key present
        obs_exit_code = run('../../tests/validate-recipe/data/recipe-notype-key.yml')
        self.assertNotEqual(obs_exit_code, 0)

        # Invalid type value present
        obs_exit_code = run('../../tests/validate-recipe/data/recipe-invalidtype-value.yml')
        self.assertNotEqual(obs_exit_code, 0)

    def test_file_does_not_exist(self):
        obs_exit_code = run('../../tests/validate-recipe/data/norecipe.yml')
        self.assertNotEqual(obs_exit_code, 0)

    def test_filepath_not_provided(self):
        results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py'])
        obs_exit_code = results.returncode
        self.assertNotEqual(obs_exit_code, 0)

if __name__ == '__main__':
        unittest.main()
