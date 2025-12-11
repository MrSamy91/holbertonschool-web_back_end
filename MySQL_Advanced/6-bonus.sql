-- 6-bonus.sql

DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
)
BEGIN
    DECLARE v_project_id INT;

    -- Vérifier si le projet existe déjà
    SELECT id INTO v_project_id
    FROM projects
    WHERE name = p_project_name
    LIMIT 1;

    -- Si le projet n'existe pas, l'ajouter
    IF v_project_id IS NULL THEN
        INSERT INTO projects(name) VALUES (p_project_name);
        SET v_project_id = LAST_INSERT_ID();
    END IF;

    -- Ajouter la correction pour l'utilisateur et le projet
    INSERT INTO corrections(user_id, project_id, score)
    VALUES (p_user_id, v_project_id, p_score);
END $$

DELIMITER ;
