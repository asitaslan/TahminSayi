import random

sayi = random.randint(1,100)
hak = 5

while hak > 0:
    hak -= 1
    tahmin = int(input("tahmininiz :"))
    if(tahmin == sayi):
        print('Tebrikler Sayiyi Bildiniz. Puaniniz :', (hak+1)*20)
        break
    elif(tahmin < sayi):
        print("Yukari")

    else:
      print("Asagi")

    if hak == 0:
        print(f'Hakkiniz Bitmistir. Tutulan sayi: {sayi}')


