import requests

class APIrequest:



    

    def getDataFromAmos(self,orden):
        INIT_REQUEST = r"http://jn1pv12:8001//Backlog/getOneAnalisis?orden="
        r = requests.get(INIT_REQUEST+orden)
        return r.text