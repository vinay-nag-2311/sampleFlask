node {
  stage 'Checkout'
  git url: 'https://github.com/vinay-nag-2311/sampleFlask.git'

  stage 'Give permission'
  sh "chmod +x -R ./deploy.sh"

  stage 'Build'
  docker.build('flask-image-new')

  stage 'Deploy'
  sh './deploy.sh'
}