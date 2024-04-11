class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            print("Quantidade de combustível insuficiente na bomba.")
            return 0

    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        print(f" - Com R$ {litros} você pagará {valor_a_pagar}")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f" - Novo valor do litro alterado para {novo_valor}")
    
    def alterar_combustivel(self, novo_combustivel):
        self.tipo_combustivel = novo_combustivel
        print(f" - Combustível alterado para {novo_combustivel}")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f" - Quantidade de combustível alterado para {nova_quantidade}")


bomba = BombaCombustivel("Gasolina", 5.0, 100.0)

valor = float(input("Qual valor deseja abastecer? "))
litros_abastecidos = bomba.abastecer_por_valor(valor)
print(f"Litros abastecidos: {litros_abastecidos}")
print(f"Quantidade de combustível restante na bomba: {bomba.quantidade_combustivel} litros")


valor_litro = float(input("Qual valor do litro? "))
bomba.alterar_valor(valor_litro)

tipo = str(input("Qual tipo de combustível deseja colocar? "))
bomba.alterar_combustivel(tipo)

qtde_combustivel = float(input("Qual a quantidade de combustível na bomba? "))
bomba.alterar_quantidade_combustivel(qtde_combustivel)

litros = float(input("Quantos litros quer colocar? "))
bomba.abastecer_por_litro(litros)
print("*" * 8)
print(f"""Novo Tipo de combustível : {bomba.tipo_combustivel}
Novo valor do combustível : R$ {bomba.valor_litro}
Nova quantidade de combustível na bomba : {bomba.quantidade_combustivel} litros
      """)

print("----------FIM----------")