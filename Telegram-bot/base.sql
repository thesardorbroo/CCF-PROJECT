CREATE TABLE IF NOT EXISTS eocus (
    id SERIAL PRIMARY KEY,
    user_id BIGINT,
    username VARCHAR(64),
    phone_number VARCHAR(15),
    language VARCHAR(16),
    barber_id INTEGER references barber(id),
    step INTEGER
);


CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY,
    barber_id INTEGER REFERENCES barber(id),
    customer_id INTEGER REFERENCES eocus(id),
    order_time TIME,
    order_day DATE,
    service_id INTEGER references service(id)
);

CREATE TABLE IF NOT EXISTS barber (
    id SERIAL PRIMARY KEY,
    user_id BIGINT,
    photo TEXT,
    fullname VARCHAR(64),
    barbershop_id INTEGER,
    start_time TIME,
    end_time TIME
);

CREATE TABLE IF NOT EXISTS barbershop (
    id SERIAL PRIMARY KEY,
    shop_name VARCHAR(64),
    photo TEXT,
    location VARCHAR(64)

);

CREATE TABLE service (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(32)
);


INSERT INTO barber (user_id, photo ,fullname, barbershop_id, start_time, end_time, key) VALUES (1395478240, '4.jpg','Huseyn Israilov', 1, '07:00','22:00','mirsaid');
SELECT * FROM orders;
DELETE FROM orders WHERE barber_id = 2;
SELECT * FROM barber;

