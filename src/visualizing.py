import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

#Función para ver la distribución de torneos por tipo 

def plot_tipo_torneo(df):
    df["Series"].value_counts().plot(kind="bar")
    plt.title("Número de partidos por tipo de torneo")
    return plt.show()

#Función para ver las superficies más comunes en torneos

def plot_superficies_comunes(df):
    df["Surface"].value_counts().plot(kind="pie", autopct="%1.1f%%")
    plt.title("Distribución de partidos por superficie")
    return plt.show()

#Funcion para ver la distribució de rankings de los ganadores de partidos

def plot_ranking_ganadores(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['WRank'], kde=True, color='blue')
    plt.title('Distribución de los ganadores según su ranking inicial')
    plt.xlabel('Ranking Inicial del Ganador')
    plt.ylabel('Número de Ganadores')
    return plt.show()  

#Función para ver los rankings de los ganadores segun superficie.

def plot_ranking_ganadores_superficie(df):
    sns.boxplot(x="Surface", y="WRank", data=df)
    plt.title("Ranking de los ganadores según la superficie")
    return plt.show()  

#Función para ver la distribución del ranking de los campeones

def plot_ranking_campeones(df):
    finals_winners = df[df["Round"] == "The Final"][["Tournament", "Winner", "WRank"]]
    plt.hist(finals_winners["WRank"], bins=10, edgecolor="black")
    plt.title("Distribución de Ranking de los Ganadores de Finales")
    plt.xlabel("Ranking")
    plt.ylabel("Frecuencia")
    return plt.show()

#Función para ver las superficies donde ganan jugadores de ranking bajo 

def plot_superficies_ranking_bajo(df):
    low_rank_winners = df[(df["WRank"] > 50) & (df["Round"] == "The Final")]
    surface_counts = low_rank_winners["Surface"].value_counts()
    surface_counts.plot(kind="bar", color=["red", "green", "blue", "gray"])
    plt.title("Superficies donde ganan jugadores de ranking bajo")
    plt.xlabel("Superficie")
    plt.ylabel("Número de victorias en finales")
    return plt.show()

#Función para ver superficies donde ganan jugadores de ranking bajo vs alto

def plot_superficies_ranking(df):
    low_rank_winners = df[(df["WRank"] > 50) & (df["Round"] == "The Final")]
    high_rank_winners = df[(df["WRank"] <= 50) & (df["Round"] == "The Final")]
    comparison = pd.DataFrame({
        "Ranking bajo (>50)": low_rank_winners["Surface"].value_counts(),
        "Ranking alto (≤50)": high_rank_winners["Surface"].value_counts()
    }).fillna(0)
    comparison.plot(kind="bar", figsize=(8,5))
    plt.title("Superficies donde ganan jugadores de ranking bajo vs alto")
    plt.xlabel("Superficie")
    plt.ylabel("Número de victorias en finales")
    plt.xticks(rotation=0)
    plt.legend(title="Ranking del ganador")
    return plt.show()

#Función para ver la relacion entre el tipo de torneo y el ranking del ganador

def plot_relacion_ranking_tipo_torneo(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Series', y='WRank')
    plt.title('Relación entre el tipo de torneo y el ranking del ganador')
    plt.xlabel('Tipo de Torneo')
    plt.ylabel('Ranking del Ganador')
    plt.xticks(rotation=45)
    return plt.show()