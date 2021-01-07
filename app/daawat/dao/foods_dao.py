from daawat.util.cql_file_util import get_cql_schema_string_from_file
from daawat.util.data_type_util import uuid_from_string
from daawat.model.foods import Foods

class FoodsDAO(object):

    table_name = "foods"

    create_stmt = get_cql_schema_string_from_file(table_name)

    insert_stmt = 'INSERT INTO {table_name} (food_id,food_name,food_price,food_description,food_img,useremail,hotel_id,category_name) ' \
                  'VALUES (:food_id,:food_name,:food_price,:food_description,:food_img,:useremail,:hotel_id,:category_name);'.format(table_name=table_name)

    # select_all_journeys_stmt = 'SELECT * FROM {table_name};'.format(table_name=table_name)

    select_all_foods_for_email = 'SELECT * FROM {table_name} WHERE useremail = :useremail ALLOW FILTERING;' \
                                              ''.format(table_name=table_name)
    select_food_for_category_name = 'SELECT * FROM {table_name} WHERE category_name = :category_name ALLOW FILTERING;' \
                                              ''.format(table_name=table_name)                                          
    select_food_for_food_id = 'SELECT * FROM {table_name} WHERE food_id = :food_id ALLOW FILTERING;' \
                                              ''.format(table_name=table_name)                        
    update_food_for_food_id = 'UPDATE {table_name} SET food_name = :food_name, food_price = :food_price, food_description = :food_description WHERE food_id = :food_id AND category_name = :category_name ' \
                                              ''.format(table_name=table_name)                                                                                                                                    
    delete_food_by_food_id =  'DELETE FROM {table_name}  WHERE food_id = :food_id ' \
                                              ''.format(table_name=table_name)                                                                                                                               
    # # select_single_journey_for_spacecraft_stmt = 'SELECT * FROM {table_name} ' \
    #                                             'WHERE spacecraft_name = :spacecraft_name AND journey_id = :journey_id;' \
    #                                             ''.format(table_name=table_name)

    def __init__(self, _session):
        self._session = _session
        self.maybe_create_schema()
        self.insert_prep_stmt = _session.prepare(self.insert_stmt)
        self.select_all_for_food_prep_stmt = _session.prepare(self.select_all_foods_for_email)
        self.select_food_for_category_name_prep_stmt = _session.prepare(self.select_food_for_category_name)
        self.select_food_for_food_id_prep_stmt = _session.prepare(self.select_food_for_food_id)
        self.update_food_prep_stmt = _session.prepare(self.update_food_for_food_id)
        self.delete_food_prep_stmt = _session.prepare(self.delete_food_by_food_id)

    def maybe_create_schema(self):
        self._session.execute(self.create_stmt)

    def create_food(self, food):
        
        def handle_success(results):
            print("food added")

        def handle_error(exception):
            raise Exception('Failed to write row: ' + exception)

        insert_future = self._session.execute_async(self.insert_prep_stmt.bind({
            'food_id':food.food_id,
            'food_name':food.food_name,
            'food_price':food.food_price,
            'food_description':food.food_description,
            'food_img':food.food_img,
            'useremail':food.userEmail,
            'hotel_id':food.hotel_id,
            'category_name':food.category_name
        }))

        insert_future.add_callbacks(handle_success, handle_error)

    def update_food(self, food, food_id):
        
        def handle_success(results):
            print("food updated")

        def handle_error(exception):
            raise Exception('Failed to write row: ' + exception)

        update_future = self._session.execute_async(self.update_food_prep_stmt.bind({
            'food_id':food_id,
            'food_name':food.food_name,
            'food_price':food.food_price,
            'food_description':food.food_description,
            'category_name':food.category_name
        }))

        update_future.add_callbacks(handle_success, handle_error)

    def delete_food(self,food_id):
        delete_result = self._session.execute(self.delete_food_prep_stmt.bind({
            'food_id': food_id}
        ))
        return True
    # def get_user_exits(self,email):
    #     count = 0
    #     result = self._session.execute(self.select_all_for_email_prep_stmt.bind({
    #         'email': email}
    #     ))
    #     for row in result:
    #         count += 1
    #     if count == 1:
    #         return True
    #     else:
    #         return False

    def get_food_by_email(self,email):
        result = self._session.execute(self.select_all_for_food_prep_stmt.bind({
            'useremail': email}
        ))
        return result
    def get_food_by_category_name(self,category_name):
        result = self._session.execute(self.select_food_for_category_name_prep_stmt.bind({
            'category_name': category_name}
        ))
        return result
    def get_food_by_food_id(self,food_id):
        result = self._session.execute(self.select_food_for_food_id_prep_stmt.bind({
            'food_id': food_id}
        ))
        return result

