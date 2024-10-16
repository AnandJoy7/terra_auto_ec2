import subprocess

def run_terraform_commands():
    try:
        # Initialize Terraform
        print("Initializing Terraform...")
        subprocess.run(["terraform", "init"], check=True)

        # Plan Terraform
        print("Planning Terraform...")
        subprocess.run(["terraform", "plan", "-out=tfplan", "-var", "ami_id=your_ami_id"], check=True)

        # Apply Terraform
        print("Applying Terraform...")
        subprocess.run(["terraform", "apply", "-input=false", "tfplan"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    run_terraform_commands()
