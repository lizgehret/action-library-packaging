#!/usr/bin/env python

import unittest
import os
import subprocess

def run(filename):
    filepath = os.path.join('data', filename)
    script = os.path.join('..', '..', 'bin', 'alp-1c8c84a3-validate-recipe.py')
    results = subprocess.run(['python', script, filepath], capture_output=True)
    return [results.returncode, results.stderr.decode('utf-8')]

class TestValidateRecipe(unittest.TestCase):

    def test_basic(self):
        obs_exit_code, obs_stderr = run('recipe-basic.yml')
        self.assertEqual(obs_exit_code, 0)
        print(obs_stderr)
        self.assertEqual(obs_stderr, '')

    def test_version_not_provided(self):
        # No version key present
        obs_exit_code, obs_stderr = run('recipe-noversion-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('KeyError' in obs_stderr)

        # Version key present, no value
        obs_exit_code, obs_stderr = run('recipe-noversion-value.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('version value not added' in obs_stderr)

    def test_name_not_provided(self):
        # No name key present
        obs_exit_code, obs_stderr = run('recipe-noname-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('KeyError' in obs_stderr)

        # Name key present, no value
        obs_exit_code, obs_stderr = run('recipe-noname-value.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('name value not added' in obs_stderr)

    def test_type_not_valid(self):
        # No type key present
        obs_exit_code, obs_stderr = run('recipe-notype-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('KeyError' in obs_stderr)

        # Invalid type value present
        obs_exit_code, obs_stderr = run('recipe-invalidtype-value.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('valid type value not added' in obs_stderr)

    def test_key_not_valid(self):
        obs_exit_code, obs_stderr = run('recipe-invalid-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('invalid key added' in obs_stderr)

    def test_file_does_not_exist(self):
        obs_exit_code, obs_stderr = run('norecipe.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue('filepath not found' in obs_stderr)

    def test_filepath_not_provided(self):
        filepath = os.path.join('..', '..', 'bin', 'alp-1c8c84a3-validate-recipe.py')
        results = subprocess.run(['python', filepath], capture_output=True)
        obs_exit_code = results.returncode
        self.assertNotEqual(obs_exit_code, 0)

if __name__ == '__main__':
        unittest.main()
