import pandas as pd

#---------------------------------- FUNCOES ----------------------------------#
def limpar_numerico(serie):
    raw = serie.astype("string").str.strip()
    
    #obs.: vai aumentar qtd de nulos pois transforma val. invalidos em nulo
    invalido = raw.isna() | (raw == "") | raw.str.match(r"^[#=]", na=False) 

    resultado = pd.to_numeric(raw.mask(invalido), errors="coerce")
    resultado = resultado.astype("float64")

    # algo que n era ausente/residuo e mesmo assim n virou numero
    inesperados = raw[resultado.isna() & ~invalido]
    if len(inesperados):
        print(f"ATENCAO {serie.name}: nao convertidos -> {inesperados.unique().tolist()}")

    return resultado
#-----------------------------------------------------------------------------#

df = pd.read_csv("dados/Dados_REG.csv", sep="\t")

#Removendo linha com "n°" duplicado ===========================================
df = df.drop_duplicates(subset=['n°'], keep='first')

#Removendo "n°" ===============================================================
df = df.drop(columns="n°")

#Padronizando nomenclatura em "GRAM"
df['GRAM'] = (
    df['GRAM']
    .str.strip()          # remove espaços no inicio/fim
    .str.lower()          # transforma td em "positivo"
    .replace({'positiva': 'positivo'})
    .str.capitalize()     # positivo -> Positivo
)

#Removendo "Cor" ==============================================================
df = df.drop(columns="Cor")

#Removendo linha com 6 valores nulos ==========================================
qtd = df.isnull().sum(axis=1).eq(6).sum()
print(f"Linhas com exatamente 6 nulos antes:\t{qtd}")

df = df[df.isnull().sum(axis=1) != 6]

qtd = df.isnull().sum(axis=1).eq(6).sum()
print(f"Linhas com exatamente 6 nulos depois:\t{qtd}")

#Transformando "Atividade 23" em numerico =====================================
df["Atividade 23"] = limpar_numerico(df["Atividade 23"])

#Removendo valores inesperados em GRAM ========================================
df = df.drop(df[df["GRAM"] == "Lavedura? não"].index)
df = df.drop(df[df["GRAM"] == "Variável"].index)

#Inserindo mediana ou moda em atributos com poucos nulos ======================
print("-- Colunas com valores nulos antes -------------------------\n", df.isna().sum().sort_values(ascending=False).loc[lambda x: x > 0], sep="")

# col. que NAO devem ser preenchidas
col_excluir = ['Atividade 20', 'Atividade 21']

# col. realmente quantitativas (utilizar mediana)
col_numericas = [
    'Atividade 02', 
    'Atividade 05',
    'Atividade 06',
    'Atividade 07',
    'Atividade 08',
    'Atividade 09',
    'Atividade 10',
    'Atividade 11',
    'Atividade 12',
    'Atividade 14',
    'Atividade 15',
    'Atividade 23',
]

# ident. linhas com valor nulo
mascara = df.isnull().any(axis=1)

# col. que podem ser preenchidas
col_preencher = [c for c in df.columns if c not in col_excluir]

# cat. = tudo que pode ser preenchido, exceto as quantitativas
col_categoricas = [c for c in col_preencher if c not in col_numericas]

# preenche quantitativas com mediana
for coluna in col_numericas:
    mediana = df[coluna].median()

    df.loc[mascara, coluna] = (
        df.loc[mascara, coluna].fillna(mediana)
    )

# preenche cat. com moda
for coluna in col_categoricas:
    moda = df[coluna].mode()

    if not moda.empty:
        df.loc[mascara, coluna] = (
            df.loc[mascara, coluna].fillna(moda.iloc[0])
        )

# verif. valores resultado
print("-- Colunas com valores nulos depois -----------------------\n", df.isna().sum().sort_values(ascending=False).loc[lambda x: x > 0], sep="")

#Salvando dataset com pre-processamento basico ================================
df.to_csv(
    "dados/Dados_REG_limpo_baseline.csv",
    sep="\t",
    index=False,
    encoding="utf-8"
)