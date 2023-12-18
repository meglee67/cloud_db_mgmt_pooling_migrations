CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> bcaf44e91947

INSERT INTO alembic_version (version_num) VALUES ('bcaf44e91947');

