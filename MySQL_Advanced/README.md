# MySQL Advanced

## Description
Ce projet couvre les concepts avancés de MySQL.  
L’objectif est de manipuler des fonctionnalités essentielles pour optimiser, automatiser et sécuriser les opérations sur une base de données relationnelle.  

À travers une série de tâches, nous mettons en pratique :
- La création de tables avec contraintes
- L’optimisation de requêtes avec des indexes
- Les procédures stockées et fonctions
- Les vues
- Les triggers

---

## Ressources
Avant de commencer, il est recommandé de lire ou regarder les documents suivants :  
- [MySQL cheatsheet](https://devhints.io/mysql)  
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.percona.com/blog/mysql-performance-how-to-leverage-mysql-database-indexing/)  
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-routines.html)  
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)  
- [Views](https://dev.mysql.com/doc/refman/8.0/en/views.html)  
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)  
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)  
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)  
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)  
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)  

---

## Objectifs d’apprentissage
À la fin du projet, vous devez être capable d’expliquer :  
- Comment créer des tables avec contraintes  
- Comment optimiser des requêtes grâce aux indexes  
- Ce que sont et comment implémenter des procédures stockées et fonctions  
- Ce que sont et comment implémenter des vues  
- Ce que sont et comment implémenter des triggers  

---

## Environnement
- Système : **Ubuntu 20.04 LTS**  
- Base de données : **MySQL 8.0**  
- Tous les fichiers `.sql` doivent être exécutables avec la commande `mysql -uroot -p`.  
- Chaque fichier doit :  
  - commencer par un commentaire décrivant la tâche  
  - utiliser les mots-clés SQL en majuscules (`SELECT`, `WHERE`, …)  
  - contenir un commentaire avant chaque requête  

---

## Comment exécuter un fichier SQL
```bash
cat fichier.sql | mysql -uroot -p nom_de_la_base
