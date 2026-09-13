from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


TEST_DATABASE_URL = (
    "postgresql+psycopg://postgres:x0tr.u21H@localhost/bootcamp_backend_test"
)

test_engine = create_engine(TEST_DATABASE_URL)

TestingSessionLocal = sessionmaker(bind=test_engine)