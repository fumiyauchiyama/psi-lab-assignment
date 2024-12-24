import csv
from pathlib import Path

from psi_lab_assignment.user import Role, User

def load_users_from_csv(
        file_path: str | Path, 
        role: Role,
        email_col_index: int = 0
        ) -> set[User]:
    """
    Load users from a CSV file.
    
    Args:
        file_path: The path to the CSV file.
        role: The role of the users.
        email_col_index: The index of the column containing the email addresses.
    
    Returns:
        A list of users.
    """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        users = set
        for row in reader:
            users.add(User(email=row[email_col_index], role=role))
    return users