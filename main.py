from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import urequests
import ujson as json

# Initialize 128*64 dot matrix OLED Display
oled_width = 128
oled_height = 64
i2c_rst = Pin(16, Pin.OUT)
i2c_rst.value(0)
sleep(0.010)
i2c_rst.value(1)
i2c_scl = Pin(15, Pin.OUT, Pin.PULL_UP)
i2c_sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = SoftI2C(scl=i2c_scl, sda=i2c_sda)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def oled_print(text, line):
    oled.fill(0)                   # Clear the display
    oled.text(text, 0, line * 10)
    oled.show()


def read_config():
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
        return config
    except Exception as e:
        oled_print("Config file missing!", 0)
        return None


def connect_wifi(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        oled_print("Connecting WiFi", 1)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    oled_print("WiFi Connected", 1)
    oled_print("IP: {}".format(wlan.ifconfig()[0]), 2)

def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        oled_print("Connecting WiFi", 1)
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        # Wait for the connection to establish
        while not wlan.isconnected():
            pass
    oled_print("WiFi connected!", 2)


# Get Bitcoin fee data from mempool.space
def get_bitcoin_fee_data():
    config = read_config()
    if config:
        response = urequests.get(config['api']['endpoint'])
        fee_data = response.json()
        response.close()
        return fee_data

# Display fee data on OLED
def display_fee_data(fee_data):
    oled.fill(0)
    oled.text("BTC Tx Fees", 0, 0)
    oled.text("Purge: {} sat/vB".format(fee_data['minimumFee']), 0, 20)
    oled.text("Low:   {} sat/vB".format(fee_data['economyFee']), 0, 30)
    oled.text("High:  {} sat/vB".format(fee_data['hourFee']), 0, 40)
    oled.text("Prio:  {} sat/vB".format(fee_data['fastestFee']), 0, 50)
    oled.show()

# Initialize
config = read_config()
if config:
    wifi_config = config['wifi']
    connect_wifi(wifi_config['ssid'], wifi_config['password'])

    # Main loop
    while True:
        try:
            fee_data = get_bitcoin_fee_data()
            display_fee_data(fee_data)
        except Exception as e:
            oled_print(f"Error: {}", e)
            oled.fill(0)
            oled.show()

        sleep(config['api']['refreshrate'])
