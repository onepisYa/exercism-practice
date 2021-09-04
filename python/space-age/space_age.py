class SpaceAge:
    period={'earth': 1,
            'mercury': 0.2408467,
            'venus': 0.61519726,
            'mars': 1.8808158,
            'jupiter': 11.862615,
            'saturn': 29.447498,
            'uranus': 84.016846,
            'neptune': 164.79132}

    def __init__(self, seconds):
        self.seconds=seconds
        for on in SpaceAge.period:
            setattr(self,"on_"+ on, self.compute_result(on))
    def compute_result(self,on):
        # 31557600 seconds => 365.25days  => 1 year
        return lambda:round((self.seconds/31557600)/SpaceAge.period[on],2)
