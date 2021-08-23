import pandas as pd
from Player import Player, s, bran, eli, mal, sab
import math
import matplotlib.pyplot as plt

season = 2022


def player_season_standings():
    summary = pd.DataFrame()
    summary["Year"] = [season] * 4
    summary["Player"] = [sab.player_name, mal.player_name, bran.player_name, eli.player_name]
    summary["Mp"] = [sum(sab.mini_standings()["MP"]), sum(mal.mini_standings()["MP"]),
                     sum(bran.mini_standings()["MP"]), sum(eli.mini_standings()["MP"])]
    summary["W"] = [sum(sab.mini_standings()["W"]), sum(mal.mini_standings()["W"]),
                    sum(bran.mini_standings()["W"]), sum(eli.mini_standings()["W"])]
    summary["D"] = [sum(sab.mini_standings()["D"]), sum(mal.mini_standings()["D"]),
                    sum(bran.mini_standings()["D"]), sum(eli.mini_standings()["D"])]
    summary["L"] = [sum(sab.mini_standings()["L"]), sum(mal.mini_standings()["L"]),
                    sum(bran.mini_standings()["L"]), sum(eli.mini_standings()["L"])]
    summary["Pts"] = [sum(sab.mini_standings()["Pts"]), sum(mal.mini_standings()["Pts"]),
                      sum(bran.mini_standings()["Pts"]), sum(eli.mini_standings()["Pts"])]
    summary["Pts/G"] = (summary["Pts"] / summary["Mp"]).round(2)
    summary["GF"] = [sum(sab.mini_standings()["GF"]), sum(mal.mini_standings()["GF"]),
                     sum(bran.mini_standings()["GF"]), sum(eli.mini_standings()["GF"])]
    summary["GA"] = [sum(sab.mini_standings()["GA"]), sum(mal.mini_standings()["GA"]),
                     sum(bran.mini_standings()["GA"]), sum(eli.mini_standings()["GA"])]
    summary["GD"] = [sum(sab.mini_standings()["GD"]), sum(mal.mini_standings()["GD"]),
                     sum(bran.mini_standings()["GD"]), sum(eli.mini_standings()["GD"])]
    summary = summary.sort_values(["Pts/G","GD"], ascending=False).reset_index(drop=True)
    return summary


def player_season_Xstandings():
    xsummary = pd.DataFrame()
    xsummary["Year"] = [season] * 4
    xsummary["Player"] = [sab.player_name, mal.player_name, bran.player_name, eli.player_name]
    xsummary["Mp"] = [sum(sab.expected_mini_standings()["MP"]), sum(mal.expected_mini_standings()["MP"]),
                      sum(bran.expected_mini_standings()["MP"]), sum(eli.expected_mini_standings()["MP"])]
    xsummary["xW"] = [sum(sab.expected_mini_standings()["xW"]), sum(mal.expected_mini_standings()["xW"]),
                      sum(bran.expected_mini_standings()["xW"]), sum(eli.expected_mini_standings()["xW"])]
    xsummary["xD"] = [sum(sab.expected_mini_standings()["xD"]), sum(mal.expected_mini_standings()["xD"]),
                      sum(bran.expected_mini_standings()["xD"]), sum(eli.expected_mini_standings()["xD"])]
    xsummary["xL"] = [sum(sab.expected_mini_standings()["xL"]), sum(mal.expected_mini_standings()["xL"]),
                      sum(bran.expected_mini_standings()["xL"]), sum(eli.expected_mini_standings()["xL"])]
    xsummary["xPts"] = [sum(sab.expected_mini_standings()["xPts"]), sum(mal.expected_mini_standings()["xPts"]),
                        sum(bran.expected_mini_standings()["xPts"]), sum(eli.expected_mini_standings()["xPts"])]
    xsummary["xPts/G"] = (xsummary["xPts"] / xsummary["Mp"]).round(2)
    xsummary["xGF"] = [sum(sab.expected_mini_standings()["xGF"]), sum(mal.expected_mini_standings()["xGF"]),
                       sum(bran.expected_mini_standings()["xGF"]), sum(eli.expected_mini_standings()["xGF"])]
    xsummary["xGA"] = [sum(sab.expected_mini_standings()["xGA"]), sum(mal.expected_mini_standings()["xGA"]),
                       sum(bran.expected_mini_standings()["xGA"]), sum(eli.expected_mini_standings()["xGA"])]
    xsummary["xGD"] = [sum(sab.expected_mini_standings()["xGD"]), sum(mal.expected_mini_standings()["xGD"]),
                       sum(bran.expected_mini_standings()["xGD"]), sum(eli.expected_mini_standings()["xGD"])]
    xsummary = xsummary.sort_values("xPts/G", ascending=False).reset_index(drop=True)
    return xsummary


