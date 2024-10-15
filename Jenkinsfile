pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')  // Set your AWS credentials ID
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')  // Set your AWS credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AnandJoy7/terra_auto_ec2.git', branch: 'main'  // Replace with your repository URL
            }
        }
        stage('Terraform Init') {
            steps {
                dir('src') {  // Change directory to 'src'
                    sh 'terraform init'
                }
            }
        }
        stage('Terraform Plan') {
            steps {
                dir('src') {  // Change directory to 'src'
                    sh 'terraform plan -out=tfplan'
                }
            }
        }
        stage('Terraform Apply') {
            steps {
                dir('src') {  // Change directory to 'src'
                    sh 'terraform apply -auto-approve tfplan'
                }
            }
        }
        stage('Run Python Script') {
            steps {
                dir('src') {  // Change directory to 'src'
                    sh 'python3 your_script.py'
                }
            }
        }
        stage('Cleanup') {
            steps {
                dir('src') {  // Change directory to 'src'
                    sh 'terraform destroy -auto-approve'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'src/**/*', fingerprint: true
        }
        failure {
            mail to: 'you@example.com',
                 subject: "Pipeline failed",
                 body: "Check the Jenkins job for details."
        }
    }
}
