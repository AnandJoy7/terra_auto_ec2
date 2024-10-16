pipeline {
    parameters {
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
        string(name: 'AMI_ID', defaultValue: '', description: 'The AMI ID for the EC2 instance') // Add this line
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

        stage('Plan') {
            steps {
                script {
                    dir('terraform/src') { 
                        sh 'pwd' // Optional: for debugging
                        sh 'terraform init'
                        // Pass the ami_id variable
                        sh "terraform plan -out=tfplan -var ami_id=${params.AMI_ID}" // Use the parameter here
                        sh 'terraform show -no-color tfplan > tfplan.txt'
                    }
                }
            }
        }

        stage('Approval') {
            when {
                not {
                    equals expected: true, actual: params.autoApprove
                }
            }
            steps {
                script {
                    def plan = readFile 'terraform/src/tfplan.txt'
                    input message: "Do you want to apply the plan?",
                    parameters: [text(name: 'Plan', description: 'Please review the plan', defaultValue: plan)]
                }
            }
        }

        stage('Apply') {
            steps {
                script {
                    dir('terraform/src') { 
                        sh "terraform apply -input=false tfplan"
                    }
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    dir('src') {
                        sh 'python3 terra_run.py'
                    }
                }
            }
        }
    }
}
