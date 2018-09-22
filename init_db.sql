PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
user_id integer PRIMARY KEY,
name text NOT NULL,
password text NOT NULL,
age integer
);
INSERT INTO users VALUES(1,'alexis','81dc9bdb52d04dc20036dbd8313ed055',21);
COMMIT;
