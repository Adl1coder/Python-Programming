# import os

import turtle
import random
from time import sleep

# Yıldız çizimi için turtle nesnesi oluşturulur.
star = turtle.Turtle()

# Yıldızın kullanacağı renkleri içeren bir liste oluşturulur.
colours = ["black", "yellow", "blue", "purple"]

# Yıldızın kalemi genişliği belirlenir.
star.width(3.5)

# Yıldızın çizimine başlamadan önce kalemi kaldırır (penup).
star.penup()

# Yıldızın başlangıç pozisyonuna gitmek için ileri doğru 20 birim hareket eder.
star.forward(20)

# Yıldız deseninin çizildiği döngüye girilir.
for i in range(35):
    # Yıldızın rengi rastgele bir renk seçer.
    star.color(random.choice(colours))

    # Yıldızın bir sonraki çizgi uzunluğunu artırarak yıldızı çizer.
    star.forward(i * 10)
    star.right(144)

# Yıldızın rengi gri yapılır.
star.color('gray')

# mesaj ekrana yazdırılır.
message2 = "\t\t\t\t\t Güzel mi?   Teşekkür ederim :) "
star.write(message2, font=("Arial", 13, "normal"))
print(message2)

# 3 saniye beklenir.
sleep(3)

# Yıldızın üzerini temizler ve "Bekle..." mesajı ekrana yazdırılır.
star.clear()
message = "\t\t\t\t\t\t\t\t Bekle..."
star.write(message, font=("Arial", 30, "italic"))
print(message)

# 3 saniye beklenir.
sleep(3)

# Yıldızın başlangıç pozisyonuna dönmesi için ev işareti çizer.
star.clear()
star.home()
star.penup()
star.forward(20)
star.pendown()

# Yıldız deseninin farklı bir renkte tekrar çizilmesi.
for i in range(35):
    star.color(random.choice(colours))
    star.forward(i * 10)
    star.right(144)

# 5 saniye beklenir.
sleep(5)

# Yıldızın üzerini temizler ve "Thanks for watching!" mesajı ekrana yazdırılır.
star.clear()
star.color('blue')
message = "\t\t\t\t\t\t\t İzlemene sevindim!"
star.write(message, font=("Arial", 20, "normal"))
print(message)


turtle.done()
