class BoundedCounter:
    def __init__(self, low: int, high: int, start: int, neigh: 'BoundedCounter' = None):
        self.lower_bound = low
        self.upper_bound = high
        self.current_value = start
        self.neighbor = neigh

    def __repr__(self):
        return f"BoundedCounter({self.lower_bound}, {self.upper_bound}, {self.current_value})"

    def __str__(self):
        return f"{self.current_value} (Range: {self.lower_bound}-{self.upper_bound})"

class ListCounter(BoundedCounter):
    def __init__(self, items: list, neigh: 'ListCounter' = None):
        self.items = items

    def __repr__(self):
        return f"ListCounter({self.items})"

class BaseballCounter(BoundedCounter):
    def __init__(self, balls: int, strikes: int, outs: int, half_inning: int, inning: int):
        self.balls = 0
        self.strikes = 0
        self.outs = 0
        self.half_inning = 0
        self.inning = 0

    def ball(self):
        pass

    def strike(self):
        pass

    def out(self):
        pass

    def new_batter(self):
        pass

    def new_game(self):
        pass
