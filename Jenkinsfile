pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
        
        
        timestamps() // Append timestamps to each line
        timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
    }
    agent {
        dockerfile {
            filename 'Dockerfile'
            // Optionally, you can specify the build context if your Dockerfile is not in the root
            // args '-v /tmp:/tmp' // Optional: docker run arguments
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Linting') {
            steps {
                script {
                    sh 'pylint **/*.py'
                }
            }
        }
        stage('Unit Testing') {
            steps {
                script {
                    sh 'python -m unittest discover -s tests/unit'
                }
            }
        }
        stage('Integration Testing') {
            steps {
                script {
                    sh """
                    ./standup_testing_environment.sh
                    python -m unittest discover -s tests/integration
                    """
                }
            }
        }
    }
    post {
        failure {
            script {
                def msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
                slackSend message: msg, channel: env.SLACK_CHANNEL
            }
        }
    }
}
