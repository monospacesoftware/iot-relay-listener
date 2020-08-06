# iot-relay-listener

Enables power on and off of a Raspberry Pi arcade cabinet (and connected devices) with a single button, using Digital Loggers IoT Relay device: https://www.amazon.com/gp/product/B00WV7GMA2/ref=ask_ql_qh_dp_hza

Mostly based on this nice guide: https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi with some script modifications.

Startup: 1 button press\
Shutdown: 2 button pressses

### Setup:

* Plug your RPi into the "always ON" outlet on the IoT Relay.
* Wire a button on your arcade control panel to GPIO 3 and GND on the RPi.
* Wire GPIO 16 to + on the IoT Relay's green phoenix connector, and GND to -.
* Plug your arcade cabinet devices like the monitor, speakers, etc into the "normally OFF" ports on the IoT Relay.
* Copy the file listen-for-shutdown.py from this repo to `/usr/local/bin` on the RPi and make it executable.
* Copy the file listen-for-shutdown.sh from this repo to `/etc/init.d` and make it executable.
* Set the script to run on boot by running `sudo update-rc.d listen-for-shutdown.sh defaults`
* Reboot the Rpi

### How it works

* Upon power up of the RPi, listen-for-shutdown.py executes and set GPIO 16 HIGH, causing the IoT relay to turn ON on the normally OFF ports.
* listen-for-shutdown.py then listens for 2 quick button presses on GPIO 3.  When it detects these, it causes the RPi to shutdown, which will set GPIO 16 LOW, causing the IoT Relay to turn off the normally OFF ports.
* The RPi will wake from the halt state when you press the button again, because GPIO 3 is the `WAKE_ON_GPIO` pin.
