#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

#create the engine to initiate the db link
engine = create_engine("sqlite:///freebies.db")
# bind the engine through the session
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

#Company instances
company1 = Company(name='Sollatek', founding_year=1993)
company2 = Company(name='Safaricom', founding_year=1998)
company3 = Company(name='Multichoice', founding_year=1995)

#developer instances
developer1 = Dev(name='Ian')
developer2 = Dev(name='Stiffler')
developer3 = Dev(name='Konyez')

#add all these to the session
session.add_all([company1, company2, company3, developer1, developer2, developer3])
session.commit()

#freebie instances
freebie1 = Freebie(item_name="Badge", value=1000, dev=developer1, company=company1)
freebie2 = Freebie(item_name="Hat", value=100, dev=developer2, company=company2)
freebie3 = Freebie(item_name="Mug", value=75, dev=developer1, company=company2)
freebie4 = Freebie(item_name="T-Shirt", value=500, dev=developer3, company=company3)
freebie5 = Freebie(item_name="Jumper", value=4500, dev=developer2, company=company1)

session.add_all([freebie1, freebie2, freebie3, freebie4, freebie5])
session.commit()
