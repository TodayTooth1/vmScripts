SELECT
    p.OBJECTID,
    p.WINDOWPANE AS original_window_pane,
    c.window_pane AS cleaned_window_pane
FROM POSTFIRE p
JOIN rawdataCA_cleaned c
    ON p.OBJECTID = c.object_id
WHERE p.OBJECTID IN (132518, 132298, 131178, 131284, 130765, 131414, 130907, 94577, 190625, 112740, 92833, 97738);