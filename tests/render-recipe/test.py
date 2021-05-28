#!/usr/bin/env python

import collections
import os
import subprocess
import tempfile
import unittest


ObservedRecord = collections.namedtuple(
    'ObserveredRecord', ['exit_code', 'stdout', 'stderr', 'rendered'])


class TestRenderRecipe(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_cmd(self, qiime2_recipe_fp):
        qiime2_recipe_fp = os.path.join('data', qiime2_recipe_fp)
        script = os.path.join('..', '..', 'bin',
                              'alp-1c8c84a3-render-recipe.py')
        conda_recipe_fp = os.path.join(self.temp_dir.name, 'rendered.yml')

        results = subprocess.run(
            ['python', script, qiime2_recipe_fp, conda_recipe_fp])

        with open(conda_recipe_fp) as fh:
            rendered = fh.read()

        stdout = None if results.stdout is None else str(results.stdout)
        stderr = None if results.stderr is None else str(results.stderr)

        return ObservedRecord(results.returncode, stdout, stderr, rendered)

    def test_basic(self):
        obs = self.run_cmd('recipe-basic.yml')
        self.assertEqual(obs.exit_code, 0)
        self.assertEqual(obs.stdout, None)
        self.assertEqual(obs.stderr, None)
        self.assertEqual(obs.rendered, '')


if __name__ == '__main__':
    unittest.main()
