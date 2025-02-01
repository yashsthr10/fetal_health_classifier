pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'yashsthr/fetal_health_detector'
        K8S_DEPLOYMENT_FILE = 'deployment.yaml'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/yashsthr10/fetal_health_classifier.git' // Ensure correct branch
            }
        }

        stage('Convert Jupyter Notebook to Python Script') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'jupyter nbconvert --to script fetal_health_classifier.ipynb'
                    } else {
                        bat 'jupyter nbconvert --to script fetal_health_classifier.ipynb'
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t ${DOCKER_IMAGE} .'
                    } else {
                        bat 'docker build -t ${DOCKER_IMAGE} .'
                    }
                }
            }
        }

        stage('Train Model') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker run --rm -v $(pwd):/app ${DOCKER_IMAGE} python fetal_health_classifier.py'
                    } else {
                        bat 'docker run --rm -v $(pwd):/app ${DOCKER_IMAGE} python fetal_health_classifier.py'
                    }
                }
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                script {
                    // Log in to Docker Hub
                    if (isUnix()) {
                        sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    } else {
                        bat 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    }
                    
                    // Build the Docker image
                    if (isUnix()) {
                        sh 'docker build -t ${DOCKER_IMAGE} .'
                    } else {
                        bat 'docker build -t ${DOCKER_IMAGE} .'
                    }
                    
                    // Push the Docker image to Docker Hub
                    if (isUnix()) {
                        sh 'docker push ${DOCKER_IMAGE}'
                    } else {
                        bat 'docker push ${DOCKER_IMAGE}'
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'kubectl apply -f ${K8S_DEPLOYMENT_FILE}'
                    } else {
                        bat 'kubectl apply -f ${K8S_DEPLOYMENT_FILE}'
                    }
                }
            }
        }
    }
}
