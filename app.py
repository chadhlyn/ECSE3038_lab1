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
    
        
    
parallel([2,3])
potential_divider(9,[8, 3])    