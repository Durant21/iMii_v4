import sys
import csv
import os
import uuid
import random

# noinspection PyPackageRequirements
from dateutil.parser import parse

from passlib.handlers.sha2_crypt import sha512_crypt
from iMii_v4.data.db_factory import DbSessionFactory
from iMii_v4.data.Car import Car
from iMii_v4.data.User import User
from iMii_v4.services.account_service import AccountService
import iMii_v4.services

class Repository:
    __car_data = {}

    @classmethod
    def all_cars(cls, limit=None):
        # cls.__load_data()
        #
        # cars = list(cls.__car_data.values())
        # if limit:
        #     cars = cars[:limit]
        #
        # return cars

        session = DbSessionFactory.create_session()

        query = session.query(Car)  # .order_by(Teacher.lName)

        if limit:
            cars = query[:limit]
        else:
            cars = query.all()

        session.close()

        return cars


    @classmethod
    def car_by_id(cls, car_id):
        # cls.__load_data()
        # return cls.__car_data.get(car_id)

        session = DbSessionFactory.create_session()

        car = session.query(Car).filter(Car.id == car_id).first()

        session.close()

        return car

    @classmethod
    def __load_data(cls):
        if cls.__car_data:
            return

        file = os.path.join(
            os.path.dirname(__file__),
            'opel.csv'
        )

        with open(file, 'r', encoding='utf-8') as fin:
            # brand,name,price,year,damage,last_seen
            reader = csv.DictReader(fin)
            for row in reader:
                key = str(uuid.uuid4())
                row['id'] = key
                cls.__car_data[key] = row

    @classmethod
    def add_car(cls, car):
        # cls.__load_data()
        # key = str(uuid.uuid4())
        # car_data['id'] = key
        # cls.__car_data[key] = car_data
        #
        # return car_data

        try:
            session = DbSessionFactory.create_session()

            db_car = Car()
            db_car.last_seen = parse(car.last_seen)  # parse(teacher.certdate)
            db_car.name = car.name
            db_car.brand = car.brand
            # db_car.image = car.image if car.image else random.choice(cls.__fake_image_url)
            db_car.year = car.year
            # db_car.teacherId = int(teacher.year)
            db_car.price = int( car.price )
            db_car.id = car.id

            session.add( db_car )
            session.commit()

            return db_car

        except Exception as e:
            print( e )  # for the repr
        # ...     print 'My exception occurred, value:', e.value



    @classmethod
    def update_car(cls, car_data):
        # key = car_data['id']
        # cls.__car_data[key] = car_data
        #
        # return car_data

        session = DbSessionFactory.create_session()

        db_car = session.query(Car).filter(Car.id == car_data.id).first()
        db_car.last_seen = parse(car_data.last_seen)
        db_car.name = car_data.name
        # db_car.image = car_data.image if car_data.image else random.choice(cls.__fake_image_url)
        db_car.brand = car_data.brand
        db_car.damage = car_data.damage
        # db_car.id = car_data.id
        db_car.price = car_data.price
        db_car.year = car_data.year

        session.commit()

        return db_car

    @classmethod
    def delete_car(cls, car_id):
        # del cls.__car_data[car_id]
        session = DbSessionFactory.create_session()
        db_car = session.query(Car).filter(Car.id == car_id).first()
        if not db_car:
            return

        session.delete(car_id)
        session.commit()


    @classmethod
    def find_user_by_api_key(cls, api_key: str) -> User:

        session = DbSessionFactory.create_session()
        user = session.query(User).filter(User.api_key == api_key).first()
        session.close()

        return user

    @classmethod
    def find_user_by_u_pw(cls, u: str, plain_text_password: str) -> User:

        session = DbSessionFactory.create_session()
        user1 = session.query( User ).filter( User.name == u ).first()

        session.close()
        if not user1:
            return None

        if not sha512_crypt.verify( plain_text_password, user1.hashed_password ):
            return None

        return user1

    @classmethod
    def create_user(cls, username,plain_text_password):

        session = DbSessionFactory.create_session()

        hashed_pw = AccountService.hash_text( plain_text_password )
        user = User(name=username)
        user.hashed_password = hashed_pw

        session.add(user)

        session.commit()

        return user