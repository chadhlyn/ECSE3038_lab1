import math
def parallel(resistor_list):
    Total_Resistance=0
    for resistor in resistor_list:
        Total_Resistance= Total_Resistance + 1/resistor
        
    Total_Resistance= 1/Total_Resistance

    print(Total_Resistance, "ohms")
    return Total_Resistance
    
    
    
parallel([10,18,12])
    