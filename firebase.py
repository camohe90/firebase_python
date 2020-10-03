
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep



# Fetch the service account key JSON file contents
cred = credentials.Certificate('C:/Users/Camilo/haiko/proyecto/clave/clave.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://haiko-bd.firebaseio.com/'
})

for i in range (0,100001,10000):

    ref = db.reference("cuentas/camilo")
    ref.update({
                    'cuenta1': i,
                    'cuenta2': i+5000 
            }) 
    print("Agregue ", i , "pesos ")              
    sleep(1.5)   

cont = db.reference('cuentas/camilo/cuenta2').get()
print("El saldo final de Camilo es ", cont)





    


    
    
