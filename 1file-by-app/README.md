# Tuto plusieurs fichiers commissionning.ini

Ce programme consiste à compter combien d'applications sont mentionnées dans le fichier `.ini`, créer un fils par application (utilisation de la méthode unix en python : `os.fork()`), se connecter au broker MQTT, recevoir les messages et les poster sur Thingsboard.

Avant de commencer, assurez-vous :
- *D'avoir bien installer les paquets mentionnées dans [README.md](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps#installation-des-librairies)*
- *D'être sur un réseau privé (si public l'accès au port 1883 doit être autorisé)*
- *D'être sur une machine Linux/MacOS (une machine qui peut utiliser des méthodes Unix)*
---

## Fichier `commissioning.ini`
Le template de ce fichier est [commissioning_sample_app.ini](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file-by-app/commissioning_sample.ini). Sa structure est la suivante :
- `[MQTT]` : pour le borker MQTT
- `[TTN]` : les champs à remplir pour s'abonner au topic de l'application
- `[THINGS]` : les informations nécessaires pour mettre les datas sur Thingsboard

## Fichier `gateway_ttn_thing_1file.py`
Le script python à exécuter est : [`gateway_ttn_thing_1file.py`](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file-by-app/gateway_ttn_thing_filename.py).

## Lancement du script
Ouvrez un terminal, rendez-vous dans le dossier où se trouve le fichier pythonet tapez la commande suivante :
```
python3 gateway_ttn_thing_filename.py <nom_fichier1.ini> <nom_fichier2.ini>
```

Dans mon cas, j'ai deux applications et voici l'affichage que vous devez avoir :
```
 $ python3 gateway_ttn_thing_filename.py commissioning_supagro.ini commissioning_stm.ini 
2021/05/27 15:43:39: Start Gateway TTN to Thingsboard (pid : 31780)

2021/05/27 15:43:39: Loading configuration in commissioning_supagro.ini
2021/05/27 15:43:39: Connection pour l'application supagro-test (pid : 31782)
2021/05/27 15:43:39: 1/3 - Start MQTT Client (pid : 31782)
2021/05/27 15:43:39: 2/3 - Connection in progress...
2021/05/27 15:43:39: 3/3 - Client MQTT is connected with TTN broker
2021/05/27 15:43:39: Connexion MQTT: code retour= 0
2021/05/27 15:43:39: Connexion MQTT: Statut= OK

2021/05/27 15:43:41: Loading configuration in commissioning_stm.ini
2021/05/27 15:43:41: Connection pour l'application stm32-kit (pid : 31785)
2021/05/27 15:43:41: 1/3 - Start MQTT Client (pid : 31785)
2021/05/27 15:43:41: 2/3 - Connection in progress...
2021/05/27 15:43:41: 3/3 - Client MQTT is connected with TTN broker
2021/05/27 15:43:41: Connexion MQTT: code retour= 0
2021/05/27 15:43:41: Connexion MQTT: Statut= OK
```
J'affiche les pid du processur père et de chaque fils pour permettre de les retrouver facilement lors par exemple d'un `ps -v` (affiche tous les processus et leurs status).

Lorsqu'on recoit une donnée on doit avoir l'affichage suivant :
```
2021/05/27 15:44:14: Recept message MQTT... (application : stm32-kit, pid : 31785)
2021/05/27 15:44:14: Topic : v3/stm32-kit@ttn/devices/6e20bd50-adb4-11eb-a50e-312e6f60d0f2/up
2021/05/27 15:44:14: data: {'barometric_pressure_0': 1014.7, 'digital_in_3': 0, 'digital_out_4': 0, 'relative_humidity_2': 54.5, 'temperature_1': 24.7}
2021/05/27 15:44:14: 1/6 - Send request to Access Token
2021/05/27 15:44:14: 2/6 - Request response ok
2021/05/27 15:44:14: 3/6 - Send request to Device token
2021/05/27 15:44:14: 4/6 - Request response ok
2021/05/27 15:44:14: 5/6 - Send request telemetry
2021/05/27 15:44:15: 6/6 - Request code reponse:
\\\\\\\\\\\\\\\\\\\\\\\\\\\\
```
Les données sont bien arrivées sur Thingsboards et sont disponibles !
