SELECT COUNT(*) FROM lab4_songs.Songs
WHERE tempo > (
    SELECT AVG(tempo)
    FROM lab4_songs.Songs
);
