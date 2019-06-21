from baseball_team import Baseball_Team



print("name", "win", "lose", "draw", "rate")
carp = Baseball_Team("Carp", 88, 51, 4)
tigers = Baseball_Team("Tigers", 78, 61, 4)
baystars = Baseball_Team("Baystars", 73, 65, 5)
giants = Baseball_Team("Giants", 72, 68, 3)
dragons = Baseball_Team("Dragons", 59, 79, 5)
swallows = Baseball_Team("Swallows", 45, 96, 2)

teams = [carp, tigers, baystars, giants, dragons, swallows]
for team in teams:
      team.show_Team_result()