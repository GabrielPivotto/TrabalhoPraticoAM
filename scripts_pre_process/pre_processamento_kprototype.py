from sklearn.preprocessing import StandardScaler
import pandas as pd

#---------------------------------- FUNCOES ----------------------------------#
#-----------------------------------------------------------------------------#

df = pd.read_csv("dados/Dados_REG_limpo_baseline.csv", sep="\t")

NUM_COLS = [                # col. numericas
    "Atividade 02",
    "Atividade 05",
    "Atividade 06",
    "Atividade 07",
    "Atividade 08",
    "Atividade 09",
    "Atividade 10",
    "Atividade 11",
    "Atividade 12",
    "Atividade 14",
    "Atividade 15",
    "Atividade 23"
]
CAT_COLS = [                # col. categoricas
    "GRAM",
    "Cores",
    "Borda",
    "Textura",
    "Forma",
    "Brilho",
    "Muco",
    "Relevo",
    "Atividade 01",
    "Atividade 03",
    "Atividade 04",
    "Atividade 13",
    "Atividade 16",
    "Atividade 17",
    "Atividade 18",
    "Atividade 19",
    "Atividade 20",
    "Atividade 21",
    "Atividade 22",
]    

df['Atividade 21'] = df['Atividade 21'].fillna(df['Atividade 21'].median())
df['Atividade 20'] = df['Atividade 20'].fillna(df['Atividade 20'].median())

print("-- Colunas com valores nulos depois -----------------------\n", df.isna().sum().sort_values(ascending=False).loc[lambda x: x > 0], sep="")

df.to_csv(
    "dados/Dados_REG_limpo_kprototype.csv",
    sep="\t",
    index=False,
    encoding="utf-8"
)