
import pythonOdev


metin = """Python ödevi test metni. Ünlemle biten cümle! Soru işareti ile biten cümle?
        İçerisinde tarih bulunan 29.12.2021 cümle. içerisinde saat barındıran 15.13 cümle.
        İçerisinde iki nokta üst üste barındıran cümle:"""
        
sesliHarfMetin= "İçerisinde"

value = "Volkan ŞİMŞEK"

print(pythonOdev.DilKontrol.cumleSayisi(metin)) 
print(pythonOdev.DilKontrol.kelimeSayisi(metin)) #cümle içerisindeki tarih ve saatlerin fonksiyon içerisinde çıkarılması gerekiyordu.
print(pythonOdev.DilKontrol.buyukUnluUyumu(metin))
print(pythonOdev.DilKontrol.sesliHarfSayisi(sesliHarfMetin))

print(pythonOdev.sifrelemeYontemleri.sha256(value))
print(pythonOdev.sifrelemeYontemleri.md5(value))
print(pythonOdev.sifrelemeYontemleri.sha1(value))
print(pythonOdev.sifrelemeYontemleri.sha224(value))

help(pythonOdev.Help())
