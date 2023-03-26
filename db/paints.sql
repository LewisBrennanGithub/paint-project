DROP TABLE paints;

CREATE TABLE paints (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  value VARCHAR(255),
  offset_value VARCHAR(255),
  offset_override BOOLEAN,
  popularity int
);

INSERT INTO paints (name, description, value, offset_value, offset_override, popularity) VALUES ('Red', 'Generic red paint!', '#FF0000', '#0000FF', FALSE, 1);

INSERT INTO paints (name, description, value, offset_value, offset_override, popularity) VALUES ('Green', 'Generic green paint!', '#00FF00', '#FF00FF', FALSE, 2);  

INSERT INTO paints (name, description, value, offset_value, offset_override, popularity) VALUES ('Yellow', 'Generic yellow paint!', '#F4D136', '#0b2ec9', FALSE, 3);  

INSERT INTO paints (name, description, value, offset_value, offset_override, popularity) VALUES ('Purple', 'Generic purple paint!', '#6A1B9A', '#95e465', FALSE, 3);

INSERT INTO paints (name, description, value, offset_value, offset_override, popularity) VALUES ('Blue', 'Generic blue paint!', '#0000FF', '#FF0000', FALSE, 3);  
