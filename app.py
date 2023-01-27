import math
def parallel(resistor_list):
    Total_Resistance=0
    for resistor in resistor_list:
        Total_Resistance= Total_Resistance + 1/resistor
        
    Total_Resistance= 1/Total_Resistance

    print(Total_Resistance, "ohms")
    return Total_Resistance
    
 
def potential_divider(volts, voltage_list): 
    Total_voltage= 0
    for voltage in voltage_list:
        Total_voltage=Total_voltage + voltage
    
    i= volts/ Total_voltage
    
    for voltage in voltage_list:
        v = voltage * i
    
    print(v, "V")
    
def temperature_check(temp,unit):

    if unit == "f":
    #coversion = temp * 1.8 + 32
        if temp <98: 
            print ("The patient is hypothermic")

        elif temp ==98:
            print ("The patient temp is normal")

        elif temp >98:
            print ("The patient is hyperthermic")
      
    if unit == "c":

        if temp <37: 
            print ("The patien is hypothermic")

        elif temp == 37:
            print ("The patient temp is normal")

        elif temp >37:
            print ("The patient is hyperthermic")


parallel([2,3])
potential_divider(9,[1, 3]) 
temperature_check(38,"c") 