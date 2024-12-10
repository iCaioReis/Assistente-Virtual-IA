import json

# Função para carregar os comandos do arquivo JSON
def load_commands():
    with open('commands.json', 'r', encoding='utf-8') as f:
        return json.load(f)

#função para processar comando e identificar qual a operação que o usuário quer realizar
def process_command(command):
    command = command.lower()
    
    commands = load_commands()

    for operation, keywords in commands.items():
        if any(keyword in command for keyword in keywords):
            return operation
    return None
