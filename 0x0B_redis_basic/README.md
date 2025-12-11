# 0x0B. Redis basic

## Description
Ce projet est une introduction à **Redis** avec **Python**.  
Il permet de comprendre comment utiliser Redis pour :
- Stocker et récupérer des données simples (str, bytes, int, float).
- Créer un système de cache.
- Compter combien de fois une fonction est appelée.
- Conserver l’historique des appels (inputs et outputs).
- Rejouer cet historique.

Redis est une base de données en mémoire, très rapide, souvent utilisée comme cache ou système de file d’attente.

---

## Prérequis
- Ubuntu 20.04 LTS  
- Python 3.9  
- Redis  

### Installation
```bash
# Installer Redis
sudo apt update
sudo apt install redis-server -y

# Installer le client Python Redis
pip3 install redis
