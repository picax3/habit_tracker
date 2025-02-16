import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit

def main():
    habits: list[Habit] = [
        track_habit('Coffee', datetime(2025, 2, 14, 6), cost=0.57, minutes_used=5, difficulty=2),
        track_habit('Redbulls', datetime(2025, 1, 29, 6), cost=11, minutes_used=5, difficulty=4),
        track_habit('Jerking', datetime(2025, 2,11, 6), cost=0, minutes_used=40, difficulty=3),
        track_habit('Snorting rits', datetime(2025, 2, 16, 6), cost=40, minutes_used=720, difficulty=5),
        track_habit('pepsi', datetime(2025, 2, 13, 6), cost=3, minutes_used=20, difficulty=1),
        track_habit('black tea/green tea', datetime(2025, 2, 16, 6), cost=0.25, minutes_used=5, difficulty=1)
    ]

    # convert Habit objects to dictionaries
    habit_dicts = [habit.__dict__ for habit in habits]

    # create the DataFrame
    df = pd.DataFrame(habit_dicts)

    # Print the DataFrame in a tabular format
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ =='__main__':
    main()