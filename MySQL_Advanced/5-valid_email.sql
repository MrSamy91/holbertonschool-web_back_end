-- Script: 5-valid_email.sql
-- Objectif: Réinitialiser valid_email seulement si l'email d'un utilisateur change

DELIMITER $$

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
