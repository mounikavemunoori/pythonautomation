
pipeline {
 agent any
 stages {
 	stage('checking versions') {
 	  steps {
 	  	sh 'java -version'
 	  	sh 'python --version'
 	  	sh 'ls -lrt'
 	  }
 	}
 	
 	stage('path') {
 		steps {
 			sh 'ls -lrt'
 			sh 'pwd'
 		}
 	}
 	
 	stage('checkout branch') {
 		steps {
 			checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: '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', url: 'https://github.com/mounikavemunoori/pythonautomation.git']]])
 			dir('selenum_automation_python') {
      				sh "pwd"
      				sh 'python tests/find_string.py'
    				}
 			sh 'pwd'
 		}
 	}
 	
 	stage('shell scripting') {
 		steps {
 			sh 'pwd'
 			dir('new_shell_programs/shell_scripting') {
 				sh 'pwd'
 				sh 'ls -lrt'
 				sh './commands.sh'
 			}
 		}
 	}
 	
 }
}
