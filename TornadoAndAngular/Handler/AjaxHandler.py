import tornado.web
from databaseConnection.postgresConnection import PostgresConnection
from tornado.escape import json_decode
from  tornado.escape import json_encode


class AjaxHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        request_data = json_decode(self.request.body) if self.request.body else None

        if 'method' in request_data.keys():

            if request_data['method'] == 'check_user_login':
                self._check_user_login(request_data['data'])

            elif request_data['method'] == 'register_user':
                self._register_user(request_data['data'])

            elif request_data['method'] == 'get_all_users':
                self._get_all_users()

        else:
            raise Exception('Wrong data format received')

    def _check_user_login(self, data):
        db = PostgresConnection()
        data = db.check_user_login(data['username'], data['password'])
        self.write(json_encode(data))

    def _register_user(self, data):
        db = PostgresConnection()
        result = db.insert_user(first_name=data['firstName'], password=data['password'],
                                last_name=data['lastName'], user_name=data['username'])
        self.write('completed')

    def _get_all_users(self):
        db = PostgresConnection()
        data = db.get_login_data()
        self.write(json_encode(data))
