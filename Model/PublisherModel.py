class PublisherModelClass:

    def __init__(self , pub_name, city, state, country):
        self._pub_name = pub_name
        self._city = city
        self._state = state
        self._country = country


class PublisherModelBClass:
    def __init__(self, pub_name, city, state, country, pub_id=0):
        self._pub_name = pub_name
        self._city = city
        self._state = state
        self._country = country
        self._pub_id = pub_id
