from os import system


if __name__ == "__main__":
    tips = [
        "Apenas Matheus e Yang estavam presentes na morte de Ricardo. (A∧B)",
        "Ricardo detesta Matheus, caso Matheus não seja bem-sucedido. (C→D)",
        "Ricardo deixa toda a herança para sua esposa. (E)",
        "Ricardo morreu com uma faca no peito. (F)",
        "Yang foi a última pessoa a pegar a faca. (G)",
        "Yang se casou por interesse. (H)",
        "Matheus está com problemas financeiros. (I)",
        "Se há motivo, Yang mataria Ricardo. (J→K)",
        "Pelas leis locais, filhos recebem a herança independente do testamento. (L)",
        "Se Matheus precisasse, ele mataria Ricardo. (N→M)"
    ]

    tips_taken = []

    solution = "matheus"

    total_tries_amount = 3

    tries_amount = total_tries_amount

    while tries_amount > 0:
        system("cls")

        print(f"Menu:\n[1] Pegar pista\n[2] Tentar responder ({tries_amount}/{total_tries_amount})")
        
        if tips_taken:
            print("\nPistas pegas:")
            for tip_taken in sorted(tips_taken):
                print(f"[{tip_taken + 1}] {tips[tip_taken]}")
        
        print("\nDigite a opção desejada:")
        response = input(" > ").strip().lower()

        match response:
            case "1":
                system("cls")
                
                print("Pistas possíveis:")
                for i, tip in enumerate(tips):
                    if not i in tips_taken:
                        print(f"[{i + 1}] Pista {i+ 1}")
                
                print("\nDigite a pista desejada:")
                response = input(" > ").strip().lower()

                print()

                if response.isnumeric() and int(response) - 1 < len(tips) and int(response) - 1 >= 0 and not (int(response) - 1) in tips_taken:
                    tip = tips[int(response) - 1]
                    tips_taken.append(int(response) - 1)
                    print(f"Você pegou a pista \"{tip}\"!")
                else:
                    print("Pista inválida.")
            case "2":
                system("cls")

                print("Digite a resposta:")
                response = input(" > ").strip().lower()

                print()

                if response == solution:
                    print(f"Você acertou utilizando {len(tips_taken)} pistas!")
                    break
                else:
                    print("Resposta errada. Tente novamente mais tarde.")
                    tries_amount -= 1
            case _:
                print("Opção inválida.")
        
        input("\n<Pressione qualquer tecla para continuar>")
    
    print(f"\n{'Parabéns!' if tries_amount > 0 else 'Não foi a sua vez.'}\nFim do jogo.\n")
