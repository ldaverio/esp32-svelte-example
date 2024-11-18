# ESP32 + SvelteKit

The an example of serving a SvelteKit app from an [ESP32 microcontroller](https://www.espressif.com/en/products/socs/esp32).

ESP32 is [$2 microcontroller](https://www.aliexpress.com/w/wholesale-esp32-chip.html) with intergrated WIFI and Bluetooth.

Tested with a [WROOM-32 devkit](https://abra-electronics.com/robotics-embedded-electronics/esp-series/wifi-esp32-esp-wroom-32-wi-fi-bluetooth-ble-low-power-iot-microcontroller.html)

## Background

- The SvelteKit app is built with the `@sveltejs/adapter-static`.
- The `build` directory is synced to the flash using `mpremote`. Thankfully Svelte bundles are very small, and can fit inside the microcontroller's flash. For larger projects, you can use an SD card.
- The `firmware` folder contains the Python code to connect to WIFI, and start an HTTP server to serve the SvelteKit build. Just copy it over to the ESP32 using `mpremote`.

## Setup

```sh
# install the mpremote cli
pip install mpremote

# build svelte-kit project
pnpm build

# copy `build` folder to device
mpremote fs cp -r build :build

# run web server on device
mpremote run firmware/server.py
```

## License

MIT
