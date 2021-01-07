from daawat.util.cql_file_util import get_cql_schema_string_from_file
from daawat.util.data_type_util import uuid_from_string
from daawat.model.categorys import Categorys

class CategorysDAO(object):

    table_name = "categorys"

    create_stmt = get_cql_schema_string_from_file(table_name)

    insert_stmt = 'INSERT INTO {table_name} (category_id,category_name,useremail,hotel_id) ' \
                  'VALUES (:category_id,:category_name,:useremail,:hotel_id);'.format(table_name=table_name)

    # select_all_journeys_stmt = 'SELECT * FROM {table_name};'.format(table_name=table_name)

    select_all_category_for_email = 'SELECT * FROM {table_name} WHERE useremail = :useremail ALLOW FILTERING;' \
                                              ''.format(table_name=table_name)
    select_category_id_for_category_name = 'SELECT category_id FROM {table_name} WHERE category_name = :category_name ALLOW FILTERING;' \
                                              ''.format(table_name=table_name)                                        

    # # select_single_journey_for_spacecraft_stmt = 'SELECT * FROM {table_name} ' \
    #                                             'WHERE spacecraft_name = :spacecraft_name AND journey_id = :journey_id;' \
    #                                             ''.format(table_name=table_name)

    def __init__(self, _session):
        self._session = _session
        self.maybe_create_schema()
        self.insert_prep_stmt = _session.prepare(self.insert_stmt)
        self.select_all_for_category_prep_stmt = _session.prepare(self.select_all_category_for_email)
        self.select_category_id_for_category_name_prep_stmt = _session.prepare(self.select_category_id_for_category_name)

    def maybe_create_schema(self):
        self._session.execute(self.create_stmt)

    def create_category(self, category):
        def handle_success(results):
            print("category added")

        def handle_error(exception):
            raise Exception('Failed to write row: ' + exception)

        insert_future = self._session.execute_async(self.insert_prep_stmt.bind({
            'category_id':category.category_id,
            'category_name':category.category_name,
            'useremail':category.userEmail,
            'hotel_id':category.hotel_id,
        }))

        insert_future.add_callbacks(handle_success, handle_error)

    def get_categroy_exits(self,email):
        count = 0
        result = self._session.execute(self.select_all_for_category_prep_stmt.bind({
            'useremail': email}
        ))
        for row in result:
            count += 1
        if count >= 1:
            return True
        else:
            return False
    def get_category_by_email(self,email):
        result = self._session.execute(self.select_all_for_category_prep_stmt.bind({
            'useremail': email}
        ))
        return result

    def get_category_id_by_category_name(self,category_name):
        result = self._session.execute(self.select_category_id_for_category_name_prep_stmt.bind({
            'category_name': category_name}
        ))
        return result
