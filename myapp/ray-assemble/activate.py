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

    env_bin_dir = os.path.join(env_dir, "bin")
    env = os.environ.copy()
    env["PATH"] = os.path.abspath(env_bin_dir) + os.pathsep + env["PATH"]
    print(env["PATH"])

    work_dir = os.path.abspath("app/app")
    # run the main script
    subprocess.run([os.path.abspath(python_path), "-m", "ray.serve", "run", "main:transalator_app"], check=True, env=env, cwd=work_dir)

if __name__ == "__main__":
    activate_environment("project.zip", "app", "serve run app/main:translator_app")
