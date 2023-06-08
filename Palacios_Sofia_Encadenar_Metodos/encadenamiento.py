class Usuario:
    def __init__(self, name):
        self.name = name
        self.balance_cuenta = 1000

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount 
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount 
        return self
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: ${self.balance_cuenta}")
        return self

    def transfer_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        return self


guido = Usuario ("Guido van Rossum")
guido.hacer_deposito(100).hacer_deposito(100).hacer_deposito(100).hacer_retiro(100).mostrar_balance_usuario()  


emi = Usuario ("Emilia")
emi.hacer_deposito(500).hacer_deposito(500).hacer_retiro(200).hacer_retiro(200).mostrar_balance_usuario()


eve = Usuario("Eve")
eve.hacer_deposito(1000).hacer_retiro(300).hacer_retiro(300).hacer_retiro(300).mostrar_balance_usuario()

guido.transfer_dinero(eve, 200).mostrar_balance_usuario()   
eve.mostrar_balance_usuario()