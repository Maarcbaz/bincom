import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()


def get_connection():

    required_variables = [
        "DB_HOST",
        "DB_PORT",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD"
    ]

    for variable in required_variables:
        if not os.getenv(variable):
            raise ValueError(f"{variable} is missing from the .env file")

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )