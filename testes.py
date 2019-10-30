import random
import bd1

nomeReserva = input('Insira o nome e a lane [Flavio "Jukes" Fernandes]-[TopLaner] -> ')    
bd1.cursor.execute(f"insert into equipes(reservas) values('{nomeReserva}')") 
bd1.connection.commit()
    