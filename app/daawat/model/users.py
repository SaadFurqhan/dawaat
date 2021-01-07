class Users(object):

    def __init__(self, first_name,last_name,phone,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password

    
    # def to_string(self):
    #     return 'SpacecraftJourneyCatalog [spacecraft_name={sc_n}, journey_id={j_id}, start={s}, end={e}, ' \
    #            'active={a}, summary={sum}]'.format(sc_n=self.spacecraft_name, j_id=self.journey_id, s=self.start,
    #                                                e=self.end, a=self.active, sum=self.summary)
