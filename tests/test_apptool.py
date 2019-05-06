import apptool
import unittest

from apptool import args, environ, package, perms
from unittest.mock import patch

test_adb_path = "test_adb_path"
test_package = "test_package"

class ArgParserTestCase(unittest.TestCase):
  @patch("apptool.args.argparse.ArgumentParser")
  def test_parse(self, mock_argument_parser):
    parser = apptool.args.ArgParser(version="1.0")
    parser.parse()
    
    parser.parser.parse_args.assert_called_once()

class EnvVarsTestCase(unittest.TestCase):
  def test_str(self):
    env = apptool.environ.EnvVars(test_adb_path, test_package)
    expected = "const val EnvVar ={\n  adb_path: %s, \n  app_package: %s\n}" % \
      (test_adb_path, test_package)
    self.assertEqual(expected, str(env))
  def test_is_valid_fails(self):
    env = apptool.environ.EnvVars(None, test_package)
    self.assertFalse(env.is_valid())
  def test_is_valid_succeeds(self):
    env = apptool.environ.EnvVars(test_adb_path, test_package)
    self.assertTrue(env.is_valid())

class PackageManagerTestCase(unittest.TestCase):
  @patch("apptool.package.subprocess.run")
  def test_remove(self, mock_run):
    env = apptool.environ.EnvVars(test_adb_path, test_package)
    package = apptool.package.PackageManager(env)
    package.remove()

    mock_run.assert_called_with([test_adb_path, "shell", "pm", "uninstall", test_package])

class PermsTestCase(unittest.TestCase):
  @patch("apptool.perms.subprocess.run")
  def test_grant(self, mock_run):
    env = apptool.environ.EnvVars(test_adb_path, test_package)
    perms = apptool.perms.Perms(env)
    perms.grant("camera")

    mock_run.assert_called_with([test_adb_path, "shell", "pm", "grant", test_package, apptool.perms.VALID_PERMS["camera"]])

class StorageTestCase(unittest.TestCase):
  @patch("apptool.storage.subprocess.run")
  def test_clear(self, mock_run):
    env = apptool.environ.EnvVars(test_adb_path, test_package)
    storage = apptool.storage.Storage(env)
    storage.clear()

    mock_run.assert_called_with([test_adb_path, "shell", "pm", "clear", test_package])