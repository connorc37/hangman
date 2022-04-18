import datetime


class Player:
    def __init__(self, name):
        self.name = name
        self.date = datetime.datetime.now().strftime("%x")

    def to_string(self):
        return f"name: {str(self.name)}, date: {str(self.date)}"
