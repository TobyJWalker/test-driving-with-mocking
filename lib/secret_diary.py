from lib.diary import Diary

class SecretDiary:
    def __init__(self, diary):
        if type(diary) != Diary:
            raise TypeError('diary must be a Diary object')

        self.diary = diary
        self.locked = True

    def read(self):
        if self.locked:
            return "Go away!"
        else:
            return self.diary.read()

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False