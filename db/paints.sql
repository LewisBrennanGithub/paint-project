DROP TABLE paints;

CREATE TABLE paints (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  value VARCHAR(255),
  offset_value VARCHAR(255),
  popularity int
);

INSERT INTO paints (name, description, value, offset_value, popularity) VALUES ('Red', 'Generic red paint!', '#FF0000', '#0000FF' 1);

INSERT INTO paints (name, description, value, offset_value, popularity) VALUES ('Green', 'Generic green paint!', '#00FF00', '#FF00FF' 2);  