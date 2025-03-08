import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_chart(file_path):
    df = pd.read_csv(file_path)
    sns.lineplot(x="date", y="calories", data=df)
    plt.title("Calories Burned Over Time")
    plt.show()

if __name__ == '__main__':
    generate_chart('data/fitness_data.csv')
