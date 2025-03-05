import uuid
import sqlite3
import threading
from typing import List
from app.models import Movie
from .log import print_log

class Database:
    _instance = None
    _lock = threading.Lock()

    _SQL_CREATE_TABLE_MOVIELIST = """
CREATE TABLE movielist (uuid VARCHAR(36) PRIMARY KEY,
year INTEGER,
title VARCHAR(65),
studios VARCHAR(60),
producers VARCHAR(115),
winner INTEGER
)
"""

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls._instance._init_db()
        return cls._instance


    def _init_db(self):
            self.conn = sqlite3.connect(':memory:', check_same_thread=False)
            self.cursor = self.conn.cursor()
            self._create_table()


    def _create_table(self) -> None:
        self.cursor.execute(self._SQL_CREATE_TABLE_MOVIELIST)
        self.conn.commit()


    def bulk_insert(self, movies: List[Movie]) -> int:
        data = []
        for m in movies:
            data.append((str(uuid.uuid4()), str(m.year), m.title, m.studios, m.producer, str(int(m.winner))))

        self.cursor.executemany("INSERT INTO movielist (uuid, year, title, studios, producers, winner) "
                           "VALUES (?, ?, ?, ?, ?, ?)", data)

        self.conn.commit()
        print_log(str(self.cursor.rowcount) + ' items persisted from movielist')
        return self.cursor.rowcount


    def close(self) -> None:
        self.cursor.close()
        self.conn.close()


    def retrieve_all_winners(self) -> List[Movie]:
        self.cursor.execute('SELECT * FROM movielist where winner = 1')
        rows = self.cursor.fetchall()
        movies = []

        for row in rows:
            movies.append(Movie(*row))

        print_log(str(len(rows)) + ' items fetched from database with criteria winner = 1')

        return movies

