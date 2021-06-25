pipeline {
      agent any 
      stages {
        stage('Clone sources') {
            steps {
                git url: 'https://github.com/vanessakovalsky/python-api-handle-it.git'
            }
        }
        stage('continuous integration') { // Compile and do unit testing
             tools {
               gradle 'installGradle'
             }
             steps {
                 parallel (
                 // run Gradle to execute compile and unit testing
                    a: {
                        sh 'gradle lint'
                    },
                    b: {
                        sh 'gradle pycode'
                    }
                )
             }
           }

        // stage('testcode') {
            //  tools {
            //    gradle 'installGradle'
            //  }
        //     steps {
        //         sh 'gradle test'
        //     }
        // }
        
        stage('Package and deploy') {
             tools {
               gradle 'installGradle'
             }
            steps {
                sh 'gradle up'
            }
        }
      }
 }