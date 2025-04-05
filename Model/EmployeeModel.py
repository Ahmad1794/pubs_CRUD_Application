class EmployeeModelClass:
    def __init__(self,fname,minit,lname,job,job_lvl,pub,hire_date):
        self._fname=fname
        self._minit=minit
        self._lname=lname
        self._job=job
        self._job_lvl=job_lvl
        self._pub=pub
        self._hire_date=hire_date


class EmployeeModelBClass:
    def __init__(self, fname, minit, lname, job, job_lvl, pub, hire_date, emp_id=0):
        self._emp_id = emp_id
        self._fname = fname
        self._minit = minit
        self._lname = lname
        self._job = job
        self._job_lvl = job_lvl
        self._pub = pub
        self._hire_date = hire_date
