import random 
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunlugu=int(input("Lütfen yapmak istediğiniz şifrenin uzunluğunu yazınız."))
sifre=""
for i in range(sifre_uzunlugu):
    sifre += random.choice(karakterler)
print(sifre)
