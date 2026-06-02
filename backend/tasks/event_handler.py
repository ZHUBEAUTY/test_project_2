from backend.notification.email_service import EmailService
from backend.notification.retry_queue import RetryQueue

email_service = EmailService()
retry_queue = RetryQueue()

class EventHandler:
    def task_completed(self, task, user):
        try:
            email_service.send(user.email, f"Task {task.title} completed")
        except Exception:
            pass

        retry_queue.push({
            "task_id": task.id,
            "email": user.email
        })
