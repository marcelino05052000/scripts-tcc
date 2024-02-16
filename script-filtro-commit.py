import pandas as pd

def salvar_valores_unicos(input_path, output_path):
    # Carregar o arquivo xlsx
    df = pd.read_excel(input_path)

    # Obter os valores da coluna "commit_id"
    # commit_ids = df['commit_id']
    commit_ids = df['codeLink']

    # Remover valores repetidos consecutivos
    valores_unicos = commit_ids[commit_ids != commit_ids.shift()]

    # Salvar os valores únicos em um arquivo de texto
    valores_unicos.to_csv(output_path, index=False, header=False)

# Substitua 'caminho/para/seu/arquivo.xlsx' pelo caminho do seu arquivo xlsx
caminho_entrada = "C:/Users/marce/Desktop/UFRPE/TCC/android.xlsx"

# Substitua 'caminho/para/saida/valores_unicos.txt' pelo caminho desejado para o arquivo de saída
# caminho_saida = 'C:/Users/marce/Desktop/UFRPE/TCC/allCommitIds_VFCs.txt'
caminho_saida = 'C:/Users/marce/Desktop/UFRPE/TCC/allCodeLinks_VFCs.txt'

salvar_valores_unicos(caminho_entrada, caminho_saida)
