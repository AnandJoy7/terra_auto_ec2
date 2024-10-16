pipeline {
    parameters {
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
        string(name: 'AMI_ID', defaultValue: '', description: 'The AMI ID for the EC2 instance') 
    } 
    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
        GITHUB_CREDENTIALS = credentials('github-credentials')
    }

    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    dir("terraform") {
                        git credentialsId: 'github-credentials', 
                            branch: 'main', 
                            url: "https://github.com/AnandJoy7/terra_auto_ec2.git"
                    }
                }
            }
        }

        stage('Run Terraform Script') {
            steps {
                script {
                    dir('terraform/src') {
                        // Pass the AMI ID to the Python script as an environment variable
                        sh "AMI_ID=${params.AMI_ID} python3 terra_run.py"
                    }
                }
            }
        }
    }
}
