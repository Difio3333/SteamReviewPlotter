import steamreviews
import datetime
import json
import time

gameDict = {"Shadow Tactics":418240,"Desperados 3":610370,"Shadow Gambit":1545560}
#edit this dictionary here with your game name and the corresponding steam game id.
#you can find that ID on https://steamdb.info/ on the page for your game.
decision = input("Do you want to download new reviews? Yes/No\n")

if decision == "Yes" or decision == "yes" or decision == "y" or decision == "Y":

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for game in gameDict:
        
        review_dict, query_count = steamreviews.download_reviews_for_app_id(gameDict[game])

        # Specify the file name for saving the review data

        json_file_name = f"{game}_review_data_{now}.json"

        # Save the dictionary as a JSON file
        with open(json_file_name, "w", encoding="utf-8") as json_file:
            json.dump(review_dict["reviews"], json_file)
        print(game,"done")
        time.sleep(5)
        # Open the file in write mode and save the review_dict data
        #with open(file_name, "w", encoding="utf-8") as file:
        #    file.write(str(review_dict["reviews"]))

    print("all done")

else:
    print("You decided to use old data instead.")