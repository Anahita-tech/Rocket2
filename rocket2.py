Input_information={}
Input_information['Initial_fuel']=int(input('Enter the initial fuel:'))
fuel=Input_information['Initial_fuel']
Input_information['Initial_speed']=int(input('Enter the initial speed:'))
Input_information['distance_traveled']=0
Input_information['Acceleration']=int(input('Enter the acceleration:'))
Input_information['speed']=0
print('Input_information',Input_information)
t=0
def check_fuel():
    if Input_information['Initial_fuel']<80:
        Input_information['Initial_fuel']+=2000
        return
while Input_information['Initial_fuel']>0:
    print('fuel',fuel)
    t+=1
    Input_information['speed']=Input_information['Acceleration']*t+Input_information['Initial_speed']
    fuel_consumption=Input_information['speed']/100
    Input_information['Initial_fuel']=Input_information['Initial_fuel']-fuel_consumption
    Distance_traveled=0.5*Input_information['Acceleration']*t**2+Input_information['Initial_speed']*t+Input_information['distance_traveled']
    Input_information['distance_traveled']=Distance_traveled
    print('Input_information', Input_information)
    check_fuel()
    if Input_information['Initial_fuel']<=0.1*fuel:
        print('Fuel level is below 10%')
    if Distance_traveled>=750000:
        print('Spacecraft arrived at Mars')
        break
