import subprocess
import sys

def execute_command(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout.decode()


def terraform_init(directory):
    try:
        subprocess.run(f"terraform -chdir={directory} init", shell=True, check=True)
        print("Terraform initialized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during initialization: {e}")
        sys.exit(1)

def terraform_plan(directory):
    try:
        subprocess.run(f"terraform -chdir={directory} plan", shell=True, check=True)
        print("Terraform plan generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during plan: {e}")
        sys.exit(1)

def terraform_apply(directory):
    try:
        subprocess.run(f"terraform -chdir={directory} apply -auto-approve", shell=True, check=True)
        print("Terraform applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during apply: {e}")
        sys.exit(1)

def terraform_destroy(directory):
    try:
        subprocess.run(f"terraform -chdir={directory} destroy -auto-approve", shell=True, check=True)
        print("Terraform destroyed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during destroy: {e}")
        sys.exit(1)

def main():
    directory = "/Users/shubham/Documents/work/TrainWithShubham/terra-practice"
    terraform_init(directory)
    
    terraform_plan(directory)
    
    terraform_apply(directory)
    
    terraform_destroy(directory)

if __name__ == "__main__":
    main()
