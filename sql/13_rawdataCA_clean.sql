DROP TABLE IF EXISTS rawdataCA_cleaned;

CREATE TABLE rawdataCA_cleaned AS

SELECT
    OBJECTID AS object_id,
    NULLIF(TRIM(DAMAGE), '') AS damage,
    NULLIF(TRIM(STRUCTURETYPE), '') AS structure_type,
    NULLIF(TRIM(STRUCTURECATEGORY), '') AS structure_category,

    CASE
        WHEN OBJECTID = 132518 THEN NULL
        WHEN OBJECTID = 132298 THEN 'Concrete'
        WHEN OBJECTID = 131178 THEN NULL
        WHEN OBJECTID = 131284 THEN 'Concrete'
        WHEN OBJECTID = 130765 THEN 'Concrete'
        WHEN OBJECTID = 131414 THEN NULL
        WHEN OBJECTID = 130907 THEN NULL
        WHEN OBJECTID = 94577 THEN NULL
        WHEN OBJECTID = 109625 THEN 'Asphalt'
        ELSE NULLIF(TRIM(ROOFCONSTRUCTION), '') 
    END AS roof_construction,


    CASE
        WHEN EAVES = 'Not Applicable' THEN NULL
        ELSE NULLIF(TRIM(EAVES), '') 
    END AS eaves,


    NULLIF(TRIM(VENTSCREEN), '') AS vent_screen,

    CASE
        WHEN EXTERIORSIDING = 'Stucco/Brick/Cement' THEN 'Stucco Brick Cement'
        ELSE NULLIF(TRIM(EXTERIORSIDING), '') 
    END AS exterior_siding,

    CASE
        WHEN OBJECTID = 112740 THEN NULL
        WHEN OBJECTID = 92833 THEN NULL
        WHEN OBJECTID = 97738 THEN NULL
        ELSE NULLIF(TRIM(WINDOWPANE), '') 
    END AS window_pane,
    
    NULLIF(TRIM(DECKPORCHONGRADE), '') AS deck_porch_on_grade,
    NULLIF(TRIM(DECKPORCHELEVATED), '') AS deck_porch_elevated,
    NULLIF(TRIM(PATIOCOVERCARPORT), '') AS patio_cover_carport,
    NULLIF(TRIM(FENCEATTACHEDTOSTRUCTURE), '') AS fence_attached_to_structure,
    LATITUDE AS latitude,
    LONGITUDE AS longitude

FROM POSTFIRE;