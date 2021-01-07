from daawat.dao.session_manager import SessionManager
from daawat.dao.users_dao import UsersDAO
from daawat.dao.hotels_dao import HotelsDAO
from daawat.dao.foods_dao import FoodsDAO
from daawat.dao.categorys_dao import CategorysDAO
from daawat.dao.customer_dao import CustomersDAO
from daawat.dao.generate_qr_dao import GenerateQRsDAO

class AstraService(object):

    user_dao = None
    hotel_dao = None
    food_dao = None
    category_dao = None
    customer_dao = None
    generate_qr_dao = None
    _session_manager = SessionManager()
    _session = None

    def get_session(self):
        if self._session is None:
            self._session = self._session_manager.get_instance().connect()

        return self._session

    def connect(self):
        return self._session_manager.connect()

    def check_connection(self):
        return self._session_manager.check_connection()

    def get_user_dao(self):
        if self.user_dao is None:
            self.user_dao = UsersDAO(self.get_session())

        return self.user_dao

    def get_hotel_dao(self):
        if self.hotel_dao is None:
            self.hotel_dao = HotelsDAO(self.get_session())

        return self.hotel_dao

    def get_food_dao(self):
        if self.food_dao is None:
            self.food_dao = FoodsDAO(self.get_session())

        return self.food_dao

    def get_category_dao(self):
        if self.category_dao is None:
            self.category_dao = CategorysDAO(self.get_session())

        return self.category_dao

    def get_customer_dao(self):
        if self.customer_dao is None:
            self.customer_dao = CustomersDAO(self.get_session())

        return self.customer_dao

    def get_generate_qr_dao(self):
        if self.generate_qr_dao is None:
            self.generate_qr_dao = GenerateQRsDAO(self.get_session())

        return self.generate_qr_dao

    # functions used to service login and signup functionalities
    def create_new_user(self, first_name, last_name, phone, email, password):
        return self.get_user_dao().create_user(first_name, last_name, phone, email, password)

    def get_user_exits(self,email):
        return self.get_user_dao().get_user_exits(email)

    def get_user_by_email(self,email):
        return self.get_user_dao().get_user_by_email(email)

    # functions used to add hotel and check whether hotel exists 
    def create_new_hotel(self, hotel):
        return self.get_hotel_dao().create_hotel(hotel)

    def get_hotel_by_email(self,email):
        return self.get_hotel_dao().get_hotel_by_email(email)

    def get_hotel_exits(self,email):
        return self.get_hotel_dao().get_hotel_exits(email)

    def create_new_category(self, category):
        return self.get_category_dao().create_category(category)
    
    def get_category_exits(self,email):
        return self.get_category_dao().get_categroy_exits(email)

    def get_category_by_email(self,email):
        return self.get_category_dao().get_category_by_email(email)

    def get_category_id_by_category_name(self,category_name):
        return self.get_category_dao().get_category_id_by_category_name(category_name)
    
    def create_new_food(self, food):
        return self.get_food_dao().create_food(food)

    def update_food(self, food, food_id):
        return self.get_food_dao().update_food(food,food_id)
    
    def delete_food(self, food_id):
        return self.get_food_dao().delete_food(food_id)

    def delete_food(self, food_id):
        return self.get_food_dao().delete_food(food_id)
    
    def get_food_by_email(self,email):
        return self.get_food_dao().get_food_by_email(email)

    def get_food_by_food_id(self,food_id):
        return self.get_food_dao().get_food_by_food_id(food_id)

    def get_food_by_category_name(self,category_name):
        return self.get_food_dao().get_food_by_category_name(category_name)
    
    def create_new_customer(self, customer):
        return self.get_customer_dao().create_customer(customer)
    
    def create_generate_qr(self, generateqr):
        return self.get_generate_qr_dao().create_generate_qr(generateqr)
    
    def get_generate_qr_exits(self,email):
        return self.get_generate_qr_dao().get_generate_by_email(email)









    def get_location_readings_for_spacecraft_journey(self, spacecraft_name, journey_id, page_size, page_state):
        return self.get_spacecraft_location_dao().get_location_readings_for_journey(spacecraft_name, journey_id,
                                                                                    page_size, page_state)

    def save_location_reading_for_spacecraft_journey(self, spacecraft_name, journey_id, data):
        self.get_spacecraft_location_dao().write_readings(spacecraft_name, journey_id, data)

    def get_pressure_readings_for_spacecraft_journey(self, spacecraft_name, journey_id, page_size, page_state):
        return self.get_spacecraft_pressure_dao().get_pressure_readings_for_journey(spacecraft_name, journey_id,
                                                                                    page_size, page_state)

    def save_pressure_reading_for_spacecraft_journey(self, spacecraft_name, journey_id, data):
        self.get_spacecraft_pressure_dao().write_readings(spacecraft_name, journey_id, data)

    def get_speed_readings_for_spacecraft_journey(self, spacecraft_name, journey_id, page_size, page_state):
        return self.get_spacecraft_speed_dao().get_speed_readings_for_journey(spacecraft_name, journey_id,
                                                                              page_size, page_state)

    def save_speed_reading_for_spacecraft_journey(self, spacecraft_name, journey_id, data):
        self.get_spacecraft_speed_dao().write_readings(spacecraft_name, journey_id, data)

    def get_temperature_readings_for_spacecraft_journey(self, spacecraft_name, journey_id, page_size, page_state):
        return self.get_spacecraft_temperature_dao().get_temperature_readings_for_journey(spacecraft_name, journey_id,
                                                                                          page_size, page_state)

    def save_temperature_reading_for_spacecraft_journey(self, spacecraft_name, journey_id, data):
        self.get_spacecraft_temperature_dao().write_readings(spacecraft_name, journey_id, data)


astra_service = AstraService()
