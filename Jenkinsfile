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
                    python3 tu_script.py
                '''
            }
        }
    }

    post {
        failure {
            echo "❌ The script failed. Check console logs to find errors."
        }
        success {
            echo "✅ Script executed successfully."
        }
    }
}
pipeline {
    agent any

    stages {
        stage('Run Tests') {
            steps {
                sh 'python3 Test_realestate.py'
            }
        }
    }
}
