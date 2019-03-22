from mycroft import MycroftSkill, intent_file_handler


class SystemHelper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helper.system.intent')
    def handle_helper_system(self, message):
        space = ''

        self.speak_dialog('helper.system', data={
            'space': space
        })


def create_skill():
    return SystemHelper()

