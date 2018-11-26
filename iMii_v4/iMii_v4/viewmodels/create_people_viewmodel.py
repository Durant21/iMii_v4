from dateutil.parser import parse

from iMii_v4.data.People import Person
from iMii_v4.viewmodels.base_viewmodel import ViewModelBase


class CreatePersonViewModel( ViewModelBase ):
    def __init__(self, data_dict):
        super().__init__()
        self.data_dict = data_dict
        self.Person = None

    def compute_details(self):

        # teacherId = self.data_dict.get('teacherId', None)
        # if teacherId:
        #     teacherId = parse(teacherId)
        # brand = self.data_dict.get('brand')
        headline = self.data_dict.get('headline' )
        fname = self.data_dict.get( 'fname' )
        lname = self.data_dict.get( 'lname' )
        title = self.data_dict.get('title')
        company = self.data_dict.get( 'company' )
        email = self.data_dict.get( 'email' )
        url1 = self.data_dict.get( 'url1' )
        url2 = self.data_dict.get( 'url2' )
        description = self.data_dict.get( 'description' )
        address = self.data_dict.get( 'address' )
        city = self.data_dict.get( 'city' )
        state = self.data_dict.get( 'state' )
        interviewed = self.data_dict.get( 'interviewed' )
        interview = self.data_dict.get( 'interview' )
        doc1 = self.data_dict.get( 'doc1' )
        # img1 = self.data_dict.get( 'img1' )
        # image = self.data_dict.get('image')
        # price = self.data_dict.get('price')
        # year = int(self.data_dict.get('year', -1))
        # last_seen =  self.data_dict.get( 'last_seen', -1 )
        id = self.data_dict.get('id')

        # if not teacherId:
        #     self.errors.append("teacherId is a required field.")
        if not lname:
            self.errors.append("lname is a required field.")
        if not fname:
            self.errors.append("fname is a required field.")
        # if price is None:
        #     self.errors.append("You must specify a price")
        # # elif price < 0:
        # #     self.errors.append("Price must be non-negative.")
        # if year is None:
        #     self.errors.append("You must specify a year")
        # elif year < 0:
        #     self.errors.append("Year must be non-negative.")

        if not self.errors:
            person = Person(
                headline=headline,
                lname=lname,
                fname=fname,
                company=company,
                title=title,
                email=email,
                url1=url1,
                url2=url2,
                description=description,
                address=address,
                city=city,
                state=state,
                interviewed=interviewed,
                interview=interview,
                doc1=doc1,
                id=id
            )
            self.Person = person

            # id, brand, name, damage, image, price, year, last_seen