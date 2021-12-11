#variale num
numero=20
numero2=20.2

nom="bat"
apellido='mal'

fecha=0

html ='''<html>
<p>
</p>'''

print ('print:python')

print(type(nom))
print(type(numero2))
print(type(numero))

soltera=False
cold=True
print(type(soltera))

list=[1,2,3,4,'ya viene por ti',[1,2],True]

curso={
    'nombre':'backend',
     'dificultad':'dificil',
    'skills':[
    {
    'nombre':'backend1',
     'nivel':'dificil1',
     },
     {
        'nombre':'backend2',
       'nivel':'dificil2',  
     }
     ]
}
print (list[2:-2])
print (curso['skills'][1]['nivel'])


personas=[{
     'nombre':'Luisa',
     'nacionalidad':'peruano',
    'hobbies':[
    {
    'nombre':'volar drones',
     'experiencia':'2 años',
     },
     {
        'nombre':'Programar ',
       'experiencia':'1 mes',  
     }
     ]
},{
     'nombre':'Luis',
     'nacionalidad':'colombiano',
    'hobbies':[
    {
    'nombre':'montar bici',
     'experiencia':'4 años',
     },
     {
        'nombre':'base de datos ',
       'experiencia':'8 mes',  
     }
     ]
}]
print (personas[0]['nacionalidad'])
print(personas[1]['hobbies'])
print(personas[0]['hobbies'][1]['experiencia'])
