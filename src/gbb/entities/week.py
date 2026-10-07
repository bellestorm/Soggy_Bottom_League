class Week():
    def __init__(self, num):
        self.week_num = num 
        self.Points = {}

    def _add_point_sections(self, Points:list):
        for p in Points:
            self.Points[p] = []

    def update_points(self,baker_dict):
        for Baker, list_points in baker_dict.items():
            performance = 0
            for item in list_points:
                Baker.accolades.append(item)
                for label in self.Points:
                    if item == label.label:
                        self.Points[label].append(Baker)
                        performance += label.point_val
            Baker.weekly_performance.append(performance)

