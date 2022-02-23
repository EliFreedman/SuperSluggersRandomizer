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
  #
  # A Captain has an index between 2 - 13.
  # A Player has an index between 14 - 72
  #
  # The first player in each team should be a captain.

  # Random Captains
  captainRoster = random.sample(names[2:13], 2)

  team1.append(captainRoster[0])
  team2.append(captainRoster[1])
  
  # Create a list of 16 random players and captains

  # Removes the 2 captains chosen and readds them after roster
  t1c = team1[0]
  t2c = team2[0]
  names.remove(t1c)
  names.remove(t2c)
  roster = random.sample(names[2:70], 16)
  names.insert(2, t1c)
  names.insert(2, t2c)

  # Add players from roster into each team
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

def ranStadium():

  # There are 15 stadiums
  # Some of the stadiums have two variations: Day and Night
  #
  # All stadiums fall between the index 73 - 87

  # Random Stadium
  stadium = random.sample(names[73:87], 1)

  # Output
  print('\nStadium:')
  print(stadium[0])

def main():
  
  ranTeam()
  ranStadium()

main()
