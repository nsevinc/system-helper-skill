from adapt.intent import IntentBuilder
from mycroft import intent_handler
from mycroft import MycroftSkill
import os, sys

class SystemHelper(MycroftSkill):
    def __init__(self):
        super(SystemHelper, self).__init__(name="SystemHelper")

    @intent_handler(IntentBuilder("CheckAvailDiskSpace").require("CheckDiscAvailSpaceKeyWord"))
    def handle_Check_Avail__Disk_Space(self, message):
        f = os.statvfs("/")
        space = round(f.f_bavail * f.f_frsize / 1024 / 1024)

        if space < 1024:
            unit = 'Megabyte'
        elif space >= 1024:
            unit = 'Gigabyte'
            space = round(space / 1024,2)

        self.speak_dialog('helper.system', data={
            'space': space,'unit': unit
        })

    @intent_handler(IntentBuilder("CheckUsedDisk").require("CheckDiscUsedDiscKeyWord"))
    def handle_Check_Used_Disk(self, message):
        f = os.statvfs("/")
        space = round(f.f_bavail * f.f_frsize / 1024 / 1024)
        total = round(f.f_blocks * f.f_frsize / 1024 / 1024)
        useddisc = total - space

        if useddisc < 1024:
            unit = 'Megabyte'
        elif useddisc >= 1024:
            unit = 'Gigabyte'
            useddisc = round(useddisc / 1024,2)

        self.speak_dialog('check.useddisc', data={
            'used': useddisc,'unit': unit
        })


        def stop(self):
            pass

def create_skill():
    return SystemHelper()

