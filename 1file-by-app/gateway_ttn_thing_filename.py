import paho.mqtt.client as mqtt_client
from library import *
import os
import time
import sys

printlog("Start Gateway TTN to Thingsboard" + " (pid : " + str(os.getpid()) + ")\n")

nbr_applications = len(sys.argv)-1
nbr_pid = 0

if (nbr_applications <= 0):
    printlog("Files names missing")
    exit()
for i in range(1, nbr_applications+1):
    pid = os.fork()

    if (pid > 0):
        nbr_pid+=1
        time.sleep(2)

    elif pid == 0:
        indiceFils_a_jour(i)
        comm = sys.argv[i]
        printlog("Loading configuration in " + comm)
        dPrm = getIniParameters(comm) #loading of all keys and connection parameters

        for key, value in dPrm.items():
            for key2,value in dPrm[key].items():
                    if value=="":
                        sys.exit("Error message: commissioning incomplete")

        printlog("Connection pour l'application " + dPrm['TTN']['appid'] + " (pid : " + str(os.getpid()) + ")")
        printlog("1/3 - Start MQTT Client (pid : "+ str(os.getpid()) + ")" )
        client = mqtt_client.Client( client_id=dPrm['MQTT']['clientid'] ) #launch of the mqtt client

        #interrupt function
        client.on_message = on_message
        client.on_connect = on_connect
        #client.on_log = on_log 
        # Connexion broker
        client.username_pw_set(username=dPrm['TTN']['appid'], password=dPrm['TTN']['accesskey'] )

        while True:
            try:
                printlog("2/3 - Connection in progress...")
                client.connect(host=dPrm['MQTT']['broker'], port=int(dPrm['MQTT']['port']), keepalive=int(dPrm['MQTT']['keep_alive']))
                break
            except TimeoutError as e:
                printlog("Timeout: (Probably: not route with the broker)")
                printlog(str(e))
                continue
            except OSError as e:
                printlog("OSError: (Probably: not permission to open port Mqtt)")
                printlog(str(e))
                continue

        client.subscribe(dPrm['MQTT']['topic'])
        printlog("3/3 - Client MQTT is connected with TTN broker")
        client.loop_forever()

    else:
        printlog("Erreur lors de du lancement de " + indice_app + " (création du fils)")
        break

while(nbr_pid):
	waitpid = os.wait()
	nbr_pid-=1
    
print("process end")

