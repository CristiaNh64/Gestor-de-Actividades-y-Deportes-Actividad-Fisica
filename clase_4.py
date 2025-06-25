print('Hola comision 7') #Esto es una funcion

#como es tipado dinamico puedo simplemente asignarle a las variables lo que quiero y el lenguaje interpreta lo que es segun lo guarde
curso = "Desarrollo WEB" #esto se toma como STRING o str

estoy_cursando = True #si yo coloco true da error porque tiene que estar la T en mayuscula

print(type(curso)) # devuelve el tipo de dato que es curso

valor = input('ingresa un valor: ') #Esto funcionaria para ingresar datos por teclado, los datos se ingresan como STRING, si queremos un numero debemos convertirlo
print("El valor ingresado es: ", valor)

valor_numerico = input("Ingresa un valor numerico: ")
valor_numerico = int(valor_numerico) #Aca estoy dandole el valor numerico en base 10

#sino podemos hacer Valor=int(input("ingresa valor para sumar: ")) y ya convierte en numero el valor ingresado
try:
    v= input("ingresa un numero")
    int(v)
except ValueError:
    print("Flaco te pedi un numero, no sabes leer?")
    #Lo que hace esto es, si se detecta el error de valueError va a decir ese mensaje
    
