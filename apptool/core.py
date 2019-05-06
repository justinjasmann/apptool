'''
  AppTool.py
    Requirements
      - ANDROID_HOME, APP_PACKAGE need to be set
    Features
      Storage
      - Clear app cache
      - Clear app storage
      - Uninstall app
      Permissions

'''
from args import ArgParser
from environ import Env
from package import PackageManager
from perms import Perms
from storage import Storage

class AppTool:
  def __init__(self):
    self.args = ArgParser(version = 1.0).parse()
    self.env = Env.get_env(self.args)
    self.perms = Perms(self.env)
    self.storage = Storage(self.env)
    self.package_manager = PackageManager(self.env)
  
  def execute(self):
    if self.args.clear is True:
      self.storage.clear()  
    elif self.args.remove is True:
      self.package_manager.remove()
    elif self.args.revoke == "camera":
      self.perms.revoke("camera")

AppTool().execute()