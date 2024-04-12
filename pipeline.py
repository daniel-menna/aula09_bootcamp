from etl import pipeline_calcular_dados_de_venda_consulidado

pasta_argumento: str = 'data'
formato_desejado: list = ["csv", "parquet"]

pipeline_calcular_dados_de_venda_consulidado(pasta_argumento, formato_desejado)