import paho.mqtt.client as mqtt_client
from library import *
import os
import time

printlog("Start Gateway TTN to Thingsboard" + " (pid : " + str(os.getpid()) + ")\n")

dPrm = getIniParameters("commissioning.ini")
for key, value in dPrm.items():
		    for key2,value in dPrm[key].items():
		            if value=="":
		                sys.exit("Error message: commissioning incomplete")

nbr_pid = 0

for i in range (1, len(dPrm)-1): #len(dPrm) = nbr d'élements dans le dico on enlève -2 pour les paramètres du broker et Things +1 car on commence le for à 1
	pid = os.fork()
	indice_app = 'TTN_APP_' + str(i)

	if (pid > 0):
		nbr_pid+=1
		time.sleep(2)


	elif (pid == 0):
		printlog("Connexion for app " + dPrm[indice_app]['appid'] + " (pid : " + str(os.getpid()) + ")")
		printlog("1/3 - Start MQTT Client")

		client = mqtt_client.Client( client_id=dPrm['MQTT']['clientid'])
		client.on_message = on_message
		client.on_connect = on_connect
		client.username_pw_set(username=dPrm[indice_app]['appid'], password=dPrm[indice_app]['accesskey'])

		
		while True:
			try:
				printlog("2/3 - Connection in progress... ")
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

		#topicsub = "v3/" + dPrm[indice_app]['appid'] + "@ttn/devices/+/up"
		topicsub = dPrm['MQTT']['topic']
		client.subscribe(topicsub)
		printlog("3/3 - Client MQTT is connected with TTN broker")
		printlog("subscribed topic : " + topicsub)
		client.loop_forever()
		break

	else:
		printlog("Erreur lors de du lancement de " + indice_app + " (création du fils)")
		break

while(nbr_pid):
	waitpid = os.wait()
	nbr_pid-=1

print("fin du process")