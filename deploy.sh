#!/bin/bash
#docker kill flask-container
#docker rm flask-container
docker run -i --name flask-container -p 5000:5000 flask-test-new bash