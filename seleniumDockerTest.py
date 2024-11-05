pipeline {
    agent any
    stages {
        stage('Pull Docker Image') {
            steps {
                script {
                    bat 'docker pull selenium/standalone-chrome'
                }
            }
        }
        stage('Start Selenium Container') {
            steps {
                script {
                    // Run the Selenium container
                    bat 'docker run -d -p 4444:4444 --name selenium-chrome selenium/standalone-chrome'
                }
            }
        }
        stage('Start HTTP Server') {
            steps {
                script {
                    // Start the HTTP server in the background
                    bat 'start cmd /c "cd tests && python -m http.server 8000"'
                    // Optional: Wait for a few seconds to ensure the server is up
                    sleep 5
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run your test file
                    bat 'python tests/seleniumDockerTest.py'
                }
            }
        }
        stage('Clean Up') {
            steps {
                script {
                    // Stop and remove the Selenium container
                    bat 'docker stop selenium-chrome'
                    bat 'docker rm selenium-chrome'
                }
            }
        }
    }
}
