pipeline {
    agent any

    environment {
        IMAGE_NAME = "healthops-app"
        REGISTRY = "docker.io/akshata234"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/Akshata-del1531/healthops-app.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${REGISTRY}/${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh "docker push ${REGISTRY}/${IMAGE_NAME}:latest"
                }
            }
        }
    }
}