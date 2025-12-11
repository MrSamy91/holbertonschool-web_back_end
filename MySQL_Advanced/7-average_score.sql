-- Procedure ComputeAverageScoreForUser:
-- Cette procédure calcule la moyenne des scores d'un étudiant
-- à partir de la table corrections et met à jour la colonne average_score
-- dans la table users pour l'utilisateur spécifié.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    -- Calculer la moyenne des scores pour l'utilisateur donné
    SELECT AVG(score)
    INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- Mettre à jour la colonne average_score de l'utilisateur
    UPDATE users
    SET average_score = avg_score
    WHERE id = p_user_id;
END $$

DELIMITER ;
