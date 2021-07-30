users={'ahmet':{'name':'ahmet','password':'istinye123','sepet':{}},
'meryem':{'name':'meryem','password':'4444','sepet':{}}}
Envanter = {'kuskonmaz': [10,5], 'brokoli': [15,6], 'havuc': [18,7], 'elmalar': [20,5], 'muz':
[10,8], 'meyve': [30,3], 'yumurta': [50,2], 'karısık meyve suyu': [0,18], 'balık cubukları':
[25,12], 'dondurma': [32,6], 'elma suyu': [40,7], 'portakal suyu': [30,8], 'uzum suyu':
[10,9]}
urunler=[]
import datetime

def giris():
    print("**** İstinye Online Market'e hoşgeldiniz ****")
    print("Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:")
    global isim
    global sifre
    isim = input('Kullanıcı adı: ')
    sifre = input("Şifre: ")

def karsilama(users,isim,sifre):#kullanıcı kimliği kontrol
    while isim not in users:
        print('Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!')
        isim=input('Kullanıcı adı: ')
        sifre=input("Şifre: ")
    while users[isim]['password']!=sifre:
        print('Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!')
        isim=input('Kullanıcı adı: ')
        sifre=input("Şifre: ")
    print("Başarıyla giriş yapıldı!")
    print('Hoşgeldin',isim,'! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.')
    menu()
def menu():#diğer tüm seçeneklere menüden ulaşıldığından menünün içindeler
    print('Lütfen aşağıdaki hizmetlerden birini seçin:\n1. Ürün ara\n2. Sepete git\n3. Satın al\n4. Oturum Kapat\n5. Çıkış yap\n')
    secim=input('Seçiminiz?: ')
    while secim not in ['1','2','3','4','5']:
        secim=input('Geçerli bir değer giriniz: ')
    if secim=='1':
        print('seçiminiz: 1', urunAra(Envanter,isim))
    elif secim=='2':
        print('seçiminiz: 2', sepeteGit(users,isim))
    elif secim=='3':
        print('seçiminiz: 3', satinAl(users,isim,Envanter))
    elif secim=='4':
        print('seçiminiz: 4')
        print('Oturumunuz kapatılıyor... ')#hesap değiştirmek için başka bir isim inputu koyduğumda hata veriyordu iki hesaptan da girebilelim diye böyle bir yol yaptım
        giris()
        karsilama(users,isim,sifre)
    elif secim=='5':
        print('çıkış yapılıyor...')
        exit()
    else:
        ValueError
def urunAra(Envanter,isim):#istenen kelime envanterde eşleşirse urunler listesinin içine yazdırılıyor fiyatlarıyla beraber
    kelime=input('Ne arıyorsunuz?: ')
    AnahtarKelimeler=list(Envanter.keys())
    sira=1
    for oge in AnahtarKelimeler:
        if kelime in oge.split():
            urunler.append(oge)
    print(len(urunler),' tane benzer ürün bulundu:')
    for urun in urunler:
        print(sira,'. ',urunler[sira-1],Envanter[urun][1],'$')
        sira+=1
    sira=1
    while len(urunler)==0:#hiçbir eşleşme olmazsa soruyu tekrarlıyor
        kelime=input('Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin):')
        for oge in AnahtarKelimeler:
            if kelime in oge.split():
                urunler.append(oge)
        print(len(urunler),' tane benzer ürün bulundu:')
        for urun in urunler:
            print(sira,'. ',urun ,Envanter[urun][1],'$')
            sira+=1
    istek=input('Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin): ')
    while istek.isdigit()==False or int(istek) not in range(len(urunler)):
        #istenilen ürün için alınan girdi sayı değilse veya çıkan listenin dışındaysa soruyu tekrarlıyor
        istek=input('hatalı bir numara girdiniz lütfen yeniden deneyin (Ana menü için 0 girin): ')
    if istek=='0':
        menu()
    else:#istenilen ürün seçilince istenen miktar soruluyor
        print(urunler[int(istek)-1],' ekleniyor...')
        miktar=input('Almak istediğiniz Miktarı Girin (Ana menü için 0 girin): ')
        while miktar.isdigit()==False:#sayı olmayan değerler için soru tekrarlanır
            miktar=input('Geçerli bir Miktar Girin (Ana menü için 0 girin): ')
        if miktar=='0':
            menu()
        while int(miktar.lstrip('-'))>Envanter[urunler[int(istek)-1]][0]:#negatif bir sayı girilirse negatif kısmı almaz sayıyı alır
            #stoktaki miktar yeterli değilse tekrarlıyor
            if Envanter[urunler[int(istek)-1]][0]==0:
                print("ürünümüz stokta kalmamıştır! Ana menüye dönülüyor...")
                urunler.clear()
                menu()
            miktar=input("Stoktaki miktardan fazla bir değer girdiniz.")
            print(Envanter[urunler[int(istek)-1]][0],"Adet ürünümüz kalmıştır.\nTekrar bir miktar giriniz (Ana menü için sıfıra(0) basın): ")
            if miktar=='0':
                menu()    
        #stoktaki miktarda ya da daha küçük bir değer girildiğinde envanterdeki stok değerleri düzenleniyor ki bir daha ürün arandığında stok miktarından fazla alınamasın
        #Envanter[urunler[int(istek)-1]][0] = Envanter[urunler[int(istek)-1]][0]-int(miktar)#envanterdeki stok güncellenir
        users[isim]['sepet'][(urunler[int(istek)-1])]=[Envanter[urunler[int(istek)-1]][1],int(miktar)*Envanter[urunler[int(istek)-1]][1]]#kullanıcının sepetine ürün eklenir
        #alınan ürünün fiyatı ve ödenecek dict şeklindeki sepetin içinde tutulur içine işlenir
        Envanter[urunler[int(istek)-1]][0]=Envanter[urunler[int(istek)-1]][0]-int(miktar)
        #alınan ürünün kalan stok durumu yazılır sonrasında kontrol için ulaşmamız adına
        print(urunler[int(istek)-1],'Sepetinize eklendi.')
        print('Ana Menüye dönülüyor...')
        urunler.clear()#bir dahaki aramaya eskileri karışmasın diye temizleniyor
        menu()
