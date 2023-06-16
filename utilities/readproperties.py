import configparser
config=configparser.RawConfigParser()
config.read(".\\configurations\\confige.ini")
class ReadConfig():
    @staticmethod
    def getappurl(self):
        url=config.get('common info','baseURL')
        return url
    @staticmethod
    def getusermail(self):
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword(self):
        password = config.get('common info', 'password')
        return password

