#Luana de Paiva Brito | Louisy Dalchiavon Tomazi | Yulianny Alejandra Perdomo Briceno
#Funções =============================================================================
def entrada():
    nome= input("Nome:")
    idade = int(input("Idade:"))
    return nome, idade

def verificar_febre(graus):
    if graus>=39.0:
        return 1 #febrealta
    elif graus>=37.5 and graus <= 38.9:
        return 2 #"Febre Moderada"
    else:
        return 3 #"Normal"

def verificar_dor_cabeca(intensidade):
    if intensidade >= 8 and intensidade <=10:
        return 1 #"Intensa(Consulta médica)"
    elif intensidade >= 5 and intensidade <=7:
        return 2 #"Moderada(repouso)"
    elif intensidade >= 0 and intensidade <=4:
        return 3 #"Leve(autocuidado)"
        
def verifica_tosse():
    catarro = input("Sua tosse possui catarro? ").lower()
    if catarro == "sim":
        return 1 #"Tosse com catarro, pode indicar possível infecção"
    else:
         return 2 #"Tosse Seca"

def relatorio_combinado(febre,tosse,dor_cabeca):
    diag_dem = "Diagnóstico:"
    rec = "Recomendações: "
    if febre==1 and dor_cabeca==1 and tosse==2:
        return diag_dem +" meningite viral/bacteriana ou infecção respiratória grave (pneumonia atípica, COVID-19 grave).\n" +rec+ "Atendimento médico imediato."

    elif febre==2 and dor_cabeca==2 and tosse==2:
        return diag_dem +" gripe (influenza) ou COVID-19 leve.\n" +rec+ "Repouso, hidratação e observação."

    elif febre==2 and dor_cabeca==2 and tosse==1:
        return diag_dem +" bronquite infecciosa ou sinusite bacteriana.\n" +rec+ "Avaliação médica recomendada."

    elif febre==1 and tosse==1:
        return diag_dem+" Forte suspeita de pneumonia.\n" +rec+ "Procurar pronto atendimento."
    elif febre==3 and tosse==2 and dor_cabeca==3:
        return diag_dem+" Alergia, irritação da garganta, ar seco, ou início de resfriado.\n" +rec+ "hidratação abundante (água, chás), evitar ambientes com poeira/fumaça, umidificar o ar."
    else:
        return "Sem diagnostico combinado"

def diag_individual(febre,tosse,dor_cabeca):
    diag=''
    if febre==1:
        diag = 'Febre: Alta'
    elif febre==2:
        diag = 'Febre: Moderada'
    else:
        diag = 'Temperatura Normal'
    
    if dor_cabeca == 1:
        diag += '\nDor de Cabeça: Intensa'
    elif dor_cabeca == 2:
        diag += '\nDor de Cabeça: Moderada'
    elif dor_cabeca == 3:
        diag += '\nDor de Cabeça: Leve'
    else:
        diag += ''

    if tosse == 1:
        diag += '\nTosse: Com catarro'
    elif tosse==2:
        diag += '\nTosse: Seca'
    
    return diag
        
    
#Início =====================================================================

print('===Isso se trata de um sistema! PROCURE UM PROFISSIONAL DA ÁREA===')    
print("Bem vindo(a) ao nosso assistente de saúde!")
nome, idade = entrada()

graus= float(input("Qual a sua temperatura corporal? "))

aux = input("Esta sentindo dor de cabeça?").lower()
intensidade = -1
if aux == "sim":
    intensidade = int(input("De 0-10 qual a intensidade da dor:"))

tosse = input("Você está com tosse? ").lower()
if tosse == "sim":
    tipo_tosse = verifica_tosse()
else:
    tipo_tosse = 0
    
tipo_febre = verificar_febre(graus)
tipo_dor = verificar_dor_cabeca(intensidade)

print('\nPaciente:',nome,idade,'anos')
print(diag_individual(tipo_febre,tipo_tosse,tipo_dor))
print(relatorio_combinado(tipo_febre,tipo_tosse,tipo_dor))
print('===Isso se trata de um sistema! PROCURE UM PROFISSIONAL DA ÁREA===')




