import os
from re import compile
import json
import shutil

FOLDER_REGEX = compile(r"[a-zA-Z0-9-_. ]+")

class OsHandler:
    def __init__(self, data_base):
        self._base_folder = "../user_folders/"
        self._db = data_base

    def create_album(self, base, name):
        response = self._create_folder(os.path.join(self._base_folder, base), name)
        if response['result'] == 'Ok':
            self._db.add_entry("folders", {"owner": base,
                                           "folder_path": os.path.join(self._base_folder, base, name),
                                           "content": None,
                                           "name": name})
        return response

    def create_user_folder(self, base):
        response = self._create_folder(self._base_folder, base)
        return response

    def create_file(self, base, album_name, image_prop_dict):
        validation_responce = self._validate_name(os.path.join(self._base_folder, base, album_name), image_prop_dict["name"])

        if validation_responce['result'] == 'Ok':
            with open(os.path.join(self._base_folder, base, album_name, image_prop_dict["name"]), "wb") as file:
                file.write(image_prop_dict['file'])

            image_prop_dict["file"] = os.path.join(self._base_folder, base, album_name, image_prop_dict["name"])

            content = self._db.get_entry_attributes("folders", {"name": album_name}, ("content",))

            if content or content[0] is None:
                content = []

            content.append(image_prop_dict)

            self._db.update_entry("folders", {"content": str(content)}, {"name": album_name})

        return validation_responce

    def _create_folder(self, path, name):

        validation_responce = self._validate_name(path, name)

        if validation_responce['result'] == 'Ok':
            os.mkdir(os.path.join(path, name))

        return validation_responce

    def _validate_name(self, path, name):
        fullmatch = FOLDER_REGEX.fullmatch(name)

        if not fullmatch:
            return {"result": "Fail", "error": "Name contains invalid characters"}
        elif fullmatch and os.path.exists(os.path.join(path, name)):
            return {"result": "Fail", "error": "Album with specified name already exists"}
        else:
            return {"result": "Ok"}

    def get_albums(self, owner_name):
        folders = self._db.get_entrys_attributes("folders", {"owner": owner_name}, ("name",))

        if folders:
            result = []
            for i in folders:
                result.append({"name": i[0], "result": "Ok"})
            return result
        else:
            return {"result": "No Albums", "error_message": "You dont have any albums"}

    def get_album_content(self, owner_name, album_name):
        content = self._db.get_entry_attributes("folders", {"owner": owner_name, "name": album_name}, ("content",))

        if content:
            return {"result": "Ok", "content": str(content)}
        else:
            return {"result": "No Albums", "message": "You dont have any albums"}

    def change_album_name(self, owner_name, album_name, new_name):
        response = self._create_folder(os.path.join(self._base_folder, owner_name), new_name)
        if response['result'] == 'Ok':
            os.rename(os.path.join(self._base_folder, owner_name, album_name), new_name)
            self._db.update_entry("folders",
                                  {"name": new_name, "folder_path": os.path.join(self._base_folder, owner_name, new_name)},
                                  {"owner": owner_name, "name": album_name})

        return response

    def change_file_attributes(self, owner_name, album_name, file_name, image_prop_dict):

        # write new validation for images - to se if any changes are availible
        validation_responce = self._validate_name(os.path.join(self._base_folder, owner_name, album_name),
                                                  image_prop_dict["name"])

        if validation_responce['result'] == 'Ok':
            os.rename(os.path.join(self._base_folder, owner_name, album_name, file_name),
                      os.path.join(self._base_folder, owner_name, album_name, image_prop_dict["name"]))

            image_prop_dict["file"] = os.path.join(self._base_folder, owner_name, album_name, image_prop_dict["name"])

            content = self._db.get_entry_attributes("folders",
                                                    {"name": album_name, "owner": owner_name},
                                                    ("content",))

            content = [json.loads(item.replace('\'', '"')) for item in content][0]

            content = [item for item in content if item["name"] != file_name]
            content.append(image_prop_dict)

            self._db.update_entry("folders",
                                  {"content": content},
                                  {"name": album_name, "owner": owner_name})

        return validation_responce

    def delete_files(self, owner_name, album_name, file_names):

        for file_name in file_names:
            os.remove(os.path.join(self._base_folder, owner_name, album_name, file_name))

            content = self._db.get_entry_attributes("folders",
                                                    {"name": album_name, "owner": owner_name},
                                                    ("content",))

            content = [json.loads(item.replace('\'', '"')) for item in content][0]

            content = [item for item in content if item["name"] != file_name]

            self._db.update_entry("folders",
                                  {"content": content},
                                  {"name": album_name, "owner": owner_name})

    def delete_album(self, owner_name, album_name):
        shutil.rmtree(os.path.join(self._base_folder, owner_name, album_name))
        self._db.delete_entry("folders", {"owner": owner_name, "name": album_name})
        return {"result": "Ok"}

