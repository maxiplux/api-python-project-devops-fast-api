pipeline {
    options {
        buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
        timestamps() // Append timestamps to each line
        timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
    }
    agent any // Run on any available agent
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                script {
                    
                    
                    
                    sh 'python -m pip  install  -r requirements.txt'
                }
            }
        }

        stage('Unit Testing') {
            steps {
                script {
                    sh 'python -m unittest discover -s tests'
                }
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    

                    // Build the Docker image with the commit ID as a build argument
                    
                 
                    sh "echo $DOCKER_PASSWORD | docker login --username $DOCKER_USERNAME --password-stdin"
                   
                }
            }
        }

        stage('Deploy to Docker Registry') {
            steps {
                script {
                    def commitId = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()

                    // Build the Docker image with the commit ID as a build argument
                    sh "#docker buildx build --platform=linux/amd64 --push --tag maxiplux/jenkins:${commitId} -f ./Dockerfile ."
                 
                    sh "docker ps"
                }
            }
        }
    }
    post {
        failure {
            script {
                def msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
               
            }
        }
    }
}
