import os
import subprocess

# Initialized from main script
def Init(project_name, repo_name):
  os.mkdir(project_name)
  os.chdir(project_name)
  # Create README.md with title of project_name
  subprocess.check_call("echo '# {}' >> README.md".format(repo_name), shell=True)
  # creating react-app - may change to use npx instead of npm
  subprocess.call("npm create-react-app .", shell=True)
