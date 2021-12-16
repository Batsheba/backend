edad= 20
edad_minima=18
print(edad>=edad_minima)

if edad >= edad_minima:
    print('eres mayor de edad,puedes ingresar')
elif edad>15:
    print('puedes ingresar solo a los quinceañeros')
elif edad>10:
    print('puedes ingresar al zoo gratis')
else:
    print('Eres menor de edad ,no puedes hacer nada')
print('yo siempre me ejecuto')

#operador ternario
resultado ='eres mayor' if edad >= edad_minima else 'eres menor'
print(resultado)

numero=6

if numero % 2 == 0:
    print('es par')
else:
    print('impar')

resultado='par ' if numero%2==0 else 'impar'
print(resultado)

persona = {
    'nombre': 'Raul',
    'nacionalidad': 'Boliviana',
    'sexo': 'M'
}
if(persona['nombre']=='Raul' and persona['nacionalidad']=='Peruana'):
    print('si,la persona es',persona['nombre'],'y su nacionalidad es:',persona['nacionalidad'])
else:
      print('No,la persona es',persona['nombre'],'y su nacionalidad es:',persona['nacionalidad'])