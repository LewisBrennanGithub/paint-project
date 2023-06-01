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

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override) VALUES ('Amber', 'A posh yellow.', '#f1a809', '#d60000', 7, FALSE);

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override) VALUES ('Red', 'Generic red paint!', '#ff0000', '#000000', 6, FALSE);  

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override) VALUES ('Turqoise', 'Weirdly apppealing.', '#077e70', '#ff8800', 5, FALSE);  

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override) VALUES ('Plum', 'Who made the offset for this, really?', '#5a0c49', '#a5f3b6', 5, FALSE);

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Not Pink', 'Or is it?', '#bc6c6c', '#439393', 4, FALSE);

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Olive Drab', 'You will not believe how this looked before.', '#52812c', '#df6298', 4, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Maroon', 'Possibly white.', '#952828', '#6ad7d7', 2, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Mauve', 'I don''t know what mauve looks like.', '#800f40', '#7ff0bf', 2, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Door Brown', 'Saw this paint on a door once.', '#5d3e09', '#73d1e8', 1, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Mist', 'Never been to Scunthorpe.', '#85c6d6', '#ae0a43', 1, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Yellowish', 'I think its yellow.', '#428641', '#bd79be', 0, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Toby Pink', 'Fabulous.', '#df8ae5', '#4da2c7', 0, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Scary Forest', 'Something clever.', '#135700', '#eb7d00', 0, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Yellow', 'Tropical fruits and musical suits.', '#ffdd00', '#3bdbde', 0, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Grey', 'Are you o-grey?', '#ada9a9', '#1e7b50', 0, FALSE); 

INSERT INTO paints (name, description, value, offset_value, popularity, offset_override,) VALUES ('Pistachio', 'A soft green!', '#bddd64', '#ac2a2a', -2, FALSE); 

