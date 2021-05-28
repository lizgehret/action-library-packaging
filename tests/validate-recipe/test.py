#!/usr/bin/env python

import unittest
import subprocess

def run(filename):
    filepath = 'data/' + filename
    results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py', filepath], capture_output=True)
    return [results.returncode, results.stderr]

class TestValidateRecipe(unittest.TestCase):

    def test_basic(self):
        obs_exit_code, obs_stderr = run('recipe-basic.yml')
        self.assertEqual(obs_exit_code, 0)
        self.assertEqual(obs_stderr, b'')

    def test_version_not_provided(self):
        # No version key present
        obs_exit_code, obs_stderr = run('recipe-noversion-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'KeyError' in obs_stderr)

        # Version key present, no value
        obs_exit_code, obs_stderr = run('recipe-noversion-value.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'version value not added' in obs_stderr)

    def test_name_not_provided(self):
        # No name key present
        obs_exit_code, obs_stderr = run('recipe-noname-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'KeyError' in obs_stderr)

        # Name key present, no value
        obs_exit_code, obs_stderr = run('recipe-noname-value.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'name value not added' in obs_stderr)

    def test_type_not_valid(self):
        # No type key present
        obs_exit_code, obs_stderr = run('recipe-notype-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'KeyError' in obs_stderr)

        # Invalid type value present
        obs_exit_code, obs_stderr = run('recipe-invalidtype-value.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'valid type value not added' in obs_stderr)

    def test_key_not_valid(self):
        obs_exit_code, obs_stderr = run('recipe-invalid-key.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'invalid key added' in obs_stderr)

    def test_file_does_not_exist(self):
        obs_exit_code, obs_stderr = run('norecipe.yml')
        self.assertNotEqual(obs_exit_code, 0)
        self.assertTrue(b'filepath not found' in obs_stderr)

    def test_filepath_not_provided(self):
        results = subprocess.run(['python', '../../bin/alp-1c8c84a3-validate-recipe.py'], capture_output=True)
        obs_exit_code = results.returncode
        self.assertNotEqual(obs_exit_code, 0)

if __name__ == '__main__':
        unittest.main()
