# Tuto un seul fichier ini

Ce programme consiste à compter combien d'applications sont mentionnées dans le fichier `.ini`, créer un fils par application (utilisation de la méthode unix en python : `os.fork()`), se connecter au broker MQTT, recevoir les messages et les poster sur Thingsboard.

Avant de commencer, assurez-vous :
- *D'avoir bien installer les paquets mentionnées dans [README.md](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps#installation-des-librairies)*
- *D'être sur un réseau privé (si public l'accès au port 1883 doit être autorisé)*
- *D'être sur une machine Linux/MacOS (une machine qui peut utiliser des méthodes Unix)*
---

## Fichier `commissioning.ini`
Le template de ce fichier est [commissioning_sample_1file.ini](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file/commissioning_sample_1file.ini). Sa structure est la suivante :
- `[MQTT]` : pour le borker MQTT
- `[TTN_APP_X]` : les champs à remplir pour s'abonner au topic de l'application (créer une catégorie `[TTN_APP_X]` pour chaque application, `X` étant le numéro de l'application)
- `[THINGS]` : les informations nécessaires pour mettre les datas sur Thingsboard

## Fichier `gateway_ttn_thing_1file.py`
Le script python à exécuter est : [`gateway_ttn_thing_1file.py`](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file/gateway_ttn_thing_1file.py). Par défaut le nom du fichier commissioning est : `commissioning.ini`. Vous pouvez le changer dans le programme python [`gateway_ttn_thing_1file.py`](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file/gateway_ttn_thing_1file.py) à la ligne 8 :
```python
file_name = "commissioning.ini"
dPrm = getIniParameters(file_name)
```
et aussi dans le fichier [`library.py`](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file/library.py) ligne 48 : 
```python
dPrm = getIniParameters('commissioning.ini')
```

## Lancement du script
Ouvrez un terminal, rendez-vous dans le dossier où se trouve le fichier pythonet tapez la commande suivante :
```shell
python3 gateway_ttn_thing_1file.py
```

Dans mon cas, j'ai trois applications et voici l'affichage que vous devez avoir :
```
$ python3 gateway_ttn_thing_1file.py
2021/05/27 15:23:47: Start Gateway TTN to Thingsboard (pid : 31460)

2021/05/27 15:23:47: Connexion for app supagro-test (pid : 31462)
2021/05/27 15:23:47: 1/3 - Start MQTT Client
2021/05/27 15:23:47: 2/3 - Connection in progress... 
2021/05/27 15:23:47: 3/3 - Client MQTT is connected with TTN broker
2021/05/27 15:23:47: subscribed topic : v3/+/devices/+/up
2021/05/27 15:23:47: Connexion MQTT: code retour= 0
2021/05/27 15:23:47: Connexion MQTT: Statut= OK

2021/05/27 15:23:49: Connexion for app stm32-kit (pid : 31464)
2021/05/27 15:23:49: 1/3 - Start MQTT Client
2021/05/27 15:23:49: 2/3 - Connection in progress... 
2021/05/27 15:23:49: 3/3 - Client MQTT is connected with TTN broker
2021/05/27 15:23:49: subscribed topic : v3/+/devices/+/up
2021/05/27 15:23:49: Connexion MQTT: code retour= 0
2021/05/27 15:23:49: Connexion MQTT: Statut= OK

2021/05/27 15:23:51: Connexion for app hubis (pid : 31465)
2021/05/27 15:23:51: 1/3 - Start MQTT Client
2021/05/27 15:23:51: 2/3 - Connection in progress... 
2021/05/27 15:23:51: 3/3 - Client MQTT is connected with TTN broker
2021/05/27 15:23:51: subscribed topic : v3/+/devices/+/up
2021/05/27 15:23:51: Connexion MQTT: code retour= 0
2021/05/27 15:23:51: Connexion MQTT: Statut= OK
```
J'affiche les pid du processur père et de chaque fils pour permettre de les retrouver facilement lors par exemple d'un `ps -v` (affiche tous les processus et leurs status).

Lorsqu'on recoit une donnée on doit avoir l'affichage suivant :
```bash
2021/05/27 15:24:01: Recept message MQTT... (application : stm32-kit, pid : 31464)
2021/05/27 15:24:01: Topic : v3/stm32-kit@ttn/devices/6e20bd50-adb4-11eb-a50e-312e6f60d0f2/up
2021/05/27 15:24:01: data: {'barometric_pressure_0': 1014.7, 'digital_in_3': 0, 'digital_out_4': 0, 'relative_humidity_2': 57, 'temperature_1': 23.9}
2021/05/27 15:24:01: 1/6 - Send request to Access Token
2021/05/27 15:24:01: 2/6 - Request response ok
2021/05/27 15:24:01: 3/6 - Send request to Device token
2021/05/27 15:24:01: 4/6 - Request response ok
2021/05/27 15:24:01: 5/6 - Send request telemetry
2021/05/27 15:24:01: 6/6 - Request code reponse:
\\\\\\\\\\\\\\\\\\\\\\\\\\\\
```
Les données sont bien arrivées sur Thingsboards et sont disponibles !
