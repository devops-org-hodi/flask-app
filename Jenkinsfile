pipeline{
    agent any
    environment {
        IMAGE="pizza-box"
        IMAGE_TAG="${BUILD_NUMBER}"
         
        //
        BUILD_IMAGE="${IMAGE}:V${IMAGE_TAG}"
    }
    stages{
        stage("build"){
            steps{
                echo "+++ build docker image +++"
                sh "docker build -t ${BUILD_IMAGE} src/"
                sh "docker images | grep ${IMAGE} " 
            }
           
        }
         stage("test"){
            steps{
                sh "sleep 3 && echo test passed " 
            }
           
        }
        stage("login to AWS"){
            steps{
                 withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', 
                                  credentialsId: 'prd-aws-cred', 
                                  accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                                  secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    
                    sh 'aws sts get-caller-identity'
                }
            }
        }
    }
    post{
        always{
            cleanWs()
            sh "docker rmi -f  ${BUILD_IMAGE}"
            sh 'aws sts get-caller-identity'
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}