from datetime import datetime
from backend.common.models import Task, User
from backend.tasks.task_repository import DB
from backend.tasks.task_service import TaskService

service = TaskService()

def bootstrap():
    DB[1] = Task(
        id=1,
        title="Demo",
        status="TODO",
        owner_id=1,
        updated_at=datetime.utcnow()
    )

    user = User(
        id=1,
        email="admin@example.com",
        roles=["admin"]
    )

    service.update_status(1, "IN_PROGRESS", user)

if __name__ == "__main__":
    bootstrap()
