class Spartan:

    def __init__(self, s_id, f_name, l_name, b_year, b_month, b_day, s_course, s_stream):
        self.sparta_id = s_id
        self.first_name = f_name    #encapsulation
        self.last_name = l_name     #We use getters & setters to add validation logic around getting and setting a value.
        self.birth_year = b_year
        self.birth_month = b_month
        self.birth_day = b_day
        self.sparta_course = s_course
        self.sparta_stream = s_stream

    def __str__(self):
        return f"ID: {self.sparta_id} \n first_name : {self.first_name} \n last_name :{self.last_name} \n birth_yoear: {self.birth_year}\n birth_month: {self.birth_month}\n birth_day: {self.birth_day}\n sparta_course: {self.sparta_course}\n sparta_stream: {self.sparta_stream}\n"

    def get_sparta_id(self):
        return self.sparta_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_birth_year(self):
        return self.birth_year

    def get_birth_month(self):
        return self.birth_month

    def get_birth_day(self):
        return self.birth_day

    def get_sparta_course(self):
        return self.sparta_course

    def get_sparta_stream(self):
        return self.sparta_stream

    def set_sparta_id(self, sparta_id):
        self.sparta_id = sparta_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_birth_year(self, birth_year):
        self.birth_year = birth_year

    def set_birth_mont(self, birth_month):
        self.birth_month = birth_month

    def set_birth_day(self, birth_day):
        self.birth_day = birth_day

    def set_sparta_course(self, sparta_course):
        self.sparta_course = sparta_course

    def set_sparta_stream(self, sparta_stream):
        self.sparta_stream = sparta_stream
