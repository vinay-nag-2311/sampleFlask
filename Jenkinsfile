node {
  stage 'Checkout'
  git url: 'https://github.com/vinay-nag-2311/sampleFlask.git'

  stage 'build'
  docker.build('flask-test')

  stage 'deploy'
  sh './deploy.sh'
}