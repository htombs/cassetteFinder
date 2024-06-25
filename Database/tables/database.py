import sqlite3
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
db = THIS_FOLDER / "cassette_finder.db"

def connect_database():
    return sqlite3.connect(db)