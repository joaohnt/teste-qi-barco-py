def printar_jogo():
    print("Lado esquerdo: ", lado_esquerdo)
    print("Lado direito: ", lado_direito)
    print("Lado do barco: ", barco_lado)
    print("Histórico de travessias: ", historico)

def validar_regras():
    for lado in [lado_esquerdo, lado_direito]:
        if "mãe" in lado and any(filho in lado for filho in ["filho1", "filho2"]) and "pai" not in lado:
            return False, "Erro: A mãe não pode ficar sozinha com os filhos!"
        if "pai" in lado and any(filha in lado for filha in ["filha1", "filha2"]) and "mãe" not in lado:
            return False, "Erro: O pai não pode ficar sozinho com as filhas!"
        if "prisioneiro" in lado and "policial" not in lado and len(lado) > 1:
            return False, "Erro: O prisioneiro não pode ficar sozinho com ninguém da família!"
    return True, ""

def escolher_personagens():
    global barco_lado
    print("Quem você quer colocar no barco? ")
    entrada = input().split()
 
    # no minimo 1 pessoa e no max 2 pra pilotar
    if len(entrada) > 2:
        print("Erro: O barco está cheio! Só é possível adicionar até 2 pessoas.")
        return 
    elif len(entrada) < 1: 
        print("Erro: O barco não pode estar vazio! Adicione pelo menos 1 pessoa.")
        return 
    
    if not any(p in entrada for p in ["pai", "mãe", "policial"]):
        print("Erro: Somente o pai, a mãe ou o policial podem pilotar o barco!")
        return
    
    # p trocar o lado
    lado_atual = lado_esquerdo if barco_lado == "esquerdo" else lado_direito
    lado_oposto = lado_direito if barco_lado == "esquerdo" else lado_esquerdo

    if all(p in lado_atual for p in entrada):  
        for p in entrada:
            lado_atual.remove(p)
            lado_oposto.append(p)
        
        barco_lado = "direito" if barco_lado == "esquerdo" else "esquerdo"
        
        valido, msg = validar_regras()
        if not valido:
            print(msg)
            for p in entrada:
                lado_oposto.remove(p)
                lado_atual.append(p)
            barco_lado = "direito" if barco_lado == "esquerdo" else "esquerdo"
        else:
            historico.extend(entrada)
    else:
        print("Erro: Um ou mais personagens não estão no mesmo lado que o barco!")

lado_esquerdo = ["mãe", "pai", "filho1", "filho2", "filha1", "filha2", "policial", "prisioneiro"]
lado_direito = []
historico = []
barco_lado = "esquerdo"

while True:
    printar_jogo()
    escolher_personagens()