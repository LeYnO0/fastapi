from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_USER, DB_PASS, DB_HOST, DB_NAME, DB_PORT

DSN = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@pg_db:{DB_PORT}/{DB_NAME}'

engine = create_engine(DSN)
Session = sessionmaker(bind=engine)
session = Session()
