from model.contact import Contact
import jsonpickle
import random
import string
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = ([Contact(name="", lastname="",
                     address="", email="", email2="", email3="",
                     homephone="", mobilephone="", workphone="", secondaryphone="")] +
            [
                Contact(name=random_string("name", 10), lastname=random_string("lastname", 10),
                        address=random_string("address", 10), email=random_string("email", 10),
                        email2=random_string("email2", 10), email3=random_string("email3", 10),
                        homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10),
                        workphone=random_string("workphone", 10), secondaryphone=random_string("secondaryphone", 10))
                for i in range(n)
            ])


testdata2 = [
    Contact(name=name, lastname=lastname, address=address, email=email, mobilephone=mobilephone, workphone=workphone)
    for name in ["", random_string("name", 10)]
    for lastname in ["", random_string("lastname", 10)]
    for address in ["", random_string("address", 10)]
    for email in ["", random_string("email", 10)]
    for mobilephone in ["", random_string("mobilephone", 10)]
    for workphone in ["", random_string("workphone", 10)]
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
