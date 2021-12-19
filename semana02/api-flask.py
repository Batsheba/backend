from flask import Flask,request
from flask_cors import CORS

app=Flask(__name__)
CORS(app=app)

@app.route('/',methods=['POST','GET'])
def inicio():
    print(request.method)

    if request.method=='POST':
        print(request.get_json())
        data=request.get_json()

        if (data['nombre']):
            nombre=data['nombre']
            return 'hola,{}!'.format(nombre)
        else:
            return 'necesito la informaación',400
    elif request.method=='GET':
        return 'bienvenido a mi api Productos',200

mis_productos=[]
@app.route('/productos', methods=['GET','POST'])
def productos():
    if request.method=='GET':
        return {
            'data': mis_productos,
            'message': 'Los productos son:',
            'ok':True
        }
    elif request.method=='POST':
        data=request.get_json()
        mis_productos.append(data)
        return {
            'data': data,
            'message': 'Producto agregado exitosamente',
            'ok':True
        },201

mis_productos = [{
    "nombre":"Paneton con arto bromato",
    "precio": 17.50,
    "disponible": True,
    "fecha_vencimiento": "2022-01-14"
}, {
    "nombre":"Chocolate con arta azucar",
    "precio": 6.90,
    "disponible": False,
    "fecha_vencimiento": "2021-12-30"
}]

@app.route('/producto/<int:id>', methods=['GET','PUT'])
def producto(id):
    if request.method == 'GET':

      if(id<len(mis_productos)):
          return {
              'ok':True,
              'data':mis_productos[id],
              'message':'El producto es:'
          }
      else:
          return {
              'ok':False,
              'data':None,
              'message':'El producto no existe'
          }
    elif request.method=='PUT':
        data=request.get_json()
        if(id<len(mis_productos)):
            mis_productos[id]=data
            return{
                 'ok':True,
                'data':mis_productos[id],
               'message':'Producto actualizado exitosamente '
            },201
        else:
            return{
                 'ok':False,
                'data':None,
                'message':'El producto con el id {} no exite'.format(id)
            }

if __name__=='__main__':
    app.run(debug=True)