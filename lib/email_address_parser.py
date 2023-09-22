# your code goes here!

import re

class EmailAddressParser:
    def __init__(self, input_string):
        self.input_string = input_string

    def parse(self):
        email_list = re.split(r'[,\s]+', self.input_string)
        email_list = [email for email in email_list if '@' in email]
        return sorted(set(email_list))

