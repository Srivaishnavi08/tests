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
        stage('Start HTTP Server') {
            steps {
                script {
                    // Start the HTTP server in the background
                    sh 'start cmd /c "cd path/to/your/html && python -m http.server 8000"'
                    // Optional: Wait for a few seconds to ensure the server is up
                    sleep 5
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
