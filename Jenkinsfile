pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirement.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python3 test.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
            }
        }
    }
}
