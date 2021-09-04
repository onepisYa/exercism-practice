class Clock:
    def __init__(self, hour, minute):
        self.total_m=(hour*60+minute)%1440 # 1 day = 24 * 60

    def __repr__(self):
        return "{:0>2d}:{:0>2d}".format(*divmod(self.total_m,60))

    def __eq__(self, other):
        return repr(self)==repr(other)

    def __add__(self, minutes):
        self.total_m+=minutes
        return Clock(*divmod(self.total_m,60))

    def __sub__(self, minutes):
        self.total_m-=minutes
        return Clock(*divmod(self.total_m,60))
    