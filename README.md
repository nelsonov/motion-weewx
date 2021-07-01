Motion WeeWX MQTT script
======

## Status
A hack that I use that is only production quality for me

## Description
Subscribes to an MQTT feed from [WeeWX](https://www.weewx.com/) and
pulls out the temperature.  The temperature is then set, along with
the camera name, as left text in a
[Motion](https://motion-project.github.io/index.html) webcam display.

Supports multiple cameras via the config file

## Usage
The config file `/etc/motioneye/mqtt.txt` should consist of
space-seperated lines of text, with the first element being the name
of the camera (this could be any arbitrary string) and the second
being the Motion Web Control URL for that camera.  An example is
included in the examples directory.

An example systemd unit file is included in the examples directory.
To us it:
```
sudo cp motion-weewx-mqtt.py /usr/local/bin/
sudo cp examples/motion-weewx.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable motion-weewx
sudo systemctl start motion-weewx
```
This should have the script running as a daemon that starts at boot on
Linux systems that use systemd.  If your system doesn't use systemd or
if you're not using Linux, then you are likely advanced enough to install
this on your system.

