import subprocess
import codecs


def executar_comando_git(commit_id, diretorio):
    comando = ["git", "-C", diretorio, "show", "--pretty=medium", "--stat", commit_id]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return resultado.stdout


def main():
    diretorios = [
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - av",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - base",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - external-libavc",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - hardware/qcom/media",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - libvpx",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - native",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - opt/net/wifi",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - ril",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - sonivox",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - system/bt",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - system-core",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//IC/Android/frameworks - system-media",
    ]

    # Executar o comando git log para cada commit_id e salvar os resultados em saidaVFC.txt
    for i in range(1, 76):  # Loop de 1 a 25
        caminho_arquivo_entrada = (
            f"C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//TCC/nonVFC/saida{i}.txt"
        )
        caminho_arquivo_saida = f"C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//TCC/nonVFC/saidaLog{i}.txt"

        with open(caminho_arquivo_entrada, "r") as arquivo_ids:
            lista_ids = arquivo_ids.read().splitlines()[1:]  # A partir da linha 2

        with codecs.open(caminho_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
            for commit_id in lista_ids:
                resultado_git = ""
                for diretorio in diretorios:
                    resultado_git = executar_comando_git(commit_id, diretorio)
                    if resultado_git:
                        break

                arquivo_saida.write(f"Commit ID: {commit_id}\n")
                arquivo_saida.write(resultado_git)
                arquivo_saida.write("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
