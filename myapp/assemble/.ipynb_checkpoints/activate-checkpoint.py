import os
import shutil
import subprocess
import zipfile

def activate_environment(package_path, task_dir, runnable):
    with zipfile.ZipFile(package_path, 'r') as zip_ref:
        zip_ref.extractall(task_dir)
    
    env_dir = os.path.join(task_dir, "env")
    python_path = os.path.join(env_dir, "bin", "python")
    # make python executable by everyone
    subprocess.run(["chmod", "+x", python_path], check=True)
    # run the main script
    subprocess.run([python_path, runnable])

if __name__ == "__main__":
    activate_environment("project.zip", "app", "app_dir/main.py")