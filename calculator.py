#função que realiza o cálculo de cada uma das operações

def calculate(operation, numbers):
    try:
        if operation == "add":
            return sum(numbers)
        elif operation == "subtract":
            return numbers[0] - numbers[1]
        elif operation == "multiply":
            result = 1
            for num in numbers:
                result *= num
            return result
        elif operation == "divide":
            return numbers[0] / numbers[1]
    except Exception as e:
        return f"Erro na operação: {e}"