import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ 1. DatabaseBuilder: SQLAlchemy 엔진 및 세션 빌더
class DatabaseBuilder:
    def __init__(self):
        self._database_url = os.getenv("DATABASE_URL", "postgresql://myuser:mypass@database:5432/mydb")
        self._echo = False
        self._future = True
        self._autocommit = False
        self._autoflush = False
        self._engine = None
        self._session_local = None
        self._base = None

    def set_database_url(self, url: str):
        self._database_url = url
        return self

    def set_echo(self, echo: bool):
        self._echo = echo
        return self

    def set_future(self, future: bool):
        self._future = future
        return self

    def set_autocommit(self, autocommit: bool):
        self._autocommit = autocommit
        return self

    def set_autoflush(self, autoflush: bool):
        self._autoflush = autoflush
        return self

    def build(self):
        if not self._database_url:
            raise ValueError("Database URL must be set before building the database engine.")
        
        self._engine = create_engine(
            self._database_url, echo=self._echo, future=self._future
        )
        self._session_local = sessionmaker(
            autocommit=self._autocommit,
            autoflush=self._autoflush,
            bind=self._engine
        )
        self._base = declarative_base()
        return self

    def get_engine(self):
        return self._engine
    
    def get_session_local(self):
        return self._session_local
    
    def get_base(self):
        return self._base

    def get_db(self):
        db = self._session_local()
        try:
            yield db
        finally:
            db.close()


