from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cockroachdb.sqlalchemy import run_transaction
from random import random

# The code below assumes you are running as 'root' and have run
# the following SQL statements against an insecure cluster.

# CREATE DATABASE pointstore;

# USE pointstore;

# CREATE TABLE points (
#     id INT PRIMARY KEY DEFAULT unique_rowid(),
#     x FLOAT NOT NULL,
#     y FLOAT NOT NULL,
#     z FLOAT NOT NULL
# );

# Create the SQLAlchemy engine
engine = create_engine(
    'cockroachdb://root@cockroachdb:26257/derive',
    connect_args={
        'sslmode': 'disable',
    },
    echo=True
)

# initalize instance of database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# will inherit from class Base in all ORM models
Base = declarative_base()
