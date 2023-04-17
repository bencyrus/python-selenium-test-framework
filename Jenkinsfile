pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // Create a new virtual environment named 'env'
                    sh 'python3 -m virtualenv env'

                    // Activate the virtual environment named 'env'
                    env.VIRTUAL_ENV = "${WORKSPACE}/env"
                    env.PATH = "${env.VIRTUAL_ENV}/bin:${env.PATH}"
                }
            }
        }

        stage('Install dependencies') {
            steps {
                // Install dependencies from requirements.txt
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Create a directory for this test run's report
                    report_directory = "allure_reports"
                    sh "mkdir -p ${report_directory}"

                    // Run the behave command to execute the tests using both the 'pretty' and 'AllureFormatter' formatters
                    sh "behave -f allure_behave.formatter:AllureFormatter -o ${report_directory} -f pretty"
                }
            }
        }
    }

    post {
        always {
            script {
                // Generate Allure report
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure_reports']]
                ])
            }
        }
    }
}
