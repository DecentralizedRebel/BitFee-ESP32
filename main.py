from time import sleep
import urequests
from config_reader import read_config
from wifi import connect_wifi

# Read configuration
config = read_config()

# Connect to WiFi
if config:
    wifi_config = config['wifi']
    connect_wifi(wifi_config['ssid'], wifi_config['password'])

    # Since we audo-download needed libraries, this need to be imported after wifi
    from hardware import init_display, display_print
        # Get Bitcoin fee data from mempool.space
    
    # Initialize display
    display = init_display() if config else None

    def get_bitcoin_fee_data():
        response = urequests.get(config['api']['endpoint'])
        fee_data = response.json()
        response.close()
        return fee_data

    # Display fee data on display
    def display_fee_data(fee_data):
        display.fill(0)
        display.text("BTC Tx Fees", 0, 0)
        display.text("Purge: {} sat/vB".format(fee_data['minimumFee']), 0, 20)
        display.text("Low:   {} sat/vB".format(fee_data['economyFee']), 0, 30)
        display.text("High:  {} sat/vB".format(fee_data['hourFee']), 0, 40)
        display.text("Prio:  {} sat/vB".format(fee_data['fastestFee']), 0, 50)
        display.show()

    # Main loop
    while True:
        try:
            fee_data = get_bitcoin_fee_data()
            display_fee_data(fee_data)
        except Exception as e:
            print(f"Error: {e}")
            display_print(display, f"Error: {str(e)}", 0)

        sleep(config['api']['refreshrate'])
