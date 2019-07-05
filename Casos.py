import requests



def Casos():
    datos = ('orden','escenario')
    return datos


class Casos:
    # id = 0
    # escenario = ""
    # accion = ""
    # responsables = ""
    # emailsResponsable = ""


    def __init__(self):
        self.id = 0
        self.orden = ""
        self.escenario = ""
        self.accion = ""
        self.responsables = []
        self.emailsResponsable = []
        self.estado = ""
        self.vecesReportado = 0

    
         

