from Clean_Fixture_DF import Fixture_DF
import pandas as pd

# These standings are for the Premier League Teams
# This is STEP 2 of the process to create the new season file
fix = Fixture_DF()


class Standings:
    def __init__(self, EnterYesForXG="No"):
        self._xG = str(EnterYesForXG).title()
        self.standings = pd.DataFrame()
        self.standings["Team"] = fix.team_list
        self.standings["MP"] = None
        self.standings["W"] = None
        self.standings["D"] = None
        self.standings["L"] = None
        self.standings["Pts"] = None
        self.standings["GF"] = None
        if self._xG == "Yes":
            self.standings["xG"] = 0
        self.standings["GA"] = None
        if self._xG == "Yes":
            self.standings["xGA"] = 0
        self.standings["GD"] = None
        if self._xG == "Yes":
            self.standings["xGD"] = 0

        self._win()
        self._loss()
        self._draw()
        self._points()
        self._matches_played()
        self._goals_for()
        self._xG_for()
        self._goals_against()
        self._xG_against()
        self._goal_difference()
        self._xGD()
        self.standings = (self.standings.sort_values(["Pts", "GD"], ascending=False)).reset_index(drop=True)

    def _win(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["Winner"] == f"{i}"])
            self.standings.loc[n, "W"] = wins
            n += 1

    def _loss(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["Loser"] == f"{i}"])
            self.standings.loc[n, "L"] = wins
            n += 1

    def _draw(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["Winner"] == "Tie"])
            self.standings.loc[n, "D"] = wins
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
            self.standings.loc[n, "GF"] = goals
            n += 1

    def _xG_for(self):
        if self._xG == "No":
            pass
        elif "xG" not in fix.fixture_list_df.columns:
            pass
        else:
            n = 0
            for i in fix.team_list:
                goals = 0.0
                # Home xGoals For
                h = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}")])
                h = h.reset_index(drop=True)
                for row in range(len(h)):
                    s = (h["xG"][row])
                    goals += round(s, 2)
                # Away xGoals For
                a = (fix.fixture_list_df[(fix.fixture_list_df["Away"] == f"{i}")])
                a = a.reset_index(drop=True)
                for r in range(len(a)):
                    s = a["xG.1"][r]
                    goals += round(s, 2)
                self.standings.loc[n, "xG"] = goals
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
            self.standings.loc[n, "GA"] = goals
            n += 1

    def _xG_against(self):
        if self._xG == "No":
            pass
        elif "xG.1" not in fix.fixture_list_df.columns:
            pass
        else:
            n = 0
            for i in fix.team_list:
                goals = 0.0
                # Home Goals Against
                h = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}")])
                h = h.reset_index(drop=True)
                for row in range(len(h)):
                    s = h["xG.1"][row]
                    goals += round(s, 2)
                # Away Goals Against
                a = (fix.fixture_list_df[(fix.fixture_list_df["Away"] == f"{i}")])
                a = a.reset_index(drop=True)
                for r in range(len(a)):
                    s = a["xG"][r]
                    goals += round(s, 2)
                self.standings.loc[n, "xGA"] = goals
                n += 1

    def _goal_difference(self):
        self.standings["GD"] = self.standings["GF"] - self.standings["GA"]

    def _xGD(self):
        if self._xG == "No":
            pass
        else:
            self.standings["xGD"] = self.standings["xG"] - self.standings["xGA"]


