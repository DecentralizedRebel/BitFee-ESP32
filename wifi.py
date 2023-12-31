import network

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting WiFi")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("WiFi Connected")
    print("IP: {}".format(wlan.ifconfig()[0]))