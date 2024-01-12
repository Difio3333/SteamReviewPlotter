# SteamReviewPlotter

SteamReviewPlotter is a simple program that enables you to plot positive and negative Steam reviews on a chart over time.

## Dependencies

Make sure to install the following dependencies before running the program:

```bash
pip install steamreviews
pip install matplotlib
```

## Getting Started

Open the reviews.py file.

Edit the gameDict dictionary with the game name and the corresponding Steam ID. You can find the ID on steamdb.info.

Run plotting.py.

Select the corresponding JSON files you've downloaded.

## Example Plot

![ShowcasePicture](https://github.com/Difio3333/SteamReviewPlotter/assets/86922197/925b46fd-48c8-448d-b17e-d2bde540f6b3)

## Sample Configuration (reviews.py)

```bash
gameDict = {
    "Shadow Tactics": 418240,
    "Desperados 3": 610370,
    "Shadow Gambit": 1545560
}
```
