'''
  Package management module
    Gives consumers the ability to add or remove packages
'''
import subprocess

class PackageManager:
  def __init__(self, env): 
    self.env = env
    self.base_commands = [
      self.env.adb_path,
      "shell", 
      "pm",
    ]

  def remove(self):
    commands = self.base_commands + [
      "uninstall",
      self.env.app_package
    ]
    subprocess.run(commands)