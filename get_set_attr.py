# Reminder

class Attributer(object):
    def __getattr__(self, name):
        print("attribute name", name)
    def __setattr__(self, name, value):
        print("Set", name, "To", value)

att_instance = Attributer()

att_instance.test
att_instance.test = 12345
