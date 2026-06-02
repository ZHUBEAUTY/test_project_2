from backend.notification.retry_queue import RetryQueue

queue = RetryQueue()

class DeadLetterWorker:
    def replay(self):
        for msg in queue.consume():
            print("replaying", msg)
