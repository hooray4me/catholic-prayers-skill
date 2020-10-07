from mycroft import MycroftSkill, intent_file_handler


class CatholicPrayers(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('prayers.catholic.intent')
    def handle_prayers_catholic(self, message):
        self.speak_dialog('prayers.catholic')


def create_skill():
    return CatholicPrayers()