def week_by_week_stat(df, stat):
    selected_columns = [col for col in df.columns if stat in col]
    selected_columns.insert(0, "Mp")
    df = df[selected_columns]
    return df


def standings_verse_players(user, opp1, opp2, opp3, win_or_lose="Winner"):
    stat_vs_opp1 = 0
    stat_vs_opp2 = 0
    stat_vs_opp3 = 0
    win_or_lose = win_or_lose.title()
    for u_t in user.players_teams:
        for opp1_t in opp1.players_teams:
            away_vs_opp1 = user.teams_fixture_results()[user.teams_fixture_results()["Home"] == opp1_t]
            home_vs_opp1 = user.teams_fixture_results()[user.teams_fixture_results()["Away"] == opp1_t]
            if win_or_lose == "Draw":
                stat_away = len(away_vs_opp1[away_vs_opp1["Winner"] == "Tie"])
                stat_vs_opp1 += stat_away
                stat_home = len(home_vs_opp1[home_vs_opp1["Winner"] == "Tie"])
                stat_vs_opp1 += stat_home
            else:
                stat_away = len(away_vs_opp1[away_vs_opp1[win_or_lose] == f"{u_t}"])
                stat_vs_opp1 += stat_away
                stat_home = len(home_vs_opp1[home_vs_opp1[win_or_lose] == f"{u_t}"])
                stat_vs_opp1 += stat_home

        for opp2_t in opp2.players_teams:
            away_vs_opp2 = user.teams_fixture_results()[user.teams_fixture_results()["Home"] == opp2_t]
            home_vs_opp2 = user.teams_fixture_results()[user.teams_fixture_results()["Away"] == opp2_t]
            if win_or_lose == "Draw":
                stat_away = len(away_vs_opp2[away_vs_opp2["Winner"] == "Tie"])
                stat_vs_opp2 += stat_away
                stat_home = len(home_vs_opp2[home_vs_opp2["Winner"] == "Tie"])
                stat_vs_opp2 += stat_home
            else:
                stat_away = len(away_vs_opp2[away_vs_opp2[win_or_lose] == f"{u_t}"])
                stat_vs_opp2 += stat_away
                stat_home = len(home_vs_opp2[home_vs_opp2[win_or_lose] == f"{u_t}"])
                stat_vs_opp2 += stat_home

        for opp3_t in opp3.players_teams:
            away_vs_opp3 = user.teams_fixture_results()[user.teams_fixture_results()["Home"] == opp3_t]
            home_vs_opp3 = user.teams_fixture_results()[user.teams_fixture_results()["Away"] == opp3_t]
            if win_or_lose == "Draw":
                stat_away = len(away_vs_opp3[away_vs_opp3["Winner"] == "Tie"])
                stat_vs_opp3 += stat_away
                stat_home = len(home_vs_opp3[home_vs_opp3["Winner"] == "Tie"])
                stat_vs_opp3 += stat_home

            else:
                stat_away = len(away_vs_opp3[away_vs_opp3[win_or_lose] == f"{u_t}"])
                stat_vs_opp3 += stat_away
                stat_home = len(home_vs_opp3[home_vs_opp3[win_or_lose] == f"{u_t}"])
                stat_vs_opp3 += stat_home

    return [stat_vs_opp1, stat_vs_opp2, stat_vs_opp3]


