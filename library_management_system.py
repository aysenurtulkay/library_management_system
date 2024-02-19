class Library:
    def __init__():
        with open("books.txt","a+") as file:
            pass 

    def list_books():
        
        with open("books.txt","a+") as file:
            pass 

        with open("books.txt","r") as file:
            file_contents=file.readlines()
            if len(file_contents)==0:
                print("Gösterilecek kitap bulunmuyor.Kitap eklemek için menüden 2 numarayı seçin.")
            else:
                for line in file_contents:
                    degisken=line.split(",")
                    print("Kitap adı:"+degisken[0]+" Yazar:"+degisken[1])

    def add_book(book_title,book_author,first_release_year,number_of_pages):

        with open("books.txt","a+") as file:
            pass 

        with open("books.txt","r") as file:
            file_contents=file.readlines()

        with open("books.txt","a+") as file:
            control=0

            for line in file_contents:
                degisken=line.split(",")
                if degisken[0]==book_title and degisken[1]==book_author:
                    control=1

            if control==1:
                print("Bu kitap kütüphanede zaten bulunuyor.Kontrol edip tekrar deneyiniz.")
            else:
                file.write(book_title.strip()+","+book_author.strip()+","+str(first_release_year)+","+str(number_of_pages)+"\n")
                print("Kitap başarılı bir şekilde eklendi.")

    def remove_book(book_title,book_author):

        with open("books.txt","a+") as file:
            pass 
        
        control=0
        with open("books.txt","r") as file:
            file_contents=file.readlines()

        with open("books.txt","w") as file:
            for line in file_contents:
                degisken=line.split(",")
                if degisken[0]==book_title and degisken[1]==book_author:
                    control=1
                else:
                    file.write(line)

        if control==1:
            print(book_author+" isimli yazarın "+"'"+book_title.strip()+"'"+" isimli kitabı silindi.")
        else:
            print("Girilen bilgilerde bir kitap bulunamadı.Lütfen kontrol edip tekrar deneyiniz.")

while True:
    choice=input("*** MENU***\n1) Kitapları göster\n2) Kitap ekle\n3) Kitap sil\n4) Çıkış(q)\n")
    
    if choice=="q":

        break

    elif choice=="1":

        Library.list_books()

    elif choice=="2":

        degisken=""
        book_title=input("Kitap adı=")
        book_author=input("Yazar=")

        control=0
        while control==0:
            control=1
            try:
                first_release_year=int(input("Yayınlanma tarihi="))
            except:
                control=0
                print("Bir tarih girmeniz gerekiyor!")
                
        control=0
        while control==0:
            control=1
            try:
                number_of_pages=int(input("Sayfa sayısı="))
            except:
                control=0
                print("Sayfa sayısı girmeniz gerekiyor!")
        
        Library.add_book(book_title,book_author,first_release_year,number_of_pages)

    elif choice=="3":
    #aynı isimde fakat farklı kişiler tarafından yazılan kitaplar olduğunu varsaydım. 
        book_title=input("Silmek istediğiniz kitabın adı=")
        book_author=input("Silmek istediğiniz kitabın yazarı=")

        Library.remove_book(book_title,book_author)

    else:
        print("Hatalı giriş yaptınız,lütfen tekrar deneyiniz.")

        

