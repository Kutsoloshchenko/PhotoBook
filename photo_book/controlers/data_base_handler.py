"""Class that incapsulates work with data base and add layer of abstraction """

from rest_app_photo_book.models import User, Folders

ALIASES = {"users": User,
           "folders": Folders}

class DataBaseHandler:

    def add_entry(self, alias, dict):
        new_entry = ALIASES[alias](**dict)
        new_entry.save()

    def delete_entry(selfalias, alias, dict):
        ALIASES[alias].objects.filter(**dict).delete()

    def update_entry(self, alias, upd_dict, search_dict):
        entry = ALIASES[alias].objects.filter(**search_dict).first()

        for key in upd_dict:
            setattr(entry, key, upd_dict[key])
        entry.save()

    def contains(self, alias, key_argument):
        dict = {key_argument[0]: key_argument[1]}
        entry = ALIASES[alias].objects.filter(**dict).first()

        if entry:
            return True
        else:
            return False

    def get_entry_attributes(self, alias, dict, attributes):

        entry = ALIASES[alias].objects.filter(**dict).first()

        if entry:
            return [getattr(entry, attribute) for attribute in attributes]
        else:
            return None, None

    def get_entrys_attributes(self, alias, dict, attributes):
        entrys = ALIASES[alias].objects.filter(**dict)

        iter_object = [(entry, attributes) for entry in entrys]

        if entrys:
            return [[getattr(iter[0], atribute) for atribute in attributes] for iter in iter_object]
        else:
            return None

    def get_email_and_pwd(self, alias, email):
        entry = ALIASES[alias].objects.filter(email=email).first()

        if entry:
            return entry.email, entry.password
        else:
            return None, None

    def get_username_and_id(self, alias, key_argument):
        dict = {key_argument[0]: key_argument[1]}
        entry = ALIASES[alias].objects.filter(**dict).first()

        if entry:
            return entry.username, entry.id
        else:
            return None, None

