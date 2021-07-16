from Clean_Fixture_DF import Fixture_DF
import pandas as pd

# These standings are for the Premier League Teams
fix = Fixture_DF()


class Standings:
    def __init__(self):
        self.standings = pd.DataFrame()
        self.standings["Team"] = fix.team_list
        self.standings["MP"] = None
        self.standings["W"] = None
        self.standings["D"] = None
        self.standings["L"] = None
        self.standings["Pts"] = None
        self.standings["GF"] = None
        self.standings["GA"] = None
        self.standings["GD"] = None

        self._win()
        self._loss()
        self._draw()
        self._points()
        self._matches_played()
        self._goals_for()
        self._goals_against()
        self._goal_difference()
        self.standings = (self.standings.sort_values(["Pts", "GD"], ascending=False)).reset_index(drop=True)

    def _win(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["Winner"] == f"{i}"])
            self.standings["W"][n] = wins
            n += 1

    def _loss(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["Loser"] == f"{i}"])
            self.standings["L"][n] = wins
            n += 1

    def _draw(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["Winner"] == "Tie"])
            self.standings["D"][n] = wins
            n += 1

    def _points(self):
        self.standings["Pts"] = (self.standings["W"] * 3) + (self.standings["D"])

    def _matches_played(self):
        self.standings["MP"] = self.standings["W"] + self.standings["D"] + self.standings["L"]

    def _goals_for(self):
        n = 0
        for i in fix.team_list:
            goals = 0
            # Home Goals For
            h = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}")])
            h = h.reset_index(drop=True)
            for row in range(len(h)):
                s = h["Score"][row]
                goals += int(s[0])
            # Away Goals For
            a = (fix.fixture_list_df[(fix.fixture_list_df["Away"] == f"{i}")])
            a = a.reset_index(drop=True)
            for r in range(len(a)):
                s = a["Score"][r]
                goals += int(s[2])
            self.standings["GF"][n] = goals
            n += 1

    def _goals_against(self):
        n = 0
        for i in fix.team_list:
            goals = 0
            # Home Goals Against
            h = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}")])
            h = h.reset_index(drop=True)
            for row in range(len(h)):
                s = h["Score"][row]
                goals += int(s[2])
            # Away Goals Against
            a = (fix.fixture_list_df[(fix.fixture_list_df["Away"] == f"{i}")])
            a = a.reset_index(drop=True)
            for r in range(len(a)):
                s = a["Score"][r]
                goals += int(s[0])
            self.standings["GA"][n] = goals
            n += 1

    def _goal_difference(self):
        self.standings["GD"] = self.standings["GF"] - self.standings["GA"]


