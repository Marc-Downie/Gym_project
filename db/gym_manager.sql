DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS gyms;



CREATE TABLE gyms(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    activity VARCHAR(255)
);

CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    membership VARCHAR(255),
    gym_id INT REFERENCES gyms(id)
);

CREATE TABLE activities(
    id SERIAL PRIMARY KEY,
    gym_id INT REFERENCES gyms(id),
    activity VARCHAR(255),
    duration VARCHAR(255),
    difficulty VARCHAR(255)
);


