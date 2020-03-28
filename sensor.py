import time
import serial
import mysql.connector
import datetime
from time import ctime
from datetime import datetime
import ntplib
import os
os.system("sudo pyhton3 python_obtner_hora_ntp.py")
firma_sensor_uno = 'pB61uO3rgsuRcQcP9Od9cSnrYr73IpyMzjuPwoaLafJ0lhbjPdiwEHjwyw3O0bJC4c3GJvogVDT0L+sR2vfQ5bLvzoXEoSrKmnNPsQHmqUqyhWshsT/4cZPOlCtqbmy5eXLn1tAQAziKOdaF75BkWQaAuCmj9av6+khflT6Fn3anVJdHDseI/bYBRuaVVO4d5S8mRIcXAUsAaqCS0t5fawj9APHvUhEwa8uDhP9p5PYd3syPmc0rCPXxzX3ywWQ92SfMiM7u+5nmjutlZd6o7Y02pUnuYRCQO0vnNFu0qPpp/Xzvx/Ehplx9ttl5/6pZunbFuuj1MbjZgUXwum7k4g=='
config = {
    'user': 'batman',
    'password': 'Foto5#13',
    'host': '127.0.0.1',
    'database': 'datos',
    'raise_on_warnings': True
    }
ser = serial.Serial("/dev/ttyACM0",9600)

try:
    while True:
        read = ser.readline()
        dato = read.splitlines()
        b = str(dato[0])
        c = b.replace("b","")
        d = c.replace("'","")
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            now = datetime.now()
            fecha = now.strftime('%Y-%m-%d')
            hora = now.strftime('%H:%M:%S')
            consulta = "INSERT INTO `intensidad` (firma, fecha, hora, variable, valor) VALUES ('"+str(firma_sensor_uno)+"','"+str(fecha)+"', '"+str(hora)+"', 'intensidad', "+str(d)+");"
            cursor.execute(consulta)
            cnx.commit()
        except mysql.connector.Error as err:
                print(err)
        else:
            cnx.close()
        time.sleep(5)
except Exception as error:
    print(error)
except KeyboardInterrupt:
    print("Saliendo del programa")
finally:
    ser.close()