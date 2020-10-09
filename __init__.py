import io
import requests
import json
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
        r = apiResponse(ipAddress,"main/getStatus")
        t = str(r.json().get("power"))
        print t
        #self.speak_dialog('prayers.catholic')
        self.speak_dialog('prayers.catholic', {"status": t})


def create_skill():
    return CatholicPrayers()

