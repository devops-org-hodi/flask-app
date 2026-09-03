pipeline{
    agent any
    environment {
        IMAGE="pizza-box"
        IMAGE_TAG="${BUILD_NUMBER}"
         
        //
        BUILD_IMAGE="${IMAGE_TAG}:V${IMAGE}"
    }
    stages{
        stage("build"){
            steps{
                echo "+++ build docker image +++"
                sh "docker build -t ${BUILD_IMAGE} src/"
                sh "docker images | grep ${IMAGE} " 
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