from dateutil.parser import parse

from iMii_v4.data.Car import Car
from iMii_v4.viewmodels.base_viewmodel import ViewModelBase
from iMii_v4.viewmodels.create_people_viewmodel import CreatePersonViewModel


class UpdatePersonViewModel( CreatePersonViewModel ):
    def __init__(self, data_dict, person_id):
        super().__init__(data_dict)
        self.person_id = person_id

    def compute_details(self):

        person_id = self.data_dict.get('id')
        if not self.person_id:
            self.errors.append("No person ID specified.")
        if self.person_id != person_id:
            self.errors.append("Person ID mismatch.")

        super().compute_details()