
def tank_erstellung ():  
    tank = { 
      "Laenge" : 5, 
      "Durchmesser" : 1.6,
      "Inhalt" : "Heizoel",
      "Fuellhoehe" : 0, 
      "Zustand" : "leer" 
      } 
    return tank 

tank = tank_erstellung()


def tank_zustand(tank):           
    if tank["Fuelhoehe"] == 0 :                   
        return("Zustand - leer")             
    elif tank["Fuelhoehe"] > 0:                   
        return("Zustand - nicht leer")    