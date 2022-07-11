from turtle import bgcolor
from pip import main
from rent import BikeRent, CarRent, Customer

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

bike = BikeRent(100)
car = CarRent(10)
customer = Customer()



main_menu = True
while True:
    if main_menu: 
        print(bcolors.WARNING + """
        ********** Araç Kiralama **********
        A. Bisiklet Menüsü
        B. Araba Menüsü
        Q. Çıkış
        """ + bcolors.ENDC)

        main_menu = False
        choice = input("Seçiminizi yapınız: ")
        choice = choice.lower()

    if choice == "a":
        print(bcolors.OKBLUE +"""
        ***** Bisiklet Menüsü *****
        1. Kiralanabilir bisiklet sayısı
        2. Saatlik kiralama ücreti $5
        3. Günlük kiralama ücreti $84
        4. Bisiklet iade
        5. Araç kiralama menüsü
        6. Çıkış
        """+ bcolors.ENDC)
        choice = input("Seçiminizi yapınız. ")
        try:
            choice = int(choice)
        except ValueError:
            print(bcolors.FAIL+"Yanlış seçim yaptınız."+ bcolors.ENDC)
            continue

        if choice == 1:
            bike.displayStock()
            choice = "a"
        elif choice == 2:
            customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike")) 
            customer.rentalBasis_b = 1
            main_menu = True
            print(25*"-")
        
        elif choice == 3:
            customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike")) 
            customer.rentalBasis_b = 2
            main_menu = True
            print(25*"-")
        elif choice == 4:
            customer.bill = bike.returnVehicle(customer.returnVehicle("bike"), "bike")
            customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:     
            break
        else:
            print(bcolors.FAIL+"Geçersiz değer!\n1-6 arasında değer giriniz."+ bcolors.ENDC)
            main_menu = True
#--------------------------------------------------------------

    elif choice == "b":
        print(bcolors.OKCYAN +"""
        ***** Araba Menüsü *****
        1. Kiralanabilir araba sayısı
        2. Saatlik kiralama ücreti $10
        3. Günlük kiralama ücreti $192
        4. Araba iade
        5. Araç kiralama menüsü
        6. Çıkış
        """ + bcolors.ENDC)
        choice = input("Seçiminizi yapınız. ")
        try:
            choice = int(choice)
        except ValueError:
            print(bcolors.FAIL+ "Yanlış seçim yaptınız."+ bcolors.ENDC)
            continue

        if choice == 1:
            car.displayStock()
            choice = "b"
        elif choice == 2:
            customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car")) 
            customer.rentalBasis_c = 1
            main_menu = True
            print(25*"-")
        
        elif choice == 3:
            customer.reantalTime_c = car.rentDaily(customer.requestVehicle("car")) 
            customer.rentalBasis_c = 2
            main_menu = True
            print(25*"-")
        elif choice == 4:
            customer.bill = car.returnVehicle(customer.returnVehicle("car"), "car")
            customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:     
            break
        else:
            print(bcolors.FAIL+"Geçersiz değer!\n1-6 arasında değer giriniz."+bcolors.ENDC)
            main_menu = True
    
    elif choice == "q":
        break 

    else: 
        print(bcolors.FAIL+"Hatalı değer!\n A,B veya Q tuşuna basınız. "+ bcolors.ENDC) 
        main_menu = True  
print(bcolors.OKGREEN+"Bizi tercih ettiğiniz için teşşekür ederiz."+ bcolors.ENDC)
