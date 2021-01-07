class CatchError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def ValueErr(self, exc):
        print(exc)
