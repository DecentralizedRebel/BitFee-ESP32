# ESP32 Bitcoin Transaction price monitor

This project is designed to display Bitcoin transaction fees (purge, low, high, and priority) fetched from the mempool.space API on an ESP32 with an OLED display. It's a perfect tool to keep an eye on transaction costs in real-time.

## Features

* Fetches real-time Bitcoin transaction fees (low, high, priority) from Mempool.space.
* Displays the fees on an ESP32's OLED display.
* Customizable Wi-Fi and API settings via a JSON configuration file.
* Adjustable data refresh rate (be nice if using the public API).

## Hardware Requirements

* ESP32 microcontroller
* OLED display module compatible with ESP32 (typically 0.96-inch, 128x64 pixels or you will need to customize the code)

## Software Requirements

* MicroPython firmware for ESP32
* ssd1306.py OLED driver for MicroPython

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
    "refreshrate": 120
  }
}
```

Replace YOUR_WIFI_SSID and YOUR_WIFI_PASSWORD with your actual Wi-Fi credentials.

## Setup and Deployment

* **Prepare the ESP32:**
  Flash your ESP32 with the latest version of MicroPython.

* **Upload Required Files:**
  Upload the ```ssd1306.py``` driver and ```main.py``` to the ESP32.

* **Configure Wi-Fi and API Settings:**
  Edit and upload the config.json file with your Wi-Fi settings to the ESP32.

* **Running the Application:**
  Restart the ESP32 to automatically run the application. It will display the latest Bitcoin transaction fees on the OLED screen, updating them according to the specified refresh rate.