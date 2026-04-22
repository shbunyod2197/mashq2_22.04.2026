# 1
class libraryBook:
    def __init__(self, title, is_available):
        self.title = title
        self.is_available = is_available

    def borrow(self):
        print(f"Kitob olindi")

    def returnBook(self):
        print(f"Kitob Qaytarildi")


a = libraryBook("Kitob olindi", True)
a.borrow()
a.returnBook()

# 2
class FoodOrder:
    def __init__(self, food, price, is_delivered=False):
        self.food = food
        self.price = price
        self.is_delivered = is_delivered

    def deliver(self):
        self.is_delivered = True
        print("Buyurtma yetkazildi")

    def status(self):
        if self.is_delivered:
            print("Buyurtma yetkazildi")
        else:
            print("Hali yetkazilmadi")


f = FoodOrder("Pizza", 50000)
f.status()
f.deliver()
f.status()


# 3
class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, input_password):
        if input_password == self.password:
            print("Xush kelibsiz")
        else:
            print("Parol xato")


u = UserLogin("ali", "1234")
u.login("1111")
u.login("1234")


# 4
class PhoneBattery:
    def __init__(self, percent):
        self.percent = percent

    def use(self, amount):
        self.percent -= amount
        if self.percent <= 0:
            self.percent = 0
            print("Quvvat tugadi")
        else:
            print(f"Batareya: {self.percent}%")

    def charge(self, amount):
        self.percent += amount
        print(f"Batareya: {self.percent}%")


ph = PhoneBattery(50)
ph.use(10)
ph.use(50)
ph.charge(30)


# 5
class CinemaTicket:
    def __init__(self, movie, price, is_booked=False):
        self.movie = movie
        self.price = price
        self.is_booked = is_booked

    def book(self):
        if self.is_booked:
            print("Allaqachon band")
        else:
            self.is_booked = True
            print("Chipta band qilindi")

    def cancel(self):
        self.is_booked = False
        print("Bron bekor qilindi")


c = CinemaTicket("Avatar", 40000)
c.book()
c.book()
c.cancel()
c.book()
