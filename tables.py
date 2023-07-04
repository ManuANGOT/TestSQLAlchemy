from sqalchemy import Table,Metadata,Column
from sqlalchemy import Integer


"""
users table:
    - id pk
    - name str
    - fullname str
    - email


comment table :
    - id pk
    - comment str
    - user_id int > users.id
"""

metra_obj = Metadata()


users_table = Table(
    "users",
    meta_obj,
    Column("id",)

)

comments_table = Table(

)