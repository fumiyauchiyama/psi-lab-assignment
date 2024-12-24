from dataclasses import dataclass
from enum import IntEnum

from psi_lab_assignment.user import Role, User
from psi_lab_assignment.utils import load_users_from_csv

class GradeMJ(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4

def intermediate_value_idx(grades: list[GradeMJ]) -> int:
    """
    Compute the index of the intermediate value of a list of grades.
    
    Args:
        grades: A list of grades.
    
    Returns:
        The index of the intermediate value.
    """
    assert len(grades) > 0
    return len(grades) // 2
    
def social_evaluation_vector(user: User, grades: list[GradeMJ]) -> list[GradeMJ]:
    """
    Compute the social evaluation vector of a user.
    
    Args:
        user: The user.
        grades: The grades.
    
    Returns:
        The social evaluation vector.
    """
    intermediates = []
    sorted_grades = sorted(grades)
    for _ in range(len(grades)):
        idx_to_pop = intermediate_value_idx(sorted_grades)
        intermediates.append(sorted_grades.pop(idx_to_pop))
    return intermediates

def majority_judgement(data: list[tuple[User, list[GradeMJ]]]) -> list[tuple[User, GradeMJ]]:
    """
    Compute the majority judgement of a list of users.

    Args:
        data: The data.

    Returns:
        The majority judgement.
    """
    majority_judgement = []
    for user, grades in data:
        social_evaluation = social_evaluation_vector(user, grades)
        majority_judgement.append((user, social_evaluation[0]))
    # sort by grade list
    majority_judgement_sorted = sorted(majority_judgement, key=lambda x: x[1])
    return majority_judgement_sorted
