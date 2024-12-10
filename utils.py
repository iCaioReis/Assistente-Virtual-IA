import re

# função para extrair apenas números do texto -> Chat GPT
def extract_numbers(command):
    return [float(num) for num in re.findall(r'\d+', command)]
