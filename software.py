def saudacao(nome)
    return f"Olá, (nome)! Bem-vindo ao software."

if __name__ == "__main__":
    nome = input("digite seu nome: ")
    print(saudacao(nome))