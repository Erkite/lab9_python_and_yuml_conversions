class FSO:
    pass

class File(FSO):
    pass

class Folder(FSO):
    def __init__(self, items: list[FSO]):
        self.items = items