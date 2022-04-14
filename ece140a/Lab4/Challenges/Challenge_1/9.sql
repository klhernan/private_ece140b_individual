SELECT artist, AVG(speechiness) 
FROM lab4_songs.Songs
GROUP BY artist HAVING COUNT(SongName) > 3;