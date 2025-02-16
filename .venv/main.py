import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit

def main():
    habits: list[Habit] = [
        track_habit('Coffee', datetime(2025, 2, 14, 6), cost=1, minutes_used=5, difficulty=3)
    ]

    # convert Habit objects to dictionaries
    habit_dicts = [habit.__dict__ for habit in habits]

    # create the DataFrame
    df = pd.DataFrame(habit_dicts)

    # Print the DataFrame in a tabular format
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ =='__main__':
    main()