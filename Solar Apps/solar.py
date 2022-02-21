#Example 1
P1 = 100000 #Power in Watts
R1 = 0.4 #Resistance in Ohms
V1 = 300 #Voltage (pressure) in Volts

#1. Work out the current in Amps
I1 = P1/V1
print(round(I1,2))

#2. Work out the power transmission losses (in Watts)
Losses1 = (I1**2)*R1
print(round(Losses1,2))

#3. Percentage Power Losses
percentage_losses1=(Losses1)/P1
print(round(percentage_losses1,2))

#Example 2
P2 = 100000 #Power in Watts
R2 = 0.4 #Resistance in Ohms
V2 = 600 #Voltage (pressure) in Volts

#1. Work out the current in Amps
I2 = P2/V2
print(round(I2,2))

#2. Work out the power transmission losses (in Watts)
Losses2 = (I2**2)*R2
print(round(Losses2,2))

#3. Percentage Power Losses
percentage_losses2=(Losses2)/P2
print(round(percentage_losses2,2))