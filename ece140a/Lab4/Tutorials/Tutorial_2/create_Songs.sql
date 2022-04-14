CREATE TABLE lab4_songs.Songs AS(
SELECT lab4_songs.Songs_data.* , lab4_songs.Songs_artist.artist
from lab4_songs.Songs_data
INNER JOIN lab4_songs.Songs_artist
ON lab4_songs.Songs_data.SongName = lab4_songs.Songs_artist.song);