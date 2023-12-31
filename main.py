from time import sleep
import urequests
from config_reader import read_config
from wifi import connect_wifi

# Read configuration file
config = read_config()

# Connect to WiFi
if config:
    wifi_config = config['wifi']
    connect_wifi(wifi_config['ssid'], wifi_config['password'])

    # Since we audo-download needed libraries, this need to be imported after wifi
    from hardware import init_display, display_print
    
    # Initialize display
    display = init_display() if config else None

    def get_bitcoin_price():
        '''Fetch Bitcoin fee data from price endpoint'''
        response = urequests.get(config['api']['price_endpoint'])
        price_data = response.json()
        response.close()
        return price_data

    def get_bitcoin_fee_data():
        '''Fetch Transaction fee data from mempool.space endpoint'''
        response = urequests.get(config['api']['endpoint'])
        fee_data = response.json()
        response.close()
        return fee_data

    # Main loop
    while True:
        try:
            # Get Bitcoin price and Tx price
            btc_price = get_bitcoin_price()
            price_str = f"${btc_price['bitcoin']['usd']:,}"        # Format it to USD
            fee_data = get_bitcoin_fee_data()
            
            display.fill(0)                                        # Clear the display
            display.text("BTC Stats", 28, 0)
            display.text("Price: {}".format(price_str), 0, 10)
            display.text("---------------", 0, 20)
            display.text("Purge: {} sat/vB".format(fee_data['minimumFee']), 0, 30)
            display.text("Low:   {} sat/vB".format(fee_data['economyFee']), 0, 40)
            display.text("High:  {} sat/vB".format(fee_data['hourFee']), 0, 50)
            display.show()
            sleep(config['api']['refreshrate'])


        except Exception as e:
            print(f"Error: {e}")
            display_print(display, f"Error: {str(e)}", 0)

        sleep(config['api']['refreshrate'])
