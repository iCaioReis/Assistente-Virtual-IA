from recognition import recognize_speech
from nlp import process_command
from calculator import calculate
from utils import extract_numbers

#Função principal do sistema que vai utilizar as outras funções dos demais arquivos
if __name__ == "__main__":
    iniciado = True
    while iniciado:
        command = recognize_speech()
        print(f"Você disse: {command}")

        if "Não entendi" in command or "Erro" in command:
            print(command)
        else:
            operation = process_command(command)
            if not operation:
                print("Comando não reconhecido.")
            else:
                numbers = extract_numbers(command)
                if len(numbers) < 2:
                    print("Por favor, forneça pelo menos dois números.")
                else:
                    result = calculate(operation, numbers)
                    print(f"O resultado é: {result}")