def sepeteGit(users,isim):
    i=1
    sepet=users[isim]['sepet']
    print('sepetiniz şunları içeriyor:\n ')#kullanıcının sepetini listeliyor
    for urun in sepet.values():
        print(i,'.) ',list(sepet.keys())[i-1],'==',urun[0],'$','==',urun[1]/urun[0],'Tanesi',urun[1],'$ ')
        print('————————————')
        i+=1
    toplam=0
    for j in sepet.values():
        toplam += j[1]
    print('Toplam: ',toplam,'$')
    #ürün değişimi için stokta olma durumu ve girilen değer kontrol ediliyor
    secenek=input("Ürün miktar değişimi için 1'e basınız. Ana menüye dönmek için sıfır(0) a basınız: ")
    while secenek.isdigit()==False and secenek not in ['1','0']:
        secenek=input('Lütfen geçerli bir değer giriniz (Ana menüye dönmek için sıfır(0) a basınız): ')
    if secenek=='0':
        menu()
    else:
        if len(sepet)==0:
            print("sepetiniz boş olduğundan bir ürünü değiştiremiyorsunuz!")
            print("menüye dönülüyor...")
            menu()
        degisim=input('Lütfen miktarını değiştireceğiniz öğeyi seçin: ')
        while degisim.isdigit()==False or int(degisim)<0 or int(degisim) not in range(len(users[isim]['sepet'])+1):
            degisim=input('lütfen geçerli bir değer giriniz: ')
        if degisim=='0':
            menu()
        degisim=int(degisim)
        degisecek_urunun_adi=list(sepet.keys())[degisim-1]
        yeniMiktar=input('Lütfen yeni miktarı yazın: ')
        eski_miktar = list(sepet.values())[degisim-1][1]/list(sepet.values())[degisim-1][0]
        while yeniMiktar.isdigit()== False or int(yeniMiktar)<0 or int(yeniMiktar)>Envanter[degisecek_urunun_adi][0] + eski_miktar:
            yeniMiktar=input('Lütfen geçerli bir yeni miktar giriniz: ')
            #değişim sonrası stoklar güncelleniyor
        Envanter[list(sepet.keys())[degisim-1]][0] += eski_miktar
        Envanter[list(sepet.keys())[degisim-1]][0] -= int(yeniMiktar)
        sepet[degisecek_urunun_adi][1]=int(yeniMiktar)*sepet[degisecek_urunun_adi][0]#fiyat çarpı miktar olarak tutulan değer
        #miktar değiştiği için güncelleniyor
    sepeteGit(users,isim)
        
def satinAl(users,isim,Envanter):
    print('Makbuzunuz işleniyor...')
    print('****** İstinye Online Market ******')
    print('*************************************')
    print('   0850 283 6000   \n   istinye.edu.tr   ')
    print('————————————')
    i=1
    sepet=users[isim]['sepet']
    print('sepetiniz şunları içeriyor:\n ')
    for urun in sepet.values():
        print(i,'.) ',list(sepet.keys())[i-1],'==',urun[0],'$','==',urun[1]/urun[0],'Tane',urun[1],'$ miktarında')
        print('————————————')
        i+=1
    toplam=0
    for urun in sepet.values():
        toplam += urun[1]
    print('Toplam: ',toplam,'$')
    print('————————————')
    x= datetime.datetime.now()
    print(x.strftime("%x"),x.strftime("%X"))
    print('————————————')
    print("Online Market’imizi kullandığınız için teşekkür ederiz!")
    dumy2=input()
    sepet.clear()
    menu()
giris()
karsilama(users,isim,sifre)