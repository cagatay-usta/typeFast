CREATE TABLE leaderboard (
    id INTEGER PRIMARY KEY,
    wpm REAL,
    record_time TEXT
);

INSERT INTO leaderboard(wpm, record_time) VALUES(118, (SELECT datetime('now'));