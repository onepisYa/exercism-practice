from typing import Counter, DefaultDict

ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
OUTCOME_MAP = {"win": "loss", "loss": "win", "draw": "draw"}


def tally(results):
    teams = DefaultDict(Counter)
    for result in results:
        home, away, outcome = result.split(";")
        teams[home][outcome] += 1
        teams[away][OUTCOME_MAP[outcome]] += 1
    table = []
    for team, record in sorted(teams.items()):
        w, d, lo = record['win'], record['draw'], record['loss']
        mp, p = w + d + lo, w * 3 + d
        table.append((team, mp, w, d, lo, p))
    table.sort(key=lambda x: x[-1], reverse=True)
    table.insert(0, ("Team", "MP", "W", "D", "L", "P"))

    return [ROW_FORMAT.format(*row) for row in table]