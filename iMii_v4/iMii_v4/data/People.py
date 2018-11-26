import uuid

import sqlalchemy
import datetime

from iMii_v4.data.sqlalchemy_base import SqlAlchemyBase


class Person(SqlAlchemyBase):

    __tablename__ = 'People'

    # columns: fname, lname, title, position, company, email, url1, url2, address, city, state, date_edited

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
                           default=lambda: str(uuid.uuid4()))
    headline = sqlalchemy.Column( sqlalchemy.String )
    fname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    lname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String)
    position = sqlalchemy.Column(sqlalchemy.String)
    company = sqlalchemy.Column( sqlalchemy.String )
    description = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    url1 = sqlalchemy.Column(sqlalchemy.String)
    url2 = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    state = sqlalchemy.Column(sqlalchemy.String)
    img1 = sqlalchemy.Column( sqlalchemy.String )
    doc1 = sqlalchemy.Column( sqlalchemy.String )
    interview = sqlalchemy.Column( sqlalchemy.String )
    interviewed = sqlalchemy.Column( sqlalchemy.String )
    date_created = sqlalchemy.Column(sqlalchemy.DateTime, index=True,
                                  default=datetime.datetime.now)

    def to_dict(self):
        return {
            'headline': self.headline,
            'fname': self.fname,
            'lname': self.lname,
            'title': self.title,
            'position': self.position,
            'company': self.company,
            'description': self.description,
            'email': self.email,
            'url1': self.url1,
            'url2': self.url2,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'img1': self.img1,
            'doc1': self.doc1,
            'interviewed': self.interviewed,
            'interview': self.interviewed,
            'date_created': self.date_created.isoformat(),
            'id': self.id,
        }