# Aprendizajes del projecto: 
# Creación de APIs
# Flask 
# ORM con Python -> SQLAlchemy

from flask import Flask, request # Import the framework
import database
from models import Nadadores

app = Flask(__name__) # Instance 

@app.route('/crear-nadador' , methods=['GET'])
def crear_nadador(): # crear-nadador?name=Marcos&sex=H
    
    # Request parameters
    name = request.args.get('name') 
    sex = request.args.get('sex')
    exception_text = "Nadador was added to database succesfully" 

    try: 
        if (name == None or sex == None): 
            exception_text = "Missing Args (name, sex)"

        elif ( name != str(name) ): 
            exception_text = "Invalid Name"

        elif ( sex not in ['H' , 'M'] ):
            exception_text = "Invalid Sex only M or H"

        else: 
            new_nadador = Nadadores(name , sex) 
            database.session.add(new_nadador)
            database.session.commit() # Confirm the changues in db 
    except: 

        exception_text = "It was not possible to create Nadador"
    
    return exception_text

@app.route('/recuperar-nadador' , methods=['GET'])
def recuperar_nadador(): 
    # Request parameters
    name = request.args.get('name') 
    nadador_recuperado = None 

    try: 

        if (name is None ): 
            nadador_recuperado = "Missing argument: Name"
        
        else: 
            
            query_nadador = database.session.query(Nadadores.nadadorId, Nadadores.nombre, Nadadores.sexo).filter_by(nombre=name).first()
            nadador_recuperado = "El nadador "+str(query_nadador[1])+" con el id "+str(query_nadador[0])+" es "+str(query_nadador[2])
    except: 
        
        nadador_recuperado = "This Nadador doesn't exist in Database"

    return nadador_recuperado


if __name__ == '__main__': # Launch the server
    database.Base.metadata.create_all(database.engine)
    app.run(debug = True , port = 8000)