sab_weekly = sab.weekly_df()
mal_weekly = mal.weekly_df()
brandon_weekly = bran.weekly_df()
eli_weekly = eli.weekly_df()

player_merge = sab_weekly.merge(mal_weekly, on="Mp", suffixes=("_Sab", "_Mal"))
other_player_merge = brandon_weekly.merge(eli_weekly, on="Mp", suffixes=("_Bra", "_Eli"))
player_weekly_merged = player_merge.merge(other_player_merge, on="Mp")
player_weekly_merged_pts = week_by_week_stat(player_weekly_merged, "Points")


def player_rank_by_week(stat):
    pts_rank = pd.DataFrame()
    players_weekly = week_by_week_stat(player_weekly_merged, stat)
    pts_rank["Mp"] = [i for i in range(1, len(players_weekly) + 1)]
    for player in players_weekly.columns[1:]:
        pts_list = []
        for i in range(len(players_weekly)):
            ranking = players_weekly.iloc[i, 1:].rank(ascending=False)
            pts_list.append(math.floor(ranking[player]))
        pts_rank[player] = pts_list
    return pts_rank


# stand = player_rank_by_week("Points")

# Player vs player standings
sab_wins = standings_verse_players(sab, bran, mal, eli, "Winner")
sab_loss = standings_verse_players(sab, bran, mal, eli, "Loser")
sab_draw = standings_verse_players(sab, bran, mal, eli, "Draw")

sab_vs = pd.DataFrame()
sab_vs["vs_Player"] = [f"{sab.player_name}_V_Brandon", f"{sab.player_name}_V_Malachi", f"{sab.player_name}_V_Eli"]
sab_vs["W"] = sab_wins
sab_vs["L"] = sab_loss
sab_vs["D"] = sab_draw
sab_vs["Pts"] = (sab_vs["W"] *3) + sab_vs["D"]
sab_vs["Pts/G"] = sab_vs["Pts"]/((sab_vs["W"])+(sab_vs["L"])+(sab_vs["D"]))
sab_vs = sab_vs[["vs_Player", "W", "D", "L", "Pts", "Pts/G"]]

mal_wins = standings_verse_players(mal, bran, sab, eli, "Winner")
mal_loss = standings_verse_players(mal, bran, sab, eli, "Loser")
mal_draw = standings_verse_players(mal, bran, sab, eli, "Draw")

mal_vs = pd.DataFrame()
mal_vs["vs_Player"] = [f"{mal.player_name}_V_Brandon", f"{mal.player_name}_V_Sabastian", f"{mal.player_name}_V_Eli"]
mal_vs["W"] = mal_wins
mal_vs["L"] = mal_loss
mal_vs["D"] = mal_draw
mal_vs["Pts"] = (mal_vs["W"] *3) + mal_vs["D"]
mal_vs["Pts/G"] = mal_vs["Pts"]/((mal_vs["W"])+(mal_vs["L"])+(mal_vs["D"]))
mal_vs = mal_vs[["vs_Player", "W", "D", "L", "Pts", "Pts/G"]]

bran_wins = standings_verse_players(bran, mal, sab, eli, "Winner")
bran_loss = standings_verse_players(bran, mal, sab, eli, "Loser")
bran_draw = standings_verse_players(bran, mal, sab, eli, "Draw")


