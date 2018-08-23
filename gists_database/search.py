from .models import Gist
#from .fixtures import populated_gists_database as db

#from gists_database.tests.fixtures import populated_gists_database as db
#from .models import Gist


DATETIME_COLUMNS = ('created_at', 'updated_at')


def is_datetime_param(param):
    for prefix in DATETIME_COLUMNS:
        if param.startswith(prefix):
            return True
    return False

def get_operator(comparison):
    operation_dict = {
        'lt': '<',
        'lte': '<=',
        'gt': '>',
        'gte': '>=',
    }
    
    return operation_dict[comparison]

def build_query(**kwargs):
    query = 'SELECT * FROM gists'
    params = {}
    if kwargs:
        filters = []
        for param, value in kwargs.items():
            if is_datetime_param(param):
                if '__' in param:
                    attribute, comparison = param.split('__')
                    operator = get_operator(comparison)
                    '''
                    ** -> multiple AND conditions
                    filters.append(
                        'datetime(%s) %s datetime(:%s)' % (
                            attribute, operator, param))
                            '''
                    filters1 = 'datetime(%s) %s datetime(:%s)' % (attribute, operator, param)
                else:
                    attribute = param
                    '''
                    ** -: multiple AND conditions
                    filters.append(
                        'datetime(%s) == datetime(:%s)' % (
                            attribute, param))
                    '''
                    filters1 = 'datetime(%s) == datetime(:%s)' % (attribute, param)
                params[param] = value
            else:
                '''
                ** -> multiple AND conditions
                filters.append(
                    '%s = :%s' % (
                        param, param))
                '''
                filters1 = '%s = :%s' % (param, param)
                params[param] = value

        query += ' WHERE '
        query += filters1
        #query += ' AND '.join(filters) **-> This is for multiple AND conditions

    return query, params

def search_gists(db_connection, **kwargs):
    query, params = build_query(**kwargs)
    cursor = db_connection.execute(query, params)
    results = []
    for gist in cursor:
        results.append(Gist(gist))
    return results

#print(search_gists(db, github_id='4232a4cdad00bd92a7a64cf3e2795820'))
        
