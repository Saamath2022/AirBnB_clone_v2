import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all_method(self):
        """Test the all method."""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_method(self):
        """Test the new method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

    def test_save_method(self):
        """Test the save method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open("file.json", "r") as file:
            data = file.read()
            self.assertIn(f"BaseModel.{obj.id}", data)

    def test_reload_method(self):
        """Test the reload method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, storage.all())

if __name__ == "__main__":
    unittest.main()

