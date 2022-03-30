#Novus Service Hub

class ServiceHub:
    def __init__(self, listHubVehicles, listOwnedVehicles):
        self.vehicles = listHubVehicles
        self.owenedVehicles = listOwnedVehicles

    def displayAvailableVehicles(self): # This display's available vehicles at service hub
        print("Vehicles avialble in 'Rankala Service hub' are:  \n (reg. no.) ")
        for vehicle in self.vehicles: 
            print(" o  " + vehicle )
    
    def getVehicle(self, vehicleNo):
        if vehicleNo in self.vehicles:
            print(f" You have been issued Novus with reg. no. {vehicleNo}. ")
            print(" Please keep it safe and park it at any 'Novus hub' within 8 hrs. ")
            self.vehicles.remove(vehicleNo)
            return True
        else:
            print("Please, Enter valid Novus Vehical reg. no. ")
            print("***Check list of available vehicles in 'Rankala Service hub' ")
            return False

    def parkVehicle (self, vehicleName):
        if vehicleName in self.owenedVehicles :
            self.vehicles.append(vehicleName)
            print(" Thanks for choosing novus mobility ! ")
            print(" Hope you enjoyed riding it. Have a great day ahead! ")
        else :
            print('Please,Enter valid reg. no.  ')
            print("***Vehicle reg. no. you entered is not owned by Novus Mobility ")
class customer:  #This class is created to take input from customer
    def getvehicle(self):
        self.vehicle = input("Enter the reg. no. of the vehicle you want: ")
        return self.vehicle

    def parkvehicle(self):
        self.vehicle = input("Enter the reg. no. of the vehicle that you want to park: ")
        return self.vehicle
         

if __name__ == "__main__":
    dashboard = ServiceHub(["4500", "4850", "4999", "4689","4359","4629","4537"], str(tuple(range(4500,5000))))
    customer = customer()
    #NovusHub.displayAvailableVehicles
    while(True):
        welcomeMsg = '''\n ====== Welcome to Novus Mobility ======
        Please, Select an option:
        1. List all Available vehicles
        2. Get a vehicle
        3. Park a vehicle
        4. Exit
        '''
        try:
            print(welcomeMsg)
            a = int(input("Enter a option: "))
            if a == 1:
                dashboard.displayAvailableVehicles()
            elif a == 2:
                dashboard.getVehicle(customer.getvehicle())
            elif a == 3:
                dashboard.parkVehicle(customer.parkvehicle())
            elif a == 4:
                print("Thanks for choosing Novus Mobility. Have a great day ahead!")
                exit()
            else:
                print("Invalid Choice!, kindly select valid option.")
        except ValueError:
            # Handle the exception
            print("Invalid Choice!, kindly select valid option.")

        
