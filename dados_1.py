import pandas as pd

def padronizar_sexo(dado):
    dado = str(dado).strip().upper() # Remove os espaços indesejados e "padroniza" a palavra inteira como maiuscula

    if dado[0] == 'F': # Verifica se a primeira letra é F
        return 'Feminino'
    
    if dado[0] == 'M': # Verifica se a primeira letra é M
        return 'Masculino'
    
def padronizar_notas(dado):
    dado = str(dado).strip() # Remove os espaços indesejados

    dado = dado.replace('.', ',') # Substitui todos os '.' na string por ',' 

    return dado

def coletar_dados_para_calculo(dado):
    dado = str(dado).strip() # Remove os espaços indesejados

    dado = dado.replace(',', '.') # Transforma a ',' de um número para um '.' permitindo a conversão para float

    return float(dado)

def calcular_media(linha):
    nota_mat = coletar_dados_para_calculo(linha['nota_matematica']) # Retorna o valor da nota de matemática como float
    nota_port = coletar_dados_para_calculo(linha['nota_portugues']) # Retorna o valor da nota de português como float
    frequencia = coletar_dados_para_calculo(linha['frequencia']) # Retorna o valor da nota da frequência como float (Não necessário nessa tabela, mas sempre importante de fazer pela garantia)

    media = (nota_mat + nota_port + (frequencia / 10)) / 3 # Calcula a média
    media = round(media, 1) # Realiza a aproximação de uma casa decimal da média

    media = padronizar_notas(media) # Padroniza a formatação para a brasileira

    return media

def verificar_aprovacao(dado):
    dado = coletar_dados_para_calculo(dado) # Transforma a ',' de um número para um '.' permitindo a conversão para float

    if dado >= 7: # Verifica se a nota é maior ou igual a 7
        return 'Sim'
    
    else:
        return 'Não'
    
# --------- Abaixo é um incremento na coluna de frequência que achei valido ser colocado ----------- #

def padronizar_frequencia(dado):
    dado = padronizar_notas(dado) # Utiliza "padronizar_notas" para substituir da formatação americana para a brasileira

    dado = f'{dado}%' # Adiciona o simbolo de porcentagem para maior entendimento e clareza do dado

    return dado

# ------------------------------- Aplicação das Funções ------------------------------------- #

arquivo = pd.read_csv('Base_despadronizada.csv') # Lê o arquivo

arquivo['sexo'] = arquivo['sexo'].apply(padronizar_sexo) # Padroniza a coluna sexo inteira

arquivo['nota_matematica'] = arquivo['nota_matematica'].apply(padronizar_notas) # Padroniza a coluna nota_matematica inteira

arquivo['nota_portugues'] = arquivo['nota_portugues'].apply(padronizar_notas) # Padroniza a nota_portugues inteira

arquivo['Media'] = arquivo.apply(calcular_media, axis = 1) # Cria a coluna Media e usa axis = 1 para passar a linha inteira para a função

arquivo['aprovado'] = arquivo['Media'].apply(verificar_aprovacao) # Cria a coluna aprovado e usa a informação de Media para definir o resultado

# ---------------------------------------------------------------------------- #

arquivo['frequencia'] = arquivo['frequencia'].apply(padronizar_frequencia) # Padroniza a coluna frequencia com a formatação que eu adicionei (Extra)

arquivo.to_csv('Base_padronizada.csv', index = False)