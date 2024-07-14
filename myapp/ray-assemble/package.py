import os
import yaml
import subprocess
import shutil

def create_virtualenv(env_dir):
    subprocess.run(["python", "-m", "venv", env_dir])

def install_dependencies(env_dir, packages):
    subprocess.run([os.path.join(env_dir, "bin", "pip"), "install", "--no-cache-dir"] + packages)

def copy_working_dir(working_dir, dest_dir):
    shutil.copytree(working_dir, dest_dir)

def package_environment(config_file, output_dir):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    
    env_dir = os.path.join(output_dir, "env")
    create_virtualenv(env_dir)
    install_dependencies(env_dir, config.get('pip', []))
    
    working_dir = config.get('working_dir', None)
    if working_dir:
        copy_working_dir(working_dir, os.path.join(output_dir, "app"))

    shutil.make_archive(output_dir, 'zip', output_dir)

if __name__ == "__main__":
    package_environment("environment.yaml", "project")