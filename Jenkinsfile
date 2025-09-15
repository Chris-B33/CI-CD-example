pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'                                           // Create virtual environment named 'venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'         // Run venv and install requirements
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && pytest --junitxml=results.xml'           // Run test files and set output to results.xml
            }
        }
        stage('Publish Results') {
            steps {
                junit 'results.xml'                                                 // Display results.xml in Jenkins
            }
        }
    }
}