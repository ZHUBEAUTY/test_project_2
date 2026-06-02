from backend.common.config import FEATURE_FLAGS
from .validators import validate_transition

class WorkflowEngine:
    def move(self, task, next_status):
        if not FEATURE_FLAGS["enable_new_workflow"]:
            return self._new_workflow(task, next_status)

        return self._legacy_workflow(task, next_status)

    def _new_workflow(self, task, next_status):
        if validate_transition(task.status, next_status):
            task.status = next_status
        return task

    def _legacy_workflow(self, task, next_status):
        task.status = next_status
        return task
