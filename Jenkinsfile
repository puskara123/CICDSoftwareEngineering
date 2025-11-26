pipeline {
    agent any

    environment {
        IMAGE = "puskara/selab:jenkins"
        VENV = ".venv"
        PYTHON = "python"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[
                    url: 'https://github.com/puskara123/CICDSoftwareEngineering.git',
                    credentialsId: 'github-creds-selab'
                  ]]
                ])
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '%PYTHON% -m venv %VENV%'
                bat '%VENV%\\Scripts\\pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '%VENV%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '%VENV%\\Scripts\\pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat 'docker build -t %IMAGE% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockercredsSELab',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    bat '''
                        @echo %PASS% | docker login -u %USER% --password-stdin
                        docker push %IMAGE%
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                echo 'Deploying Docker container...'
                bat '''
                    docker pull %IMAGE%
                    docker stop ci-cd-demo 2>nul || exit /b 0
                    docker rm ci-cd-demo 2>nul || exit /b 0
                    docker run -d -p 5000:5000 --name ci-cd-demo %IMAGE%
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed! Check logs above.'
        }
    }
}
