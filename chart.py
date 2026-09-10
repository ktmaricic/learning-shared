import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("survey.csv")
means = df.groupby("group")["score"].mean()
print(means)
means.plot(kind="bar")
plt.ylabel("mean score")
plt.savefig("chart.png")
print("saved chart.png")
