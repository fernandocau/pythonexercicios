"""
Módulo de Cálculos de Forças e Pesos Físicos

Este módulo fornece uma interface interativa para calcular diversas grandezas físicas
relacionadas a peso, forças e medidas corporais.

Autor: Fernando Cau
Data: 12/08/2025
Versão: 1.0
"""

from time import sleep


def exibir_menu():
    """Exibe o menu principal com as opções disponíveis."""
    sleep(1.5)
    print(f''' REGISTRO DE PESO
[1] Massa Corporal
[2] IMC - Índice de Massa Corporal
[3] Peso em Planeta
[4] Força Normal
[5] Força de Atrito
[6] Tensão em Cabos/Molas
[7] Pressão Exercida por um Objeto
[8] Peso Aparente/Empuxo
[9] Força Centrípeta''')


def calcular_massa_corporal():
    """
    Calcula o maior e menor peso entre 5 pessoas.

    Returns:
        tuple: (maior_peso, menor_peso) em kg
    """
    print('Massa Corporal')
    pesomaior = 0
    pesomenor = 0

    for pessoa in range(1, 6):
        sleep(1)
        peso = float(input('Digite o peso da {}a pessoa: '.format(pessoa)))

        if pessoa == 1:
            pesomaior = peso
            pesomenor = peso
        else:
            if peso > pesomaior:
                pesomaior = peso
            if peso < pesomenor:
                pesomenor = peso

    print(f'O maior peso lido foi de {pesomaior}kg')
    print(f'O menor peso lido foi de {pesomenor}kg')
    return pesomaior, pesomenor


def calcular_imc():
    """
    Calcula o Índice de Massa Corporal (IMC).

    Returns:
        float: Valor do IMC calculado
    """
    sleep(1)
    print('IMC')
    nome = str(input('Digite seu nome: ')).strip()
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))
    imc = peso / (altura ** 2)
    print(f'O IMC do senhor {nome} é de: {imc:.2f}.')
    return imc


def calcular_peso_planeta():
    """
    Calcula o peso em um planeta com gravidade específica.

    Returns:
        float: Peso no planeta em Newtons
    """
    sleep(1)
    print('Peso em planeta')
    massa = float(input('Digite sua massa (kg): '))
    gravidade = float(input('Digite a gravidade do planeta (m/s²): '))
    peso_em_planeta = massa * gravidade
    print(f'O peso no planeta é de: {peso_em_planeta:.2f}N.')
    return peso_em_planeta


def calcular_forca_normal(gravidade=9.8):
    """
    Calcula a força normal exercida por um objeto.

    Args:
        gravidade (float): Aceleração gravitacional (padrão: 9.8 m/s²)

    Returns:
        float: Força normal em Newtons
    """
    sleep(1)
    print('Força normal')
    massa_kg = float(input('Digite a massa (kg): '))
    forca = massa_kg * gravidade
    print(f'A força normal foi de {forca:.2f}N.')
    return forca


def calcular_forca_atrito(gravidade=9.8):
    """
    Calcula a força de atrito.

    Args:
        gravidade (float): Aceleração gravitacional (padrão: 9.8 m/s²)

    Returns:
        float: Força de atrito em Newtons
    """
    sleep(1)
    print('Força de atrito')
    massa_kg = float(input('Digite a massa (kg): '))
    coeficiente_atrito = float(input('Digite o coeficiente de atrito: '))
    forca_atrito = massa_kg * coeficiente_atrito * gravidade
    print(f'A força de atrito foi de {forca_atrito:.2f}N.')
    return forca_atrito


def calcular_tensao_cabos(gravidade=9.8):
    """
    Calcula a tensão em cabos ou molas.

    Args:
        gravidade (float): Aceleração gravitacional (padrão: 9.8 m/s²)

    Returns:
        float: Tensão em Newtons
    """
    sleep(1)
    print('Tensão em cabos/molas')
    massa_kg = float(input('Digite a massa (kg): '))
    tensao_cabos = massa_kg * gravidade
    print(f'A tensão dos cabos foi de {tensao_cabos:.2f}N.')
    return tensao_cabos


def calcular_pressao_exercida(gravidade=9.8):
    """
    Calcula a pressão exercida por um objeto.

    Args:
        gravidade (float): Aceleração gravitacional (padrão: 9.8 m/s²)

    Returns:
        float: Pressão em Pascal (Pa)
    """
    sleep(1)
    print('Pressão exercida por um objeto')
    massa_kg = float(input('Digite a massa (kg): '))
    area_m2 = float(input('Digite a área (m²): '))
    pressao_exercida = (massa_kg * gravidade) / area_m2
    print(f'A pressão exercida foi de {pressao_exercida:.2f}Pa.')
    return pressao_exercida


def calcular_peso_aparente(gravidade=9.8):
    """
    Calcula o peso aparente considerando o empuxo.

    Args:
        gravidade (float): Aceleração gravitacional (padrão: 9.8 m/s²)

    Returns:
        float: Peso aparente em Newtons
    """
    sleep(1)
    print('Peso aparente/empuxo')
    massa_kg = float(input('Digite a massa (kg): '))
    densidade_fluido = float(input('Digite a densidade do fluido (kg/m³): '))
    volume_submerso = float(input('Digite o volume submerso (m³): '))
    empuxo = densidade_fluido * volume_submerso * gravidade
    peso_aparente = (massa_kg * gravidade) - empuxo  # Correção na fórmula
    print(f'O peso aparente foi de {peso_aparente:.2f}N.')
    return peso_aparente


def calcular_forca_centripeta():
    """
    Calcula a força centrípeta.

    Returns:
        float: Força centrípeta em Newtons
    """
    sleep(1)
    print('Força centrípeta')
    massa_kg = float(input('Digite a massa (kg): '))
    velocidade_m_s = float(input('Digite a velocidade (m/s): '))
    raio_m = float(input('Digite o raio (m): '))
    forca_centripeta = massa_kg * (velocidade_m_s ** 2) / raio_m  # Correção na fórmula
    print(f'A força centrípeta foi de {forca_centripeta:.2f}N.')
    return forca_centripeta


def main():
    """Função principal que executa o programa."""
    # Variáveis globais
    gravidade = 9.8  # m/s²

    # Exibir menu
    exibir_menu()

    # Obter opção do usuário
    try:
        opcao = int(input('Qual é a opção desejada? '))
    except ValueError:
        print('Opção inválida! Digite um número entre 1 e 9.')
        return

    # Executar função correspondente à opção
    if opcao == 1:
        calcular_massa_corporal()
    elif opcao == 2:
        calcular_imc()
    elif opcao == 3:
        calcular_peso_planeta()
    elif opcao == 4:
        calcular_forca_normal(gravidade)
    elif opcao == 5:
        calcular_forca_atrito(gravidade)
    elif opcao == 6:
        calcular_tensao_cabos(gravidade)
    elif opcao == 7:
        calcular_pressao_exercida(gravidade)
    elif opcao == 8:
        calcular_peso_aparente(gravidade)
    elif opcao == 9:
        calcular_forca_centripeta()
    else:
        print('Opção Inválida')


# Executar o programa se este arquivo for executado diretamente
if __name__ == "__main__":
    main()