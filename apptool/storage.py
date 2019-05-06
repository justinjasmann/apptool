'''
  Storage module
    Gives consumers the ability to manipulate app storage
'''
import subprocess

class Storage:
  def __init__(self, env):
    self.env = env
    self.base_commands = [
      self.env.adb_path,
      "shell", 
      "pm",
    ]

  def clear(self):
    commands = self.base_commands + [
      "clear",
      self.env.app_package
    ]
    subprocess.run(commands)
