#!/bin/bash
#docker kill flask-container
#docker rm flask-container
docker run -di --name flask-container -p 5010:5000 flask-test-new /bin/bash