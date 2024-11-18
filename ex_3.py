def transformarCelsiusParaFahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Digite a temperatura em Celsius: "))
    print(f"A temperatura em Fahrenheit é {transformarCelsiusParaFahrenheit(celsius)}")

main()