import pandas as pd
import sqlite3

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    return df

def store_data_to_db():
    df = clean_data('data/fitness_data.csv')
    conn = sqlite3.connect('database/fitness_tracker.db')
    df.to_sql('fitness_data', conn, if_exists='replace', index=False)
    conn.close()

if __name__ == '__main__':
    store_data_to_db()
    print("✅ Data successfully stored in database.")
