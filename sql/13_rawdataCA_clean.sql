DROP TABLE IF EXISTS rawdataCA_cleaned;

CREATE TABLE rawdataCA_cleaned AS

SELECT

    DAMAGE AS damage,
    STRUCTURETYPE AS structure_type,
    STRUCTURECATEGORY AS structure_category,
    ROOFCONSTRUCTION AS roof_construction,
    EAVES AS eaves,
    VENTSCREEN AS vent_screen,
    EXTERIORSIDING AS exterior_siding,
    WINDOWPANE AS window_pane,
    DECKPORCHONGRADE AS deck_porch_on_grade,
    DECKPORCHELEVATED AS deck_porch_elevated,
    PATIOCOVERCARPORT AS patio_cover_carport,
    FENCEATTACHEDTOSTRUCTURE AS fence_attached_to_structure,
    LATITUDE AS latitude,
    LONGITUDE AS longitude

FROM POSTFIRE;