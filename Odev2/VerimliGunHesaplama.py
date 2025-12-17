#verimli gün kontorlü

#uyku süresini kontrol eden bir fonksiyon yazıyoruz
def uyku_suresi(uyku):
    if uyku < 6:
        #eğer uyku süresi 6 dan az ise yetersiz
        return "yetersiz uyku"
    elif uyku <= 8:
        #6 ile 8 saat arası ise normal
        return "normal uyku"
    else:
        #8 den fazla ise fazla uyku
        return "fazla uyku"
    
#ders çalışma süresini kontrol eden bir fonksiyon yazıyoruz
def ders_suresi(ders):
    if ders < 6:
        #eğer uyku süresi 6 dan az ise normal
        return "normal çalışma"
    else:
        #6 dan fazla ise fazla çalışma
        return "fazla çalışma"
    
#kullanıcı ile etkileşim kısmı
#eğer kullanıcı hata yaparsa sürekli tekrar başa gelmesini istiyoruz
while True:
    #kullanıcıdan günlük uyku, ders çalışma ve serbest zaman sürelerini alıyoruz
    uyku = input("Günlük uyku sürenizi giriniz: ").strip()
    ders = input("Günlük ders çalışma sürenizi giriniz: ").strip()
    serbest = input("Günlük serbest zaman sürenizi giriniz: ").strip()

    #girilen verinin sayı olup olmadığına bakıyoruz
    if not uyku.isdigit() or not ders.isdigit() or not serbest.isdigit():
        print("Lütfen geçerli bir sayı giriniz.")
        continue
    
    #girilen sürenin toplam 24 saat olup olmadığına bakıyoruz
    if int(uyku) + int(ders) + int(serbest) != 24:
        print("Toplam süre 24 saat olmalıdır. Lütfen tekrar deneyin.")
        continue

    #girilen sürenin negatif olup olmadığına bakıyoruz
    if int(uyku) < 0 or int(ders) < 0 or int(serbest) < 0:
        print("Süreler negatif olamaz. Lütfen tekrar deneyin.")
        continue
        
    #eğer tüm kontrolleri geçtiyse şimdi değerlendirme yapıyoruz
    uyku_durum = uyku_suresi(int(uyku))
    ders_durum = ders_suresi(int(ders))
    print(f"Uyku durumu: {uyku_durum}")
    print(f"Ders çalışma durumu: {ders_durum}")

    #Günün verimli geçip geçmediğine bakıyoruz
    if uyku_durum == "yetersiz uyku" and ders_durum == "fazla çalışma":
        print("Bugün verimsiz bir gün geçirmişsiniz")
    else:
        print("Gününüz verimli şekilde geçmiş")
    #programı sonlandırmak için kullanıcıya soruyoruz
    devam = input("Başka bir değerlendirme yapmak ister misiniz? (e/h): ").strip().lower()
    if devam != 'e':
        print("Programdan çıkılıyor...")
        break
