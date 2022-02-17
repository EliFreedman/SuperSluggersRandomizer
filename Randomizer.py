# Import packages
import random
import csv

# Import Super Sluggers Character Data
with open("Sluggers Characters.csv") as file:
    reader = csv.reader(file)
    names = list(reader)

# List of each team
team1 = []
team2 = []

# Write a function that returns a full randomized team
def ranTeam():

  # There are two character types:
  #     Captains and Players.
  
  # A Captain has an index between 2 - 13.
  # A Player has an index between 14 - 72

  # The first player in each team should be a captain.

  # Random Captains
  captainRoster = random.sample(names[2:13], 2)

  team1.append(captainRoster[0])
  team2.append(captainRoster[1])
  
  # Create a list of 16 random players
  roster = random.sample(names[14:72], 16)
  
  for player in roster:
    if len(team1) != 9:
      team1.append(player)
    else:
      team2.append(player)
      
  # Output
  print('Team 1:')
  for player in team1:
    print(player)
  print('\nTeam 2:')
  for player in team2:
    print(player)

ranTeam()
