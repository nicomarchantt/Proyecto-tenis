import src.cleaning as clean
import src.visualizing as vis

# imports
import pandas as pd

# df
df = pd.read_csv("Data.csv")
df_clean = pd.read_csv("Data_Final_ATP.csv")
df_players = pd.read_csv("player_overviews.csv")

# Funciones para limpiar
clean_df = clean.clean(df)
df_final = clean.export_clean_df(df_clean)
df_players_clean = clean.clean_2(df_players)
df_players_final = clean.export_clean_2_df(df_players_clean)

# Funciones para visualizar
vis.plot_tipo_torneo(df_clean)
vis.plot_superficies_comunes(df_clean)
vis.plot_ranking_ganadores(df_clean)
vis.plot_ranking_ganadores_superficie(df_clean)
vis.plot_ranking_campeones(df_clean)
vis.plot_superficies_ranking_bajo(df_clean)
vis.plot_superficies_ranking(df_clean)
vis.plot_relacion_ranking_tipo_torneo(df_clean)