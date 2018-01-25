import os, math, sys

OS_bit = (round(math.log(sys.maxint,2)+1))

os.system("sudo apt-get install python-pip python-dev build-essential -y")
os.system("sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-setuptools -y")
os.system("pip install -U selenium && sudo apt-get install firefoxdriver -y")
os.system("pip install mechanize &&  pip install requests && pip install xmpppy==0.5.0rc1")
os.system("pip install stem && pip install pyvirtualdisplay && apt-get install xvfb")

print("\n \n {} \n \n".format(OS_bit))

if OS_bit == 64:

    os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz")
    os.system("tar -xvzf geckodriver-v0.16.1-linux64.tar.gz")
    os.system("rm geckodriver-v0.16.1-linux64.tar.gz")

elif OS_bit == 32:

    os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux32.tar.gz")
    os.system("tar -xvzf geckodriver-v0.16.1-linux32.tar.gz")
    os.system("rm geckodriver-v0.16.1-linux32.tar.gz")

os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")

fp = open("/etc/tor/torrc")
fx = open("/etc/tor/torrc2","w+")

for i, line in enumerate(fp):
    if i+1 == 57 or i+1 == 61:
        line = line.replace("#","")
    fx.write(line)
fp.close()
fx.close()

os.system("rm /etc/tor/torrc && mv /etc/tor/torrc2 /etc/tor/torrc")
os.system("service tor restart && service tor stop")

print("\ntorrc modification success\n")
