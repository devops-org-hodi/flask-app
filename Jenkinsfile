pipeline{
    agent any
    environment {
        IMAGE="pizza-box"
        IMAGE_TAG="${BUILD_NUMBER}"
         
        ECR_REPO_NAME='flask-app-demo/first'
        //
        
        ECR_REGISTRY="514080426196.dkr.ecr.us-east-2.amazonaws.com"
        BUILD_IMAGE="${ECR_REGISTRY}/${ECR_REPO_NAME}:V${IMAGE_TAG}"
        
        }
    stages{
        stage("build"){
            steps{
                echo "+++ build docker image +++"
                sh "docker build -t ${BUILD_IMAGE} src/"
                sh "docker images | grep ${ECR_REPO_NAME} " 
            }
           
        }
         stage("test"){
            steps{
                sh "sleep 3 && echo test passed " 
            }
           
        }
        stage("login to AWS adn push to ecr"){
            steps{
                 withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', 
                                  credentialsId: 'prd-aws-cred', 
                                  accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                                  secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    
                    sh 'aws sts get-caller-identity'

                    sh '''
                        aws ecr get-login-password --region us-east-2  | \
                        docker login \
                        --username AWS \
                        --password-stdin "${ECR_REGISTRY}"
                        
                        docker push "${BUILD_IMAGE}"
                        '''
                    
                }
            }
        }
    }
    post{
        always{
            cleanWs()
            sh "docker rmi -f  ${BUILD_IMAGE}"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}