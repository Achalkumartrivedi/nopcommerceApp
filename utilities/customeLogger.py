import logging

class LogGenclass():
   @staticmethod
   def loggenmethod():
       for handler in logging.root.handlers[:]:
           logging.root.removeHandler(handler)
           logging.basicConfig(filename=r'C:\Users\achal\PycharmProjects\nopcommerceApp\Logs\automation.log', format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
           logger = logging.getLogger()
           logger.setLevel(logging.INFO)
       return logger



#filename='../Logs/automation.log'
#call 'loggenmethod' method from 'LoGgenClass' class- return logger object
#logger.setLevel(logging.INFO) //-if not mentioned in basicconfig write by setlevel()