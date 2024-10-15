pipeline {
    parameters {
        booleanParam(name: 'autoApprove', defaultValue: false, description: 'Automatically run apply after generating plan?')
    } 
    environment {
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
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
                sh 'pwd; cd terraform/; terraform init'
                sh "pwd; cd terraform/; terraform plan -out=tfplan"
                sh 'pwd; cd terraform/; terraform show -no-color tfplan > tfplan.txt'
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
                    def plan = readFile 'terraform/tfplan.txt'
                    input message: "Do you want to apply the plan?",
                    parameters: [text(name: 'Plan', description: 'Please review the plan', defaultValue: plan)]
                }
            }
        }

        stage('Apply') {
            steps {
                sh "pwd; cd terraform/; terraform apply -input=false tfplan"
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    dir('src') {
                        sh 'python3 terra_auto.py'  // Update with your Python script name
                    }
                }
            }
        }
    }
}
