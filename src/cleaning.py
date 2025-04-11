import pandas as pd


# Diccionario para mapear el resultado del perdedor según la ronda en que perdió
round_mapping = {
    'The Final': 'Runner-Up',
    'Semifinals': 'Semifinals',
    'Quarterfinals': 'Quarterfinals',
    '4th Round': '4th Round',
    '3rd Round': '3rd Round',
    '2nd Round': '2nd Round',
    '1st Round': '1st Round',
    }

# Función para limpiar el DataFrame
def clean (df):
    df.drop(columns=['CBW', 'CBL', 'GBW', 'GBL', 'IWW', 'IWL', 'SBW', 'SBL',
       'B365W', 'B365L', 'B&WW', 'B&WL', 'EXW', 'EXL', 'PSW', 'PSL', 'UBW', 'UBL', 'LBW', 'LBL', 'SJW', 'SJL', 'MaxW', 'MaxL',
       'AvgW', 'AvgL'])
    df[df["Series"].isin(["Grand Slam", "Masters 1000", "ATP250", "ATP500"])]
    df["Date"] = pd.to_datetime(df["Date"])
    df["WRank"] = df["WRank"].fillna(0).astype(int)
    df["LRank"] = df["LRank"].fillna(0).astype(int)
    df["WPts"] = df["WPts"].fillna(0).astype(int)
    df["LPts"] = df["LPts"].fillna(0).astype(int)
    df["W1"] = df["W1"].fillna(0).astype(int)
    df["L1"] = df["L1"].fillna(0).astype(int)
    df["W2"] = df["W2"].fillna(0).astype(int)
    df["L2"] = df["L2"].fillna(0).astype(int)
    df["W3"] = df["W3"].fillna(0).astype(int)
    df["L3"] = df["L3"].fillna(0).astype(int)
    df["W4"] = df["W4"].fillna(0).astype(int)
    df["L4"] = df["L4"].fillna(0).astype(int)
    df["W5"] = df["W5"].fillna(0).astype(int)
    df["L5"] = df["L5"].fillna(0).astype(int)
    df["Wsets"] = df["Wsets"].fillna(0).astype(int)
    df["Lsets"] = df["Lsets"].fillna(0).astype(int)
    df["WPts"] = df["WPts"].fillna(0).astype(int)
    df["LPts"] = df["LPts"].fillna(0).astype(int)
    df["Year"] = df["Date"].dt.year
    df["TorneoID"] = df["Tournament"] + "_" + df["Year"].astype(str)
    df = df[~((df['Series'] == 'ATP250') & (df['Round'] == '0th Round'))]
    df.loc[(df['Series'].isin(['ATP250', 'ATP500'])) & (df['Round'] == '3rd Round'), 'Round'] = '4th Round'
    df.loc[(df['Series'].isin(['ATP250', 'ATP500'])) & (df['Round'] == '2nd Round'), 'Round'] = '3rd Round'
    df.loc[(df['Series'].isin(['ATP250', 'ATP500'])) & (df['Round'] == '1st Round'), 'Round'] = '2nd Round'
    df['WinnerResult'] = df['Round'].apply(lambda x: 'Champion' if x == 'The Final' else 'Next Round')
    df['LoserResult'] = df['Round'].map(round_mapping)
    df['Surface'] = df['Surface'].replace('Carpet', 'Hard')

    return df

#Función para exportar el DataFrame limpio
def export_clean_df(clean_df):
    clean_df.to_csv("Data_Final_ATP.csv", index=False)
    return clean_df

#Función para el segundo DataFrame
def clean_2 (df_players):
    df_players['displayname'] = df_players['last_name'].str.title() + ' ' + df_players['first_name'].str[0].str.upper() + '.'
    df_players = df_players[
        (df_players['displayname'].notna()) & 
        (df_players['displayname'] != '') & 
        (df_players['displayname'] != 'Unknown U.')
        ]   
    df_players = df_players.drop_duplicates(subset=['displayname'])
    df_players = df_players[df_players['flag_code'].notna()]
    return df_players

#Función para exportar el segundo DataFrame limpio
def export_clean_2_df(clean_2_df):
    clean_2_df.to_csv("player_overviews_clean.csv", index=False)
    return clean_2_df