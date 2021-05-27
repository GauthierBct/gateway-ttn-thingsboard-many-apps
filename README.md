# Script python pour transmettre les données de TTN (v3) vers Thingsboard (en MQTT)
Utilisation du script Python de @guiguitt et @DDorch, pour le rendre utilisable pour plusieurs applications avec un seul script. Ce script peut tourner uniquement sur des machines compatibles aux méthodes Unix.

## Choix du dispositifs 
Dans ce répertoire Git, vous pouvez trouver deux fichiers `.py` :
- `gateway_ttn_thing_1file.py` ([tuto avec un seul fichier commissioning](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file-by-app/README.md)) : est utile si vous utilisez un nombre important d'applications.
- `gateway_ttn_thing_filename.py` ([tuto avec plusieurs fichiers commissioning](https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file/README.md)) : est utile dans le cas où vous auriez plus de deux ou trois applications (utilise un fichier `.ini` par application). Un autre avantage est aussi vous pouvez envoyer les données de chaque app sur un serveur Thingsboard différents.

Choissiez en fonction de votre utilisation le dispositif adéquat.

## Installation des librairies
Pour installer les librairies nécessaires, il faut avoir le gestionnaire de paquet python `pip`. 
```bash
pip3 --version
```
Cette commande renvoie la version installée de `pip3`. Si le retour est de la forme suivante :
```
pip3: command not found
```
Il faut alors installer pip3 : https://www.linuxscrew.com/install-pip  

Il faut installer deux librairies 
- paho-mqtt : 
```bash
pip3 install paho-mqtt
```
- requests : 
```bash
pip3 install requests
```
Lorsque les deux sont installées, faites :
```bash
$ pip3 list
Package    Version
---------- ---------
certifi    2020.12.5
chardet    4.0.0
idna       2.10
paho-mqtt  1.5.1
pip        21.1.2
requests   2.25.1
setuptools 41.2.0
six        1.15.0
urllib3    1.26.4
wheel      0.33.1
```
Normalement, les deux bibliothèques installées sont listées et les autres utilisées sont déjà disponibles l'environnement par défaut de python3. 

Vous pouvez à présent utiliser les scripts fournis. ⚠️ Il se peut que la connexion MQTT ne se fasse pas, c'est le cas si vous utilisez un réseau public tel que "WIFI CAMPUS" (bloque très souvent l'accèes au port 1883) ⚠️
