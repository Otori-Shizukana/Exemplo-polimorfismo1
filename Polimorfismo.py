class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_detalhes(self):
        print(f"Marca: {self.marca}, Modelo:{self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def mostrar_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Portas: {self.portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def mostrar_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cilindradas: {self.cilindrada}")

def mostrar_informações_veiculo(veiculo):
    veiculo.mostrar_detalhes()

carro = Carro("Fiat", "Argo", 4)
moto = Moto("Honda", "Xj6", 600)
mostrar_informações_veiculo(carro)
mostrar_informações_veiculo(moto)