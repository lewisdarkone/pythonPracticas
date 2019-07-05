from Casos import Casos
from crud import insertReport

c = Casos()

c.id = 1
c.escenario = "Quitese no capturado"
c.accion = "Digitar Quitese"
c.responsables = ["Analisis y correccion de ordenes","Digitacion de ordenes"]
c.emailsResponsable = ["analisis@claro.com.do","digitacion@claro.com.do"]


insertReport()


print("")

