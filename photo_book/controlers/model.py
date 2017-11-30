from controlers.validation import Validator
from controlers.data_base_handler import DataBaseHandler
from controlers.token_controler import TokenController
from controlers.os_handler import OsHandler
from functools import wraps

class Model():

    def __init__(self):
            """ Initialize function, creates instances on needed classes"""

            # creates data base orm class
            self._db = DataBaseHandler()

            # creates class that handle user validation
            self._validator = Validator(self._db)

            # imports secret key from config file and creates token controller class instance
            from photo_book.settings import SECRET_KEY
            self._jwt_token_creator = TokenController(SECRET_KEY)

            # create osHandler instance
            self._os_handler = OsHandler(self._db)

    def _validate_token(self, token, username):
        token_dict = self._jwt_token_creator.decode_token(bytes(token, "UTF-8"))
        username, id_bd = self._db.get_entry_attributes('users', {"username": username}, ("username", "id"))

        if username == token_dict["username"] and id_bd == token_dict["id"]:
            # is provided user name and user id is same as in decoded token that verification is successful
            return True

        else:
            return False

    def sign_up(self, display_name, email, password, repeted_password):
        """Calls validation function of validator class and returns response

            inputs:
                    display_name - username entered by user
                    email - email address entered by user
                    password - password entered by user
                    repeted_password - repeat of the password entered by user

            return:
                    response item returned by validator sign_up function

        """
        response = self._validator.sign_up(display_name.lower(), email.lower(), password, repeted_password)

        if response["result"] == "Ok":
            self._os_handler.create_user_folder(display_name)

        return response

    def sign_in(self, email, password):
        """Calls sign_in function of validator class, and on success adds jwt token to the response object

            inputs:
                    email - email address entered by user
                    password - password entered by user
            return:
                    response item dict containing status, error, token and username keys

        """

        response = self._validator.sign_in(email.lower(), password)
        if response["result"] == "Ok":
            username, id = self._db.get_entry_attributes('users', {"email": email}, ("username", "id"))

            if username and id:
                response["token"] = self._jwt_token_creator.create_token(username, id)
                response["username"] = username
            else:
                raise AttributeError

        return response

    def create_album(self, token, username, folder_name):

        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.create_album(username, folder_name)

        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response

    def create_file(self, token, username, album_name, image_dict):
        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.create_file(username, album_name, image_dict)
        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response

    def get_albums(self, token, username):
        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.get_albums(username)
        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response

    def get_files_in_album(self, token, username, folder_name):
        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.get_album_content(username, folder_name)
        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response

    def change_album_name(self, token, username, folder_name, new_folder_name):
        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.change_album_name(username, folder_name, new_folder_name)
        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response

    def change_file_attributes(self, token, username, folder_name, file_name, image_prop_dict):
        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.change_file_attributes(username, folder_name, file_name, image_prop_dict)
        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response

    def delete_album(self, token, username, folder_name):
        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.delete_album(username, folder_name)
        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response

    def delete_files(self, token, username, folder_name, file_names):
        if self._validate_token(token, username):
            # is provided user name and user id is same as in decoded token that verification is successful
            response = self._os_handler.delete_files(username, folder_name, file_names)
        else:
            response = {"result": 'Fail', "error": 'Auth error'}

        return response