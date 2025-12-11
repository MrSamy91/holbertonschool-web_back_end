-- Script: 4-store.sql
-- Objectif: Décrémenter la quantité d'un item dans la table items après l'ajout d'une nouvelle commande

DELIMITER $$

CREATE TRIGGER update_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITE
