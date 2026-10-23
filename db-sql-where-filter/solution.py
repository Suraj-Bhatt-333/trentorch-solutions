-- Tables available (already created and filled for you):
--
--   CREATE TABLE users (
--       id INTEGER PRIMARY KEY,
--       name TEXT NOT NULL,
--       email TEXT NOT NULL,
--       age INTEGER
--   )
--
-- Run (Ctrl/Cmd+Enter) executes your query; Submit checks it against the tests.

-- TODO: Return all columns for users aged 18 or older.
SELECT * FROM users
WHERE age>=18;
