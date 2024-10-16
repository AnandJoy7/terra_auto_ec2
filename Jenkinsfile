pipeline {
    parameters {
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
    } 
    environment {
        AWS_ACCESS_KEY_ID     = credentials('aws-access-key')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-key')
        GITHUB_CREDENTIALS = credentials('github-credentials') // Replace with your GitHub credentials ID
    }

    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                    dir("terraform") {
                        // Use GitHub credentials for authentication
                        git credentialsId: 'github-credentials', // Your stored GitHub credentials ID
                            branch: 'main', 
                            url: "https://github.com/AnandJoy7/terra_auto_ec2.git"
                    }
                }
            }
        }

        stage('Plan') {
            steps {
                script {
                    dir('terraform/src') { // Change to the directory containing .tf files
                        sh 'pwd' // Optional: for debugging
                        sh 'terraform init'
                        sh "terraform plan -out=tfplan"
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
                    def plan = readFile 'terraform/src/tfplan.txt' // Adjust the path
                    input message: "Do you want to apply the plan?",
                    parameters: [text(name: 'Plan', description: 'Please review the plan', defaultValue: plan)]
                }
            }
        }

        stage('Apply') {
            steps {
                script {
                    dir('terraform/src') { // Change to the directory containing .tf files
                        sh "terraform apply -input=false tfplan"
                    }
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    dir('src') {
                        sh 'python3 terra_run.py'  // Update with your Python script name
                    }
                }
            }
        }
    }
}
