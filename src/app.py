import time
import os 
from wifi_heandler import PrintWiFis
from monitoring_network import MonitoringProgram
import subprocess

class Program:

    def __init__(self):
        self.wifis_ssid_list = []
        self.wifis_bssid_list = []
        self.BSSID_selected_network = ""
        self.SSID_selected_network = ""

        # setings funktions
        self.set_wifis_ssid_list()
        self.set_wifis_bssid_list()

    
    # SET SECTION 

    def set_wifis_ssid_list(self):
        siemanko = PrintWiFis()
        new_list = siemanko.return_ssid_list()
        self.wifis_ssid_list = new_list

    def set_wifis_bssid_list(self):
        object_02 = PrintWiFis()
        self.wifis_bssid_list = object_02.return_bssid_list()

    def set_selected_network(self,network_id):
        self.selected_network = network_id 

        self.test_name = "siemanko marjan"

    def set_BSSID_selected_network(self, bssid):
        self.BSSID_selected_network = bssid

    def set_SSID_selected_network(self, ssid):
        self.SSID_selected_network = ssid
    # END SET SECTION 


    # other functions()
    def print_wifis(self):
        print_wifis_01 = PrintWiFis()
        wifi_list = print_wifis_01.return_ssid_list()

        for (index ,i) in enumerate(wifi_list,start=1):
            print(index, i)

    def print_wifi_list(self):
        for i in self.wifis_ssid_list:
            print (i)

    def select_network(self):
        pass

    def start_monitoring(self):
        pass


    # Display section 
    def introducing(self):
        self.clear_screen()
        print ("=== WiFi-Menager© by 'PermissionnDenied©' ===")
        print ("===        Wersja Programu 1.0.0          ===")
        print ("---------------------------------------------")
        print ("--The task of the program is to monitor the--")
        print ("--activity of the wifi network. When       --")
        print ("--someone connects we get an SMS if someone--")
        print ("--disconnects we also get an SMS.          --")
        print ("---------------------------------------------")

    def menu_01(self):
        print (f"[*] Selected Network: {self.SSID_selected_network}")
        print ("[1] Select Network")
        print (f"[2] Start Monitoring selected network ! {self.SSID_selected_network}")
        print ("[0] Wyjdz !")


    # system
    def stop_program(self):
        pass

    def clear_screen(self):
        os.system('clear')


# Here an important moment. We create an OBJECT class PROGRAM. 
# Like ; class Car, class Person, class Employye. Instead of 
# return_car_color() function, we have for example: print_wifis(). 


program_01 = Program()



def main():

    

    while True:

        #wyswietlanko menu 
        program_01.introducing()
        program_01.menu_01()
        
        

        choice = input("Select option: ")

        if choice == "1":

            program_01.clear_screen()

            program_01.print_wifis()
            program_01.set_wifis_bssid_list()
            program_01.set_wifis_ssid_list()


            # Select the NETWORK you want to monitor

            print (" ")
            print ("TYPE 'r' to refresh networks !!!")
            choice_01 = input("Select network: ")


            # Block try: except: to avoid krash

            try:
                choice_01 = int(choice_01)

                #podajac indek sieci wybietamy ja z listy :) 
                program_01.set_selected_network(program_01.wifis_ssid_list[choice_01 - 1])
                
                #ustawiamy bssid i ssid wybranej sieci 
                program_01.set_BSSID_selected_network(program_01.wifis_bssid_list[choice_01 -1])
                program_01.set_SSID_selected_network(program_01.wifis_ssid_list[choice_01 -1])

            except:

                if choice_01 == 'r' or 'R':
                    program_01.clear_screen()

                    program_01.print_wifis()
                    program_01.set_wifis_bssid_list()
                    program_01.set_wifis_ssid_list()

                else:
                    print ("")



        # The purpose of the program is to monitor the 
        # network whether someone has connected or disconnected. 
        # When the program detects such movement it should immediately send an SMS. 



        elif choice == "2":
            program_01.clear_screen()
            print(f"NETWORK MONITORING {program_01.SSID_selected_network}")
            
            monitoring_program_01 = MonitoringProgram(program_01.BSSID_selected_network,program_01.SSID_selected_network)

            monitoring_program_01.run_START_wlan0_monitor_mode()
            
    
            
            monitoring_program_01.run_airodump_ng()


            while True:
                program_01.clear_screen()
                anser = input("IF you wont end type 'stop' or 's' !!! : ")
                if anser.lower() == 's' or 'stop':
                    monitoring_program_01.run_STOP_wlan0_monitore_mode()
                    break
                else:
                    print ("zle klikniete")


        # END PROGRAM

        elif choice == "0":
            print("Zamykanie programu...")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")



if __name__=="__main__":
    main()

