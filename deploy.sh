#!/bin/bash
#docker kill flask-container
#docker rm flask-container
docker run -i --name flask-container -p 8080:8080 flask-test bash