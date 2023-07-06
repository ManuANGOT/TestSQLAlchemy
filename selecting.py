from tables import users_table
from connect import engine
from sqlalchemy import select

statement = select(users_table).where(users_table.c.name == "Joe")

#print(statement)

with engine.connect() as connection:
    result = connection.execute(statement)

    for row in result:
        #print(row)
       print(f"<Username= {row.name} ; fullname= {row.fullname}>")

# print(users_table.c.name) #renvoie juste "users.name"
# print(users_table.c.fullname)
# print(users_table.c.ide)