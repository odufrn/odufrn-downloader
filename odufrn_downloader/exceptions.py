class odufrException(Exception):
    def __init__(self):
        default_message = 'Default Exception!'
        super().__init__()


class odufrIOError(odufrException):
    def __init__(self):
        default_message = 'odufrIOError Exception!'
        super().__init__()
