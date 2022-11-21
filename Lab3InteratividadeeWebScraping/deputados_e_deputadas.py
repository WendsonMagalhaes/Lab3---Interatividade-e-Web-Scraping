# importing pandas
import pandas as pd
  
# merging two csv files

df = pd.concat(
    map(pd.read_csv, ['/home/wendson/Área de Trabalho/Lab3 - Interatividade  e Web Scraping/Lab3InteratividadeeWebScraping/deputados.csv','/home/wendson/Área de Trabalho/Lab3 - Interatividade  e Web Scraping/Lab3InteratividadeeWebScraping/deputadas.csv']), ignore_index=True)
print(df)
df.to_csv( "deputados_e_deputadas.csv", index=False, encoding='utf-8-sig')