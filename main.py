class UQCSTalk:
    def __init__(self, name):
        self.name = name
        self.hours = 1

    def get_hours(self):
        return self.hours

    def get_name(self):
        return self.name

    def add_hour(self):
        self.hours += 1
        return True

    