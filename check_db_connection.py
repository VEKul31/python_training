import pymysql.cursors
# from fixture.db import DbFixture
from fixture.orm import ORMFixture

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()

# try:
#    groups = db.get_group_list()
#    for group in groups:
#        print(group)
#    print(len(groups))
# finally:
#    db.destroy()

# try:
#    cursor = connection.cursor()
#    cursor.execute("select * from group_list")
#    for row in cursor.fetchall():
#        print(row)
# finally:
#    connection.close()
