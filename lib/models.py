from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)


Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', backref('company'))

    def __repr__(self):
        return f'<Company {self.name}>'
    
    
    @property
    def devs(self):
        return list({freebie.dev for freebie in self.freebies})
    
    def give_freebie(self, item_name, value, dev):
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev)
        return new_freebie
    
    @classmethod
    def oldest_company(cls, session):
        return session.query(cls).order_by(cls.founding_year).first()
    

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    freebies = relationship('Freebie', backref('dev'))

    def __repr__(self):
        return f'<Dev {self.name}>'

    @property
    def companies_list(self):
        return list({freebie.dev for freebie in self.freebies})
    
    def item_received(self, item_name):
        return any(freebie.item_name == item_name for freebie in self.freebies)
    
    def item_given(self, other_dev, freebie):
        if freebie in self.freebies:
            freebie.dev = other_dev
    

class Freebie(Base):
    __tablename__= 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)
    dev_id= Column(ForeignKey('devs.id'))
    company_id=Column(ForeignKey('companies.id'))
    dev=relationship('Dev', back_populates='freebies')
    company=relationship('Company', back_populates='freebies')

    def print_details(self):
        return f'{self.dev.name} has a {self.item_name} that he got from {self.company.name}'


