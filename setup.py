import os, math, sys, subprocess

OS_bit = (round(math.log(sys.maxint,2)+1))
cmd = "firefox -v"

os.system("sudo apt-get install python-pip && sudo apt-get install tor")
os.system("pip install -U selenium && sudo apt-get install firefoxdriver -y")
os.system("pip install mechanize && pip install requests")
os.system("pip install stem && pip install pyvirtualdisplay && apt-get install xvfb")

print("\n \n {} \n \n".format(OS_bit))


os.system('firefox -v > tmp')
result    =  open('tmp', 'r').read()
marker    = result.find('Firefox') + 8
fversion  = result[marker:].splitlines()[0]
firefoxV,b,c = fversion.split(".")
os.remove('tmp')

second = 0

if OS_bit == 64:

    bit = 64

elif OS_bit == 32:

    bit = 32

if firefoxV < 53:

    first = 16
    second = 1

if firefoxV == 53 or firefoxV == 54:

    first = 18

if firefoxV > 54:

    first = 19

os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,bit))
os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,bit))
os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,bit))


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

print("{} {} {} {}".format(firefoxV,first,second,bit))
