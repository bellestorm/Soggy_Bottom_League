from gbb.entities.baker import Baker
from gbb.entities.points import Points
from gbb.entities.week import Week
from gbb.entities.team import Team

class Series():
    def __init__(self, series_num):
        self.series_num = series_num
        self.num_weeks = 10
        self.Bakers = []
        self.Points = []
        self.Weeks = []
        self.Teams = []

    def _add_bakers(self, list_of_names, dict_of_bios = None):
        for n in list_of_names:
            b = Baker(n)
            if dict_of_bios is not None:
                if n in dict_of_bios:
                    b._add_bio(dict_of_bios[n])
            self.Bakers.append(b)

    def _add_points(self, point_dict):
        for label, value in point_dict.items():
            p= Points(label, value)
            self.Points.append(p)

    def _add_weeks(self):
        num = self.num_weeks
        while num > 0:
            w = Week(num)
            self.Weeks.append(w)

    def _add_teams(self, teams_dict):
        for name, baker_list in teams_dict.items():
            t = Team(name)
            t._add_bakers(baker_list, self.Bakers)