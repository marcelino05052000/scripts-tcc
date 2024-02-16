import subprocess
import os


def obter_arquivos_modificados(commit_hash, diretorio):
    os.chdir(diretorio)
    comando = f'git show --pretty="" --name-only {commit_hash}'
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    arquivos_modificados = resultado.stdout.splitlines()
    return arquivos_modificados


def obter_commits_que_modificaram_arquivos(
    arquivos_modificados, commit_atual, diretorio
):
    os.chdir(diretorio)
    log_format = "--pretty=format:%H"  # Apenas os hashes dos commits
    comando = (
        f'git log {log_format} {commit_atual} -- {", ".join(arquivos_modificados)}'
    )
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    commits_relacionados = resultado.stdout.splitlines()
    return commits_relacionados


def main():
    # Substitua o caminho do arquivo conforme necessário
    caminho_arquivo_ids = (
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/TCC/allCommitIds_non_VFCs.txt"
    )
    with open(caminho_arquivo_ids, "r") as arquivo_ids:
        lista_ids = arquivo_ids.read().splitlines()[0:]  # IDs da linha 27 à 51

    diretorios = [
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - av",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - base",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - external-libavc",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - hardware/qcom/media",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - libvpx",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - native",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - opt/net/wifi",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - ril",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - sonivox",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - system/bt",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - system-core",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/IC/Android/frameworks - system-media",
    ]

    for i, commit_id in enumerate(lista_ids, start=1):
        # Escolher o diretório adequado para o commit_id
        for diretorio in diretorios:
            os.chdir(diretorio)
            comando_check_commit = f"git rev-list -n 1 {commit_id}"
            resultado_check_commit = subprocess.run(
                comando_check_commit, shell=True, capture_output=True, text=True
            )

            if resultado_check_commit.returncode == 0:
                break

        # Criar um arquivo de saída para cada execução
        nome_arquivo_saida = (
            f"C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/TCC/nonVFC/saida{i}.txt"
        )

        # Passo 1: Identificar arquivos modificados no commit atual
        arquivos_modificados = obter_arquivos_modificados(commit_id, diretorio)

        # Passo 2: Identificar commits que modificaram os mesmos arquivos
        commits_relacionados = obter_commits_que_modificaram_arquivos(
            arquivos_modificados, commit_id, diretorio
        )

        # Imprimir os commits relacionados e salvar no arquivo de saída
        with open(nome_arquivo_saida, "w") as arquivo_saida:
            arquivo_saida.write(
                f"Commits que modificaram os mesmos arquivos para o commit {commit_id}:\n"
            )
            arquivo_saida.write("\n".join(commits_relacionados))


if __name__ == "__main__":
    main()
