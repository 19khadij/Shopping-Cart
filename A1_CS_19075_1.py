##Online shopping cart is a virtual shopping trolley, where shoppers can put all of their want-to-buy products in,
##review to make adjustments in quantity, product attributes, etc., and remove it before or during the checkout if
##they change their mind. 

##1. Store and display a product list with price and other relevant information. Use fixed products; there should be
##at least 10 products for the user to choose from.
##2. Allow user to create an account with some basic information like username, password, first and last names,
##address, etc.
##3. Maintain record of all account holders. Current carts and shopping history should also be stored.
##4. When user checks out, the items of the cart are transferred to his/her shopping history. For simplicity payment
##process is omitted.
##5. Products information, account holders list, current cart details and shopping history for each user shall be
##maintained and stored in files.
##6. Each account holder should be able to
## view the list of products and their relevant information from the virtual shopping shelves
## add products to the cart
## remove products from the cart
## view the cart with product names, prices, quantities, total price, etc.
## checkout
## view shopping history

## Organize the application into at least 4 interlinked user-defined classes.
## Your application must exhibit at least 4 of the following object oriented features:
##- Inheritance
##- Association
##- Method overriding
##- Operator overloading
##- Abstract classes
##- Exception handling
## Organize your code in classes, functions/methods and files.
## The code must be easy to read and follow. Provide concise and useful comments generously.
## You may use any built-in library functions or external library/package. 



class Logout:
    def logout(self):
            print('You are now logout!')

class User:
    def login(self):
            print('Choose what you want:)!')
            print('********************************')
            print('Select the option you want')
            print('*********************************')
            print('a.View list for products')
            print('b.Add product to your shopping cart')
            print('c.Remove product from your cart')
            print('d.View your cart')
            print('e.Checkout')
            print('f.View shopping history')
            print('g.Logout')
          
class Product(User):
    def display(self):
        lst=[['CadburryCrunch',230,250,111],['Hob Nob',123,120,112],['Triscuit',45,70,113],
             ['Cream Wheat',67,540,222],['Malt-O-Meal',123,450,223],['Scotts Porage',456,230,224],
             ['Dunkin Donuts',356,345,333],['Betty Crocker',456,780,334],['Mars Mufin',367,235,335],
             ['AngelDelight',120,245,444],['Magnolia',89,170,445],['Selecta',34,115,446]]
        print('S.no\tProducts\t\tStock\tPrice_per_item\tBarcode')
        print('****************************************************************')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('****************************************************************')
        count=1
        for i in lst:
            print(f'{count:3}     {i[0]:15} \t{i[1]:0} \t{i[2]:0} \t\t{i[3]:0}')
            count+=1
    lst=[['CadburryCrunch',230,250,111],['Hob Nob',123,120,112],['Triscuit',45,70,113],
             ['Cream Wheat',67,540,222],['Malt-O-Meal',123,450,223],['Scotts Porage',456,230,224],
             ['Dunkin Donuts',356,345,333],['Betty Crocker',456,780,334],['Mars Mufin',367,235,335],
             ['AngelDelight',120,245,444],['Magnolia',89,170,445],['Selecta',34,115,446]]
    def saveProducts(self,FileName):
        f=open(FileName,'a')
        for i in self.lst:
            f.write(str(i)+'\n')
        f.close
