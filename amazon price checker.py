try:
    import requests
    from bs4 import BeautifulSoup #to parse the data and get individual items from the data
    import smtplib
    import time

    URL='https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_2?keywords=sony+a7&qid=1565236633&s=gateway&sr=8-2'
    headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


    class price:
        
            
        
        def check_price(self,price):
            

            page=requests.get(URL,headers=headers) #return all the data from the website

            soup=BeautifulSoup(page.content,'html.parser')#to actually take the individual elements (html-parser will parse the data)
            #print(soup.prettify()) to print the data from wabpage
            title=soup.find(id="productTitle").get_text()  #give the data with id of product id
            price=soup.find(id="priceblock_ourprice").get_text() #give the price og the item in string
            price=price.replace(',','')
            converted_price=float(price[1:10]) #converting the string to float

            if(converted_price==price):
                send_mail()

            print(title.strip())  #print title of the product
            print(converted_price)

        def send_mail(self,time):
            server=smtplib.SMTP('smtp.gmail.com',587)#gmail SMTP and port no
            server.ehlo() #command ssend by a email server while connecting to another email server\
            server.starttls() #to encrypt the session
            server.ehlo()

            server.login('kaushikankit484@gmail.com','atxhswxojopnxlwq')

            subject="AMAZON PRICE ALERT! price has fallen"
            body="check the link  https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_2?keywords=sony+a7&qid=1565236633&s=gateway&sr=8-2"
            msg=f"subject:{subject}\n\n{body}"

            server.sendmail(
                'kaushikankit484@gmail.com' ,#from
                'ankit.kaushik066@gmail.com' ,#to
                msg #final msg
            )
            print("MAIL HAS BEEN SENT")
            server.quit()

            while(True):
                check_price()
                time.sleep(time)
    
    c=price()
    p=int(input("Enter the price you want to check against"))
    t=int(input("Enter the time you want to check in(in seconds)"))
    
    c.check_price(p)
    c.send_mail(t)
            
except Exception as e:
    print(e)

