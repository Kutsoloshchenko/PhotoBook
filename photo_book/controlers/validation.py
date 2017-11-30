"""Module which checks client info used in different process"""

from re import compile
from passlib.hash import pbkdf2_sha256 as hash

# RegEx constants for validating different inputs
EMAIL_REGEX = compile(r"[a-zA-Z0-9-_]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+")
USERNAME_REGEX = compile(r"[a-zA-Z0-9-_ ]+")
PASSWORD_REGEX = compile(r".*[A-Z]+.*[!@#$%^&*()_+-=]+.*\d+.*")


class Validator:
    """Class that validates all user data used durin log in and sign up process"""

    def __init__(self, data_base):
        """Initilizes Validator class, in which DataBase object is created"""
        self._DB = data_base

    def sign_up(self, display_name, email, password, repeated_password):
        """Function to validate user data from Sign Up page

            Args:
                display_name -- entered login
                email -- entered email
                password -- entered password
                repeated_password -- repeated password



            Returns:
                True, None - if validation is successful. True is status of operation, None is error message
                False, Tuple - if validation is failed, returns Status False, and error messages

         """

        # Validates email, and receives status and error message
        email_result, email_message = self._validate_field(email,
                                                           EMAIL_REGEX,
                                                           ("email", email))

        # Validates login, and receives status and error message
        username_result, username_message = self._validate_field(display_name.lstrip().rstrip(),
                                                                 USERNAME_REGEX,
                                                                 ("username", display_name.lstrip().rstrip()))

        # Validates password, and receives status and error message
        password_result, password_message = self._validate_field(password,
                                                                 PASSWORD_REGEX)

        # Validates that repeated password is same as first password
        if password == repeated_password:
            repeat_password_result, repeat_password_message = True, "Ok"
        else:
            repeat_password_result, repeat_password_message = False, "Passwords does not match"

        # if every validation is successful - adds entry in DB and returns JSON with result OK
        if email_result and username_result and password_result and repeat_password_result:
            self._DB.add_entry('users', {"email": email,
                                         "username": display_name.lstrip().rstrip(),
                                         "password": hash.hash(password)})
            return {"result": "Ok"}

        # if at least one validation is not successful - then returns error messages and result Fail
        else:
            return {"result": "Fail", "email_error": email_message, "displayNameError": username_message,
                    "password_error": password_message, "repeatedPasswordError": repeat_password_message}

    def sign_in(self, email, password):
        """Method to validate data submitted by user during sign in process

            Args:
                email -- email submitted by user
                password -- passwordsubmittedd by user

            Returns:
                Dictionary with "result" and "password_error":
                False, Message - If validation of data is not successful - then returns status fail and error message
                True, None - If validation is successful - returns status True and None as error message

         """

        email, psw = self._DB.get_entry_attributes('users', {"email": email}, ("email", "password"))
        if not email or not hash.verify(password, psw):
            return {"result": "Fail", "password_error": "Username or password are not correct"}
        else:
            return {"result": "Ok"}

    def _validate_field(self, field, reg_ex, tuple=None):
        """Private function to validate any value against provided regular expression"""

        if tuple:
            contains = self._DB.contains("users", tuple)
        else:
            contains = False
            tuple = ("password",)

        fullmatch = reg_ex.fullmatch(field)

        if fullmatch and not contains:
            return True, "Ok"
        elif fullmatch and contains:
            return False, "%s is already taken" % tuple[0]
        else:
            return False, "%s is not correct" % tuple[0]


if __name__ =="__main__" :

    val = Validator()

    print(val.sign_in("Name", "GStyle@P1nk"))

    print(val.sign_in('asdfasdf', 'asdfasdfasdf'))