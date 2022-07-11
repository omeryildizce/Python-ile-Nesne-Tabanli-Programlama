import datetime


class VehicleRent:
    def __init__(self, stock):
        """Araç Sayısı"""
        self.stock = stock
        self.__now = 0

    def displayStock(self):
        """
            Display Stock
        """
        print(f"{self.stock} araç kiralama için uygun.")
        return self.stock

    def rentHourly(self, n):
        """
            Rent hourly
        """
        if n <= 0:
            print("Sayı pozitif olmalı.")
            return None
        elif n > self.stock:
            print(f"Yeterli kadar stok yok.\nStok: {self.stock}")
            return None
        else:
            self.now = datetime.datetime.now()
            print(f"{n} araç {(self.now.hour)} saatlik kiralandı.")
            self.stock -= n

            return self.now

    def rentDaily(self, n):
        """
            Rent daily
        """
        if n <= 0:
            print("Sayı pozitif olmalı.")
            return None
        elif n > self.stock:
            print(f"Yeterli kadar stok yok.\nStok: {self.stock}")
            return None
        else:
            self.now = datetime.datetime.now()
            print(f"{n} araç {(self.now.hour)} saatlik kiralandı.")
            self.stock -= n

            return self.now

    def returnVehicle(self, request, brand):
        """
            return a bill
        """
        car_h_price = 10
        car_d_price = car_h_price * 8 / 10 * 24
        bike_h_price = 5
        bike_d_price = bike_h_price * 7/10 * 24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.seconds / 3600 * car_h_price*numOfVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.seconds / \
                        (3600 * 24) * car_d_price*numOfVehicle
                if (2 <= numOfVehicle):
                    print("%20 indirim kazandınız.")
                    bill *= 0.8

                print(f"Fiyat: ${bill}")
                return bill

        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.seconds / 3600 * bike_h_price*numOfVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.seconds / \
                        (3600 * 24) * bike_d_price*numOfVehicle
                if (4 <= numOfVehicle):
                    print("%20 indirim kazandınız.")
                    bill *= 0.8

                print(f"Fiyat: ${bill}")
                return bill
            
            else:
                print("Araç kiralama işlemi yapılamadı.")
                return None
            
#---------------------------------------------------------------
class CarRent(VehicleRent):
    global discount_rate 
    discount_rate = 15

    def __init__(self, stock):
        super().__init__(stock)

    def discount(self, b):
        """
            Discount
        """ 
        bill = b - (b * discount_rate) / 100
        return bill

#---------------------------------------------------------------
class BikeRent(VehicleRent):
    def __init__(self, stock):
        super().__init__(stock)
        pass


#---------------------------------------------------------------
class Customer:
    def __init__(self):
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self, brand):
        """
            Request vehicle
        """
        if brand == "bike":
            bikes = input("Kaç adet bisiklet kiralamak istersiniz? ")
            try:
                bikes = int(bikes)
            except ValueError:
                print("Lütfen sayısal değerler giriniz.")
                return -1

            if bikes < 1:
                print("Kiralanacak araç sayısı 0 dan büyük olmalı")
            else:
                self.bikes = bikes

            return self.bikes

        elif brand == "car":
            cars = input("Kaç adet araba kiralamak istersiniz? ")
            try:
                cars = int(cars)
            except ValueError:
                print("Lütfen sayısal değerler giriniz.")
                return -1

            if cars < 1:
                print("Kiralanacak araç sayısı 0 dan büyük olmalı")
            else:
                self.cars = cars

            return self.cars
        else:
            print("Araç kiralama için istek hatası oluştu.")

    def returnVehicle(self, brand):
        """
            Return bikes or cars
            \n brand == 'bike' or 'car'
        """
        if brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0, 0, 0

        elif brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return 0,0,0

        else:
            print("Araç tipi yanlış girildi.")
