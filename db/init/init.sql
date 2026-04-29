CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    level INT DEFAULT 1,
    xp INT DEFAULT 0,
    coins INT DEFAULT 0,
    streak INT DEFAULT 0,
    avatar_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, email, password_hash, level, xp, coins, streak, avatar_url)
VALUES
('Nurislam', 'nurislam@example.com', 'demo_hash_1', 5, 420, 150, 7, 'lion'),
('Aza', 'aza@example.com', 'demo_hash_2', 3, 250, 80, 4, 'wolf'),
('Kuanysh', 'kuanysh@example.com', 'demo_hash_3', 2, 120, 40, 2, 'eagle');
