
import uuid

import sqlalchemy
import datetime

from iMii_v4.data.sqlalchemy_base import SqlAlchemyBase


class Event(SqlAlchemyBase):

    __tablename__ = 'Events'

    # Name,Date,Description,URL
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True,
                           default=lambda: str(uuid.uuid4()))
    headline = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    event_date = sqlalchemy.Column( sqlalchemy.DATE, index=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # title = sqlalchemy.Column(sqlalchemy.String)
    # position = sqlalchemy.Column(sqlalchemy.String)
    # email = sqlalchemy.Column(sqlalchemy.String)
    url = sqlalchemy.Column(sqlalchemy.String)
    # url2 = sqlalchemy.Column(sqlalchemy.String)
    # address = sqlalchemy.Column(sqlalchemy.String)
    # city = sqlalchemy.Column(sqlalchemy.String)
    # state = sqlalchemy.Column(sqlalchemy.String)
    img1 = sqlalchemy.Column( sqlalchemy.String )
    date_created = sqlalchemy.Column(sqlalchemy.DateTime, index=True,
                                   default=datetime.datetime.now)

    def to_dict(self):
        return {
            'headline': self.headline,
            'event_date': self.event_date.isoformat(),
            'description': self.description,
            'url': self.url,
            'img1': self.img1,
            # 'date_created': self.date_created.isoformat(),
            'id': self.id,
        }