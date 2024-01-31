Sure, here's your text formatted with Markdown:

markdown
# Deploying a Web Application using Docker Compose on AWS

This project leverages Terraform for infrastructure provisioning. The project architecture incorporates a multi-service application setup with a PostgreSQL database and a FastAPI application service, which are containerized and orchestrated using Docker Compose. Additionally, the Terraform script automates the AWS cloud infrastructure setup, including networking, security, and an EC2 instance configuration for hosting the Docker containers.

## Prerequisites

- AWS Account & AWS CLI with admin credentials
- Terraform installed
- Docker and Docker Compose installed
- Git (for version control and cloning repositories)

## Terraform Execution Guide

1. **Initialization**: Navigate to the Terraform script directory and run `terraform init` to initialize the Terraform workspace and download required providers.
2. **Plan**: Execute `terraform plan` to review the infrastructure changes that will be applied.
3. **Apply**: Deploy the infrastructure with `terraform apply`. Confirm the action when prompted to proceed with the deployment.

**Note**: The Terraform script generates an SSH key pair. The private key (`terraform-pem-ansible-dec04.pem`) is saved locally and should be used for SSH access to the EC2 instance.

## AWS Components Configuration

- **VPC & Networking**: A custom VPC with an internet gateway, route table, and a public subnet to host the EC2 instance.
- **Security Groups**: Configured to allow SSH, ICMP (ping), and HTTP access on port 8080.
- **EC2 Instance**: Hosts the Docker containers, accessible via a public DNS.

## Docker Compose Overview

- **PostgreSQL Database (db)**: Uses the `postgres:15.0` image, pre-configured with user credentials. It's meant for development and requires security hardening for production.
- **FastAPI Application (app)**: Built from `maxiplux/fastapidevops-auth:latest`, it serves as the web application backend.

## Accessing the Application

After deployment, the web application will be accessible through the EC2 instance's public DNS on port 8080. Detailed instructions on accessing and testing the application are provided in the Terraform script outputs.

#Video about how to deploy this project, step by step:
-- ** https://www.youtube.com/watch?v=03fnj4TSAwI


## Conclusion

This setup demonstrates a basic but comprehensive approach to deploying a multi-service web application on AWS using Docker Compose, managed and provisioned by Terraform. It illustrates the power of Infrastructure as Code (IaC) in automating and simplifying cloud infrastructure deployment and management.

Please remeber delete all the resources here using terraform destroy at the end.
 






Contributing
------------

Feel free to fork, modify, and send a pull request. Contributions are welcome!

License
-------

[MIT License](LICENSE)


