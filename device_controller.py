```python
import json

class DeviceController:
    def __init__(self, config_file):
        with open(config_file) as f:
            self.devices = json.load(f)

    def get_device_status(self, device_name):
        device = self.devices.get(device_name)
        if device:
            return device.get('status')
        else:
            return None

    def set_device_status(self, device_name, status):
        device = self.devices.get(device_name)
        if device:
            device['status'] = status
            with open(config_file, 'w') as f:
                json.dump(self.devices, f)
            return True
        else:
            return False

    def get_all_devices(self):
        return self.devices
```
