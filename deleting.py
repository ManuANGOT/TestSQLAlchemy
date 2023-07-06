from tables import users_table
from connect import engine
from sqlalchemy import delete

statement = delete(users_table).where(
    users_table.c.name == "Jarry"
)

with engine.connect() as connection:
    connection.execute(statement)
    connection.commit()