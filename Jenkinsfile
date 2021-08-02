pipeline{
    agent any
    parameters{
        choice(
            name: 'BROWSER',
            description: 'select desired browser',
            choices: ['chrome', 'firefox'])
    }
    stages{
        stage('Starting Docker Grid'){
            steps{
                sh "docker-compose up -d"
                sh "sleep 10"
            }
        }
        stage('Execution'){
            steps{
                sh "pytest"
            }
        }
        stage('Stopping Docker Grid'){
            steps{
                sh "docker-compose down"
            }
        }
    }
    post {
            always {
                archiveArtifacts allowEmptyArchive: true, artifacts: 'target/**/*', fingerprint: true
            }
        }
}
