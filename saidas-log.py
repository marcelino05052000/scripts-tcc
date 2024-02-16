import subprocess
import codecs


def executar_comando_git(commit_id, diretorio):
    comando = ["git", "-C", diretorio, "show", "--pretty=medium", "--stat", commit_id]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    return resultado.stdout


def main():
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
    # Ler os commit_ids do arquivo allCommitIds.txt
    with open(
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/TCC/allCommitIds_non_VFCs.txt",
        "r",
    ) as arquivo_ids:
        lista_ids = arquivo_ids.read().splitlines()[0:]  # A partir da linha 27

    # Executar o comando git log para cada commit_id e salvar os resultados em saidaVFC.txt
    with codecs.open(
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE/TCC/saida_non_VFC.txt",
        "w",
        encoding="utf-8",
    ) as arquivo_saida:
        for commit_id in lista_ids[:75]:  # Pegar os primeiros 25 commit_ids
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
