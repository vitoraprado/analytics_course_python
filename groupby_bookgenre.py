import pandas as pd
import matplotlib.pyplot as plt

rd_ptrns = pd.read_csv("reading_habits.csv")

genre_counts = rd_ptrns.groupby('Favorite_Book_Genre')['User_ID'].count()

plt.bar(genre_counts.index,genre_counts.values)
plt.show()
