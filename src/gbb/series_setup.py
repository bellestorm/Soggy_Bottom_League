from gbb.entities.series import Series

#entry for the data
point_dict = {}

baker_dict = {}

team_dict = {}

#initialize series
series = Series(17)

#add elements
series._add_bakers(baker_dict.keys(), baker_dict)
series._add_points(point_dict)
series._add_weeks()
series._add_teams(team_dict)

#export