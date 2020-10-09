import io
import requests
import json
import time
from mycroft import MycroftSkill, intent_file_handler

def apiResponse(ipAddress,cmd):
    uri="http://" + str(ipAddress) + "/YamahaExtendedControl/v1/" + str(cmd)
    response = requests.get(uri)
    return response

class CatholicPrayers(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('prayers.catholic.intent')
    def handle_prayers_catholic(self, message):
        ipAddress = self.settings["yamaha_ip"]
        #self.log.info(ipAddress)
        r = apiResponse(ipAddress,"main/getStatus")
        t = str(r.json().get("power"))
        if str(r.json().get("power")) == "standby":
            apiResponse(ipAddress,"main/setPower?power=on")
            time.sleep(8)
            
        if str(r.json().get("input")) != "aux":
            apiResponse(ipAddress,"main/setInput?input=aux")
        apiResponse(ipAddress,"main/setVolume?volume=125")
        self.log.info(t)
        #self.speak_dialog('prayers.catholic')
        self.speak_dialog('prayers.catholic', {"status": t})


def create_skill():
    return CatholicPrayers()

