def printar_jogo():
    print("Lado esquerdo: ", lado_esquerdo)
    print("Lado direito: ", lado_direito)
    print("Lado do barco: ", barco_lado)
    print("Histórico de travessias: ", historico)

def escolher_personagens():
    print("Quem você quer colocar no barco? ")
    entrada = input().split()
 
    if len(entrada) > 2:
        print("Erro: O barco está cheio! Só é possível adicionar até 2 pessoas.")
        return 
    elif len(entrada) < 1: 
        print("Erro: O barco não pode estar vazio! Adicione pelo menos 1 pessoa.")
        return 

    lado_atual = lado_esquerdo if barco_lado == "esquerdo" else lado_direito
    lado_oposto = lado_direito if barco_lado == "esquerdo" else lado_esquerdo

    if all(p in lado_atual for p in entrada):  
        for p in entrada:
            lado_atual.remove(p)
            lado_oposto.append(p) 
            historico.append(p)
        mover_barco()

    else:
        print("Erro: Um ou mais personagens não estão no mesmo lado que o barco!")

def mover_barco():
    global barco_lado
    barco_lado = "direito" if barco_lado == "esquerdo" else "esquerdo"


lado_esquerdo = ["mãe", "pai", "filho1", "filho2", "filha1", "filha2", "policial", "prisioneiro"]
lado_direito = []
historico = []
barco_lado = "esquerdo"

while True:
    printar_jogo()
    escolher_personagens()