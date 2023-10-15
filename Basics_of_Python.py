# Python-Basics

def main():
    # 1. variables and data types


    # (int)
    age = 25

    #  (float)
    price = 19.99

    #  (string)
    name = "John Doe"

    #  (bool)
    is_student = True


    result = 5 + 3
    product = 4 * 7

    is_equal = age == 30
    is_less_than = price < 20

    is_valid = age > 18 and is_student

    if age < 18:
        print("Yaşınız 18'den küçük.")
    elif age == 18:
        print("Yaşınız 18'e eşit.")
    else:
        print("Yaşınız 18'den büyük.")


    fruits = ["elma", "armut", "çilek"]
    for fruit in fruits:
        print(fruit)

    count = 0
    while count < 5:
        print(count)
        count += 1


    def greet(name):
        print(f"Merhaba, {name}!")

    greet("Adile")


    colors = ["kırmızı", "yeşil", "mavi"]

    first_color = colors[0]



    person = {"ad": "John", "yaş": 30, "meslek": "mühendis"}


    name = person["ad"]


if __name__ == '__main__':
    main()
