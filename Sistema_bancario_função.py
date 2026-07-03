def menu():
 print("========== Menu ========== ")
 print('  Saldo = 1 \n  Sacar = 2 \n  Depositar = 3 \n  Limites = 4 \n  Extratos = 5 \n Novo usuario = 6 \n Criar conta = 7\n Mostra contas = 8')

 print("==========================")

  
def depositar(saldo,valor, extrato): 
  if valor>0:
    saldo=saldo+valor
    extrato=extrato + f"Deposito: R$ {valor:.2f}\n"
    print("Depisito concluido com sucesso!! ")
  else:
    print("Operação invalida!!")
  return saldo, extrato
    

def sacar(saldo,valor,limite,extrato,cont):
  if saldo>0 and  valor<saldo and  valor<=500:
    saldo=saldo-valor
    extrato=extrato +f"Saque R$ {valor:.2f}\n"
    print("Saque ralizado com sucesso!!")
    cont=cont+1
  elif saldo<0:
    print("Você não tem saldo o suficinte para sacar!!")
  elif cont==3:
    print("Você atingio o limite de três saques do dia, tentar amanhã")
  elif valor>500:
    print("Você excedeu o limite de R$500 por saque")
  else:
    print("Invalido")
  return saldo,valor,limite,extrato,cont

def extrato_mostra(extrato,saldo):
  if not extrato:
    print("Não existe extrato")
  else:
    print("========= Extratos ======")
    print(extrato)
    print(f"Seu saldo é: {saldo:.2f} ")
    return extrato,saldo

def limites():
  print("=======================================================")
  print("Regras de negocio:\n")
  print("So é permitido realizar saques de até no maximo 500$\n")
  print("Só é possivel ralizar até três sques por dia \n")
  print("=======================================================")
          
def criar_usuario(usuarios,cpfs,extrato):
  cpf=int(input("Digite o seu cpf:"))
  cont2=0
  if cpf<11:
    print("CPF invalido!")
  else:
   existe=verificar_cpf(cpf,cpfs) #Sempre utulizar uma variavel quando tem retono sempre 
  if not existe: #Operadores de associassão verifica se estão em uma lista
    usuario={}
    usuario["Nome"]=input("Nome:")
    usuario["Data  nascimento "]=input("Data  nascimento :")
    usuario["CPF"]=cpf
    usuario["Enfereço"]=input("Endereço:")
    extrato = extrato + f"Novo usuario cadastrado: {usuario['Nome']} e CPF:{cpf} \n"
    cpfs.append(cpf)# Adicina o cpf  a lista
    usuarios.append(usuario)
    print("Novo usuario cadastrado com suscesso!")
  else:
    print("Já existe uma conta cadastrada com esse CPF")
  return usuarios , cpfs, extrato
  
  
  
def verificar_cpf(cpf,cpfs):
  for i in cpfs:
    if i == cpf:
     return  True
  return False
    
def criar_cont(usuarios, agencia, contas):
    cpf = int(input("Digite o CPF do usuário: "))

    for usuario in usuarios:
        if usuario["CPF"] == cpf: #Verifica se o CPF de algum usuario e igual ao cpf cadastrado

            conta = {}
            conta["Agência"] = agencia
            conta["Conta"] = len(contas) + 1
            conta["Usuário"] = usuario

            contas.append(conta)
            print("Conta criada com sucesso!")
            return contas

    print("Usuário não cadastrado!")
    return contas


def mostrar_contas(contas):
    for conta in contas:
        print(conta)
  


      
  

  
#Funçãom locar ==============================================================
def main():
  saldo=0
  limite=500
  cont=0
  extrato=""
  agencia="00001"
  usuarios=[] # Tenho que ter uma lista de usuarios que gusrda um conjunto de discionariosx
  cpfs=[71338203401]
  contas=[]

  menu() # para chaaar a função de menu
  
  while True:
    opição=int(input("Digite qual operação deseja realizar:"))
    
    if opição==1:
     print(f"O valor do saldo é: {saldo:.2f}")

    elif opição ==2:
      valor=float(input("Digite o valor que pretende sacar:"))
      saldo,valor,limite,extrato,cont = sacar(saldo,valor,limite,extrato,cont) #Atribuo todos os valores e chamo a função com os parametros que passei
      continue
      
    elif opição==3:
      valor=float(input("Valor que deseja depositar:"))
      saldo, extrato =depositar(saldo,valor,extrato) # Ou seja, estou dizendo que saldo e estrato vao ser atualizados com oque eu colocar na função
      continue

    elif opição==4:
     limites() #Apenas mostra função escrita, sem retorno, ou seja passo apenas mostra ela.
     continue

    elif opição==5:
      extrato,saldo=extrato_mostra(extrato,saldo) # As variavies que entram na função saem, obs os nomes das funções diferentes das variaveis
      continue
    elif opição==6:
      usuarios,cpfs, extrato=criar_usuario(usuarios,cpfs, extrato)
      continue
    elif opição ==7:
     contas = criar_cont(usuarios, agencia, contas)
     continue

    elif opição ==8:
     mostrar_contas(contas)
     continue
    else:
      print("Operação invalida!!!")
      menu()
      continue

main() #Chamo a função em baixo

#Criar novo usuario e verificar se o cpf ja nao esta cadastrado