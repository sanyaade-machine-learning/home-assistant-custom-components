# home-assistant-custom-components
Home Assistant Custom Components

Custom components I wrote for my implementation of home-assistant - the open-source home automation platform.

Learn more about the [Home-Assistant Platform](https://home-assistant.io/)

# Included Components

See below:
 * Nest Camera Component

## Nest Camera

Components for [Nest Camera](https://nest.com/camera/meet-nest-cam/):

* **Switch** - (``nestcameras``) a simple on/off switch that turns Nest camara streaming on or off
  * ``nestcameras`` includes on/off switch for camera streaming

## Instalation

Make sure you have already installed and properly configured the [Nest Component](https://home-assistant.io/components/nest/)  for Home-Assistant.

1. Download and place nestcameras.py files in the home-assistant folder like this (you may have to create the folder:

    - .homeassistant/custom_components/switch/nestcameras.py
  
2. Add the new platform in the configuration.yaml:

    ```yaml
     switch:
       platform: nestcameras
    ```

5. Restart the home assistant service.
