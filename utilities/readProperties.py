import configparser
import datetime
import os


config = configparser.RawConfigParser()
config.read(r'C:\Users\achal\PycharmProjects\nopcommerceApp\Configuration\config.ini')

# configparser - class
# Rawconfigparser() - method
# create object as 'config'


#config.read(os.path.join(os.path.dirname(__file__), 'config', 'config.ini'))


#  '.\\Configuration\\config.ini' //it is not working path
#  r'C:\Users\achal\PycharmProjects\nopcommerceApp\Configuration\config.ini'   //it is working path



# how that we can value
# like page object classmethod
# three staticmethod - directly access by class name without creating object
# create method for every variable


class ReadConfig():
    @staticmethod
    def getBaseURL() :
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getUsername():
        email = config.get('common info', 'username')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getEmail():
        mail = config.get('common info', 'email')
        return mail

    @staticmethod
    def getLoginscreenshot():
        path = config.get('common info', 'ss_loginpage')
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.chdir(path)
        NewFolder = 'Test_1_Login_' + DateString
        os.makedirs(NewFolder)
        return NewFolder

    @staticmethod
    def getDashboardscreenshot():
        path = config.get('common info', 'ss_dashboad')
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.chdir(path)
        NewFolder = 'Test_2_Dashboard_' + DateString
        os.makedirs(NewFolder)
        return NewFolder

    @staticmethod
    def getDDTscreenshot():
        path = config.get('common info', 'ss_ddt')
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.chdir(path)
        NewFolder = 'Test_DDT_' + DateString
        os.makedirs(NewFolder)
        return NewFolder


"""
It is for common screenshot folder

    @staticmethod
    def getDirectory():
        path = config.get('common info', 'direcrotypath')
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        os.chdir(path)
        NewFolder = 'Test_shots_' + DateString
        os.makedirs(NewFolder)
        return NewFolder
"""








"""
1) import configparser

2) call method 'RawConfigParcer()' of 'configParser' ,create 'config' object
code: config = configparser.RawConfigParser()

3) use config.read() for read config.ini file
code : config.read(".\\Configuration\\config.ini")
 
4)user object method read() for location on 'config.ini' file
code: config.read()

5)make static method for each variable in class 
code :class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseurl')
        return url
        
6)import package in 'testcase.py' file for access static methods
( from utilites.readProperties import Readconfig )  

Configuration file parser.

A configuration file consists of sections, lead by a "[section]" header,
and followed by "name: value" entries, with continuations and such in
the style of RFC 822.

Intrinsic defaults can be specified by passing them into the
ConfigParser constructor as a dictionary.

class:

ConfigParser -- responsible for parsing a list of
                    configuration files, and managing the parsed database.      

"""