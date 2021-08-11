from Clean_Fixture_DF import Fixture_DF
import pandas as pd

# These standings are for the Premier League Teams
# This is STEP 2 of the process to create the new season file
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

    def _goal_difference(self):
        self.standings["GD"] = self.standings["GF"] - self.standings["GA"]


class xStandings(Standings):
    def __init__(self):
        super().__init__()

        self.xStandings = pd.DataFrame()
        self.xStandings["Team"] = fix.team_list
        self.xStandings["MP"] = self.standings["MP"]
        self.xStandings["xW"] = None
        self.xStandings["xD"] = None
        self.xStandings["xL"] = None
        self.xStandings["xPts"] = None
        self.xStandings["xGF"] = None
        self.xStandings["xGA"] = None
        self.xStandings["xGD"] = None

        self._xWins()
        self._Draws()
        self._xLoss()
        self._xPts()
        self._xGF()
        self._xGA()
        self._xGDiff()
        self.xStandings = (self.xStandings.sort_values(["xPts", "xGD"], ascending=False)).reset_index(drop=True)

    def _xWins(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["xWinner"] == f"{i}"])
            self.xStandings.loc[n, "xW"] = wins
            n += 1

    def _Draws(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["xWinner"] == "Tie"])
            self.xStandings.loc[n, "xD"] = wins
            n += 1

    def _xLoss(self):
        n = 0
        for i in fix.team_list:
            t = (fix.fixture_list_df[(fix.fixture_list_df["Home"] == f"{i}") | (fix.fixture_list_df["Away"] == f"{i}")])
            wins = len(t[t["xLoser"] == f"{i}"])
            self.xStandings.loc[n, "xL"] = wins
            n += 1

    def _xPts(self):
        self.xStandings["xPts"] = (self.xStandings["xW"] * 3) + (self.xStandings["xD"])

    def _xGF(self):
        if "xG" not in fix.fixture_list_df.columns:
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
                self.xStandings.loc[n, "xGF"] = round(goals)
                n += 1

    def _xGA(self):
        if "xG.1" not in fix.fixture_list_df.columns:
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
                self.xStandings.loc[n, "xGA"] = round(goals)
                n += 1

    def _xGDiff(self):
            self.xStandings["xGD"] = self.xStandings["xGF"] - self.xStandings["xGA"]


