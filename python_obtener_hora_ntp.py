#
#   python_obtener_hora_ntp.py
#
#   Obtiene la hora de un servidor NTP
#   octubre 2019 - Rogelio Ferreira Escutia
#
#   Requiere instalar la librería: ntplib
#   En consola ejecutar: pip install ntplib
#
#   La lista de algunos servidores se hora:
#   https://tf.nist.gov/tf-cgi/servers.cgi
#   http://support.ntp.org/bin/view/Servers/StratumOneTimeServers
#

import datetime
from time import ctime
import ntplib
import os

try:
    servidor_de_tiempo = "https://tf.nist.gov/tf-cgi/servers.cgi"
    client = ntplib.NTPClient()
    response = client.request(servidor_de_tiempo, version=4)
    print("====================================")
    print("Pidiendo hora a: "+servidor_de_tiempo)
    print(" Offset : "+str(response.offset))
    print(" Version : "+str(response.version))
    print(" Date Time : "+str(ctime(response.tx_time)))
    print(" Leap : "+str(ntplib.leap_to_text(response.leap)))
    print(" Root Delay : "+str(response.root_delay))
    print(" Ref Id : "+str(ntplib.ref_id_to_text(response.ref_id)))
    os.system("sudo date -s '"+str(ctime(response.tx_time))+"'")
    print("Hora actualizada")
    print("====================================" )
except:
    os.system("sudo date")
    print("NTP Server Down Date Time NOT Set At The Startup")
    pass

