import time
from pywifi import PyWiFi, const
import os 
import subprocess

class MonitoringProgram:

    def __init__(self, BSSID_monitored_wifi, SSID_monitored_wifi):
        self.BSSID_monitored_wifi = BSSID_monitored_wifi
        self.SSID_monitored_wifi = SSID_monitored_wifi
        self.connected_devices = []




    # seting funktions
        # self.example()    


    # SET section 

        # ther is no set function but i will levt this for future

    # def set_example(self):
    #   self.example = 4202173 

    # END SET section 


    
    
    # test section 
    def test_print_monitored(self):
        print (self.BSSID_monitored_wifi)
        print (self.SSID_monitored_wifi)


    
    
    # bash command's
    def run_START_wlan0_monitor_mode(self):
        command = "sudo airmon-ng start wlan0"
        os.system(command)

    def run_STOP_wlan0_monitore_mode(self):
        command = "sudo airmon-ng stop wlan0mon"
        os.system(command)

    def run_airodump_ng(self):
        #subprocess.run(["sudo", "airodump-ng", "wlan0mon", "-d",self.BSSID_monitored_wifi])
        command = f"sudo gnome-terminal -x sh -c 'airodump-ng wlan0mon -d {self.BSSID_monitored_wifi}'"
        os.system(command)

    
    
    
    
    # Czyszczenie ekranu itd
    def clear_screen(self):
        command = "clear"
        os.system(command)


















def monitor_wifi_connections(monitored_bssid):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming only one Wi-Fi interface is available
    
    # Set monitor mode
    iface.disconnect()
    iface.mode = const.IFACE_MODE_MONITOR
    time.sleep(1)
    iface.disconnect()
    
    print(f"Monitoring Wi-Fi connections for BSSID: {monitored_bssid}")
    
    while True:
        try:
            # Scan for nearby access points
            iface.scan()
            time.sleep(2)
            results = iface.scan_results()
            
            for ap in results:
                if ap.bssid == monitored_bssid:
                    print(f"New connection: {ap.ssid} (BSSID: {ap.bssid})")
            
            time.sleep(5)  # Wait for 5 seconds before scanning again
            
        except KeyboardInterrupt:
            break

# Example usage:
monitored_bssid = "ac:22:0b:7c:7b:68"  # Replace with the BSSID of the Wi-Fi network to monitor
