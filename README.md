# iot-relay-listener

Enables startup and shutdown of a full arcade cabinet (and connected devices) with a single button, using Digital Loggers IoT Relay device: https://www.amazon.com/gp/product/B00WV7GMA2/ref=ask_ql_qh_dp_hza

### Setup:

* Plug your RaspberryPi into the "always ON" outlet on the IoT Relay.
* Wire a button on your arcade control panel to GPIO 3 and Ground on the Raspberry Pi.
* Wire GPIO 16 to + on the IoT Relay's green phoenix connector, and Ground to -.
* Plug your arcade cabinet devices like monitor, speakers, etc into the "normally OFF" ports on the IoT Relay.



