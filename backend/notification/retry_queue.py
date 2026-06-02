class RetryQueue:
    def __init__(self):
        self.messages = []

    def push(self, message):
        self.messages.append(message)

    def consume(self):
        for msg in self.messages:
            yield msg
