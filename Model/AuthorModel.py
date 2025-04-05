class AuthorModelClass:
    def __init__(self,au_lname,au_fname,phone,address,city,state,zip,contract):
        self._au_lname=au_lname
        self._au_fname=au_fname
        self._phone=phone
        self._address=address
        self._city=city
        self._state=state
        self._zip=zip
        self._contract=contract

class AuthorModelBClass:
    def __init__(self,au_lname,au_fname,phone,address,city,state,zip,contract,au_id=0):
        self._au_lname=au_lname
        self._au_fname=au_fname
        self._phone=phone
        self._address=address
        self._city=city
        self._state=state
        self._zip=zip
        self._contract=contract
        self._au_id = au_id