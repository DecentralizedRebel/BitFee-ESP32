# ESP32 Bitcoin Transaction price monitor

This project is designed to display Bitcoin transaction fees fetched from the mempool.space API on an ESP32 with a display. It's a perfect tool to keep an eye on transaction costs in real-time.

## Features

* Fetches real-time Bitcoin transaction fees (purge, low, high, priority) from Mempool.space.
* Displays the fees on an ESP32's OLED display.
* Customizable Wi-Fi and API settings via a JSON configuration file.
* Adjustable data refresh rate (be nice if using the public API).

## Hardware Requirements

* ESP32 microcontroller
* OLED display module compatible with ESP32 (typically 0.96-inch, 128x64 pixels or you will need to customize the code)

<img src="img/heltec-lora-32-wifi.jpeg" alt="Heltec Lora 32 Wifi" width="50%"/>

## Software Requirements

* MicroPython firmware for ESP32
* WiFi with Internet connectivity

## Configuration

1. **Wi-Fi Settings:**
       Configure your ESP32 to connect to your Wi-Fi network by editing the config.json file.

2. **API Settings:**
        Set the API endpoint and data refresh rate in the config.json file.
        
**Sample `config.json` file**
```json
{
  "wifi": {
    "ssid": "YOUR_WIFI_SSID",
    "password": "YOUR_WIFI_PASSWORD"
  },
  "api": {
    "endpoint": "https://mempool.space/api/v1/fees/recommended",
    "price_endpoint": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd",
    "refreshrate": 120
    },
  "hw": {
    "platform": "heltec-lora-32",
    "display": "ssd1306"
    }
}
```

Replace YOUR_WIFI_SSID and YOUR_WIFI_PASSWORD with your actual Wi-Fi credentials in ```config.json```.

## Setup and Deployment

* **Prepare the ESP32:**
  Flash your ESP32 with the latest version of MicroPython. Example:
  ```shell
  esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ~/Downloads/esp32/micropython/ESP32_GENERIC-OTA-20231227-v1.22.0.bin
  ```

* **Upload Required Files:**
  Upload the ```config_reader.py```, ```hardware.py```, ```main.py``` & ```wifi.py``` to the root of the ESP32.

* **Configure Wi-Fi and API Settings:**
  Edit and upload the config.json file with your Wi-Fi settings to the root of the ESP32.

* **Running the Application:**
  Restart the ESP32 to automatically run the application. It will display the latest Bitcoin transaction fees on the screen, updating them according to the specified refresh rate.