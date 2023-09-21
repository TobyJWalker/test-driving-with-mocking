class Diary:
    def __init__(self, contents):
        if type(contents) != str:
            raise TypeError('contents must be a string')
        if contents.strip() == "":
            raise ValueError('contents must not be empty')
        self.contents = contents

    def read(self):
        return self.contents