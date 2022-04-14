CREATE TABLE lab4_songs.Songs_data (
    id              INT NOT NULL AUTO_INCREMENT,
    SongName        VARCHAR(100) NOT NULL,
    danceability    DECIMAL(10,3) NULL,
    energy          DECIMAL(10,3) NULL,
    loudness        DECIMAL(10,3) NULL,
    speechiness     DECIMAL(10,5) NULL,
    acousticness    DECIMAL(10,7) NULL,
    liveness        DECIMAL(10,5) NULL,
    valence         DECIMAL(10,5) NULL,
    tempo           DECIMAL(10,3) NULL,
    duration_ms     INTEGER NULL,
    time_signature  INTEGER NULL,
    PRIMARY key (id));