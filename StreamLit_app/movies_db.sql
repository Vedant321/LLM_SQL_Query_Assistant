
CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    release_year INT,
    duration_minutes INT,
    rating FLOAT,
    revenue_million FLOAT
);

INSERT INTO movies (title, release_year, duration_minutes, rating, revenue_million) VALUES
('Inception', 2010, 148, 8.8, 829),
('Interstellar', 2014, 169, 8.6, 677),
('The Dark Knight', 2008, 152, 9.0, 1005),
('The Matrix', 1999, 136, 8.7, 466),
('Parasite', 2019, 132, 8.6, 258),
('Avengers: Endgame', 2019, 181, 8.4, 2797),
('Joker', 2019, 122, 8.5, 1074),
('The Shawshank Redemption', 1994, 142, 9.3, 58),
('Her', 2013, 126, 8.0, 47),
('The Imitation Game', 2014, 114, 8.0, 233);


CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name TEXT UNIQUE
);

INSERT INTO genres (genre_name) VALUES
('Action'),
('Drama'),
('Sci-Fi'),
('Thriller'),
('Crime'),
('Adventure'),
('Comedy'),
('Romance');


CREATE TABLE movie_genres (
    movie_id INT REFERENCES movies(movie_id),
    genre_id INT REFERENCES genres(genre_id),
    PRIMARY KEY (movie_id, genre_id)
);

INSERT INTO movie_genres VALUES
(1, 3), (1, 1),           
(2, 3), (2, 2), (2, 6),   
(3, 1), (3, 5), (3, 4),   
(4, 3), (4, 1),           
(5, 2), (5, 5),           
(6, 1), (6, 6),           
(7, 2), (7, 4),           
(8, 2),                   
(9, 3), (9, 8),           
(10, 2), (10, 4);         


CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    actor_name TEXT
);

INSERT INTO actors (actor_name) VALUES
('Leonardo DiCaprio'),
('Matthew McConaughey'),
('Christian Bale'),
('Heath Ledger'),
('Keanu Reeves'),
('Song Kang-ho'),
('Robert Downey Jr.'),
('Joaquin Phoenix'),
('Morgan Freeman'),
('Scarlett Johansson');


CREATE TABLE movie_cast (
    movie_id INT REFERENCES movies(movie_id),
    actor_id INT REFERENCES actors(actor_id),
    PRIMARY KEY (movie_id, actor_id)
);

INSERT INTO movie_cast VALUES
(1,1),(2,2),(3,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10),(10,1);


CREATE TABLE directors (
    director_id SERIAL PRIMARY KEY,
    director_name TEXT
);

INSERT INTO directors (director_name) VALUES
('Christopher Nolan'),
('Bong Joon-ho'),
('Todd Phillips'),
('The Wachowskis'),
('Denis Villeneuve'),
('Damien Chazelle'),
('Morten Tyldum'),
('Anthony Russo'),
('Joe Russo');


CREATE TABLE movie_directors (
    movie_id INT REFERENCES movies(movie_id),
    director_id INT REFERENCES directors(director_id),
    PRIMARY KEY (movie_id, director_id)
);

INSERT INTO movie_directors VALUES
(1,1),(2,5),(3,1),(4,4),(5,2),(6,8),(6,9),(7,3),(8,1),(9,6),(10,7);


CREATE TABLE ratings (
    rating_id SERIAL PRIMARY KEY,
    movie_id INT REFERENCES movies(movie_id),
    user_id INT,
    rating FLOAT,
    rating_date DATE
);

INSERT INTO ratings (movie_id, user_id, rating, rating_date) VALUES
(1,101,9.0,'2024-01-10'),
(1,102,8.5,'2024-01-12'),
(2,103,9.0,'2024-02-01'),
(3,104,9.5,'2024-02-20'),
(4,105,8.7,'2024-03-15'),
(5,106,8.6,'2024-04-10'),
(6,107,8.4,'2024-05-05'),
(7,108,8.5,'2024-06-01'),
(8,109,9.3,'2024-06-10'),
(9,110,8.0,'2024-07-01'),
(10,111,8.0,'2024-07-05');
