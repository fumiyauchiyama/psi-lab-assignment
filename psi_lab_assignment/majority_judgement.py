from dataclasses import dataclass
from enum import IntEnum

from psi_lab_assignment.user import Role, User
from psi_lab_assignment.utils import load_users_from_csv

class GradeMJ(IntEnum):
    A = 1
    B = 2
    C = 3
    D = 4 #それぞれが希望順位に該当


def intermediate_value_idx(grades: list[GradeMJ]) -> int:
    """
    評価リストの中間値のインデックスを計算します。

    引数:
        grades: 評価リスト。
    
    戻り値:
        中間値のインデックス。
    """

    assert len(grades) > 0
    return len(grades) // 2
    
def social_evaluation_vector(user: User, grades: list[GradeMJ]) -> list[GradeMJ]:
    """
    ユーザーの社会的評価ベクトルを計算します。

    引数:
        user: ユーザー。
        grades: 評価リスト。
    
    戻り値:
        社会的評価ベクトル。
    """

    intermediates = []
    sorted_grades = sorted(grades)
    for _ in range(len(grades)):
        idx_to_pop = intermediate_value_idx(sorted_grades)
        intermediates.append(sorted_grades.pop(idx_to_pop))
    return intermediates

def majority_judgement(user_data: list[tuple[User, list[GradeMJ]]]) -> dict[str, list[GradeMJ]]:
    """
    研究室ごとの多数評価法を計算し、中央値の順序をリスト形式で出力します。

    引数:
        user_data: 各ユーザーごとの評価リスト。

    戻り値:
        各研究室の中央値の順序をリスト形式で格納した辞書。
    """
    lab_data = {}

    # ユーザーデータを研究室ごとに分類
    for user, grades in user_data:
        for i, grade in enumerate(grades):
            lab_name = f"Lab{i + 1}"
            if lab_name not in lab_data:
                lab_data[lab_name] = []
            lab_data[lab_name].append(grade)

    result = {}

    # 各研究室ごとの中央値を計算
    for lab, grades in lab_data.items():
        social_evaluations = social_evaluation_vector(None, grades)
        
        result[lab] = social_evaluations

    return result

def calculate_popularity(results: dict[str, list[GradeMJ]]) -> list[tuple[int, list[str]]]:
    """
    各研究室の人気順を計算します。同率の場合は同じ順位を割り当てます。

    引数:
        results: 各研究室の中央値の順序。

    戻り値:
        順位とその順位に対応する研究室名のリスト。
    """
    lab_popularity = {lab: sum(grade.value for grade in grades) for lab, grades in results.items()}
    sorted_labs = sorted(lab_popularity.items(), key=lambda x: x[1])

    rankings = []
    current_rank = 1
    previous_score = None
    same_rank_labs = []

    for lab, score in sorted_labs:
        if score != previous_score:
            if same_rank_labs:
                rankings.append((current_rank, same_rank_labs))
            current_rank = len(rankings) + 1
            same_rank_labs = [lab]
        else:
            same_rank_labs.append(lab)
        previous_score = score

    if same_rank_labs:
        rankings.append((current_rank, same_rank_labs))

    return rankings