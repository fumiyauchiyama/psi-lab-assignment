import random
from psi_lab_assignment.user import User, Role
from psi_lab_assignment.majority_judgement import GradeMJ, majority_judgement, calculate_popularity

# ランダムなデータを生成する関数
def generate_random_data(num_users=10, num_grades=5):
    """
    ランダムなユーザーデータと評価データを生成します。

    引数:
        num_users: 学生の数。
        num_grades: 各ユーザーに割り当てる研究室の数。

    戻り値:
        ランダムに生成された (User, List[GradeMJ]) のリスト。
    """
    data = []
    for i in range(num_users):
        # ユーザーをランダムに作成
        user = User(email=f"user{i}@example.com", role=Role.STUDENT)
        
        # ランダムな評価リストを作成
        grades = [random.choice(list(GradeMJ)) for _ in range(num_grades)]
        
        data.append((user, grades))
    return data

def main():
    # ランダムデータ生成
    user_data = generate_random_data(num_users=55, num_grades=27)

    # 入力データの表示
    print("--- 入力データ ---")
    for user, grades in user_data:
        grade_labels = [grade.name for grade in grades]
        print(f"{user.email}: {grade_labels}")

    # Majority Judgement の実行
    results = majority_judgement(user_data)

    # 結果の表示
    print("\n--- 研究室ごとの中央値の順序 ---")
    for lab, sorted_intermediates in results.items():
        print(f"{lab}: {[grade.name for grade in sorted_intermediates]}")

    # 人気順の計算
    popularity_order = calculate_popularity(results)

    # 人気順の表示
    print("\n--- 研究室の人気順 ---")
    for rank, lab in enumerate(popularity_order, start=1):
        print(f"{lab}")

if __name__ == "__main__":
    main()