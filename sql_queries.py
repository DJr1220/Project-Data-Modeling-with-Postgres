# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id  VARCHAR PRIMARY KEY,
        start_time TIMESTAMP,
        user_id VARCHAR,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id VARCHAR,
        location VARCHAR,
        user_agent VARCHAR
    );
""")
user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id VARCHAR PRIMARY KEY, 
        first_name VARCHAR, 
        last_name VARCHAR, 
        gender VARCHAR,
        level VARCHAR
    );
""")
song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR,
        artist_id VARCHAR,
        year VARCHAR,
        duration VARCHAR
    );
""")
artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY,
        name VARCHAR,
        location VARCHAR,
        latitude VARCHAR,
        longitude VARCHAR
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday VARCHAR
    );
""")

# INSERT RECORDS
songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """)

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
    """)

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s,%s,%s,%s,%s)
    """)

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s,%s,%s,%s,%s)
    """)

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """)

# FIND SONGS
song_select = ("""
    SELECT songs.song_id, songs.artist_id
    FROM songs
    JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s and artists.name = %s and songs.duration = %s;
    """)

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
