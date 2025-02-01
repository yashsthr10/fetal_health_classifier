pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'yashsthr/fetal_health_detector'
        K8S_DEPLOYMENT_FILE = 'deployment.yaml' 
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/yashsthr10/fetal_health_classifier.git' // Replace with your GitHub repo URL
            }
        }

        stage('Convert Jupyter Notebook to Python Script') {
            steps {
                sh 'jupyter nbconvert --to script fetal_health_classifier.ipynb' // Converts the .ipynb to .py
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .' // Build the Docker image from your Dockerfile
            }
        }

        stage('Train Model') {
            steps {
                sh 'docker run --rm -v $(pwd):/app ${DOCKER_IMAGE} python fetal_health_classifier.py' // Run model training in the container
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    
                    // Build the Docker image
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                    
                    // Push the Docker image to Docker Hub
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Apply your Kubernetes YAML file
                sh 'kubectl apply -f ${K8S_DEPLOYMENT_FILE}'
            }
        }
    }
}
