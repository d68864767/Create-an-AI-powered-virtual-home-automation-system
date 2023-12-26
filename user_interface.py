```python
import json
from device_controller import DeviceController

class UserInterface:
    def __init__(self, config_file):
        self.device_controller = DeviceController(config_file)

    def display_device_status(self, device_name):
        status = self.device_controller.get_device_status(device_name)
        if status is not None:
            print(f"Device {device_name} is currently {status}.")
        else:
            print(f"Device {device_name} does not exist.")

    def change_device_status(self, device_name, status):
        success = self.device_controller.set_device_status(device_name, status)
        if success:
            print(f"Device {device_name} status has been set to {status}.")
        else:
            print(f"Failed to set the status of device {device_name}.")

    def display_all_devices(self):
        devices = self.device_controller.get_all_devices()
        for device_name, device_info in devices.items():
            print(f"Device {device_name} is currently {device_info.get('status')}.")

if __name__ == "__main__":
    ui = UserInterface("config.json")
    ui.display_all_devices()
```
