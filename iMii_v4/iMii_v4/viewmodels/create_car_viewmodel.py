from dateutil.parser import parse

from iMii_v4.data.Car import Car
from iMii_v4.viewmodels.base_viewmodel import ViewModelBase


class CreateCarViewModel( ViewModelBase ):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Car = None

    def compute_details(self):

        # teacherId = self.data_dict.get('teacherId', None)
        # if teacherId:
        #     teacherId = parse(teacherId)
        brand = self.data_dict.get('brand')
        name = self.data_dict.get('name' )
        damage = self.data_dict.get( 'damage' )
        image = self.data_dict.get('image')
        price = self.data_dict.get('price')
        year = int(self.data_dict.get('year', -1))
        last_seen =  self.data_dict.get( 'last_seen', -1 )
        id = self.data_dict.get('id')

        # if not teacherId:
        #     self.errors.append("teacherId is a required field.")
        if not name:
            self.errors.append("name is a required field.")
        if not brand:
            self.errors.append("brand is a required field.")
        if price is None:
            self.errors.append("You must specify a price")
        # elif price < 0:
        #     self.errors.append("Price must be non-negative.")
        if year is None:
            self.errors.append("You must specify a year")
        # elif year < 0:
        #     self.errors.append("Year must be non-negative.")

        if not self.errors:
            car = Car(
                    brand=brand,
                    name=name,
                    damage=damage,
                    image=image,
                    price=price,
                    year=year,
                    last_seen=last_seen,
                    id=id
            )
            self.Car = car

            # id, brand, name, damage, image, price, year, last_seen