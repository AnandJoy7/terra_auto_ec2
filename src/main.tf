provider "aws" {
  region = "us-east-1"  # Change to your desired region
}

resource "aws_instance" "my_ec2" {
  ami           = "ami-0866a3c8686eaeeba"  # Replace with your desired AMI ID
  instance_type = "t2.micro"  # Change instance type if needed

  tags = {
    Name = "MyEC2Instance"
  }
}
