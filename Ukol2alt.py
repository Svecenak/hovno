def main():
    list_souboru = ["diabeticka Noha.jpg", "dekubit_1.jpeg", "pooperacni rana 2.pdf", "ZLOMENINA.JPg", "pooperacni rana 1.jpg ", "dekuBit_2.pdf", " defekt DK.pdf", "dekubit 99.png"]
    while True:
        if input("Chceš něco přidat? (y/n)\n").strip().lower() != "y":
            break
        pridavacka(list_souboru)
        
    
    upraveny_list_souboru = []
    for soubor in list_souboru:
        upraveny_list_souboru.append(snejk(soubor))
    seznam_obrazku = []
    for pic in upraveny_list_souboru:
        if pic.endswith("jpg") or pic.endswith("jpeg") or pic.endswith("png"):
           seznam_obrazku.append(pic) 
    
    seznam_obrazku.sort()
    
    print(f"Posledním obrázkem seznamu je {seznam_obrazku[-1]}")


def snejk(slovo):
    return slovo.strip().lower().replace(" ","_")
    
def pridavacka(list):
    list.append(input("Vepiš plzky jméno souboru:\n"))
        
if __name__ == "__main__":
    main()