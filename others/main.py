from backend import db_connect as db
import matplotlib.pyplot as plt
import numpy as np

cur = db.database()


query = """ SELECT TO_CHAR(SAL_ORDER_DT,'YYYY') YEAR,SUM(SAL_PROFIT) INCOME,
            SUM(SAL_RATE) EXPENSE
FROM SAM_SAL_DATA 
GROUP BY TO_CHAR(SAL_ORDER_DT,'YYYY')
ORDER BY 1 """

cur.execute(query)
data = cur.fetchall()

years = [entry[0] for entry in data]
income = [entry[1] for entry in data]
expense = [entry[2] for entry in data]

bar_width = 0.35
file_name = "img.png"
save_path  = f"D:\\Small Projects\\{file_name}"
# Indices for x-axis
indices = np.arange(len(years))

# Plotting the bars
plt.figure(figsize=(10, 6))
bars1 = plt.bar(indices - bar_width/2, income, bar_width, label='Income')
bars2 = plt.bar(indices + bar_width/2, expense, bar_width , label='Expense')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Comparison of Income and Expense for 2020-2023')
plt.xticks(indices, years)
plt.legend()

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f'{height:.2f}', ha='center', va='bottom')

plt.tight_layout()
plt.savefig(save_path, dpi=300)
plt.show()




