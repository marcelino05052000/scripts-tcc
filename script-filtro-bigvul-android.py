import pandas as pd

#bigvul = pd.read_csv("D:/Área de Trabalho/all_c_cpp_release2.0.csv") #lê os dados do csv e salva eles dentro da variavel bigvul
bigvul = pd.read_csv("D:/Área de Trabalho/MSR_data_cleaned.csv", low_memory=False) #tira a limitação de memoria quando vai ler arquivos muito grandes
page_score = bigvul[["cve_page","score"]] #pega só as colunas especificadas

#page_score_filter = bigvul.loc[bigvul["score"] > 7, ["project","cve_page", "score", "lang", "ref_link"]] #filtra os dados por score maior que 7 e com as colunas de project, cve_page, score, lang e ref_link

#page_score_filter.to_excel("D:/Área de Trabalho/page_score.xlsx", sheet_name="filtro", index=False) #exporta os dados salvos na variavel para um arquivo xlsx

filter = bigvul.loc[bigvul["Score"] > 7, ["project","CVE Page", "Score", "lang", "codeLink"]]

filter.to_excel("D:/Área de Trabalho/filter-MSR.xlsx", sheet_name="filtro", index=False)

#print(bigvul.dtypes) serve para saber os tipos de dados que tem no csv
#print(bigvul.head()) serve para imprimir as 5 primeiras linhas e as 5 ultimas, ou especificar linhas dentro dos parenteses