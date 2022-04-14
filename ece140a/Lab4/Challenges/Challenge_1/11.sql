SELECT artist
FROM lab4_songs.Songs 
GROUP BY artist
ORDER BY SUM(duration_ms) ASC ;
