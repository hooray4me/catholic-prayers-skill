import io
import requests
import json
import time
from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking

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
            time.sleep(5)
        apiResponse(ipAddress,"main/setVolume?volume=125")
        if str(r.json().get("input")) != "aux":
            apiResponse(ipAddress,"main/setInput?input=aux")
            time.sleep(1)
        #self.log.info(t)
        #self.speak_dialog('prayers.catholic')
        self.speak_dialog('prayers.catholic', {"status": t})
        wait_while_speaking()
        apiResponse(ipAddress,"main/setVolume?volume=" + str(r.json().get("volume")))
        if str(r.json().get("input")) != "aux":
            apiResponse(ipAddress,"main/setInput?input=" + str(r.json().get("input")))
        if str(r.json().get("power")) == "standby":
            apiResponse(ipAddress,"main/setPower?power=standby")


def create_skill():
    return CatholicPrayers()

