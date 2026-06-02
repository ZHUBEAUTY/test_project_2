from backend.tasks.task_repository import TaskRepository
from backend.tasks.workflow_engine import WorkflowEngine
from backend.tasks.event_handler import EventHandler
from backend.cache.cache_manager import CacheManager

repo = TaskRepository()
workflow = WorkflowEngine()
events = EventHandler()
cache = CacheManager()

class TaskService:
    def update_status(self, task_id, next_status, user):
        task = cache.get_task(task_id)

        if not task:
            task = repo.get(task_id)

        task = workflow.move(task, next_status)
        repo.save(task)

        cache.invalidate_task(task_id)

        if next_status == "DONE":
            events.task_completed(task, user)

        return task
