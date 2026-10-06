class Week():
    def __init__(self, num):
        self.week_num = num 
        self.Points = {}

    def _add_point_sections(self, Points:list):
        for p in Points:
            self.Points[p.label] = []

    