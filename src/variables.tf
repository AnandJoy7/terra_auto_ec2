variable "aws_region" {
  description = "The AWS region to deploy the EC2 instance"
  default     = "us-east-1"  # Change as necessary
}

variable "ami_id" {
  description = "The AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "The type of the instance"
  default     = "t2.micro"  # Change as necessary
}
