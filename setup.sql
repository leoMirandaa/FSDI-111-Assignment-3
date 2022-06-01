-- Create a database table calle "user":
-- primary key = not null (implicit)
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  hobbies TEXT,
  active BOOLEAN NOT NULL DEFAULT 1
);

-- Dummy data to play with:
INSERT INTO user (
  first_name,
  last_name,
  hobbies
) VALUES (
  "Leopoldo",
  "MIranda",
  "Play the guitar"
);

INSERT INTO user (
  first_name,
  last_name,
  hobbies
) VALUES (
  "Josh",
  "Gilbert",
  "Go to movies"
);

INSERT INTO user (
  first_name,
  last_name,
  hobbies
) VALUES (
  "Michale",
  "Jordan",
  "Play basketball"
);

CREATE TABLE vehicle (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model VARCHAR(45) NOT NULL,
  color VARCHAR(45) NOT NULL,
  year INTEGER NOT NULL,
  mileage INTEGER NOT NULL,
  active BOOLEAN NOT NULL DEFAULT 1,
  user_id INTEGER NOT NULL,
  FOREIGN KEY(user_id) REFERENCES user(id)
);

INSERT INTO vehicle (
  model,
  color,
  year,
  mileage,
  user_id
) VALUES (
  "Toyota",
  "Red",
  2000,
  12000,
  12
);

INSERT INTO vehicle (
  model,
  color,
  year,
  mileage,
  user_id
) VALUES (
  "Ford",
  "Green",
  2008,
  30000,
  18
);

INSERT INTO vehicle (
  model,
  color,
  year,
  mileage,
  user_id
) VALUES (
  "Nissan",
  "Blue",
  2018,
  10000,
  17
);