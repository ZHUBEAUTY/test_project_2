from datetime import datetime, timedelta
from backend.tasks.task_repository import DB

class CleanupWorker:
    def cleanup(self):
        now = datetime.now()

        for task_id, task in list(DB.items()):
            if task.updated_at < now - timedelta(days=7):
                del DB[task_id]
