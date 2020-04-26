from mycroft import MycroftSkill, intent_file_handler


class MyUpdate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('update.my.intent')
    def handle_update_my(self, message):
        self.speak_dialog('update.my')


def create_skill():
    return MyUpdate()

