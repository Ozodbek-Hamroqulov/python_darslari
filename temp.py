# # -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """

# #----------------------------------------------->//
# print("Hello World!")
# print('Assalom alaykum')
# print(2+4*2)
# print(19/5)
# print(2**4)

# # ------------------------------------------->
# print("Assalom alaykum")
# print("Hayrli tong!")
# print('Hayrli tong!')
# print('Men "Dell" markasidagi noutbuk sotib oldim')
# print("""Odami ersang, demagil odami,
# Oniki, yo'q xalq g'amidin g'ami""")
# print("Odami ersang, demagil odami,\nOniki, yo'q xalq g'amidin g'ami")
# print('Odami ersang, demagil odami, \nOniki, yo\'q xalq g\'amidin g\'ami')
# print(2+4*2)
# print(19/5)
# print(20//5)
# print(16//4)
# print(10//3)
# print(2**4)
# print("To'qqizning kvadrati", 9**2, "ga teng")
# print('3x3=',3*3)
# print(2*5*3.14159)
# print("Assalom alaykum!") # Bu matn konsolda chiqadi
# #Keyingi qator esa bajarilmaydi
# #print("Mening ismim Anvar")

# #--------------------------------------------->>
# ism = "Abdulloh"
# yosh = 25
# print(ism)
# print(yosh)

# ism = "Abdulloh"
# print(ism)
# ism="Muhammad"
# print(ism)

# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

# #----------------------------------------------------->>
# shahar = "Қўқон"
# viloyat = 'Фарғона'

# matn = "Men yangi 📱 oldim"
# print(matn)

# ism = 'Ahmad'
# print("Mening ismim " + ism)

# ism = 'Ahad'
# familiya = 'Qayum'
# print(ism + familiya)

# ism = 'Ahad'
# familiya = 'Qayum'
# print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

# ism = "Ahad"
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# ism = "James"
# familiya = 'Bond'
# print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')

# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())

# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.lower())

# ism_sharif = 'james bond'
# print(ism_sharif.title())

# ism_sharif = 'james bond'
# print(ism_sharif.capitalize())

# print('james bond'.upper())

# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# =============================================================================
# sonlar
# =============================================================================

# a = 20  # Sonlar musbat yoko
# b = -30 # manfiy bo'lishi mumkin
# c = a + b
# print(c)

# # Kvadratning yuzini hisoblaymiz
# kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
# kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
# print(kvdrt_yuzi)

# pi = 3.14159 # o'nlik son (float)
# radius = 10  # butun son (integer)
# diametr = 2*radius
# print("Aylana uzunligi ", pi*diametr, " ga teng.")

# a = -20
# b = 40
# c = b/a
# print(c) # natija o'nlik son bo'ladi

# a = 2
# b = 3.0
# # Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
# print(a+b) 
# print(a*b)
# print(a**b)
# print(2*(a+b))

# aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
# print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

# PI = 3.14159
# raduis = 21.2

# x, y, z = 10, -7.25, -30

# ism = 'Jobir'
# yosh = 36
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)

# ism = 'Jobir'
# yosh = 36
# print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
# print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz

# ism = 'Jobir'
# yosh = 36
# print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
# print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz


#1.1 foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil = input("Tug'ilgan yilingizni kiriting: ")
# #1.2 t_yil o'zgaruvchini int ga aylantiramiz
# t_yil = int(t_yil)
# #2 foydalanuvchi yoshini xisoblaymiz
# yosh = 2022 - t_yil # 
# #3 foydalanuvchi yoshini konsolga chiqaramiz
# print("Siz " + str(yosh) + " yoshda ekansiz")


# #============================================================
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)

# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)

# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# #======================================================================
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)

# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# sonlar = list(range(0,10)) # 
# print(sonlar)

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# max_qiymat = max(toq_sonlar)
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)
# print(max_qiymat)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars) 
# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# tomonlar = (20, 30, 55.2)
# print(tomonlar)    

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])



# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)

# #=============================================================================
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print("Xayir,", mehmon)

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

# print(sonlar)
# print(sonlar_kvadrati)

# #dostlar = [] # bo'sh ro'yxat
# #print("5 ta eng yaqin do'stingiz kim?")
# #for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
# #    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# #print(dostlar)

# #=======================================================================
avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
     print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

ism = 'Ali'
ism.lower() == 'ali'

ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")

javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")
    
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')


login = input("Yangi login tanlang:")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart!")

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 202-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")


yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")



x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")
#=================================================================================

yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')


yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
else:
    price = 10000
    
print(f"Sizga kirish {price} so'm")


yosh = int(input('Yoshingiz nechida? '))
if yosh<=4: # yosh bolalarga bepul
    price = 0
elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
    price = 5000
elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
    price = 10000
else: # qariyalarga esa 8000 so'm
    price = 8000
print(f"Sizga kirish {price} so'm")


kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')


kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz!")


kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
    print("Cho'milgani ketdik!")
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
    print("Uyda dam olamiz!")



narh = 15000 # mijoz 15000 so'mga taom oldi.
choy = True # mijoz choy ham oldi
salat = False # mijoz salat olmadi

if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
elif choy or salat: # agar choy yoki salat olgan bo'lsa
    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz



narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi.')
else:
    print('Afsuski bizda bunday ovqat yo\'q')


menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input('Nima ovqat yeysiz?>>>')
if ovqat.lower() not in menu:
    print('Afsuski bizda bunday ovqat yo\'q')
else:
    print('Buyurtma qabul qilindi.')


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")








 
# =============================================================================




























