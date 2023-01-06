import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\Logs\\Swag.log',filemode='a',level=logging.INFO,format= '%(asctime)s - %(name)s - %(levelname)s - %(massage)s',datefmt='%d/%m/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        return logger

