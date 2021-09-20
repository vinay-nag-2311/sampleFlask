#!/bin/bash
#docker stop flask-container
#docker rm flask-container
docker run -di --name flask-container -p 5000:5000 flask-test-new /bin/bash