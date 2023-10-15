import turtle
from math import *

kalem = turtle.Turtle()

# Dikdörtgen çizimi fonksiyonu
def dikdortgen(kenar_uzunlugu):
    for i in range(2):
        kalem.forward(kenar_uzunlugu * 1.5)
        kalem.left(90)
        kalem.forward(kenar_uzunlugu)
        kalem.left(90)

# Alanı boyama fonksiyonu
def alan_boyama(x, y, renk):
    kalem.penup()
    kalem.goto(x, y)
    kalem.pendown()
    kalem.color(renk)
    kalem.begin_fill()

# Ay çizimi fonksiyonu
def ay_ciz(radyan):
    kalem.circle(radyan)
    kalem.end_fill()

# Yıldız çizimi fonksiyonu
def yildiz_ciz(x, y, uzunluk):
    alan_boyama(x, y, "white")
    kalem.left(36)
    kalem.forward(uzunluk / 2)
    for i in range(6):
        if i == 0:
            aci = 160
        else:
            aci = 144
        if i == 5:
            aci = 189
            kalem.left(aci)
            kalem.penup()
            kalem.end_fill()
            return
        kalem.left(aci)
        kalem.forward(uzunluk)

# Türk bayrağı çizimi fonksiyonu
def bayrak_ciz(x, y, g):
    alan_boyama(x, y, "red")
    dikdortgen(g)
    kalem.end_fill()

    # Bayrak direği ve ay ve yıldız çizimi
    bayrak_diregi = g / 2  # (x ekseni)
    buyuk_dairenin_yaricapi = g / 4  # büyük dairenin yarıçapı (y ekseni)
    iki_daire_arasi_mesafe = g / 16  # büyük daire ve küçük dairenin merkezleri arasındaki mesafe
    kucuk_dairenin_yaricapi = g / 5  # küçük dairenin yarıçapı
    iki_daire_arasi_mesafe = g / 3  # yıldızların merkezi ve küçük dairenin merkezi arasındaki mesafe
    yildiz_yaricapi = g / 8  # yıldızların yarıçapı

    # Ayın çizimi
    alan_boyama(g / 2 + x, g / 4 + y, "white")
    ay_ciz(g / 4)
    alan_boyama(g / 2 + g / 16 + x, g / 2 - g / 5 + y, "red")
    ay_ciz(g / 5)

    # Yıldız çizimi
    yildiz_x = (bayrak_diregi + iki_daire_arasi_mesafe + iki_daire_arasi_mesafe - yildiz_yaricapi + yildiz_yaricapi)
    yildiz_y = g / 2
    yildiz_uzunlugu = (yildiz_yaricapi + (cos(radians(36)) * yildiz_yaricapi) / cos(radians(18)))
    yildiz_ciz(yildiz_x + x, yildiz_y + y, yildiz_uzunlugu)

# Türk bayrağı çizme komutu
bayrak_ciz(0, 0, 100)

# Pencereyi kapatma işlemi
turtle.done()
