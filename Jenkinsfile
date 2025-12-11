pipeline {
    agent any

    // Il job controllerà il repo ogni minuto
    triggers {
        pollSCM('* * * * *')
    }

    stages {

        // (Opzionale ma utile) Stage di debug per vedere i file nel changeset
        stage('Debug changeset') {
            steps {
                script {
                    echo "DEBUG: elenco file nel changeset"
                    currentBuild.changeSets.each { cs ->
                        cs.items.each { entry ->
                            echo "Commit: ${entry.msg}"
                            entry.affectedFiles.each { f ->
                                echo "File modificato: ${f.path}"
                            }
                        }
                    }
                }
            }
        }

        stage('Esegui quando cambia prova.py') {
            when {
                // Esegue lo stage solo se nel changeset c'è il file prova.py
                // (nella root del repo)
                changeset pattern: "prova.py", comparator: "GLOB"
            }
            steps {
                echo "prova.py è stato modificato su Git. Eseguo la pipeline."
                // Assumo che l'agent abbia Python nel PATH
                sh "python prova.py"
            }
        }
    }
}
