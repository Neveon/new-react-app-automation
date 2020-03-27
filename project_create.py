import os
import subprocess

# Initialized from main script
def Init(project_name, repo_name):
  os.mkdir(project_name)
  os.chdir(project_name)
  # Creates react app
  subprocess.call("npx create-react-app .", shell=True)
