```python
import unittest
from ai_model import AIModel
from device_controller import DeviceController
from user_interface import UserInterface

class TestHomeAutomation(unittest.TestCase):
    def setUp(self):
        self.ai_model = AIModel()
        self.device_controller = DeviceController("config.json")
        self.user_interface = UserInterface("config.json")

    def test_ai_model(self):
        # Assuming we have some dummy data for testing
        features = [[0, 0], [1, 1]]
        labels = [0, 1]
        self.ai_model.train(features, labels)
        self.assertEqual(self.ai_model.predict([[2., 2.]]), [1])

    def test_device_controller(self):
        # Assuming we have a device named "device1" in config.json
        self.assertEqual(self.device_controller.get_device_status("device1"), "off")
        self.assertTrue(self.device_controller.set_device_status("device1", "on"))
        self.assertEqual(self.device_controller.get_device_status("device1"), "on")

    def test_user_interface(self):
        # Assuming we have a device named "device1" in config.json
        self.user_interface.display_device_status("device1")
        self.user_interface.change_device_status("device1", "off")
        self.user_interface.display_device_status("device1")

if __name__ == "__main__":
    unittest.main()
```
