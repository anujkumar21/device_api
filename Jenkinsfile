pipeline{
    agent any
    parameters{
        choice(
            name: 'BROWSER',
            description: 'select desired browser',
            choices: ['chrome', 'firefox'])
    }
    stages{
        stage('Execution'){
            steps{
                sh "pytest"
            }
        }
    }
    post {
            always {
                archiveArtifacts allowEmptyArchive: true, artifacts: 'target/**/*', fingerprint: true
            }
        }
}
