import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from com.jinmini.utils.creational.builder.query_builder import QueryBuilder
from com.jinmini.utils.creational.singleton import db_singleton

# SQLAlchemy를 이용한 데이터베이스 엔진 및 세션 빌더
class DatabaseBuilder:
    def __init__(self):
        if not hasattr(db_singleton, "db_url"):
            raise AttributeError("⚠️ db_singleton 인스턴스에 'db_url' 속성이 존재하지 않습니다.")
        
        print(f"✅ Initializing DatabaseBuilder... db_url: {db_singleton.db_url}")  

        self.database_url = db_singleton.db_url
        self._engine = None
        self._session_factory = None

    def build(self):
        if not self.database_url:
            raise ValueError("⚠️ Database URL must be set before building the database")

        # 비동기 드라이버를 사용하도록 URL 수정
        # postgresql:// -> postgresql+asyncpg://
        if self.database_url.startswith('postgresql://'):
            self.database_url = self.database_url.replace('postgresql://', 'postgresql+asyncpg://')
            print(f"🔄 Database URL 변환: {self.database_url}")

        print(f"🚀 Connecting to PostgreSQL: {self.database_url}")  

        # 비동기 엔진 생성
        self._engine = create_async_engine(
            self.database_url,
            echo=True,  # SQL 로깅
            future=True,  # 2.0 스타일 API 사용
            pool_size=10,  # 커넥션 풀 크기
            max_overflow=20,  # 최대 추가 커넥션
            pool_timeout=60,  # 커넥션 타임아웃(초)
        )
        
        # 비동기 세션 팩토리 생성
        self._session_factory = sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False,  # 커밋 후 객체 만료 방지
        )
        
        return self

    def get_session(self):
        """비동기 세션 반환"""
        return self._session_factory()


# 의존성 주입을 위한 데이터베이스 세션 생성기
async def get_db():
    # .env 파일 강제 로드
    load_dotenv()

    if not hasattr(db_singleton, "db_url") or not db_singleton.db_url:
        print("⚠️ db_singleton이 올바르게 초기화되지 않았습니다. 환경 변수를 다시 로드합니다.")
        db_singleton.db_url = os.getenv("DATABASE_URL")
        
        if not db_singleton.db_url:
            raise AttributeError("❌ 환경 변수를 다시 로드했지만 'db_url'이 설정되지 않았습니다. .env 파일을 확인하세요.")

    print(f"✅ db_singleton 초기화 확인: {db_singleton.db_url}")  

    # 빌더 생성 및 세션 얻기
    builder = DatabaseBuilder().build()
    async_session = builder.get_session()
    
    try:
        async with async_session as session:
            yield session
    finally:
        await session.close()


async def init_db():
    """데이터베이스 초기화"""
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e

if __name__ == "__main__":
    # 🔹 SQLAlchemy DB 설정 빌드
    db_builder = (
        DatabaseBuilder()
        .echo(True)
        .future(True)
        .build()
    )

    engine = db_builder._engine
    session_local = db_builder._session_local
    Base = db_builder._base

    # 🔹 pymysql 쿼리 실행 예시
    query_result = (
        QueryBuilder()
        .connect()
        .query("SELECT * FROM users")
        .execute()
    )
    
    print(f"Query Result: {query_result}")
