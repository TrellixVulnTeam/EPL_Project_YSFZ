import pandas as pd

# Cleans the excel fixture file into a data frame that will be used as the basis for this project
# This is STEP 1 of the process to create the new season file


class Fixture_DF:
    def __init__(self):
        # The file being read needs to be the appropriate season
        self._fixture_list = pd.read_excel(r"C:\Users\sabzu\Documents\All EPL Project Files\Fixtures\Fixtures_2020_2021.xlsx", header=1)
        fixture_list = pd.DataFrame(self._fixture_list)

        if "xG" in fixture_list.columns:
            fixture_list = fixture_list[["Day", "Date", "Home", "xG", "Score", "xG.1", "Away", "Referee"]]
            fixture_list = fixture_list.dropna(subset=["Score"])
            fixture_list = fixture_list.reset_index(drop=True)
            fixture_list["xG"] = fixture_list["xG"].round()
            fixture_list["xG.1"] = fixture_list["xG.1"].round()
            self.fixture_list_df = fixture_list

            self.fixture_list_df["Winner"] = None
            self.fixture_list_df["Loser"] = None
            self.fixture_list_df["xWinner"] = None
            self.fixture_list_df["xLoser"] = None
            self._win_loss()
            self._expected_win_loss()

            self.team_list = list(self.fixture_list_df.Home.unique())
            self.team_list.sort()

        else:
            fixture_list = fixture_list[["Day", "Date", "Home", "Score", "Away", "Referee"]]
            fixture_list = fixture_list.dropna(subset=["Score"])
            fixture_list = fixture_list.reset_index(drop=True)
            self.fixture_list_df = fixture_list

            self.fixture_list_df["Winner"] = None
            self.fixture_list_df["Loser"] = None
            self._win_loss()

            self.team_list = list(self.fixture_list_df.Home.unique())
            self.team_list.sort()

    def _win_loss(self):
        for i in range(len(self.fixture_list_df)):
            if self.fixture_list_df.loc[i, "Score"][0] > self.fixture_list_df.loc[i, "Score"][2]:
                self.fixture_list_df.loc[i, "Winner"] = self.fixture_list_df.loc[i, "Home"]
                self.fixture_list_df.loc[i, "Loser"] = self.fixture_list_df.loc[i, "Away"]
            elif self.fixture_list_df.loc[i, "Score"][0] < self.fixture_list_df.loc[i, "Score"][2]:
                self.fixture_list_df.loc[i, "Winner"] = self.fixture_list_df.loc[i, "Away"]
                self.fixture_list_df.loc[i, "Loser"] = self.fixture_list_df.loc[i, "Home"]
            else:
                self.fixture_list_df.loc[i, "Winner"] = "Tie"
                self.fixture_list_df.loc[i, "Loser"] = "Tie"

    def _expected_win_loss(self):
        for i in range(len(self.fixture_list_df)):
            if self.fixture_list_df.loc[i, "xG"] > self.fixture_list_df.loc[i, "xG.1"]:
                self.fixture_list_df.loc[i, "xWinner"] = self.fixture_list_df.loc[i, "Home"]
                self.fixture_list_df.loc[i, "xLoser"] = self.fixture_list_df.loc[i, "Away"]
            elif self.fixture_list_df.loc[i, "xG"] < self.fixture_list_df.loc[i, "xG.1"]:
                self.fixture_list_df.loc[i, "xWinner"] = self.fixture_list_df.loc[i, "Away"]
                self.fixture_list_df.loc[i, "xLoser"] = self.fixture_list_df.loc[i, "Home"]
            else:
                self.fixture_list_df.loc[i, "xWinner"] = "Tie"
                self.fixture_list_df.loc[i, "xLoser"] = "Tie"


