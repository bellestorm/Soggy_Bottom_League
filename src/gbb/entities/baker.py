class Baker():
    def __init__(self, name):
        self.name = name
        self.weekly_performance = []
        self.accolades = {}

    @property
    def total_points(self):
        return sum(self.weekly_performance)

    def get_week_performance(self, week_num):
        ix = week_num -1
        return self.weekly_performance[ix]

    def _add_bio(self, bio):
        self.bio = bio


    