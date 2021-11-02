class ParseException(BaseException):

    def __init__(self, message, *args: object):
        self.message = message
        super().__init__(*args)

    def __repr__(self):
        return self.message