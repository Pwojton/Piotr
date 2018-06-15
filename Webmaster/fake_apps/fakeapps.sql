DROP TABLE IF EXISTS fakeapps;
CREATE TABLE fakeapps (
    id INTEGER  PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT DEFAULT  '',
    downloads INTEGER,
    price DECIMAL DEFAULT NULL
);
