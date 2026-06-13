pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Среда деплоя')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying to ${params.ENV}"

                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'local-deploy-server',
                            transfers: [
                                sshTransfer(
                                    cleanRemote: false,
                                    excludes: '.git/**',
                                    execCommand: "echo DEPLOYED_TO_${params.ENV} && ls -la /opt/deploy_app/${params.ENV}",
                                    execTimeout: 120000,
                                    flatten: false,
                                    makeEmptyDirs: false,
                                    noDefaultExcludes: false,
                                    patternSeparator: '[, ]+',
                                    remoteDirectory: "${params.ENV}",
                                    remoteDirectorySDF: false,
                                    removePrefix: '',
                                    sourceFiles: '**/*'
                                )
                            ],
                            usePromotionTimestamp: false,
                            useWorkspaceInPromotion: false,
                            verbose: true
                        )
                    ]
                )
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}
