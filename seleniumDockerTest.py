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
        stage('Run Tests') {
            steps {
                script {
                    // Ensure the HTTP server is running on the host machine before running tests
                    bat 'python -m http.server 8000 &'
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
