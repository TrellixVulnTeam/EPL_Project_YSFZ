import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np


# This only gets run at the end of the season to update the stats


def list_of_specific_files(r_then_file_directory):
    files = os.listdir(f"{r_then_file_directory}")
    new_file = []
    for i in files:
        new_file.append(i)
    return new_file


def year_season():
    year = []
    for file_number in range(len(list_of_specific_files(r"C:\Users\sabzu\Documents\Fantasy_EPL"))):
        year_in_file = list_of_specific_files(r"C:\Users\sabzu\Documents\Fantasy_EPL")[file_number]
        split_year_in_file = year_in_file.split(" ")
        for i in split_year_in_file:
            if 'xlsx' in i:
                y = i.split(".")
                year.append(y[0])
    return year


def weekly_stats(Df, player_name_from_class):
    for year in year_season():
        weekly = pd.read_excel(rf"C:\Users\sabzu\Documents\Fantasy_EPL\EPL Season {year}.xlsx",
                               sheet_name=player_name_from_class)
        weekly = weekly.iloc[:, 1:9]
        weekly.insert(0, "Year", [int(year)] * 38)
        df_cols = weekly.columns
        selected_cols = df_cols[2:]
        lists_of_weekly_stats = []

        column = 2
        for col in selected_cols:
            weekly_stat = []
            row = 0
            for i in weekly[col]:
                if i == weekly.iloc[0, column]:
                    weekly_stat.append(i)
                    row += 1
                else:
                    this = int(i) - weekly.iloc[(row - 1), column]
                    weekly_stat.append(this)
                    row += 1
            lists_of_weekly_stats.append(weekly_stat)
            column += 1

        for col in selected_cols:
            i = 0
            weekly[f"Wkly_{col}"] = lists_of_weekly_stats[i]
            lists_of_weekly_stats.pop(0)

        weekly = weekly[
            ['Year', 'Mp', 'Wkly_Wins', 'Wkly_Ties', 'Wkly_Loss', 'Wkly_Points',
             'Wkly_Tot_GF', 'Wkly_Tot_GA', 'Wkly_GD']]

        weekly["Wkly_GF"] = weekly["Wkly_Tot_GF"]
        del weekly["Wkly_Tot_GF"]

        weekly["Wkly_GA"] = weekly["Wkly_Tot_GA"]
        del weekly["Wkly_Tot_GA"]

        if Df.empty:
            Df = weekly
        else:
            Df = pd.concat([Df, weekly])
    return Df


def player_total_stats():
    player_totals = pd.DataFrame()
    cols, cols2 = df_all_time_player_standings.columns[1:7], df_all_time_player_standings.columns[8:12]
    cols = [i for i in cols]
    cols2 = [n for n in cols2]
    cols = cols+cols2

    player = df_all_time_player_standings["Player"].unique()

    for i in cols[1:]:
        totals = []
        for p in player:
            pdf = df_all_time_player_standings[df_all_time_player_standings[cols[0]] == p]
            summ = sum(pdf[i])
            totals.append(summ)
        player_totals[i] = totals
    player_totals.insert(6,"Pts/G", (player_totals["Pts"] / player_totals["Mp"]).round(2))
    player_totals.insert(0,"Player", player)
    player_totals.sort_values(["Pts", "GD"], ascending=False, inplace=True)
    return player_totals


sab_wkly_stats_df = pd.DataFrame()
sabastian_weekly_stats = weekly_stats(sab_wkly_stats_df, "Sabastian")

df_team_standings = pd.DataFrame()
for year in year_season():
    team_standings = pd.read_excel(
        rf"C:\Users\sabzu\Documents\All EPL Project Files\Seasons\Fantasy Premier League {year}.xlsx",
        sheet_name="Standings")
    team_standings = team_standings.iloc[:20, 0:9]
    team_standings.insert(0, "Year", [int(year)] * 20)
    if df_team_standings.empty:
        df_team_standings = team_standings
    else:
        df_team_standings = pd.concat([df_team_standings, team_standings])
df_team_standings = df_team_standings.sort_values(["Pts", "GD"], ascending=False).reset_index(drop=True)

