import os
os.system("sudo apt-get install python-pip python-dev build-essential -y")
os.system("sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-setuptools -y")
os.system("pip install -U selenium && sudo apt-get install firefoxdriver -y")
os.system("pip install mechanize && pip install paramiko && pip install requests && pip install xmpppy==0.5.0rc1")
os.system("pip install stem && pip install pyvirtualdisplay && apt-get install xvfb")
