'''
  Argument parsing module
    Parses command-line arguments
'''
import argparse

class ArgParser: 
  def __init__(self, version):
    self.parser = argparse.ArgumentParser(
      prog="APP TOOL",
      description="Android AppTool"
    )
    
    self.parser.add_argument("--version",
      action="version",
      version='%(prog)s v' + str(version)
    )

    # app-tool
    self.parser.add_argument("--package",
      default=None,
      help="Set the package to run commands on"
    )

    # storage
    self.parser.add_argument("-c", "--clear",
      action="store_true",
      help="Clear storage for this app"
    )

    # package manager
    self.parser.add_argument("-r", "--remove",
      action="store_true",
      help="Uninstall this app"
    )

    # perms
    self.parser.add_argument("--revoke",
      choices="camera",
      default=False,
      help="Revoke a permission"
    )

  def parse(self):
    return self.parser.parse_args()
