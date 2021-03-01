"""
    use sql alchemy based data access layer for cockroachdb

    add, remove, update, insert <context, interest, comments/answer/correction> row
    add, update <status>
    add tabels/database
    get counts, aggregates, ...
"""
# import os

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = os.getenv("DB_CONN")

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