bran_vs = pd.DataFrame()
bran_vs["vs_Player"] = [f"{bran.player_name}_V_Malachi", f"{bran.player_name}_V_Sabastian", f"{bran.player_name}_V_Eli"]
bran_vs["W"] = bran_wins
bran_vs["L"] = bran_loss
bran_vs["D"] = bran_draw
bran_vs["Pts"] = (bran_vs["W"] *3) + bran_vs["D"]
bran_vs["Pts/G"] = bran_vs["Pts"]/((bran_vs["W"])+(bran_vs["L"])+(bran_vs["D"]))
bran_vs = bran_vs[["vs_Player", "W", "D", "L", "Pts", "Pts/G"]]

eli_wins = standings_verse_players(eli, mal, sab, bran, "Winner")
eli_loss = standings_verse_players(eli, mal, sab, bran, "Loser")
eli_draw = standings_verse_players(eli, mal, sab, bran, "Draw")


eli_vs = pd.DataFrame()
eli_vs["vs_Player"] = [f"{eli.player_name}_V_Malachi", f"{eli.player_name}_V_Sabastian", f"{eli.player_name}_V_Brandon"]
eli_vs["W"] = eli_wins
eli_vs["L"] = eli_loss
eli_vs["D"] = eli_draw
eli_vs["Pts"] = (eli_vs["W"] *3) + eli_vs["D"]
eli_vs["Pts/G"] = bran_vs["Pts"]/((eli_vs["W"])+(eli_vs["L"])+(eli_vs["D"]))
eli_vs = eli_vs[["vs_Player", "W", "D", "L", "Pts", "Pts/G"]]


standings = s.standings
xstandings = s.xStandings
# Sabastian Team Standings
sab_team_standings = sab.mini_standings()
sab_team_standings.insert(0, "Year", [season] * 5)
sab_team_Xstandings = sab.expected_mini_standings()
sab_team_Xstandings.insert(0, "Year", [season] * 5)
# Malachi Team Standings
mal_team_standings = mal.mini_standings()
mal_team_standings.insert(0, "Year", [season] * 5)
mal_team_Xstandings = mal.expected_mini_standings()
mal_team_Xstandings.insert(0, "Year", [season] * 5)
# Brandon Team Standings
bran_team_standings = bran.mini_standings()
bran_team_standings.insert(0, "Year", [season] * 5)
bran_team_Xstandings = bran.expected_mini_standings()
bran_team_Xstandings.insert(0, "Year", [season] * 5)
# Eli Team Standings
eli_team_standings = eli.mini_standings()
eli_team_standings.insert(0, "Year", [season] * 5)
eli_team_Xstandings = eli.expected_mini_standings()
eli_team_Xstandings.insert(0, "Year", [season] * 5)

# Creates the workbook
writer = pd.ExcelWriter(fr"C:\Users\sabzu\Documents\All EPL Project Files\Seasons\Fantasy Premier League {season}.xlsx")

# Adds Standings to the Standings sheet
standings.to_excel(writer, sheet_name="Standings", index=False)
xstandings.to_excel(writer, sheet_name="Standings", index=False, startcol=10)
# Add Player Standings to Standings sheet
ps = player_season_standings()
pxs = player_season_Xstandings()
ps.to_excel(writer, sheet_name="Standings", index=False, startcol=20)
pxs.to_excel(writer, sheet_name="Standings", index=False, startcol=20, startrow=7)

player_weekly_merged_pts.to_excel(writer, sheet_name="Standings", index=False, startcol=32)

# Format the column widths of Standings Sheet
sd_sheet = writer.sheets["Standings"]
sd_sheet.set_column('A:A', 13.75)
sd_sheet.set_column('B:J', 5)
sd_sheet.set_column('K:K', 13.75)
sd_sheet.set_column('L:U', 5)
sd_sheet.set_column('W:AA', 5)
sd_sheet.set_column('AB:AB', 5.85)
sd_sheet.set_column('AC:AG', 5)
sd_sheet.set_column('AH:AK', 9.5)

