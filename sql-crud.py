from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

db = create_engine("postgresql:///chinook")
base = declarative_base()

class Programmer(base):
    __tablename__ = "Programmer"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

    def __str__(self):
        return f"Programmer: {self.first_name} {self.last_name} | Gender: {self.gender} | Nationality: {self.nationality} | Famous for: {self.famous_for} | ID: {self.id}"



Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)




ada_lovelace = Programmer(
    first_name="Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL Language"
)

margararet_hamilton = Programmer(
    first_name="Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

test_testington = Programmer(
    first_name="Test",
    last_name = "Testington",
    gender = "M",
    nationality = "Testovian",
    famous_for = "Testing",
)

#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margararet_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)
#session.add(test_testington)
session.commit()


programmer = session.query(Programmer).filter_by(id=7).first()
programmer.famous_for = "Testing, and also leading the Testovian revolution"
session.commit()

people = session.query(Programmer)
for person in people:
    if person.gender == "F":
        person.gender = "Female"
    elif person.gender == "M":
        person.gender = "Male"
    else:
        print("Gender not defined")
    session.commit()


programmers = session.query(Programmer)
for programmer in programmers:
    print(programmer)



