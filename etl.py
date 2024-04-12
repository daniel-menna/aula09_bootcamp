import pandas as pd
import os
import glob
import pandera

# Uma função de extract que lê os Arquivos e concatena os Arquivos
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index="True")
    return df_total

# Uma função que transformas os Arquivos

def transformar_dados(df: pd.DataFrame) -> pd.DataFrame :
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

# Uma função que dá load dos meus arquivos (posso decidir por 2 caminhos)
def carregar_dados(dados: pd.DataFrame, formato_saida: list):
    """
    parametro que vai ser ou "csv" ou "parquet" ou os dois
    """
    for format in formato_saida :
        if format == "csv" :
            dados.to_csv("dados.csv", index=False)
        if format == "parquet" :
            dados.to_parquet("dados.parquet")


def pipeline_calcular_dados_de_venda_consulidado(pasta: str, formato_desejado: list) :
    data_frame = extrair_dados(pasta)
    dados_carregados = transformar_dados(data_frame)
    carregar_dados(dados_carregados, formato_desejado)