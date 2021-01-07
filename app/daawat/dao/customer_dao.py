from daawat.util.cql_file_util import get_cql_schema_string_from_file
from daawat.util.data_type_util import uuid_from_string
from daawat.model.customer import Customers

class CustomersDAO(object):

    table_name = "customers"

    create_stmt = get_cql_schema_string_from_file(table_name)

    insert_stmt = 'INSERT INTO {table_name} (customer_name,status,hotel_id,table_no) ' \
                  'VALUES (:customer_name,:status,:hotel_id,:table_no);'.format(table_name=table_name)

    # select_all_journeys_stmt = 'SELECT * FROM {table_name};'.format(table_name=table_name)

    select_all_customer_for_hotel = 'SELECT * FROM {table_name} WHERE hotel_id = :hotel_id ALLOW FILTERING;' \
                                              ''.format(table_name=table_name)
                                              

    # # select_single_journey_for_spacecraft_stmt = 'SELECT * FROM {table_name} ' \
    #                                             'WHERE spacecraft_name = :spacecraft_name AND journey_id = :journey_id;' \
    #                                             ''.format(table_name=table_name)

    def __init__(self, _session):
        self._session = _session
        self.maybe_create_schema()
        self.insert_prep_stmt = _session.prepare(self.insert_stmt)
        self.select_all_customer_for_hotel_prep_stmt = _session.prepare(self.select_all_customer_for_hotel)
        

    def maybe_create_schema(self):
        self._session.execute(self.create_stmt)

    def create_customer(self, customer):
        

        def handle_success(results):
            print("customer added")

        def handle_error(exception):
            raise Exception('Failed to write row: ' + exception)


        insert_future = self._session.execute_async(self.insert_prep_stmt.bind({
            'customer_name':customer.customer_name,
            'status':customer.status,
            'hotel_id':customer.hotel_id,
            'table_no':customer.table_no,
        }))

        insert_future.add_callbacks(handle_success, handle_error)

    # def get_customer_exits(self,email):
    #     count = 0
    #     result = self._session.execute(self.select_all_for_hotel_prep_stmt.bind({
    #         'useremail': email}
    #     ))
    #     for row in result:
    #         count += 1
    #     if count == 1:
    #         return True
    #     else:
    #         return False

    def get_customer_by_hotel_id(self,hotel_id):
        result = self._session.execute(self.select_all_customer_for_hotel_prep_stmt.bind({
            'hotel_id': hotel_id}
        ))
        return result
