# ejercicio 7
class Cuenta():
    
    def constructor(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad


    def setcantidad(self, cantidad):
        self.__cantidad = cantidad
    
    def getcantidad(self, titular):
        self.__titular = titular

    def mostrar(self):
        return f"El titular es: "+self.__titular +", el saldo es: "+str(self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = self.__cantidad + cantidad
            print("Ingresando: "+str(cantidad))

    def retirar(self, cantidad):
        if cantidad >=0:
            self.__cantidad = self.__cantidad - cantidad
            print("Retirando: "+str(cantidad))


cuenta1 = Cuenta()
cuenta1.constructor("Juan Perez", 1000)
print(cuenta1.mostrar())
cuenta1.ingresar(50)
print(cuenta1.mostrar())

#ejercicio 8
class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion, edad):
        Cuenta.constructor(self, titular, cantidad)
        self.__bonificacion = bonificacion
        self.__edad = edad
 

    def setbonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
    
    def getbonificacion(self):
        return str(self.__bonificacion)
    
    def titular_valido(self):
        if self.__edad >= 18 and self.__edad <= 25:
            return True        
        else: 
            return False

    def retirar(self, cantidad):
        if self.titular_valido():
            super().retirar(cantidad)
            print("Retiro correcto.")
        else: 
            print("El titular no es valido. Retiro anulado")

    def mostrar(self):
        return super().mostrar() +", edad: "+str(self.__edad)+", la bonificacion es: "+ self.getbonificacion()


cuentajoven1 = CuentaJoven("Pepe", 10000, 10, 19)
print(cuentajoven1.mostrar())
cuentajoven1.retirar(500)
print(cuentajoven1.mostrar())
cuentajoven2 = CuentaJoven("Gomez", 5000, 10, 17)
print(cuentajoven2.mostrar())
cuentajoven2.retirar(500)
print(cuentajoven2.mostrar())


            



    






    

    