# Add player weekly stats to each players sheet
sab_weekly.to_excel(writer, sheet_name=f"{sab.player_name}")
mal_weekly.to_excel(writer, sheet_name=f"{mal.player_name}")
brandon_weekly.to_excel(writer, sheet_name=f"{bran.player_name}")
eli_weekly.to_excel(writer, sheet_name=f"{eli.player_name}")
# Format the column widths
sab_sheet = writer.sheets["Sabastian"]
sab_sheet.set_column('B:L', 6.5)
sab_sheet.set_column('M:M', 13.75)
sab_sheet.set_column('N:T', 5)

mal_weekly.to_excel(writer, sheet_name="Malachi")
mal_sheet = writer.sheets["Malachi"]
mal_sheet.set_column('B:L', 6.5)
mal_sheet.set_column('M:M', 13.75)
mal_sheet.set_column('N:T', 5)

brandon_weekly.to_excel(writer, sheet_name="Brandon")
bran_sheet = writer.sheets["Brandon"]
bran_sheet.set_column('B:L', 6.5)
bran_sheet.set_column('M:M', 13.75)
bran_sheet.set_column('N:T', 5)

eli_weekly.to_excel(writer, sheet_name="Eli")
eli_sheet = writer.sheets["Eli"]
eli_sheet.set_column('B:L', 6.5)
eli_sheet.set_column('M:M', 13.75)
eli_sheet.set_column('N:T', 5)

# Adds players mini table to each players sheet
sab_team_table = sab.mini_standings()
sab_team_table.insert(0, "Year", [season] * 5)
mal_team_table = mal.mini_standings()
mal_team_table.insert(0, "Year", [season] * 5)
bran_team_table = bran.mini_standings()
bran_team_table.insert(0, "Year", [season] * 5)
eli_team_table = eli.mini_standings()
eli_team_table.insert(0, "Year", [season] * 5)

sab_team_table.to_excel(writer, sheet_name="Sabastian", startcol=11, index=False)
mal_team_table.to_excel(writer, sheet_name="Malachi", startcol=11, index=False)
bran_team_table.to_excel(writer, sheet_name="Brandon", startcol=11, index=False)
eli_team_table.to_excel(writer, sheet_name="Eli", startcol=11, index=False)

sab_Xteam_table = sab.expected_mini_standings()
sab_Xteam_table.insert(0, "Year", [season] * 5)
mal_Xteam_table = mal.expected_mini_standings()
mal_Xteam_table.insert(0, "Year", [season] * 5)
bran_Xteam_table = bran.expected_mini_standings()
bran_Xteam_table.insert(0, "Year", [season] * 5)
eli_Xteam_table = eli.expected_mini_standings()
eli_Xteam_table.insert(0, "Year", [season] * 5)

sab_Xteam_table.to_excel(writer, sheet_name="Sabastian", startcol=11, startrow=7, index=False)
mal_Xteam_table.to_excel(writer, sheet_name="Malachi", startcol=11, startrow=7, index=False)
bran_Xteam_table.to_excel(writer, sheet_name="Brandon", startcol=11, startrow=7, index=False)
eli_Xteam_table.to_excel(writer, sheet_name="Eli", startcol=11, startrow=7, index=False)

# Add player vs other player
sab_vs.to_excel(writer, sheet_name="Sabastian", startcol=22, index=False)
sab_sheet.set_column("W:W", 18.65)
sab_sheet.set_column("X:AA", 5)

mal_vs.to_excel(writer, sheet_name="Malachi", startcol=22, index=False)
mal_sheet.set_column("W:W", 18.65)
mal_sheet.set_column("X:AA", 5)

bran_vs.to_excel(writer, sheet_name="Brandon", startcol=22, index=False)
bran_sheet.set_column("W:W", 18.65)
bran_sheet.set_column("X:AA", 5)

eli_vs.to_excel(writer, sheet_name="Eli", startcol=22, index=False)
eli_sheet.set_column("W:W", 18.65)
eli_sheet.set_column("X:AA", 5)

writer.save()
