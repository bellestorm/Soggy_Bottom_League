class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.Bakers = []

    @property
    def total_points(self):
        total_points = 0
        for b in self.Bakers:
            total_points += b.total_points
        return total_points

    def _add_bakers(self, name_list, Bakers):
        for b in Bakers:
            if b.name in name_list:
                self.Bakers.append(b)
                name_list.remove(b.name)