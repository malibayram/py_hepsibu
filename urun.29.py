import urllib.request
import re
import io

f = open("altkategori2/altkategori2_30.txt", "r")
lines = f.read().split('\n')

urunler = set()
seen = set()
sayi = 0
altsayi = 0

for ln in lines:
    url = 'https://www.hepsiburada.com' + ln
    request = urllib.request.Request(url)
    print(url)

    sayi = sayi + 1
    print(sayi)    
    try:
        response = urllib.request.urlopen(request)
    except:
        print("something wrong")

    htmlBytes = response.read()
    htmlStr = htmlBytes.decode("utf8")

    aranan = '<a href="(.*?)-c-(.*?)sayfa=(.*?)" class="page-(.*?)">(.*?)</a>'
    sayfalar = re.findall(aranan, htmlStr)

    if len(sayfalar) > 0:
        sayfa_sayisi = int(sayfalar[-1][2])

        print('sayfa sayisi: ' + str(sayfa_sayisi))
        sayfa = 1        

        for x in range(sayfa_sayisi):
            url2 = url + '?sayfa=' + str(x+1)
            print(url2)
            request2 = urllib.request.Request(url2)
            try:
                response2 = urllib.request.urlopen(request2)
            except:
                print("something wrong")

            htmlBytes2 = response2.read()
            htmlStr2 = htmlBytes2.decode("utf8")

            aranan2 = '"(.*?)" data-sku="(.*?)"'
            sonuc2 = re.findall(aranan2, htmlStr2)

            for word in sonuc2:
                if word[0] not in urunler:
                    urunler.add(word[0])
                    print(word[0])

            altsayi = altsayi + 1
            print(altsayi)
            sayfa = sayfa + 1
            print('sayfa: ' + str(sayfa))
    else:
        url3 = url
        print(url3)
        request3 = urllib.request.Request(url3)
        try:
            response3 = urllib.request.urlopen(request3)
        except:
            print("something wrong")

        htmlBytes3 = response3.read()
        htmlStr3 = htmlBytes3.decode("utf8")

        aranan3 = '"(.*?)" data-sku="(.*?)"'
        sonuc3 = re.findall(aranan3, htmlStr3)

        for word in sonuc3:
            if word[0] not in urunler:
                urunler.add(word[0])
                print(word[0])

        altsayi = altsayi + 1
        print(altsayi)


with open("output_30.txt", "w") as txt_file:
    for line in urunler:
        txt_file.write(line + "\n")