from pyramid.view import view_config


# @view_config(route_name='home', renderer='../templates/mytemplate.pt')
@view_config(route_name='home', renderer='../templates/splash.pt')
def my_view(request):
    return {'project': 'iMii_v4'}


@view_config(route_name='splash', renderer='../templates/splash.pt')
def splash(request):
    return {'project': 'iMii_v4'}
