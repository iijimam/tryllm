import pandas as pd
import random
from datetime import datetime, timedelta
from faker import Faker
#fake=Faker()
fake = Faker('ja_JP')

# -------------------------------
# パラメータ設定
# -------------------------------
num_persons = 50  # 人数（必要に応じて変更）
start_date_range = datetime(1950, 1, 1)
end_date_range = datetime(2025, 4, 7)

# -------------------------------
# 補助関数: ランダムな日付生成
# -------------------------------
def random_date(start, end):
    """startからendの間でランダムな日付を生成"""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# -------------------------------
# patients.csv の生成
# -------------------------------
persons = []
for i in range(1, num_persons + 1):
    person_id = i
    name =  fake.name()
    gender = random.choice(["M", "F"])
    # 誕生日をランダムに設定
    dob_date = random_date(start_date_range, end_date_range)
    persons.append({
        "PID": person_id,
        "Name": name,
        "Gender": gender,
        "DOB": dob_date.strftime('%Y-%m-%d'),
    })

df_persons = pd.DataFrame(persons)

# -------------------------------
# persons.csv の生成
# -------------------------------
df_persons.to_csv("persons.csv", index=False, encoding="utf-8-sig")

print("persons.csvが生成されました。")