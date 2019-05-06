'''
  Permissions module
    Gives consumers the ability to control specific app permissions
'''
import subprocess

VALID_PERMS = {
  "camera": "android.permission.camera"
}

class Perms:
  def __init__(self, env):
    self.env = env
    self.base_commands = [
      self.env.adb_path,
      "shell", 
      "pm"
    ]
  
  def __validate_perm__(self, perm):
    assert perm in VALID_PERMS
    return VALID_PERMS[perm]

  def grant(self, perm):
    commands = self.base_commands + [
      "grant",
      self.env.app_package,
      self.__validate_perm__(perm),
    ]
    subprocess.run(commands)

  def revoke(self, perm):
    commands = self.base_commands + [
      "revoke",
      self.env.app_package,
      self.__validate_perm__(perm)
    ]
    subprocess.run(commands)