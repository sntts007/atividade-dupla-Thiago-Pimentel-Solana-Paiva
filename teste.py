# Equipe: Thiago Pimentel, Solana Paiva:

class carro:
    def __init__(self,marca,modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def ligar(self):
        return f"{self.ligar} está ligado."
    def desligar(self):
        return f"{self.desligar} está desligado"
    def acelerar(self):
        return f"{self.acelerar} está acelerando"  
 
if __name__ == "__main__" :
    carro1 = carro ("chevrollet", "chevette", "1995", "bege")
    print('marca', carro1.marca)
    print('modelo', carro1.modelo)
    print('ano', carro1.ano)
    print('cor', carro1.cor)
    
    print(carro1.ligar())
    print(carro1.desligar())
    print(carro1.acelerar())
    
