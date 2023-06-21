import pywifi
import time


class PrintWiFis:

    def __init__(self):
        self.wifis_bssid_list = []
        self.wifis_ssid_list = []
        self.set_wifi_list()

    def set_wifi_list(self):
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[1]
        iface.scan()
        time.sleep(0.5)
        results = iface.scan_results()

        for (i) in results:
            bssid = i.bssid
            ssid  = i.ssid
            #print(i,f"{bssid}: {ssid}")
            self.wifis_bssid_list.append(bssid)
            self.wifis_ssid_list.append(ssid)

    def return_bssid_list(self):
        return self.wifis_bssid_list

    def return_ssid_list(self):
        return self.wifis_ssid_list

    def print_wifis(self):
        for (index, item) in enumerate(self.return_ssid_list(), start=1):
            print(index, item)







