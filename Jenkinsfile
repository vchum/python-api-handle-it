pipeline {
      agent any 
      stages {
        stage('Clone sources') {
            steps {
                git url: 'https://github.com/vanessakovalsky/python-api-handle-it.git'
            }
        }
        
       stage('Lint') { // Compile and do unit testing
             tools {
               gradle 'installGradle'
             }
             steps {
               // run Gradle to execute compile and unit testing
               sh 'gradle lint'
             }
           }
        stage('Pycode') {
            steps {
                sh 'gradle pycode'
            }
        }
        // stage('testcode') {
        //     steps {
        //         sh 'gradle test'
        //     }
        // }
        
        stage('Package and deploy') {
            steps {
                sh 'gradle up'
            }
        }
      }
 }