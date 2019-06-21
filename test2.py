from test import BaseballTeam

carp = BaseballTeam('Carp', 88, 51, 4)
tigers = BaseballTeam('Tigers', 78, 61, 4)
baystars = BaseballTeam('Baystars', 73, 65, 5)
giants = BaseballTeam('Giants', 72, 68, 3)
dragons = BaseballTeam('Dragons', 59, 79, 5)
swallows = BaseballTeam('Swallows', 45, 96, 2)

teams = [carp, tigers, baystars, giants, dragons, swallows]
for team in teams:
    team.show_team_result()