import time

ID = 1
Drivers = [("ID001","Walid","Hermel"), ("ID002","Rami","Hermel"),("ID003","Ibrahim","Beirut"),("ID004","Omar","Akkar")]
Cities = ["Akkar","Beirut","Baalback","Jbeil","Zahle"]

line1 = ["Akkar","Beirut","Jbeil"]
line2 = ["Baalback","Zahle"]

lines= [line1, line2]

def DriverMenu():
    print("")
    print("Enter:")
    print("1. To view all the drivers")
    print("2. To add a driver")
    print("3. Check similar drivers")
    print("4. To go back to the main menu")
    print("")
    userInputDriver = input()

    if (userInputDriver == "1"):
        PrintAllDrivers()
        MainMenu()

    elif (userInputDriver == "2"):
        AddDriver()
        MainMenu()
    
    elif (userInputDriver == "3"):
        PrintSimilarDrivers()
        MainMenu()

    elif (userInputDriver == "4"):
        MainMenu()
    
    else:
        print("Wrong Input")
        time.sleep(1)
        DriverMenu()

def CitiesMenu():
    print("")
    print("Enter:")
    print("1. Show cities")
    print("2. Search city")
    print("3. Print neighboring cities")
    print("4. Print Drivers delivering to city")
    print("")
    userInputCity = input()

    if (userInputCity == "1"):
        ShowCities()
        MainMenu()

    elif (userInputCity == "2"):
        key = input("Please enter a search key: ")
        Search(key)
        MainMenu()
    
    elif (userInputCity == "3"):
        city = input("Please enter the city: ")
        PrintNeighboringCity(city)
        MainMenu()

    elif (userInputCity == "4"):
        city = input("Please enter the city: ")
        PrintDriversDeliveringToCity(city)
        MainMenu()
    
    else:
        print("Wrong Input")
        time.sleep(1)
        DriverMenu()

def MainMenu():
    print("")
    print("Hello! Please enter:")
    print("1. To go to the drivers’ menu")
    print("2. To go to the cities’ menu")
    print("3. To exit the system")
    print("")
    user_input = input()

    if (user_input == "1"):
        DriverMenu()
    elif (user_input == "3"):
        print("")
    elif (user_input == "2"):
        CitiesMenu()
    else:
        print("Wrong Input")
        time.sleep(1)
        DriverMenu()

def PrintAllDrivers():
    for driver in Drivers:
        print(driver[0] +", "+driver[1]+", "+ driver[2])

def AddDriver():
    global ID
    name = input("Please enter the driver name: ")
    city = input("Please enter the starting city: ")
    if (not city in Cities):
        response = input("City is not available do you want to add it YES/NO")
        if(response == "YES"):
            Cities.append(city)
        else:
            return
    driverId = ""
    if (ID < 9):
        driverId = "ID00" + str(ID)
    elif((ID > 9) and (ID < 100)):
        driverId = "ID0" + str(ID)
    else:
        driverId = "ID" + str(ID)
    ID = ID +1

    driver = (driverId,name,city)
    Drivers.append(driver)
    
def PrintSimilarDrivers():
    for city in Cities:
        cityDrivers = ""
        for driver in Drivers:
            if (driver[2] == city):
                if (cityDrivers == ""):
                    cityDrivers = driver[1]
                else:
                    cityDrivers = cityDrivers + "," + driver[1]
        if (cityDrivers != ""):
            print(city + ": " + cityDrivers)

def ShowCities():
    CitiesDescending = sorted(Cities, reverse=True)
    for city in  CitiesDescending:
        print(city)

def Search(key):
    result = ""
    for city in Cities:
        if(key in city):
            if (result == ""):
                    result = city
            else:
                    result = result + "," + city
    print(result)

def PrintNeighboringCity(city):
    neighboringCities  = ""
    for line in lines:
        if city in line:
            for n_city in line:
                if (n_city != city):
                    if (neighboringCities == ""):
                         neighboringCities = n_city
                    else:
                         neighboringCities = neighboringCities + "," + n_city
            break
       
    print(neighboringCities) 


def PrintDriversDeliveringToCity(city):
    driversToCity = ""
    line = []
    for subLine in lines:
        if city in Cities:
            line = subLine
            break
    for driver in Drivers:
        if (driver[2] in line):
            if (driversToCity == ""):
                         driversToCity = driver[1]
                    
            else:
                         driversToCity = driversToCity + "," + driver[1]
    print(driversToCity)
            
MainMenu()