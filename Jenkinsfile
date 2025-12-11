pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Run if prova.py changed') {
            when {
                changeset pattern: "prova.py", comparator: "GLOB"
            }
            steps {
                echo "prova.py è stato modificato. Eseguo la pipeline."
                sh "python3 prova.py"
            }
        }
    }
}
