dias=['lunes','martes','miercoles']

#agregar
dias.append('jueves')
print(dias)

#eliminar
dias.remove('martes')
print(dias)
# dias.clear()
# print(dias)

otros_dias =['sabado','domingo']
dias_semana=dias + otros_dias
print(dias_semana)


#variables mutables/inmutables
nombre1='luis'
nombre2=nombre1
nombre1='felipe'

lista1=[1,2,3,4,5]
lista2=lista1
lista3=lista1[:]
lista1[0]=50
print(id(lista1))
print(id(lista2))
print(id(lista3))
print('la lista 1 es :',lista1)
print('la lista 2 es :',lista2)
print('la lista 3 es :',lista3)
