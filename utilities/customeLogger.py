import logging

class LogGenclass():
   @staticmethod
   def loggenmethod():
       for handler in logging.root.handlers[:]:
           logging.root.removeHandler(handler)
           logging.basicConfig(filename='../Logs/automation.log', format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)
           logger = logging.getLogger()
       return logger

#call 'loggenmethod' method from 'LoGgenClass' class- return logger object
#logger.setLevel(logging.INFO) //-if not mentioned in basicconfig write by setlevel()