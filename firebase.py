
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
datos =[]


# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/Camilo/haiko/proyecto_BD_2/clave/clave.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-haiko.firebaseio.com//'
})


for i in range (10):

    ref = db.reference("mensajes")
    mensaje= "herrera" +str(i) 
    ref.child("3").push(mensaje)

datos = ref.get("mensajes/1")
print(datos[0])





    



    
    
