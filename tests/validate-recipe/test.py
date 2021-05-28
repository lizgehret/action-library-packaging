#!/usr/bin/env python

import unittest
import subprocess

def run(filepath):
    results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py', filepath], capture_output=True)
    return [results.returncode, results.stderr]

class TestValidateRecipe(unittest.TestCase):

    def test_basic(self):
        filepath = '../../tests/validate-recipe/data/recipe-basic.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertEqual(obs_exit_code, 0)
        self.assertEqual(obs_stderr, b'')

    def test_version_not_provided(self):
        # No version key present
        filepath = '../../tests/validate-recipe/data/recipe-noversion-key.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'KeyError' in obs_stderr)

        # Version key present, no value
        filepath = '../../tests/validate-recipe/data/recipe-noversion-value.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'version value not added' in obs_stderr)

    def test_name_not_provided(self):
        # No name key present
        filepath = '../../tests/validate-recipe/data/recipe-noname-key.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'KeyError' in obs_stderr)

        # Name key present, no value
        filepath = '../../tests/validate-recipe/data/recipe-noname-value.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'name value not added' in obs_stderr)

    def test_type_not_valid(self):
        # No type key present
        filepath = '../../tests/validate-recipe/data/recipe-notype-key.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'KeyError' in obs_stderr)

        # Invalid type value present
        filepath = '../../tests/validate-recipe/data/recipe-invalidtype-value.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'valid type value not added' in obs_stderr)

    def test_key_not_valid(self):
        filepath = '../../tests/validate-recipe/data/recipe-invalid-key.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'invalid key added' in obs_stderr)

    def test_file_does_not_exist(self):
        filepath = '../../tests/validate-recipe/data/norecipe.yml'
        obs_exit_code, obs_stderr = run(filepath)
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'filepath not found' in obs_stderr)

    #TODO: fix this unit test
    def test_filepath_not_provided(self):
        results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py'])
        obs_exit_code = results.returncode
        self.assertNotEqual(obs_exit_code, 0)

if __name__ == '__main__':
        unittest.main()
