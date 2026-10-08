from . import baker
from . import week
from . import team
import pandas as pd


class Series():
    def __init__(self, series_num):
        self.series_num = series_num
        self.num_weeks = 10
        self.Bakers = []
        self.Weeks = []
        self.Teams = []

        #set up baseline
        self._add_bakers()
        self._add_teams()
        self._add_points()
        self._add_weeks()

    def _add_bakers(self):
         # Read Bakers file as a dictionary
         b_df = pd.read_csv('./Bakers.csv', header=0)
         bakers_dict = b_df.set_index(b_df.columns[0])[b_df.columns[1]].to_dict()
         for name, bio in bakers_dict.items():
             b = baker.Baker(name)
             b._add_bio(bio)
             self.Bakers.append(b)

    def _add_teams(self):
        # Read Teams file as a dictionary
        df = pd.read_csv('./Teams.csv', header=0)
        teams_dict = df.set_index(df.columns[0]).apply(list, axis=1).to_dict()
        for name, baker_list in teams_dict.items():
                    t = team.Team(name)
                    t._add_bakers(baker_list, self.Bakers)
                    self.Teams.append(t)

    def _add_points(self):
        # Read Points file as a dictionary
        df = pd.read_csv('./points.csv', header=0)
        self.points_dict = df.set_index(df.columns[0])[df.columns[1]].to_dict()

    def _add_weeks(self):
        num = self.num_weeks
        while num > 0:
            w = week.Week(num)
            self.Weeks.append(w)

    def export_series():
        pass

    def update_status():
        pass