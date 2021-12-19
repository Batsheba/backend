console.log("hola desde el navegador")

fetch('http://127.0.0.1:5000/productos',{method:'GET'})
.then((response)=>{
  return response.json();
})
.then((data)=>{
  console.log(data);
})
.catch((error)=>{
    console.log(error);
});

fetch('http://127.0.0.1:5000/productos',{
    method:'POST',
    body: JSON.stringify({
        "nombre":"Paneton con arto bromato",
        "precio": 17.50,
        "disponible": true,
        "fecha_vencimiento": "2022-01-14"
    }),
    headers:{
        "Content-Type": "application/json",
    }
})
.then((response)=>{
    return response.json();
})
.then((data)=>{
    console.log(data);
})
.catch((error)=>{
      console.log(error);
});
