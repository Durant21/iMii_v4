
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

import iMii_v4.infrastructure.auth as auth
from iMii_v4.data.repository import Repository
from iMii_v4.data.repository_events import Repository_events
from iMii_v4.data.repository_people import Repository_people
from iMii_v4.viewmodels.create_car_viewmodel import CreateCarViewModel
from iMii_v4.viewmodels.create_event_viewmodel import CreateEventViewModel
from iMii_v4.viewmodels.create_people_viewmodel import CreatePersonViewModel
from iMii_v4.viewmodels.update_car_viewmodel import UpdateCarViewModel
from iMii_v4.viewmodels.update_event_viewmodel import UpdateEventViewModel
from iMii_v4.viewmodels.update_person_viewmodel import UpdatePersonViewModel


@view_config(route_name='autos_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def all_autos(_):
    cars = Repository.all_cars(limit=25)
    return cars


@view_config(route_name='autos_api',
             request_method='GET',
             accept='text/csv',
             renderer='csv')
def all_autos_csv(_):
    cars = Repository.all_cars(limit=25)
    return cars


@view_config(route_name='auto_api',
             request_method='GET',
             renderer='json')
def single_auto(request: Request):
    car_id = request.matchdict.get('car_id')
    car = Repository.car_by_id(car_id)

    if not car:
        msg = "The car with id '{}' was not found.".format(car_id)
        return Response(status=404,json_body={'error': msg})

    return car


@view_config(route_name='autos_api',
             request_method='POST',
             renderer='json')
def create_auto(request: Request):
    try:
        car_data = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # TODO: Validate
    vm = CreateCarViewModel( car_data )
    vm.compute_details()
    if vm.errors:
        return Response(status=400, body=vm.error_msg)

    try:
        Car = Repository.add_car(vm.Car)
        return Response(status=201, json_body=Car.to_dict() )
    except Exception as x:
        return Response(status=400, body='Could not save car.')


@view_config(route_name='auto_api',
             request_method='PUT')
def update_auto(request: Request):
    car_id = request.matchdict.get('car_id')
    car = Repository.car_by_id(car_id)

    if not car:
        msg = "The car with id '{}' was not found.".format(car_id)
        return Response(status=404, json_body={'error': msg})

    try:
        car_data = request.json_body
        # car = Car.from_dict(car_data)
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # Validate
    vm = UpdateCarViewModel( car_data, car_id )
    vm.compute_details()
    if vm.errors:
        return Response( status=400, body=vm.error_msg )
    try:
        Repository.update_car(vm.Car)
        return Response(status=204, body='Car updated successfully.')
    except:
        return Response(status=400, body='Could not update car.')


@view_config(route_name='auto_api',
             request_method='DELETE')
def delete_auto(request: Request):
    car_id = request.matchdict.get('car_id')
    car = Repository.car_by_id(car_id)
    if not car:
        msg = "The car with id '{}' was not found.".format(car_id)
        return Response(status=404, json_body={'error': msg})

    try:
        Repository.delete_car(car_id)
        return Response(status=204, body='Car deleted successfully.')
    except:
        return Response(status=400, body='Could not update car.')


@view_config(route_name='login_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
def verifyLogIn(request):

    # u1 = request.params('u')
    u = request.GET['u']
    pw = request.GET['pw']
    # p = request.params['pw']
    y = "abc"

    user = Repository.find_user_by_u_pw(u=u,plain_text_password=pw)
    if not user:
        thisdict = {
            "api_key": "none"
        }
        # return Response( status=403, body="Invalid user or password; no user with these credentials" )
        return thisdict

    return user.to_dict()


# @view_config(route_name='people_interviewed_api',
#              request_method='GET',
#              accept='application/json',
#              renderer='json')
# # @auth.require_api_auth
# def all_people_interviewed(_):
#     people = Repository_people.all_people(limit=25)
#     return people


@view_config(route_name='people_interviewed_api',
             request_method='GET',
             renderer='json')
def interviewed_people(request: Request):
    interviewed = request.matchdict.get('interviewed')
    people = Repository_people.people_interviewed(interviewed,limit=25)
    #people = Repository_people.all_people( limit=25 )

    # if not person:
    #     msg = "The person with id '{}' was not found.".format(person_id)
    #     return Response(status=404,json_body={'error:': msg})
    #
    # return person

    return people


@view_config(route_name='people_api',
             request_method='GET',
             accept='application/json',
             renderer='json')
# @auth.require_api_auth
def all_people(_):
    # all_headers = dict(request.headers)
    # # v = t["Authorization"]
    #
    #
    # if "Authorization" not in request.headers:
    #     return Response(status=403,body="No auth header")
    #
    # auth_header = all_headers["Authorization"]
    # parts = auth_header.split(':')
    # if len(parts) != 2 or parts[0].strip() != "api-key":
    #     return Response( status=403, body="Invalid auth header" )
    #
    # api_key = parts[1].strip()
    # user = Repository.find_user_by_api_key(api_key)
    # if not user:
    #     return Response( status=403, body="Invalid api-key; no user with this account number" )
    #
    # print("Listing People for {}".format(user.name))

    people = Repository_people.all_people(limit=25)
    return people


@view_config(route_name='people_api',
             request_method='GET',
             accept='text/csv',
             renderer='csv')
def all_people_csv(_):
    people = Repository_people.all_people(limit=25)
    return people


@view_config(route_name='person_api',
             request_method='GET',
             renderer='json')
def single_person(request: Request):
    person_id = request.matchdict.get('person_id')
    person = Repository_people.person_by_id(person_id)

    if not person:
        msg = "The person with id '{}' was not found.".format(person_id)
        return Response(status=404,json_body={'error:': msg})

    return person


@view_config(route_name='people_api',
             request_method='POST',
             renderer='json')
def create_person(request: Request):
    try:
        person_data = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # Validate
    vm = CreatePersonViewModel( person_data )
    vm.compute_details()
    if vm.errors:
        return Response(status=400, body=vm.error_msg)

    try:
        person = Repository_people.add_person(vm.Person)
        return Response(status=201, json_body=person.to_dict())
    except:
        return Response(status=400, body='Could not save person information.')


@view_config(route_name='person_api',
             request_method='PUT')
def update_person(request: Request):
    person_id = request.matchdict.get('person_id')
    person = Repository_people.person_by_id(person_id)

    if not person:
        msg = "The person with id '{}' was not found.".format(person_id)
        return Response(status=404, json_body={'error': msg})

    try:
        person_data = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # Validate
    vm = UpdatePersonViewModel(person_data, person_id)# event_data , event_id
    vm.compute_details()
    if vm.errors:
        return Response(status=400, body=vm.error_msg)

    try:
        Repository_people.update_person(vm.Person)
        return Response(status=204, body='Person updated successfully.')
    except:
        return Response(status=400, body='Could not update person.')


@view_config(route_name='person_api',
             request_method='DELETE')
def delete_person(request: Request):
    person_id = request.matchdict.get('person_id')
    person = Repository_people.person_by_id(person_id)
    if not person:
        msg = "The Person with id '{}' was not found.".format(person_id)
        return Response(status=404, json_body={'error': msg})

    try:
        Repository_people.delete_person(person_id)
        return Response(status=204, body='Person deleted successfully.')
    except:
        return Response(status=400, body='Could not delete Person.')


@view_config(route_name='events_api',
             request_method='GET',
             renderer='json')
def all_events(_):
    events = Repository_events.all_events(limit=25)
    return events


@view_config(route_name='event_api',
             request_method='GET',
             renderer='json')
def single_event(request: Request):
    event_id = request.matchdict.get('event_id')
    event = Repository_events.event_by_id(event_id)

    if not event:
        msg= "The event with id '{}' was not found.".format(event_id)
        return Response(status=404,json_body={'error:': msg})

    return event


@view_config(route_name='events_api',
             request_method='POST',
             renderer='json')
def create_event(request: Request):
    try:
        event_data = request.json_body
    except:
        return Response(status=400, body='Could not parse your post as JSON.')

    # Validate
    vm = CreateEventViewModel( event_data )
    vm.compute_details()
    if vm.errors:
        return Response(status=400, body=vm.error_msg)

    try:
        event = Repository_events.add_event(vm.Event)
        return Response(status=201, json_body=event.to_dict())
    except:
        return Response(status=400, body='Could not save event information.')


@view_config( route_name='event_api',
              request_method='PUT' )
def update_event(request: Request):
    event_id = request.matchdict.get( 'event_id' )
    event = Repository_events.event_by_id( event_id )

    if not event:
        msg = "The event with id '{}' was not found.".format( event_id )
        return Response( status=404, json_body={'error': msg} )

    try:
        event_data = request.json_body
    except:
        return Response( status=400, body='Could not parse your post as JSON.' )

    # Validate
    vm = UpdateEventViewModel( event_data , event_id)
    vm.compute_details()
    if vm.errors:
        return Response(status=400, body=vm.error_msg)

    try:
        Repository_events.update_event( vm.Event )
        return Response( status=204, body='Event updated successfully.' )
    except:
        return Response( status=400, body='Could not update event.' )


@view_config( route_name='event_api',
              request_method='DELETE' )
def delete_event(request: Request):
    event_id = request.matchdict.get( 'event_id' )
    event = Repository_events.event_by_id( event_id )
    if not event:
        msg = "The Event with id '{}' was not found.".format( event_id )
        return Response( status=404, json_body={'error': msg} )

    try:
        Repository_events.delete_event( event_id )
        return Response( status=204, body='Event deleted successfully.' )
    except:
        return Response( status=400, body='Could not delete Person.' )


# @view_config(route_name='store_img1_view', renderer='templates/fileUpload.pt')
# def my_view2(request: Request):
#     store_img1_view(Request)
#     return {'project': 'fileUpload'}


