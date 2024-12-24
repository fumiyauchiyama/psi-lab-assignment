from enum import Enum
from dataclasses import dataclass

class Role(Enum):
    STUDENT = 'student'
    TEACHER = 'teacher'

@dataclass
class User:
    email: str
    role: Role