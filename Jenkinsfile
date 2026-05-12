pipeline {
    agent any

    environment {
        IMAGE_NAME = "healthops-app"
        REGISTRY = "docker.io/akshata234"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/YOUR_USERNAME/healthops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${REGISTRY}/${IMAGE_NAME}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image("${REGISTRY}/${IMAGE_NAME}").push('latest')
                    }
                }
            }
        }
    }
}