
def harf(char):
    
    return char.isalpha()

def küçükharf(metin):
    
    return metin.lower()

def frekanshesabı(metin):
    
    frekans = {}
    maxkarakter = len(metin)

    for char in metin:
        if harf(char):  
            char = küçükharf(char)  
            if char in frekans:
                frekans[char] += 1
            else:
                frekans[char] = 1

    results = {}
    for char, sayac in frekans.items():
        frekansoranı = (sayac / maxkarakter) * 100
        results[char] = frekansoranı

    return results

def frekansyazdır(sonuçlar):
    
    print("Kucuk harf halinde metin ve frekanslari:")
    
    for char, frequency in sonuçlar.items():
        print(f"'{char}' karakteri metinde %{frequency:.2f} siklikla geciyor.")


def main():
    
    metin = input("Lütfen bir metin girin: ")
    metin = küçükharf(metin)
    sonuc = frekanshesabı(metin)
    frekansyazdır(sonuc)
    

if __name__ == "__main__":
    main()