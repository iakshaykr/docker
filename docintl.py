#!/usr/bin/python

import os

os.system('sudo apt-get install docker.io')
os.system('sudo docker pull registry:2')
os.system('sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2')
os.system('sudo docker tag ubuntu localhost:5000/ubuntu')
os.system('sudo docker push localhost:5000/Ubuntu')
os.system('sudo docker rmi ubuntu')
os.system('sudo docker images')
os.system('sudo docker run -it --rm localhost:5000/ubuntu /bin/bash')
os.system('sudo docker images')
exit()
