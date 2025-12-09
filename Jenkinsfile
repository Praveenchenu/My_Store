pipeline {
    agent any
    
    // Tools block is removed as Maven is not needed
    // The Python steps will rely on system-installed Python/pip 
    // or a base image in the Docker step.

    stages {
        stage ('checkout') {
            steps {
                echo 'Checking out source code...'
                git branch: 'master', url: 'https://github.com/Praveenchenu/My_Store.git'
            }
        } 

        // --- NEW PYTHON DEPENDENCY STAGE ---
        stage ('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                // Assuming you have a virtual environment setup or Python is available
                sh 'pip install -r requirements.txt' 
                // Note: The Docker build will handle the final dependencies for the image.
            }
        }

        // --- SONARQUBE ANALYSIS (Using Sonar Scanner for Generic Projects) ---
        stage ('sonarQube') {
            steps {
                echo 'Running SonarQube analysis...'
                // Use SonarScanner for non-Maven projects. This requires a 
                // sonar-project.properties file in the root of the repository.
                sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=sonar-token \
                    -Dsonar.host.url=http://3.1.196.239:9000 \
                    -Dsonar.login=sqa_bbadc1a60d2a2ec37ba1dbbc31bcd7598a548d3e
                '''
            }
        }

        // --- ARTIFACT BUILD STAGE REMOVED ---
        // Artifact build is inherent in the Docker image creation for Python projects.

        stage ('Docker Build') {
            steps {
                echo 'Building and pushing Docker image...'
                // Using Groovy string for variable interpolation 
                sh "docker build -t praveenkumar446/django-image:latest:${env.BUILD_NUMBER} ."
            }
        }
        
        stage ('push to registry') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_HUB_PASSWORD')]) {
                        sh '''
                            echo $DOCKER_HUB_PASSWORD | docker login -u praveenkumar446 --password-stdin
                            docker push praveenkumar446/django-image:latest:${BUILD_NUMBER}
                        '''
                    }
                }
            }
        }

        stage ('update deployment files') {
            steps {
                echo 'Updating deployment files...'
                // Using Groovy string for variable interpolation
                sh "sed -i 's|image: praveenkumar446/django-image:.*|image: praveenkumar446/django-image:latest:${env.BUILD_NUMBER}|' k8s/deployment.yaml"
            }
        }
    }
}
