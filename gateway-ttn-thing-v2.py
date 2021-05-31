import paho.mqtt.client as mqtt_client
from library import *
import os
import time
import signal 

npid = 0
nfiles = 0
napps = 0

def exit_handler(signum, frame):
    print('Exiting....')
    exit(0)

signal.signal(signal.SIGTSTP, exit_handler)

printlog("Start Gateway TTN to Thingsboard" + " (pid : " + str(os.getpid()) + ")\n")

print("******** INITILIAZATION STARTING ********\n")
nfiles = len(sys.argv) - 1

if (nfiles <= 0):
    printlog("Files names missing")
    exit()

printlog(str(nfiles) + " files found !")

for i in range (1, nfiles+1):
    dPrm = getIniParameters(sys.argv[i])
    taille = len(dPrm) - 2
    printlog(str(taille) + " app(s) found in " + sys.argv[i])
    napps += taille

printlog("Starting connexion for " + str(napps) + " app(s)...\n")

for i in range(1, nfiles+1):
    dPrm = getIniParameters(sys.argv[i])
    taille = len(dPrm) - 2
    udpateFileNum(i)

    for k in range(1, taille + 1):
        pid = os.fork()
        app_name = 'TTN_APP_' + str(k)

        if (pid > 0):
            npid+=1
            time.sleep(2)

        elif pid == 0:
            printlog("Connexion for app " + dPrm[app_name]['appid'] + " (pid : " + str(os.getpid()) + ")")
            printlog("1/3 - Start MQTT Client")

            client = mqtt_client.Client( client_id=dPrm['MQTT']['clientid'])
            client.on_message = on_message
            client.on_connect = on_connect
            client.username_pw_set(username=dPrm[app_name]['appid'], password=dPrm[app_name]['accesskey'])

            
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

            topicsub = "v3/" + dPrm[app_name]['appid'] + "@ttn/devices/+/up"
            #topicsub = dPrm['MQTT']['topic']
            client.subscribe(topicsub)
            printlog("3/3 - Client MQTT is connected with TTN broker")
            printlog("subscribed topic : " + topicsub)
            client.loop_forever()
            break
        
        else:
            printlog("Error in fork()")
            exit()


print("******** INITILIAZATION DONE ********\n")

while(npid):
	waitpid = os.wait()
	npid-=1
