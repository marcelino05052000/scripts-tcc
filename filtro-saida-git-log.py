def filtrar_saidas_git(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, "r", encoding="utf-8") as entrada:
        linhas = entrada.readlines()

    with open(arquivo_saida, "w", encoding="utf-8") as saida:
        commit_id = None
        autor = None
        data = None
        modificacoes = []
        code_churn = 0

        for linha in linhas:
            if linha.startswith("Commit ID:"):
                # Salvar as informações do commit anterior, se houver
                if commit_id is not None:
                    saida.write(f"Commit ID: {commit_id}\n")
                    saida.write(f"Author: {autor}\n")
                    saida.write(f"Date: {data}\n")
                    saida.write("\n".join(modificacoes) + "\n")
                    saida.write(f"Code Churn: {code_churn}\n")
                    saida.write("=" * 50 + "\n")

                # Iniciar um novo commit
                commit_id = linha.split()[-1].strip()
                autor = None
                data = None
                modificacoes = []
                code_churn = 0
            elif linha.startswith("Author:"):
                autor = linha.split(":", 1)[1].strip()
            elif linha.startswith("Date:"):
                data = linha.split(":", 1)[1].strip()
            elif linha.startswith((" ", "\t")):
                # Verificar se a linha contém "file changed" ou "files changed"
                if "files changed" in linha:
                    modificacoes.append(linha.strip())
                elif "file changed" in linha:
                    modificacoes.append(linha.strip())

                # Calcular o code churn
                partes = linha.split(",")
                for parte in partes:
                    if "insertion" in parte:
                        code_churn += int(parte.split()[0])
                    elif "deletion" in parte:
                        code_churn += int(parte.split()[0])

        # Salvar as informações do último commit
        if commit_id is not None:
            saida.write(f"Commit ID: {commit_id}\n")
            saida.write(f"Author: {autor}\n")
            saida.write(f"Date: {data}\n")
            saida.write("\n".join(modificacoes) + "\n")
            saida.write(f"Code Churn: {code_churn}\n")
            saida.write("=" * 50 + "\n")


if __name__ == "__main__":
    filtrar_saidas_git(
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//TCC/saida_non_VFC.txt",
        "C:/Users/marce/OneDrive/Área de Trabalho/UFRPE//TCC/saidaFiltrada_non_VFC.txt",
    )
