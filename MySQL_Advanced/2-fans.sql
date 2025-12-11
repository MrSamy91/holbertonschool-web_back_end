-- Script: 2-fans.sql
-- Objectif: Classer les pays d'origine des groupes de métal par nombre total de fans (non-uniques)
-- Importer d'abord le dump metal_bands.sql avant d'exécuter ce script

SELECT
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;
