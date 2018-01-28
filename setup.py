import os, math, sys

OS_bit = (round(math.log(sys.maxint,2)+1))  # get the bit

os.system("sudo apt-get install python-pip && sudo apt-get install tor")   # installing dependencies
os.system("pip install -U selenium")
os.system("pip install mechanize && pip install requests")
os.system("pip install stem && pip install pyvirtualdisplay && apt-get install xvfb")

print("\n \n {} \n \n".format(OS_bit))


os.system('firefox -v > tmp')                  # store result of firefox -v in tmp
result       =  open('tmp', 'r').read()        # result var reads the output
marker       = result.find('Firefox') + 8      # marker marks the 8th letter from the word "Firefox"
version      = result[marker:].splitlines()[0] # spliting the output, the version is something like aa.bb.cc
a,b,c = version.split(".")              # firefoxV is the var with the aa
os.remove('tmp')                               # removing the temporary file


FirefoxVersion = int(a)

second = 0

if OS_bit == 64:

    bit = 64

elif OS_bit == 32:

    bit = 32


if FirefoxVersion  < 53:

    first = 16
    second = 1

elif FirefoxVersion == 53 or FirefoxVersion == 54:

    first = 18

elif FirefoxVersion > 54:

    first = 19

os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.{}.{}/geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,first,second,bit))
os.system("tar -xvzf geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,bit))
os.system("rm geckodriver-v0.{}.{}-linux{}.tar.gz".format(first,second,bit))
os.system("chmod +x geckodriver")
os.system("mv geckodriver /usr/local/bin/")

fp = open("/etc/tor/torrc")
fx = open("/etc/tor/torrc2","w+")     #torrc with edits

for i, line in enumerate(fp):         #some reading and editing action going on here
    if i+1 == 57 or i+1 == 61:
        line = line.replace("#","")
    fx.write(line)
fp.close()
fx.close()

os.system("rm /etc/tor/torrc && mv /etc/tor/torrc2 /etc/tor/torrc")
os.system("service tor restart && service tor stop")

print("\ntorrc modification success\n")
