# Génération d'images Docker à la volée

Ce script Python permet de générer facilement des images Docker pour différentes architectures (macOS, Ubuntu, Windows). Il offre la possibilité de choisir l'architecture cible, de spécifier un numéro de version pour l'image, ainsi que de choisir l'API (client ou BO) à utiliser.

### Notes

- Windows : Le support pour Windows n'est pas encore implémenté.
- Exécution : Après la génération, le script vous proposera d'exécuter l'image Docker avec les bonnes configurations d'environnement pour l'API.

## Fonctionnalités

- **Choix de l'architecture OS** : Créez des images Docker pour macOS, Ubuntu ou Windows.
- **Numérotation des versions** : Spécifiez le numéro de version de l'image Docker (exemple : `1.0.0`).
- **Choix de l'API** : Choisissez l'API cible entre `client` et `bo` pour laquelle l'image Docker doit être générée.
- **Sauvegarde et exécution** : Le script permet de sauvegarder l'image générée dans un fichier `.tar`, de la compresser en `.zip`, et offre la possibilité d'exécuter l'image.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre système avant d'exécuter le script :

- **Python 3.x**
- **Docker** avec le support `buildx`
- **ZIP** (pour la compression des fichiers d'image Docker)

## Utilisation

### Étape 1 : Clonez le dépôt

Clonez le projet sur votre machine locale :

```bash
git clone https://github.com/acoory/docker-generator-image
cd docker-generator-image
```

### Étape 2 : Exécution du script

Pour lancer le script Python, exécutez la commande suivante :

```bash
python3 generate_docker_image.py
```

### Étape 3 : Interagir avec le script

Le script vous demandera de fournir plusieurs informations :

- Choix de l'architecture OS : Sélectionnez l'OS cible pour l'image Docker (mac, ubuntu, windows).

- Numéro de version de l'image : Fournissez un numéro de version (exemple : 1.0.0).

- API cible : Choisissez l'API client ou bo.

Le script vous fournira ensuite un récapitulatif de la configuration choisie avant de procéder à la création de l'image Docker.

### Structure du projet

Le projet contient les dossiers suivants :

```
├── Dockerfile-prod
├── README.md
├── docker-image
│   ├── mac-arm64
│   └── ubuntu-amd64
├── image-builder.py
├── index.js
├── lib
│   ├── __pycache__
│   │   ├── config_utils.cpython-312.pyc
│   │   ├── docker_utils.cpython-312.pyc
│   │   └── os_utils.cpython-312.pyc
│   ├── config_utils.py
│   ├── docker_utils.py
│   └── os_utils.py
└── package.json
```
