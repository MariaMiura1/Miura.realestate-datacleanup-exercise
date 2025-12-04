pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install pandas
                '''
            }
        }

        stage('Run script') {
            steps {
                sh '''
                    # 👇 CAMBIA "tu_script.py" por el nombre real de tu script
                    python3 Test_realestate.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 Test_realestate.py'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully."
        }
        failure {
            echo "❌ The pipeline failed. Check console logs to find errors."
        }
    }
}

