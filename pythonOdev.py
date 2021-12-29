import re
import hashlib

class DilKontrol():
    
    def __init__(self):
        cumleAdedi = 0
        kelimeAdedi =0
        sesliHarfAdedi =0
        
    
    def cumleSayisi(metin):
        listem = ["Yrd.", "Prof.", "Alm.","vb.","Alb.","Yrd. Doç.", "Cad.","Sok.","sf.","İng.","Ar.","Md."]

        cumleler = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![0-9]\.)(?<=\.|\?|\:|\!)\s',metin)
        cumleAdedi = len(cumleler)
        

        for i in listem:
            if any(i in s for s in cumleler):
                cumleAdedi=cumleAdedi-1
                break
        
        return cumleAdedi
    
    def kelimeSayisi(metin):
        if len(metin) == 0:
            return 0
        else:
            listem = metin.split()
            kelimeAdedi = len(listem)
            return kelimeAdedi
         
    def sesliHarfSayisi(metin):
        sesliHarfler = "aeiöüuoıAEİÖÜOU"
        liste = [each for each in metin if each in sesliHarfler]
        SesliHarfAdedi = len(liste)
        return SesliHarfAdedi
    
    def buyukUnluUyumu(metin):
        kalin_unluler = list("aıouAIOU")  
        ince_unluler = list("eiöüEİÖÜ") 
        liste = metin.split()
        uyumlu = 0
        uyumsuz =0
        
        for i in liste:
            if (sum(i.count(kalin) for kalin in kalin_unluler)) != 0 and (sum(i.count(ince) for ince in ince_unluler)) != 0:  
                 uyumsuz = uyumsuz + 1
            else:
                 uyumlu = uyumlu + 1 
               
                
        return [uyumlu,uyumsuz] 
    
class sifrelemeYontemleri():
    def __init__(self):
        pass
    
    def md5(input):
        sifreliMetin = hashlib.md5(input.encode())
        return sifreliMetin.hexdigest()
    
    def sha256(input):
        sifreliMetin = hashlib.sha256(input.encode())
        return sifreliMetin.hexdigest()
    
    
    def sha1(input):
        sifreliMetin = hashlib.sha1(input.encode())
        return sifreliMetin.hexdigest()
    
    def sha224(input):
        sifreliMetin = hashlib.sha224(input.encode())
        return sifreliMetin.hexdigest()
    
    
            

class Help():
    def __init__(self):
        '''help sınıfı kullanılır durumda.'''
           
    def sha224(self):
        '''input olarak alınan ifade sha224 ile hashlenir, geriye hexadecimal değer döner.'''
    
    def sha1(input):
        '''input olarak alınan ifade sha1 ile hashlenir, geriye hexadecimal değer döner.'''
        
    def sha256(input):
        '''input olarak alınan ifade sha256 ile hashlenir, geriye hexadecimal değer döner.'''
    def md5(input):
        '''input olarak alınan ifade md5 ile hashlenir, geriye hexadecimal değer döner.'''
    def cumleSayisi(metin):
        '''paramtere olarak string ifade alır. geriye string içerisindeki cümle adedini döner. Cümle yoksa 0 değerini döner.'''
    def kelimeSayisi(metin):
        '''paramtere olarak string ifae alır. geriye string içerisindeki kelime adedini döner. Kelimye yoksa 0 değerini döner.'''  
    def sesliHarfSayisi(metin):
        '''paramtere olarak string ifae alır. geriye string içerisindeki sesli harf adedini döner.'''   
    def buyukUnluUyumu(metin):
        '''paramtere olarak string ifade alır. geriye string içerisindeki kelimelerin kaç tanesinin büyük
            ünlü uyumuna uyan ve uymayan adetleri liste ile döner. Listenin 0. elemanı uyanı 1. elemanı uymayanı
            temsil eder.'''