class ShoppingCart(User):
    q_CadburryCrunch=0
    q_HobNob=0
    q_Triscuit=0
    q_CreamWheat=0
    q_MaltOMeal=0
    q_ScottsPorage=0
    q_DunkinDonuts=0
    q_BettyCrocker=0
    q_MarsMufin=0
    q_AngelDelight=0
    q_Magnolia=0
    q_Selecta=0
    p_CadburryCrunch=250
    p_HobNob=120
    p_Triscuit=70
    p_CreamWheat=540
    p_MaltOMeal=450
    p_ScottsPorage=230
    p_DunkinDonuts=345
    p_BettyCrocker=780
    p_MarsMufin=235
    p_AngelDelight=245
    p_Magnolia=170
    p_Selecta=115
    lst4=[['CadburryCrunch',q_CadburryCrunch,p_CadburryCrunch,111],['Hob Nob',q_HobNob,p_HobNob,112],['Triscuit',q_Triscuit,p_Triscuit,113],
             ['Cream Wheat',q_CreamWheat,p_CreamWheat,222],['Malt-O-Meal',q_MaltOMeal,p_MaltOMeal,223],
              ['Scotts Porage',q_ScottsPorage,p_ScottsPorage,224],['Dunkin Donuts',q_DunkinDonuts,p_DunkinDonuts,333],
              ['Betty Crocker',q_BettyCrocker,p_BettyCrocker,334],['Mars Mufin',q_MarsMufin,p_MarsMufin,335],
             ['AngelDelight',q_AngelDelight,p_AngelDelight,444],['Magnolia',q_Magnolia,p_Magnolia,445],['Selecta',q_Selecta,p_Selecta,446]]
    def addProducts(self):
        try:
            x=int(input('Do you want to add CadburryCrunch in your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            x=int(input('Do you want to add CadburryCrunch in your cart enter the quantity, for no 00 press any key:'))
        if 0<x<231:
            self.q_CadburryCrunch+=x
        elif x==00:
            print('ok no problem')
        elif x>230:
            print('Outof stock!')
        else:
            print('Please enter valid key')
        try:
            y=int(input('Do you want to add Hob Nob in your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            y=int(input('Do you want to add Hob Nob in your cart enter the quantity, for no 00 press any key:'))
        if 0<y<124:
            self.q_HobNob+=y
        elif y==00:
            print('ok no problem')
        elif x>123:
            print('Outof stock!')
        else:
            print('Please enter invalid key')
        try:
            z=int(input('Do you want to add  Triscuit in your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            z=int(input('Do you want to add  Triscuit in your cart enter the quantity, for no 00 press any key:'))
        if 0<z<46:
            self.q_Triscuit+=z
        elif z==00:
            print('ok no problem')
        elif z>45:
            print('Outof stock!')
        else:
            print('Please enter invalid key')
        try:
            a=int(input('Do you want to add  Cream Wheat in your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            a=int(input('Do you want to add  Cream Wheat in your cart enter the quantity, for no 00 press any key:'))
        if 0<a<68:
            self.q_CreamWheat+=a
        elif a==00:
            print('ok no problem')
        elif a>67:
            print('Outof stock!')
        else:
            print('Please enter invalid key')
        try:
            b=int(input('Do you want to add  Malt-O-Meal in your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            b=int(input('Do you want to add  Malt-O-Meal in your cart enter the quantity, for no 00 press any key:'))
        if 0<b<124:
            self.q_MaltOMeal+=b
        elif b==00:
            print('ok no problem')
        elif b>123:
            print('Outof stock!')
        else:
            print('Please enter invalid key')
        try:
            c=int(input('Do you want to add  Scotts Porage your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            c=int(input('Do you want to add  Scotts Porage in your cart enter the quantity, for no 00 press any key:'))
        if 0<c<457:
            self.q_ScottsPorage+=c
        elif c==00:
            print('ok no problem')
        elif c>456:
            print('Outof stock!')
        else:
            print('Please enter invalid key')
        try:
            d=int(input('Do you want to add Dunkin Donuts your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            d=int(input('Do you want to add  Dunkin Donuts in your cart enter the quantity, for no 00 press any key:'))
        if 0<d<357:
            self.q_DunkinDonuts+=d
        elif d==00:
            print('ok no problem')
        elif d>356:
            print('Outof stock!')
        else:
            print('Please enter invalid key')

        try:
            e=int(input('Do you want to add Betty Crocker your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            e=int(input('Do you want to add  Betty Crocker in your cart enter the quantity, for no 00 press any key:'))
        if 0<e<457:
           self.q_BettyCrocker+=e
        elif e==00:
            print('ok no problem')
        elif e>456:
            print('Outof stock!')
        else:
            print('Please enter invalid key')


        try:
            f=int(input('Do you want to add Mars Mufin your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            f=int(input('Do you want to add  Mars Mufin in your cart enter the quantity, for no 00 press any key:'))
        if 0<f<368:
           self.q_MarsMufin+=f
        elif f==00:
            print('ok no problem')
        elif f>367:
            print('Outof stock!')
        else:
            print('Please enter invalid key')


        try:
            g=int(input('Do you want to add AngelDelight your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            g=int(input('Do you want to add  AngelDelight in your cart enter the quantity, for no 00 press any key:'))
        if 0<g<121:
           self.q_AngelDelight+=g
        elif g==00:
            print('ok no problem')
        elif g>120:
            print('Outof stock!')
        else:
            print('Please enter invalid key')


        try:
            h=int(input('Do you want to add Magnolia your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            h=int(input('Do you want to add  Magnolia in your cart enter the quantity, for no 00 press any key:'))
        if 0<h<90:
           self.q_Magnolia+=h
        elif h==00:
            print('ok no problem')
        elif h>89:
            print('Outof stock!')
        else:
            print('Please enter invalid key')


        try:
            i=int(input('Do you want to add Selecta your cart enter the quantity, for no 00 press any key:'))
        except:
            print('Enter a valid integer!')
            i=int(input('Do you want to add  Selecta in your cart enter the quantity, for no 00 press any key:'))
        if 0<i<35:
           self.q_Selecta+=i
        elif i==00:
            print('ok no problem')
        elif i>34:
            print('Outof stock!')
        else:
            print('Please enter invalid key')
        print('\n***************************************************')
        print('Products in your cart added successfully\n')
        print('*****************************************************')


        
    def removeProduct(self):
        lst4=[['CadburryCrunch',self.q_CadburryCrunch,self.p_CadburryCrunch,111],['Hob Nob',self.q_HobNob,self.p_HobNob,112],
              ['Triscuit',self.q_Triscuit,self.p_Triscuit,113],
             ['Cream Wheat',self.q_CreamWheat,self.p_CreamWheat,222],['Malt-O-Meal',self.q_MaltOMeal,self.p_MaltOMeal,223],
              ['Scotts Porage',self.q_ScottsPorage,self.p_ScottsPorage,224],
              ['Dunkin Donuts',self.q_DunkinDonuts,self.p_DunkinDonuts,333],
              ['Betty Crocker',self.q_BettyCrocker,self.p_BettyCrocker,334],['Mars Mufin',self.q_MarsMufin,self.p_MarsMufin,335],
             ['AngelDelight',self.q_AngelDelight,self.p_AngelDelight,444],['Magnolia',self.q_Magnolia,self.p_Magnolia,445],
              ['Selecta',self.q_Selecta,self.p_Selecta,446]]
        if self.q_CadburryCrunch==0 and self.q_HobNob==0 and self.q_Triscuit==0 and self.q_CreamWheat==0 and self.q_MaltOMeal==0 and self.q_ScottsPorage==0 and self.q_DunkinDonuts==0 and self.q_BettyCrocker==0 and self.q_MarsMufin==0 and self.q_AngelDelight==0 and self.q_Magnolia==0 and self.q_Selecta==0:
            print('Your cart is empty! Add some thing in your cart!\n')
        else:
            count=int(input('How many products you want to remove:'))
            for k in range(count):
                print('Enter the ID of Product:',k+1,end='')
                print()
                try:
                    x=int(input())
                except:
                    print('Value Error! Enter digit number')
                    x=int(input())                
                if x==111:
                    lst4.remove(['CadburryCrunch',self.q_CadburryCrunch,self.p_CadburryCrunch,111])
                if x==112:
                    lst4.remove(['Hob Nob',self.q_HobNob,self.p_HobNob,112])
                if x==113:
                    lst4.remove(['Triscuit',self.q_Triscuit,self.p_Triscuit,113])
                if x==222:
                    lst4.remove(['Cream Wheat',self.q_CreamWheat,self.p_CreamWheat,222])
                if x==223:
                    lst4.remove(['Malt-O-Meal',self.q_MaltOMeal,self.p_MaltOMeal,223])
                if x==224:
                    lst4.remove(['Scotts Porage',self.q_ScottsPorage,self.p_ScottsPorage,224])
                if x==333:
                    lst4.remove(['Dunkin Donuts',self.q_DunkinDonuts,self.p_DunkinDonuts,333])
                if x==334:
                    lst4.remove(['Betty Crocker',self.q_BettyCrocker,self.p_BettyCrocker,334])
                if x==335:
                    lst4.remove(['Mars Mufin',self.q_MarsMufin,self.p_MarsMufin,335])
                if x==444:
                    lst4.remove(['AngelDelight',self.q_AngelDelight,self.p_AngelDelight,444])
                if x==445:
                    lst4.remove(['Magnolia',self.q_Magnolia,self.p_Magnolia,445])
                if x==446:
                    lst4.remove(['Selecta',self.q_Selecta,self.p_Selecta,446])
            print('*********************************************\n')
            print('Product has been removed from your cart!\n')
            print('*********************************************')
            print('New cart after removing Products!')
            print('**********************************************')
            print('S.no\tProducts\t\tStock\tPrice_per_item\tBarcode')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            count=1
            for i in lst4:
                print(f'{count:3}     {i[0]:15} \t{i[1]:0} \t{i[2]:0} \t\t{i[3]:0}')
                count+=1
            f=open('A1_CS19075_3.txt','a')
            for i in lst4:
                f.write(str(i)+'\n')
            f.close
            
    def displayCart(self):
        print('***Your Cart***\n')
        if self.q_CadburryCrunch==0 and self.q_HobNob==0 and self.q_Triscuit==0 and self.q_CreamWheat==0 and self.q_MaltOMeal==0 and self.q_ScottsPorage==0 and self.q_DunkinDonuts==0 and self.q_BettyCrocker==0 and self.q_MarsMufin==0 and self.q_AngelDelight==0 and self.q_Magnolia==0 and self.q_Selecta==0:
            print('Your cart is empty! Add some thing in your cart!\n')
            print('Go to main menu if you want to add somthing in your cart\n')
        else:
            lst4=[['CadburryCrunch',self.q_CadburryCrunch,self.p_CadburryCrunch,111],['Hob Nob',self.q_HobNob,self.p_HobNob,112],
              ['Triscuit',self.q_Triscuit,self.p_Triscuit,113],
             ['Cream Wheat',self.q_CreamWheat,self.p_CreamWheat,222],['Malt-O-Meal',self.q_MaltOMeal,self.p_MaltOMeal,223],
              ['Scotts Porage',self.q_ScottsPorage,self.p_ScottsPorage,224],
              ['Dunkin Donuts',self.q_DunkinDonuts,self.p_DunkinDonuts,333],
              ['Betty Crocker',self.q_BettyCrocker,self.p_BettyCrocker,334],['Mars Mufin',self.q_MarsMufin,self.p_MarsMufin,335],
             ['AngelDelight',self.q_AngelDelight,self.p_AngelDelight,444],['Magnolia',self.q_Magnolia,self.p_Magnolia,445],
              ['Selecta',self.q_Selecta,self.p_Selecta,446]]

            print('S.no\tProducts\t\tStock\tPrice_per_item\tBarcode')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            count=1
            for i in lst4:
                print(f'{count:3}     {i[0]:15} \t{i[1]:0} \t{i[2]:0} \t\t{i[3]:0}')
                count+=1
            f=open('A1_CS_19075_4.txt','a')
            for i in lst4:
                f.write(str(i)+'\n')
            f.close

class Shopping(ShoppingCart):
    cart=[]
    total=0
    def placeOrder(self):
        super().displayCart()
        if self.q_CadburryCrunch==0 and self.q_HobNob==0 and self.q_Triscuit==0 and self.q_CreamWheat==0 and self.q_MaltOMeal==0 and self.q_ScottsPorage==0 and self.q_DunkinDonuts==0 and self.q_BettyCrocker==0 and self.q_MarsMufin==0 and self.q_AngelDelight==0 and self.q_Magnolia==0 and self.q_Selecta==0:
            print('Your cart is empty! Add some thing in your cart!\n')
        else:
            count=int(input('How many products you want to buy:'))
            for k in range(count):
                print('Enter the BarCode of Product:',k+1,end='')
                print()
                try:
                    k=int(input('Enter the BarCode of the product you want to buy:'))
                except:
                    print('Value error! please enter a correct BarCode!')
                    k=int(input('Enter the BarCode of the product you want to buy:'))
                if k==111:
                    print('Enter the quantity you want to purchase')
                    try:
                        y=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y=int(input())
                    if 0<y<=self.q_CadburryCrunch:
                        lst1=[]
                        self.q_CadburryCrunch-=y
                        a=self.p_CadburryCrunch*y
                        lst1.append('CadburryCrunch')
                        lst1.append(a)
                        self.cart.append(lst1)
                        self.total+=a
                    else:
                        print('The quantity of Cadburry Crunch is less than that you add in your cart')
                if k==112:
                    print('Enter the quantity you want to purchase')
                    try:
                        y1=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y1=int(input())
                    if 0<y1<=self.q_HobNob:
                        lst2=[]
                        self.q_HobNob-=y1
                        b=self.p_HobNob*y1
                        lst2.append('Hob Nob')
                        lst2.append(b)
                        self.cart.append(lst2)
                        self.total+=b
                    else:
                        print('The quantity of Hob Nob is less than that you add in your cart')
                if k==113:
                    print('Enter the quantity you want to purchase')
                    try:
                        y2=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y2=int(input())
                    if 0<y2<=self.q_Triscuit:
                        lst3=[]
                        self.q_Triscuit-=y2
                        c=self.p_Triscuit*y2
                        lst3.append('Triscuit')
                        lst3.append(c)
                        self.cart.append(lst3)
                        self.total+=c
                    else:
                        print('The quantity of Triscuit is less than that you add in your cart')
                if k==222:
                    print('Enter the quantity you want to purchase')
                    try:
                        y3=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y3=int(input())
                    if 0<y3<=self.q_CreamWheat:
                        lst4=[]
                        self.q_CreamWheat-=y3
                        d=self.p_CreamWheat*y3
                        lst4.append('Cream Wheat')
                        lst4.append(d)
                        self.cart.append(lst4)
                        self.total+=d
                    else:
                        print('The quantity of Cream Wheat is less than that you add in your cart')
                if k==223:
                    print('Enter the quantity you want to purchase')
                    try:
                        y4=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y4=int(input())
                    if 0<y4<=self.q_MaltOMeal:
                        lst5=[]
                        self.q_MaltOMeal-=y4
                        e=self.p_MaltOMeal*y4
                        lst5.append('Malt-O-Meal')
                        lst5.append(e)
                        self.cart.append(lst5)
                        self.total+=e
                    else:
                        print('The quantity of Malt-O-Meal is less than that you add in your cart')
                if k==224:
                    print('Enter the quantity you want to purchase')
                    try:
                        y5=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y5=int(input())
                    if 0<y5<=self.q_ScottsPorage:
                        lst6=[]
                        self.q_ScottsPorage-=y5
                        f=self.p_ScottsPorage*y5
                        lst6.append('Scotts Porage')
                        lst6.append(f)
                        self.cart.append(lst6)
                        self.total+=f
                    else:
                        print('The quantity of Scotts Porage is less than that you add in your cart')
                if k==333:
                    print('Enter the quantity you want to purchase')
                    try:
                        y6=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y6=int(input())
                    if 0<y6<=self.q_DunkinDonuts:
                        lst7=[]
                        self.q_DunkinDonuts-=y6
                        g=self.p_DunkinDonuts*y6
                        lst7.append('Dunkin Donuts')
                        lst7.append(g)
                        self.cart.append(lst7)
                        self.total+=g
                    else:
                        print('The quantity of Dunkin Donuts is less than that you add in your cart')
                if k==334:
                    print('Enter the quantity you want to purchase')
                    try:
                        y7=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y7=int(input())
                    if 0<y7<=self.q_BettyCrocker:
                        lst8=[]
                        self.q_BettyCrocker-=y7
                        h=self.p_BettyCrocker*y7
                        lst8.append('Betty Crocker')
                        lst8.append(h)
                        self.cart.append(lst8)
                        self.total+=h
                    else:
                        print('The quantity of Betty Crocker is less than that you add in your cart')
                if k==335:
                    print('Enter the quantity you want to purchase')
                    try:
                        y8=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y8=int(input())
                    if 0<y8<=self.q_MarsMufin:
                        lst9=[]
                        self.q_MarsMufin-=y8
                        i=self.p_MarsMufin*y8
                        lst9.append('Mars Mufin')
                        lst9.append(i)
                        self.cart.append(lst9)
                        self.total+=i
                    else:
                        print('The quantity of Mars Mufin is less than that you add in your cart')
                if k==444:
                    print('Enter the quantity you want to purchase')
                    try:
                        y9=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y9=int(input())
                    if 0<y9<=self.q_AngelDelight:
                        lst10=[]
                        self.q_AngelDelight-=y9
                        j=self.p_AngelDelight*y9
                        lst10.append('Angel Delight')
                        lst10.append(j)
                        self.cart.append(lst10)
                        self.total+=j
                    else:
                        print('The quantity of Angel Delight is less than that you add in your cart')
                if k==445:
                    print('Enter the quantity you want to purchase')
                    try:
                        y10=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y10=int(input())
                    if 0<y10<=self.q_Magnolia:
                        lst11=[]
                        self.q_Magnolia-=y10
                        l=self.p_Magnolia*y10
                        lst11.append('Magnolia')
                        lst11.append(l)
                        self.cart.append(lst11)
                        self.total+=l
                    else:
                        print('The quantity of Mangolia is less than that you add in your cart')
                if k==446:
                    print('Enter the quantity you want to purchase')
                    try:
                        y11=int(input())
                    except ValueError:
                        print('Please enter value in digits!')
                        y11=int(input())
                    if 0<y11<=self.q_Selecta:
                        lst12=[]
                        self.q_Selecta-=y11
                        m=self.p_Selecta*y11
                        lst12.append('Selecta')
                        lst12.append(m)
                        self.cart.append(lst12)
                        self.total+=m
                    else:
                        print('The quantity of Selecta is less than that you add in your cart')
            print('Thank You For Shoping')
    def displayShoppingHistory(self):
        if self.cart!=[]:
            self.placeOrder()
        if self.cart==[]:
            print('You didn\'t buy any thing from this shop...')
            print('Do you want to purchase some thing from this shop?[Y/N]')
            x=input()
            if x=='Y' or x=='y':
                self.placeOrder()
            else:
                print('Okay no Problem! Good Bye')
        print('***Your Shopping History is given below***')
        print('S.no\tProducts\tPrice_per_item')
        print('****************************************************************')
        count=1
        for i in self.cart:
            print(f'{count:3}     {i[0]:15} \t{i[1]:0}')
            count+=1
        print('Your total bill is Rs.',self.total)
        f=open('A1_CS_19075_5.txt','a')
        for i in self.cart:
            f.write(str(i)+'\n')
        f.close
        f=open('A1_CS_19075_5.txt','a')
        lst_total=[]
        lst_total.append(self.total)
        for j in lst_total:
            f.write(str(j)+'\n')
        f.close
        f.close

class CheckOut(Shopping):
    def check(self):
        print('S.no\tProducts\tPrice_per_item')
        print('****************************************************************')
        count=1
        for i in self.cart:
            print(f'{count:3}     {i[0]:15} \t{i[1]:0}')
            count+=1
        print('Your total bill is Rs.',self.total,'\n')

class UserChoice(Product,CheckOut,Shopping,ShoppingCart,Logout):
    def choice(self):
        choice=input('Enter your choice:')
        print('\n')
        if choice=='a':
            super().display()
            print('Do you want to go in main menu again? press y or Y, if you dont want to go in main menu and want to logout,\nPress any key...')
            x=input()
            if x=='y' or x=='Y':
                self.login()
                self.choice()
            else:
                super().logout()
        elif choice=='b':
            super().addProducts()
            print('Do you want to go in main menu again? press y or Y, if you dont want to go in main menu and want to logout,\nPress any key...')
            x=input()
            if x=='y' or x=='Y':
                self.login()
                self.choice()
            else:
                super().logout()
        elif choice=='c':
            super().removeProduct()
            print('Do you want to go in main menu again? press y or Y, if you dont want to go in main menu and want to logout,\nPress any key...')
            x=input()
            if x=='y' or x=='Y':
                self.login()
                self.choice()
            else:
                super().logout()
        elif choice=='d':
            super().displayCart()
            print('Do you want to go in main menu again? press y or Y, if you dont want to go in main menu and want to logout,\nPress any key...')
            x=input()
            if x=='y' or x=='Y':
                self.login()
                self.choice()
            else:
                super().logout()
        elif choice=='e':
            super().check()
            print('Do you want to go in main menu again? press y or Y, if you dont want to go in main menu and want to logout,\nPress any key...')
            x=input()
            if x=='y' or x=='Y':
                self.login()
                self.choice()
            else:
                super().logout()
        elif choice=='f':
            super().displayShoppingHistory()
            print('Do you want to go in main menu again? press y or Y, if you dont want to go in main menu and want to logout,\nPress any key...')
            x=input()
            if x=='y' or x=='Y':
                self.login()
                self.choice()
            else:
                super().logout()
        elif choice=='g':
            super().logout()
        else:
            print('Please enter valid number!\U0001f610')
            
            
class Customer(UserChoice):
    def __init__(self,ID='none'):
        self.ID=ID
    lst3=[]
    def inputInfo(self):
        print('First you have to make an account\nKindly share some your basic informations!')
        self.firstName=input('Enter your First name:')
        self.lastName=input('Enter your Last name:')
        self.email=input('Enter your email:')
        self.address=input('Write your address:')
        self.ID=input('Enter your ID:')
        try: 
            self.phone=int(input('Enter your phone number:'))
        except:
            print('Enter input in digits!')
            self.phone=int(input('Enter your phone number:'))            
        self.lst3.append(self.firstName)
        self.lst3.append(self.lastName)
        self.lst3.append(self.email)
        self.lst3.append(self.phone)
        self.lst3.append(self.address)
        self.lst3.append(self.ID)
    def display1(self):
        print('\nyour account has been made successfully')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('Name:',self.firstName,self.lastName,'\nEmail:',self.email,'\nPhone number:',self.phone,'\nAddress:',self.address)
    def saveAccountInfo(self,FileName):
        f=open(FileName,'w')
        for i in self.lst3:
            f.write(str(i)+'\n')
        f.close
    def loginInto(self):       
        print('\nPlease enter your ID for log in!\n')
        y=input('Password:')
        if y!=self.ID:
            print('Incorrect password enter correct password!')
            while True:
                y=input('Try Again:')
                if y==self.ID:
                    break
        print('Successfull Login\n')
        self.login()
        super().choice()


       
c=Customer()
c.inputInfo()
c.display1()
c.loginInto()
c.saveAccountInfo('A1_CS_19075_1.txt')
p=Product()
p.saveProducts('A1_CS_19075_2.txt')






















