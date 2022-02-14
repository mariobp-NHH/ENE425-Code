#This script replicate the results in this webpage:
#(https://corporatefinanceinstitute.com/resources/knowledge/finance/levelized-cost-of-energy-lcoe/)

#Costs
EC=1500 #Entry Cost (Euros)
IC=100 #Installation cost (Euros)
c=0.02 #Increase Installation cost per year (2%)
f=0 #Fuel cost (Euros)

#Energy Production
E=3000 #Total Energy produced in a year (KWh)

#Years operation
years=11

#Discount rate
r=1.08 #8%

#Total Cost and total Energy
C_total = EC
E_total = 0

for y in range(2, years):
    MC_year = IC*(1+(c*(y-2)))
    FC_year = f
    discount_factor=1/(r**y)
    C_year = (MC_year+FC_year)*discount_factor
    C_total = C_total+C_year
    E_year = E*discount_factor
    E_total = E_total+E_year
    print(y, round(MC_year,2), round(discount_factor,2), round(C_year,2), round(C_total,2), round(E_year,2), round(E_total,2))

LCOE=C_total/E_total
print(round(LCOE,2))






