import datetime
import matplotlib.pyplot as plt
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog
import json
import reviews

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Create the main window (you can hide it if you prefer)
root = tk.Tk()
root.withdraw()

game_reviews_dict = {}


for game, app_id in reviews.gameDict.items():
    print(f"Select {game} Reviews")
    file_path = filedialog.askopenfilename(initialdir=script_directory, title=f"Select {game} Reviews JSON file")
    
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            game_reviews_dict[game] = json.load(file)
    else:
        print(f"No file selected for {game}")


def process_reviews(reviews, is_positive):
    review_counts = {}
    
    for review_id, review_data in reviews.items():
        timestamp = review_data['timestamp_created']
        voted_up = review_data['voted_up']

        if voted_up == is_positive:
            review_date = datetime.datetime.utcfromtimestamp(timestamp).date()
            review_counts[review_date] = review_counts.get(review_date, 0) + 1
            
    return review_counts
def plot_reviews(game_name, positive_counts, negative_counts):
    dates_positive = sorted(positive_counts.keys())
    positive_review_counts = [positive_counts[date] for date in dates_positive]
    dates_negative = sorted(negative_counts.keys())
    negative_review_counts = [negative_counts[date] for date in dates_negative]
    
    plt.plot(dates_positive, positive_review_counts, label=f'{game_name} - Positive Reviews', marker='o')
    plt.plot(dates_negative, negative_review_counts, label=f'{game_name} - Negative Reviews', marker='o')


# Create a single figure
plt.figure(figsize=(10, 6))


# Plot the review data and player data on the same graph
for game_name, game_reviews in game_reviews_dict.items():
    positive_counts = process_reviews(game_reviews, is_positive=True)
    negative_counts = process_reviews(game_reviews, is_positive=False)
    plot_reviews(game_name, positive_counts, negative_counts)


# Set labels and title
plt.xlabel('Date')
plt.ylabel('Reviews')
plt.title('Daily Amount of Positive and Negative Reviews')
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
