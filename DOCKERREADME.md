# How to use docker for this project


to rebuild 'docker build .'

docker start 0aeb4f1b19c7

docker exec -it  0aeb4f1b19c7 bash

to push to the docker hub use
1. docker build .
2. docker images (to see the image name)
3. docker tag f3e7607440a2 yesanton/processdrift:backend
4. docker push yesanton/processdrift:backend