df_team_Xstandings = pd.DataFrame()
for year in year_season():
    if int(year) > 2017:
        team_standings = pd.read_excel(
            rf"C:\Users\sabzu\Documents\All EPL Project Files\Seasons\Fantasy Premier League {year}.xlsx",
            sheet_name="Standings")
        team_standings = team_standings.iloc[:20, 10:19]
        team_standings.insert(0, "Year", [int(year)] * 20)
        if df_team_Xstandings.empty:
            df_team_Xstandings = team_standings
        else:
            df_team_Xstandings = pd.concat([df_team_Xstandings, team_standings])
df_team_Xstandings = df_team_Xstandings.sort_values(["xPts", "xGD"], ascending=False).reset_index(drop=True)

df_all_time_player_standings = pd.DataFrame()
for year in year_season():
    mini_standings = pd.read_excel(
        rf"C:\Users\sabzu\Documents\All EPL Project Files\Seasons\Fantasy Premier League {year}.xlsx",
        sheet_name="Standings")
    mini_standings = mini_standings.iloc[0:4, 20:31]
    mini_standings["Year"] = [int(year)] * 4
    if df_all_time_player_standings.empty:
        df_all_time_player_standings = mini_standings
    else:
        df_all_time_player_standings = pd.concat([df_all_time_player_standings, mini_standings])

df_all_time_player_standings.rename(
    columns={"W.1": "W", "D.1": "D", "L.1": "L", "Pts.1": "Pts", "GF.1": "GF", "GA.1": "GA", "GD.1": "GD"},
    inplace=True)
df_all_time_player_standings = df_all_time_player_standings.sort_values(["Pts/G", "GD"], ascending=False).reset_index(
    drop=True)


df_all_time_player_Xstandings = pd.DataFrame()
for year in year_season():
    if int(year) > 2017:
        mini_standings = pd.read_excel(
            rf"C:\Users\sabzu\Documents\All EPL Project Files\Seasons\Fantasy Premier League {year}.xlsx",
            sheet_name="Standings")
        mini_standings = mini_standings.iloc[7:11, 20:31]
        mini_standings["Year"] = [int(year)] * 4
        if df_all_time_player_Xstandings.empty:
            df_all_time_player_Xstandings = mini_standings
        else:
            df_all_time_player_Xstandings = pd.concat([df_all_time_player_Xstandings, mini_standings])

df_all_time_player_Xstandings.rename(columns={"W.1": "xW", "D.1": "xD", "L.1": "xL", "Pts.1": "xPts", "GF.1": "xGF", "GA.1": "xGA", "GD.1": "xGD"},
                                     inplace=True)
df_all_time_player_Xstandings = df_all_time_player_Xstandings.sort_values(["Pts/G", "xGD"], ascending=False).reset_index(drop=True)

totals = player_total_stats()

y = df_team_standings["Pts"]
x = df_team_standings["GD"]
plt.scatter(x, y, alpha=0.5)
# calc the trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")
plt.ylabel("Points")
plt.xlabel("Goal Differential")
plt.title("Relationship between Goal Differential and Points")
plt.text(-50, 85, f"y= {z[0]:.4}x + {z[1]:.4}")
#plt.show()


writer = pd.ExcelWriter(
    r"C:\Users\sabzu\Documents\All EPL Project Files\Historical\Historical_Fantasy_Epl_Records_Stats.xlsx")
df_team_standings.to_excel(writer, sheet_name="Team Standings", index=False)
sd_sheet = writer.sheets["Team Standings"]
sd_sheet.set_column('A:A', 5)
sd_sheet.set_column('B:B', 13.75)
sd_sheet.set_column('C:J', 5)
df_team_Xstandings.to_excel(writer, sheet_name="Team Standings", index=False, startcol=11)
sd_sheet = writer.sheets["Team Standings"]
sd_sheet.set_column('L:L', 5)
sd_sheet.set_column('M:M', 13.75)
sd_sheet.set_column('N:U', 5)
df_all_time_player_standings.to_excel(writer, sheet_name="Team Standings", index=False, startcol=22)
sd_sheet.set_column('Y:AG', 5)
df_all_time_player_Xstandings.to_excel(writer, sheet_name="Team Standings", index=False, startcol=34)
sd_sheet.set_column('AK:AS', 5)
totals.to_excel(writer, sheet_name="Team Standings", index=False, startcol= 46)
writer.save()

