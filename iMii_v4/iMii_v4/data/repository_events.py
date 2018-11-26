import csv
import os
import uuid
from dateutil.parser import parse

from iMii_v4.data.db_factory import DbSessionFactory
from iMii_v4.data.Event import Event


class Repository_events:
    __events_data = {}

    @classmethod
    def all_events(cls, limit=None):
        # cls.__load_data()
        #
        # events = list(cls.__events_data.values())
        # if limit:
        #     events = events[:limit]
        #
        # return events
        session = DbSessionFactory.create_session()

        query = session.query(Event).order_by(Event.event_date)

        if limit:
            events = query[:limit]
        else:
            events = query.all()

        session.close()

        return events

    @classmethod
    def event_by_id(cls, events_id):
        # cls.__load_data()
        # return cls.__events_data.get(events_id)
        session = DbSessionFactory.create_session()

        event = session.query(Event).filter(Event.id == events_id).first()

        session.close()

        return event

    @classmethod
    def __load_data(cls):
        if cls.__events_data:
            return

        file = os.path.join(
            os.path.dirname(__file__),
            'events.csv'
        )

        with open(file, 'r', encoding='utf-8') as fin:
            # brand,name,price,year,damage,last_seen
            reader = csv.DictReader(fin)
            for row in reader:
                key = str(uuid.uuid4())
                row['id'] = key
                cls.__events_data[key] = row

    @classmethod
    def add_event(cls, event):
        # cls.__load_data()
        # key = str(uuid.uuid4())
        # event_data['id'] = key
        # cls.__events_data[key] = event_data
        #
        # return event_data

        try:
            session = DbSessionFactory.create_session()

            db_event = Event()
            # db_people.last_seen = parse( person.last_seen )  # parse(teacher.certdate)
            db_event.headline = event.headline
            db_event.description = event.description
            db_event.event_date = parse(event.event_date)
            # db_car.image = person.image if car.image else random.choice(cls.__fake_image_url)
            db_event.url = event.url
            # db_car.teacherId = int(teacher.year)
            # db_people.price = int( person.price )
            # db_event.date_created = parse(event.date_created)
            db_event.id = event.id

            session.add( db_event )
            session.commit()

            return db_event

        except Exception as e:
            print( e )  # for the repr
        # ...     print 'My exception occurred, value:', e.value


    @classmethod
    def update_event(cls, event_data):
        # key = event_data['id']
        # cls.__events_data[key] = event_data
        #
        # return event_data

        session = DbSessionFactory.create_session()

        db_event = session.query(Event).filter(Event.id == event_data.id).first()

        # db_car.last_seen = parse(car_data.last_seen)
        db_event.headline = event_data.headline
        db_event.description = event_data.description
        db_event.url = event_data.url
        db_event.event_date = parse( event_data.event_date )

        session.commit()

        return db_event

    @classmethod
    def delete_event(cls, event_id):
        # del cls.__events_data[event_id]
        session = DbSessionFactory.create_session()
        db_event = session.query(Event).filter(Event.id == event_id).first()
        if not db_event:
            return

        session.delete(db_event)
        session.commit()
