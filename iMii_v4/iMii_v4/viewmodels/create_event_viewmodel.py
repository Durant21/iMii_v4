from dateutil.parser import parse

from iMii_v4.data.Event import Event
from iMii_v4.viewmodels.base_viewmodel import ViewModelBase


class CreateEventViewModel( ViewModelBase ):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Event = None

    def compute_details(self):

        # teacherId = self.data_dict.get('teacherId', None)
        # if teacherId:
        #     teacherId = parse(teacherId)
        # brand = self.data_dict.get('brand')
        headline = self.data_dict.get('headline' )
        description = self.data_dict.get( 'description' )
        url = self.data_dict.get('url')
        # price = self.data_dict.get('price')
        # year = int(self.data_dict.get('year', -1))
        event_date = self.data_dict.get('event_date', -1 )
        # date_created = self.data_dict.get('date_created', -1 )
        id = self.data_dict.get('id')

        # if not teacherId:
        #     self.errors.append("teacherId is a required field.")
        if not headline:
            self.errors.append("headline is a required field.")
        if not description:
            self.errors.append("description is a required field.")
        # if price is None:
        #     self.errors.append("You must specify a price")
        # # elif price < 0:
        # #     self.errors.append("Price must be non-negative.")
        # if year is None:
        #     self.errors.append("You must specify a year")
        # elif year < 0:
        #     self.errors.append("Year must be non-negative.")

        if not self.errors:
            event = Event(
                    headline=headline,
                    description=description,
                    url=url,
                    event_date=event_date,
                    id=id
            )
            self.Event = event

            # id, brand, name, damage, image, price, year, last_seen