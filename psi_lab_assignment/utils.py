import csv
from pathlib import Path

from psi_lab_assignment.user import Role, User

def load_users_from_csv(
        file_path: str | Path, 
        role: Role,
        email_col_index: int = 0
        ) -> set[User]:
    """
    CSVファイルからユーザー情報を読み込みます。

    引数:
        file_path: CSVファイルのパス。
        role: ユーザーの役割。
        email_col_index: メールアドレスが格納されている列のインデックス。
        
    戻り値:
        ユーザーの集合。
    """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        users = set
        for row in reader:
            users.add(User(email=row[email_col_index], role=role))
    return users