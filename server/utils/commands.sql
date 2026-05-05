CREATE TABLE apps (
    app_id VARCHAR(255) NOT NULL PRIMARY KEY UNIQUE COMMENT 'Primary Key',
    app_metadata JSON,
    app_rows INT
)

SELECT * FROM apps;
DROP TABLE apps;
DELETE FROM apps WHERE app_id = "";