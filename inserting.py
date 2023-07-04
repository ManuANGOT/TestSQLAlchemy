from sqlalchemy import insert
from tables import users_table
from connect import engine

statement = insert(users_table)
#statement = insert(users_table).values(name="ANGOT",fullname= "Emmanuel ANGOT")

with engine.connect() as connection:
    connection.execute(statement,[
        {'name':"Joe","fullname":"Joe Biden"},
        {'name':"Jean-Michel","fullname":"Jean-Michel Apeuprès"},
        {'name':"Marcel","fullname":"Marcel et son Orchestre"},
    ])
    connection.commit()



print(statement)