pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    sh 'docker pull selenium/standalone-chrome'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome'
                }
            }
        }
        stage('Start HTTP Server') {
            steps {
                script {
                    // Navigate to the directory containing index.html and start the HTTP server
                    sh 'cd path/to/your/html && python -m http.server 8000 &'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Assuming your test file is in the workspace
                    sh 'python seleniumDockerTest.py'
                }
            }
        }
        stage('Clean Up') {
            steps {
                script {
                    // Stop and remove the Docker container
                    sh 'docker ps -q -f ancestor=selenium/standalone-chrome | xargs docker stop'
                    sh 'docker ps -a -q -f ancestor=selenium/standalone-chrome | xargs docker rm'
                }
            }
        }
    }
}
