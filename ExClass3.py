class Triangulo:
    ladoA = None
    ladoB = None
    ladoC = None
    
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def perimetro(self): #Todo método tem um self
        return self.ladoA + self.ladoB + self.ladoC
    
    def pegarMaiorlado(self):
        maiorLado = None
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            maiorLado = self.ladoA
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            maiorLado = self.ladoB
        elif self.ladoC > self.ladoA and self.ladoC > self.ladoB:
            maiorLado = self.ladoC
        else:
            maiorLado = "Todos os lados são iguais"

        return maiorLado

T1 = Triangulo(7, 8, 9)
print(T1.perimetro())
print(T1.pegarMaiorlado())

