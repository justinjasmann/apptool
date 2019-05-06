'''
  Environment variables container
'''
import os
import sys

class EnvVars:
  def __init__(self, adb_path, app_package):
    self.adb_path = adb_path
    self.app_package = app_package

  def __str__(self):
    return "const val EnvVar ={\n  adb_path: %s, \n  app_package: %s\n}" % \
      (self.adb_path, self.app_package)

  def is_valid(self):
    return self.adb_path is not None

class Env:
  @staticmethod
  def get_env(args):
    # Detect if ANDROID_HOME is set
    android_root = os.environ.get("ANDROID_HOME", None)
    if not android_root:
      print("ANDROID_HOME is not set")
      sys.exit(-1)

    # Detect app package in this priority
    # 1. if --package is specified
    # 2. if env(APP_PACKAGE) is set
    app_package = args.package
    if not app_package:
      app_package = os.environ.get("APP_PACKAGE", None)
      if not app_package:
        print("APP_PACKAGE is not set")
        sys.exit(-1)

    adb_path = os.path.join(android_root, "platform-tools", "adb")
    return EnvVars(adb_path, app_package)