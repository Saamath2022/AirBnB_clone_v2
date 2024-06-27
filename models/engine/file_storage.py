import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, "w") as file:
            temp_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(temp_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (if it exists)."""
        try:
            with open(self.__file_path, "r") as file:
                temp_dict = json.load(file)
                for obj_dict in temp_dict.values():
                    cls_name = obj_dict['__class__']
                    if cls_name == "BaseModel":
                        self.new(BaseModel(**obj_dict))
        except FileNotFoundError:
            pass
