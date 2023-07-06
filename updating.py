from tables import users_table
from connect import engine
from sqlalchemy import update

statement = update(users_table).where(
    users_table.c.name == "Joe"
).values(name="Jarry")


with engine.connect() as connection :
    connection.execute(statement)
    connection.commit()


# print(statement)