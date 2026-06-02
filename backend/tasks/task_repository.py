from datetime import datetime
from backend.common.models import Task

DB = {}

class TaskRepository:
    def get(self, task_id):
        return DB.get(task_id)

    def save(self, task):
        task.updated_at = datetime.utcnow()
        DB[task.id] = task
        return task
