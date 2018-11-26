import csv
import os
import uuid

from iMii_v4.data.db_factory import DbSessionFactory
from iMii_v4.data.People import Person

class Repository_people:
    __people_data = {}

    @classmethod
    def all_people(cls, limit=None):
        # cls.__load_data()
        #
        # people = list(cls.__people_data.values())
        # if limit:
        #     people = people[:limit]
        #
        # return people

        session = DbSessionFactory.create_session()

        query = session.query(Person)  # .order_by(Teacher.lName)

        if limit:
            people = query[:limit]
        else:
            people = query.all()

        session.close()

        return people

    @classmethod
    def person_by_id(cls, person_id):
        # cls.__load_data()
        # return cls.__people_data.get(person_id)

        session = DbSessionFactory.create_session()

        person = session.query(Person).filter(Person.id == person_id).first()

        session.close()

        return person


    @classmethod
    def people_interviewed(cls, interviewed, limit=None):

        #         session = DbSessionFactory.create_session()
        #
        #         person = session.query(Person).filter(Person.interviewed == 'yes')       #Person.id == person_id).first()
        #
        #         session.close()
        #
        #         return person
        # ------------
        session = DbSessionFactory.create_session()

        # query = session.query( Person )  # .order_by(Teacher.lName)
        query = session.query(Person).filter(Person.interviewed == 'yes')

        if limit:
            people = query[:limit]
        else:
            people = query.all()

        session.close()

        return people


    @classmethod
    def __load_data(cls):
        if cls.__people_data:
            return

        file = os.path.join(
            os.path.dirname(__file__),
            'people.csv'
        )

        with open(file, 'r', encoding='utf-8') as fin:
            # brand,name,price,year,damage,last_seen
            reader = csv.DictReader(fin)
            for row in reader:
                key = str(uuid.uuid4())
                row['id'] = key
                cls.__people_data[key] = row

    @classmethod
    def add_person(cls, person):
        # cls.__load_data()
        # key = str(uuid.uuid4())
        # person_data['id'] = key
        # cls.__people_data[key] = person_data
        #
        # return person_data

        try:
            session = DbSessionFactory.create_session()

            db_people = Person()
            # db_people.last_seen = parse( person.last_seen )  # parse(teacher.certdate)
            db_people.headline = person.headline
            db_people.fname = person.fname
            db_people.lname = person.lname
            db_people.title = person.title
            db_people.company = person.company
            db_people.email = person.email
            db_people.url1 = person.url1
            db_people.url2 = person.url2
            db_people.description = person.description
            db_people.address = person.address
            db_people.city = person.city
            db_people.state = person.state
            db_people.interviewed = person.interviewed
            # db_people.img1 = person.img1
            # db_car.image = person.image if car.image else random.choice(cls.__fake_image_url)
            # db_people.year = person.year
            # db_car.teacherId = int(teacher.year)
            # db_people.price = int( person.price )
            db_people.id = person.id

            session.add( db_people )
            session.commit()

            return db_people

        except Exception as e:
            print( e )  # for the repr
        # ...     print 'My exception occurred, value:', e.value

    @classmethod
    def update_person(cls, person):
        # key = person_data['id']
        # cls.__people_data[key] = person_data
        #
        # return person_data
        # id,name,title,company,email,url1,url2,description, address, city,state,img1

        session = DbSessionFactory.create_session()

        db_person = session.query(Person).filter(Person.id == person.id).first()
        # db_car.last_seen = parse(car_data.last_seen)
        db_person.headline = person.headline
        db_person.fname = person.fname
        db_person.lname = person.lname
        db_person.title = person.title
        db_person.company = person.company
        db_person.email = person.email
        db_person.url1 = person.url1
        db_person.url2 = person.url2
        db_person.description = person.description
        db_person.address = person.address
        db_person.city = person.city
        db_person.state = person.state
        # db_person.img1 = person.img1
        # db_car.image = car_data.image if car_data.image else random.choice(cls.__fake_image_url)
        # db_car.brand = car_data.brand
        # db_car.damage = car_data.damage
        # db_car.id = car_data.id
        # db_car.price = car_data.price
        # db_car.year = car_data.year

        session.commit()

        return db_person

    @classmethod
    def delete_person(cls, person_id):
        # del cls.__people_data[person_id]
        session = DbSessionFactory.create_session()
        db_person = session.query(Person).filter(Person.id == person_id).first()
        if not db_person:
            return

        session.delete(db_person)
        session.commit()
