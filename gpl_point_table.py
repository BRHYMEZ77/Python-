teams = [
    {"name": "Kotoko", "points": 25},
    {"name": "Hearts", "points": 23},
    {"name": "Aduana Stars", "points": 18}
]

for team in teams:
    print(f"{team['name']}: {team['points']} points")

team_name = input('Please enter the name of the team you want to update: ').title()
new_points = int(input('Please enter the new points: '))

for team in teams:
    if team['name'].title() == team_name.title():
        team['points'] = new_points
        break
else:
    print('Team not found.')

for team in teams:
    print(f"{team['name']}: {team['points']} points")