from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class User:
    id: int
    email: str
    roles: List[str] = field(default_factory=list)

@dataclass
class Task:
    id: int
    title: str
    status: str
    owner_id: int
    updated_at: datetime
    metadata: Dict = field(default_factory=dict)
