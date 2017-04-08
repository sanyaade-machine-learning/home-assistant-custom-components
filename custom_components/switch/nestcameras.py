import logging
import homeassistant.components.nest as nest
from homeassistant.helpers.entity import ToggleEntity

_LOGGER = logging.getLogger(__name__)

DEPENDENCIES = ['nest']

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up a Nest Cameras as Switches"""
    camera_devices = hass.data[nest.DATA_NEST].cameras()
    cameras = [NestCameraSwitch(structure, device)
               for structure, device in camera_devices]

    add_devices(cameras, True)

class NestCameraSwitch(ToggleEntity):
    """Representation of a Nest Camera as switch."""
    def __init__(self, structure, device):
        """Initialize"""
        super(NestCameraSwitch, self).__init__()
        self.structure = structure
        self.device = device
        self._location = None
        self._name = None
        self._online = None
        self._is_streaming = None

    @property
    def should_poll(self):
        """Nest camera should poll periodically."""
        return True

    @property
    def unique_id(self):
        """Return the device id"""
        return self.device._device['device_id']

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self._is_streaming

    @property
    def is_online(self):
        """Return true if camera is online."""
        return self._online

    def turn_on(self):
        """Only toggle lights if camera is online."""
        if self.is_online == True:
            self._turn_switch('on')

    def turn_off(self):
        """Only toggle lights if camera is online."""
        if self.is_online == True:
            self._turn_switch('off')

    def _turn_switch(self, state):
        try:
            if state == 'off':
                self.device._set('devices/cameras', {'is_streaming': False})
                self._is_streaming = False
            else:
                self.device._set('devices/cameras', {'is_streaming': True})
                self._is_streaming = True
        except nest.nest.APIError as error:
            _LOGGER.error("Error updating camera streaming status: %s", error)

        super().schedule_update_ha_state()

    def update(self):
        """Cache value from Python-nest."""
        self._location = self.device.where
        self._name = self.device.name
        self._online = self.device.online
        self._is_streaming = self.device.is_streaming
