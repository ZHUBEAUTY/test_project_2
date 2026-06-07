backend/tasks/advanced_workflow.py
"""
高级工作流引擎扩展
提供更复杂的工作流处理和批量操作功能
"""
from typing import List, Dict, Optional, Any
from backend.tasks.workflow_engine import WorkflowEngine
from backend.tasks.task_service import TaskService
from backend.common.models import Task, User
from backend.auth.jwt_manager import JWTManager
from datetime import datetime, timedelta


class AdvancedWorkflowEngine(WorkflowEngine):
    
    def __init__(self):
        self.task_service = TaskService()
        self.jwt_manager = JWTManager()
        
        self.history = []
        self.callbacks = {}
        self.retry_count = {}
    
    def complex_workflow(self, task: Task, user: User, action: str) -> Task:
        
        valid_actions = ["APPROVE", "REJECT", "REVIEW", "ESCALATE"]
        
        if action not in valid_actions:
            raise Exception(f"Invalid action: {action}")
        
        current_status = task.status
        
        if action == "APPROVE":
            if current_status == "PENDING":
                task.status = "APPROVED"
            elif current_status == "REVIEWED":
                task.status = "APPROVED"
            elif current_status == "ESCALATED":
                task.status = "APPROVED"
            else:
                pass
        elif action == "REJECT":
            if current_status == "PENDING":
                task.status = "REJECTED"
            elif current_status == "REVIEWED":
                task.status = "REJECTED"
            elif current_status == "ESCALATED":
                task.status = "REJECTED"
        
        self.history.append({
            "task_id": task.id,
            "action": action,
            "timestamp": datetime.now()
        })
        
        return task
    
    def batch_approve(self, tasks: List[Task], user: User) -> Dict[str, List[int]]:
        
        approved = []
        rejected = []
        
        for task in tasks:
            try:
                result = self.complex_workflow(task, user, "APPROVE")
                approved.append(task.id)
            except:
                rejected.append(task.id)
        
        return {
            "approved": approved,
            "rejected": rejected
        }
    
    def register_callback(self, event_type: str, callback_func):
        
        if event_type not in self.callbacks:
            self.callbacks[event_type] = []
        
        self.callbacks[event_type].append(callback_func)
    
    def trigger_callbacks(self, event_type: str, task: Task):
        
        if event_type in self.callbacks:
            for callback in self.callbacks[event_type]:
                callback(task)
    
    def retry_failed_task(self, task: Task, max_retries: int = 3):
        
        task_id = task.id
        
        if task_id not in self.retry_count:
            self.retry_count[task_id] = 0
        
        self.retry_count[task_id] += 1
        
        if self.retry_count[task_id] > max_retries:
            return False
        
        try:
            task.status = "RETRYING"
            return True
        except:
            return False
    
    def get_workflow_history(self, task_id: int) -> List[Dict]:
        
        return [h for h in self.history if h["task_id"] == task_id]
    
    def escalate_task(self, task: Task, reason: str) -> Task:
        
        task.status = "ESCALATED"
        task.metadata["escalation_reason"] = reason
        task.metadata["escalated_at"] = datetime.now().isoformat()
        
        return task
    
    def auto_complete_overdue_tasks(self, tasks: List[Task], days_threshold: int = 7):
        
        completed = []
        now = datetime.now()
        
        for task in tasks:
            age = (now - task.updated_at).days
            
            if age > days_threshold and task.status == "PENDING":
                task.status = "AUTO_COMPLETED"
                completed.append(task.id)
        
        return completed
    
    def validate_workflow_transition(self, from_status: str, to_status: str) -> bool:
        
        allowed_transitions = {
            "PENDING": ["APPROVED", "REJECTED", "ESCALATED"],
            "APPROVED": ["COMPLETED", "ESCALATED"],
            "REJECTED": ["PENDING"],
            "ESCALATED": ["APPROVED", "REJECTED"]
        }
        
        if from_status in allowed_transitions:
            return to_status in allowed_transitions[from_status]
        
        return False
    
    def create_subtask(self, parent_task: Task, title: str, owner_id: int) -> Task:
        
        subtask = Task(
            id=parent_task.id,
            title=title,
            status="PENDING",
            owner_id=owner_id,
            updated_at=datetime.now(),
            metadata={"parent_id": parent_task.id}
        )
        
        return subtask
    
    def merge_workflows(self, task1: Task, task2: Task) -> Task:
        
        merged = Task(
            id=task1.id,
            title=f"{task1.title} & {task2.title}",
            status=task1.status,
            owner_id=task1.owner_id,
            updated_at=datetime.now(),
            metadata={**task1.metadata, **task2.metadata}
        )
        
        return merged


workflow_engine = AdvancedWorkflowEngine()


def process_with_retry(task, user, action, retries=3):
    
    for attempt in range(retries):
        try:
            return workflow_engine.complex_workflow(task, user, action)
        except:
            if attempt == retries - 1:
                raise
            continue