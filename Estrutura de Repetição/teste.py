def main():
    primo = True  # vamos assumir que o número é primo

    # vamos solicitar um número inteiro positivo
    numero = int(input("Informe um número inteiro positivo: "))

    # o número é negativo?
    if numero < 0:
        print("Número inválido.")
    # é 0 ou 1?
    elif (numero == 0) or (numero == 1):
        print("Número válido, mas não é primo.")
    # passou até aqui. Vamos testar se o número é primo
    else:
        for i in range(2, int((numero / 2))):
            # se passar no teste, não é primo
            if numero % i == 0:
                primo = False  # recebe false
                break

        if primo:
            print("O número informado é primo")
        else:
            print("O número informado não é primo")


if __name__ == "__main__":
    main()
