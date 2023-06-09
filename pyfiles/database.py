"""
This module contains methods for making and querying from a database.
The database is a table of strings that are file paths to media that the bot will tweet
"""

#!/usr/bin/env python
import os
import sqlite3


def makeDatabase():
    """
    Make the database file if it doesn't exist
    """
    if os.path.isfile("./pyfiles/image.db"):
        print("Database already exists")
        return
    with open("./pyfiles/image.db", "w", encoding="utf-8") as database:
        database.close()
    return

def makeImageTable():
    connect = sqlite3.connect("./pyfiles/image.db")
    connect.execute("""
                    CREATE TABLE IF NOT EXISTS images
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    image_path TEXT NOT NULL UNIQUE);
                    """)
    connect.commit()
    connect.close()

def populateTable():
    """
    Run this to make the database and populate it with image paths. Please run this
    before trying to tweet!
    """
    makeDatabase()
    makeImageTable()
    paths = os.listdir("./media")
    connect = sqlite3.connect("./pyfiles/image.db")
    for image in paths:
        connect.execute("""
                        INSERT INTO images(id, image_path)
                        VALUES (?,?);
                        """, (None, image))
        connect.commit()
    connect.close()
    return

def randomImage():
    connect = sqlite3.connect("./pyfiles/image.db")
    image = connect.execute("""
        SELECT image_path FROM images
        ORDER BY RANDOM()
        LIMIT 1;
    """).fetchall()
    connect.commit()
    connect.close()
    return image[0][0]

def randomKeyWordImage(word):
    connect = sqlite3.connect("./pyfiles/image.db")
    word = "%"+word+"%"
    image = connect.execute("""
        SELECT image_path FROM images
        WHERE image_path LIKE ?
        ORDER BY RANDOM()
        LIMIT 1;
    """,(word,)).fetchall()
    connect.commit()
    connect.close()
    return image[0][0]
