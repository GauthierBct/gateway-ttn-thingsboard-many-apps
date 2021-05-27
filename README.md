# Script python pour transmettre les données de TTN (v3) vers Thingsboard (en MQTT)
Utilisation du script Python de @guiguitt et @DDorch, pour le rendre utilisable pour plusieurs applications avec un seul script. Ce script peut tourner uniquement sur des machines compatibles aux méthodes Unix.

## Choix du dispositifs 
Dans ce répertoire Git, vous pouvez trouver deux fichiers `.py` :
- `gateway_ttn_thing_1file.py` (<a href="https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file-by-app/README.md">Tuto avec un seul fichier commissioning</a>) est utile si vous utilisez un nombre important d'applications .
- `gateway_ttn_thing_filename.py` (<a href="https://github.com/GauthierBct/gateway-ttn-thingsboard-many-apps/blob/main/1file/README.md">Tuto avec plusieurs fichiers commissioning</a>) est utile dans le cas où vous auriez plus de deux ou trois applications (utilise un fichier `.ini` par application).

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
pip3 list
```
Normalement, les deux bibliothèques installées sont listées et les autres utilisées sont déjà disponibles l'environnement par défaut de python3. 

Vous pouvez à présent utiliser les scripts fournis. ⚠️ Il se peut que la connexion MQTT ne se fasse pas, c'est le cas si vous utilisez un réseau public tel que "WIFI CAMPUS" (bloque très souvent l'accèes au port 1883) ⚠️
