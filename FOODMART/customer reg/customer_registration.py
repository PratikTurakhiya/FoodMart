import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from decimal import Decimal
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from collections import OrderedDict
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
import smtplib
import MySQLdb
Builder.load_string('''
<DataTable>: 
    id: main_win
    RecycleView:
        viewclass: 'CustLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 5
            default_size: (None,250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
<CustLabel@Label>:
    bcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
''')
class DataTable(BoxLayout):
    def __init__(self,table='', **kwargs):
        super().__init__(**kwargs)

        products = table

        col_titles = [k for k in products.keys()]
        rows_len = len(products[col_titles[0]])
        self.columns = len(col_titles)
        
        table_data = []
        for t in col_titles:
            table_data.append({'text':str(t),'size_hint_y':None,'height':40,'bcolor':(.06,.45,.45,1)})

        for r in range(rows_len):
            for t in col_titles:
                table_data.append({'text':str(products[t][r]),'size_hint_y':None,'height':30,'bcolor':(.06,.25,.25,1)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

class online_storeWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        item_scrn = self.ids.scrn_item1_content
        dominos = self.get_items()
        userstable = DataTable(table=dominos)
        item_scrn.add_widget(userstable)

        mac_d = self.ids.scrn_item2_content
        macd = self.get_items2()
        userstable = DataTable(table=macd)
        mac_d.add_widget(userstable)

        subway = self.ids.scrn_item3_content
        pizzahut = self.get_items3()
        userstable = DataTable(table=pizzahut)
        subway.add_widget(userstable)

        
        rp = self.ids.scrn_item4_content
        realpeprika = self.get_items4()
        userstable = DataTable(table=realpeprika)
        rp.add_widget(userstable)

        bk = self.ids.scrn_item5_content
        burgerking = self.get_items5()
        userstable = DataTable(table=burgerking)
        bk.add_widget(userstable)

        sb = self.ids.scrn_item6_content
        subway = self.get_items6()
        userstable = DataTable(table=subway)
        sb.add_widget(userstable)

        od = self.ids.scrn_item7_content
        orders = self.get_items7()
        userstable = DataTable(table=orders)
        od.add_widget(userstable)



        ca5 = self.ids.scrn_c_content
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    
        ca5 = self.ids.scrn_c_content
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)

        ca5 = self.ids.scrn_c_content
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)

        ca5 = self.ids.scrn_c_content
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)

        ca5 = self.ids.scrn_c_content
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)

        ca5 = self.ids.scrn_c_content
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
        
        promo = self.ids.scrn_promo_content
        dominos = self.get_promo()
        userstable = DataTable(table=dominos)
        promo.add_widget(userstable)
        
        

    def change_screen(self, instance):
        if instance.text == 'REGISTRATION':
            self.ids.scrn_mngr.current = 'scrn_reg_content'
        if instance.text == 'LOGIN':
            self.ids.scrn_mngr.current = 'scrn_log_content'
        if instance.text == 'CONTACTUS':
            self.ids.scrn_mngr.current = 'scrn_con_content'
        if instance.text == 'COMPLAINT':
            self.ids.scrn_mngr.current = 'scrn_com_content'
        if instance.text == 'REASTURANT':
            self.ids.scrn_mngr.current = 'scrn_res_content'
        if instance.text == 'PAYMENT':
            self.ids.scrn_mngr.current = 'scrn_payment_content'
        if instance.text == 'broteche':
            self.ids.scrn_mngr.current = 'scrn_mycart_content'
        if instance.text == 'cheese mania':
            self.ids.scrn_mngr.current = 'scrn_mycart2_content'
        if instance.text == 'ham & cheese':
            self.ids.scrn_mngr.current = 'scrn_mycart3_content'
        if instance.text == 'dominoz deluxe':
            self.ids.scrn_mngr.current = 'scrn_mycart4_content'
        if instance.text == 'metza':
            self.ids.scrn_mngr.current = 'scrn_mycart5_content'
        if instance.text == 'ADDITEM':
            self.ids.scrn_mngr.current = 'scrn_finalcart_content'
        if instance.text == 'CART':
            self.ids.scrn_mngr.current = 'scrn_c_content'
        if instance.text == 'PROMOTION':
            self.ids.scrn_mngr.current = 'scrn_promo_content'
        if instance.text == 'FEEDBACK':
            self.ids.scrn_mngr.current = 'scrn_feedback_content'
        
        
        
        
        

    def chng_screen(self, instance):
        if instance.text == 'dominos':
            self.ids.scrn_mngr.current = 'scrn_item1_content'
        if instance.text == 'Subway':
            self.ids.scrn_mngr.current = 'scrn_item2_content'
        if instance.text == 'burgerking':
            self.ids.scrn_mngr.current = 'scrn_item3_content'
        if instance.text == 'pizzahut':
            self.ids.scrn_mngr.current = 'scrn_item4_content'
        if instance.text == 'macd':
            self.ids.scrn_mngr.current = 'scrn_item5_content'
        if instance.text == 'rp':
            self.ids.scrn_mngr.current = 'scrn_item6_content'
        if instance.text == 'ORDER':
            self.ids.scrn_mngr.current = 'scrn_item7_content'
       
        
        # if instance.text == 'Sign In':
        #     self.ids.scrn_mngr.current = 'scrn_res_content'

    def validate_customer(self,instance):
        username = self.ids.username_field
        password = self.ids.pwd_field

        info = self.ids.info
 
        uname = username.text
        pas = password.text 

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 
        
        query = ("select * from customer_registration WHERE username='%s' AND password='%s'") %(str(uname),str(pas))
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:


          #  if  uname == '' or pas == '':
           #     info.text = '[color=#FF0000]username and/ or password required[/color]'
            if  ([uname == row[4] and pas == row[5]]):
                 if instance.text == 'Sign In':
                    self.ids.scrn_mngr.current = 'scrn_res_content'
                    info.text = '[color=#00FF00]Logged In successfully!!![/color]'
            else:
                    info.text = '[color=#FF0000]Invalid store id and/ or Username and/or Password[/color]'

        if  uname == '' or pas == '':
            info.text = '[color=#FF0000]username and/ or password required[/color]'
            self.ids.scrn_mngr.current = 'scrn_log_content'

           

        username.text = ''
        password.text = ''
    def send_otp(self):
        email = self.ids.email_field1
        mai = email.text
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('foodmartapp@gmail.com','foodmartpy')
        server.sendmail('foodmartapp@gmail.com',mai,'the verification code for the foodmart registration is 1411')
    def clear_customer(self, instance):
        fname = self.ids.fname_field
        lname = self.ids.lname_field
        email = self.ids.email_field1
        code = self.ids.emailcode_field
        username = self.ids.username_field1
        password = self.ids.pass_field
        phone_no = self.ids.phone_field1
        address = self.ids.add_field
       

        fname.text = ""
        lname.text = ""
        email.text = ""
        code.text = ""
        username.text = ""
        password.text = ""
        phone_no.text = ""
        address.text = ""
    def register_customer(self, instance):

        fname = self.ids.fname_field
        lname = self.ids.lname_field
        email = self.ids.email_field1
        code = self.ids.emailcode_field
        username = self.ids.username_field1
        password = self.ids.pass_field
        phone_no = self.ids.phone_field1
        address = self.ids.add_field
        vali = self.ids.vali

        first = fname.text
        last = lname.text
        mail = email.text
        cod = code.text
        use = username.text
        pas = password.text
        phn = phone_no.text 
        loc = address.text
        
    

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        if first == '' or last == '' or mail == '' or use == '' or pas == '' or phn == '' or loc == '':
            vali.text = '[color=#FF0000]Given fields should not be empty[/color]'
        elif not mail.endswith(".com") or not mail.find("@"):
                vali.text = '[color=#FF0000]invalid email address[/color]'
        elif  not len(phn) == 10:
                vali.text = '[color=#FF0000]phone number should be in 10 digits[/color]'
        elif  not cod == '1411':
                vali.text = '[color=#FF0000]invalid OTP[/color]'
                print (cod)
        else:
            query = ("insert into customer_registration (fname,lname,email,username,password,phone_no,address) VALUES('%s','%s','%s','%s','%s','%s','%s')" %(str(first),str(last),str(mail),str(use),str(pas),str(phn),str(loc)))
            cursor.execute(query)
            
            

            rows = cursor.fetchall()

            for users in rows:
                
                first = users[1]
                last = users[2]
                mail = users[3]
    
                use = users[4]
                pas = users[5]
                phn = users[6]
                loc = users[7]

            conn.commit()
            self.ids.scrn_mngr.current = 'scrn_log_content'
            conn.close()

      
    def sub_com(self):
    
        name = self.ids.name_field
        comment = self.ids.comment_field
        email = self.ids.email_field
        phone = self.ids.phone_field
        

        fir = name.text
        sec = comment.text
        thi = email.text
        fou= phone.text
      

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        

        query = ("insert into contact_us (name,comment,email,phone) VALUES('%s','%s','%s','%s')" %(str(fir),str(sec),str(thi),str(fou)))
        cursor.execute(query)
        

        rows = cursor.fetchall()

        for users in rows:
            
            fir = users[0]
            sec = users[1]
            thi = users[2]
            fou = users[3]
           

        conn.commit()
        conn.close()

        name.text = ''
        comment.text = ''
        email.text = ''
        phone.text = ''
    def feedback(self):
        
        orderno = self.ids.orderid
        feedback = self.ids.feedback_field
   
        

        fir = orderno.text
        sec = feedback.text
      
      

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        q = ("select *from orders where ord_id='%d'") %(int(fir))
        crs = conn.cursor()
        crs.execute(q) 
        r = crs.fetchall()
        for rows in r:
            if ([fir == rows[0]]):
                cursor = conn.cursor() 
                query = ("insert into feedback (orderno,feedback) VALUES('%d','%d')" %(int(fir),int(sec)))
                cursor.execute(query)
            

            rows = cursor.fetchall()

            for users in rows:
                
                fir = users[0]
                sec = users[1]
           

            conn.commit()
            conn.close()

            orderno.text = ''
            feedback .text = ''
      
    def sub_issue(self):
        
        order_id = self.ids.number_field
        cust_name = self.ids.cusname_field
        item_name = self.ids.item_field
        issue = self.ids.issue_field
        v = self.ids.v

        a = order_id.text
        b = cust_name.text
        c = item_name.text
        d= issue.text
      

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        q = ("select *from orders where ord_id='%d'") %(int(a))
        crs = conn.cursor()
        crs.execute(q) 
        r = crs.fetchall()
        for rows in r:
            if ([a == rows[0]]):
                cursor = conn.cursor()
                query = ("insert into complaint (order_id,cust_name, item_name, issue) VALUES('%d','%s','%s','%s')" %(int(a),str(b),str(c),str(d)))
                cursor.execute(query)
            

            rows = cursor.fetchall()

            for users in rows:
                
                a = users[0]
                b = users[1]
                c = users[2]
                d = users[3]
           
               

            conn.commit()
            conn.close()
            order_id.text = ''
            cust_name.text = ''
            item_name.text = ''
            issue.text = ''
        else:
                v.text = '[color=#FF0000]invalid order id[/color]'

           
            
               
    def ord_content(self):
        
        od = self.ids.scrn_payment_content
        od.clear_widgets()
        
        name = self.ids.fname_field1
        phone = self.ids.phone_field2
        address = self.ids.add_field3
        payment = self.ids.item10
        delivery = self.ids.item11
        promo = self.ids.promocode12
        total = self.ids.totalprice
        va2 = self.ids.va2

        a = name.text
        b = phone.text
        c = address.text
        d= payment.text
        e= delivery.text
        f= promo.text
        g= total.text
        

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        q = ("select *from customer_registration where username='%s'") %(str(a))
        crs = conn.cursor()
        crs.execute(q) 
        r = crs.fetchall()
       
        if a == '' or b == '' or c == '':
            va2.text = "given fields should not be empty"
        elif  not len(b) == 10:
            va2.text = '[color=#FF0000]phone number should be in 10 digits[/color]'
        for rows in r:
            if ([a == rows[0]]):   
                cursor = conn.cursor() 
                query = ("insert into orders(name,phone,address, payment,delivery,promo,total) VALUES('%s','%s','%s','%s','%s','%s','%s')" %(str(a),str(b),str(c),str(d),str(e),str(f),str(g)))
                cursor.execute(query)
                
            
            rows = cursor.fetchall()

            for users in rows:
                
                a = users[1]
                b = users[2]
                c = users[3]
                d = users[4]
                e = users[5]
                f = users[6]
                g = users[7]
                

            conn.commit()
            conn.close()
        va2.text = "[color=#00FF00]ORDER HAS BEEN PLACED SUCCESSFULLY[/color]"
       
        orders = self.get_items7()
        userstable = DataTable(table=orders)
        od.add_widget(userstable)
            
        
      
    
    def ins_cart(self):
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
       

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(1,'Broteche',150)")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()
        conn.commit()
        conn.close()

        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)

    def ins_cart2(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(2,'chese mania',170)")
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)

    def ins_cart3(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(3,'ham & chese',180)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        conn.commit()
        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def ins_cart4(self):
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(4,'dominos delux',158)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

     
        
        conn.commit()
    

        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def ins_cart5(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(5,'meatzza',160)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        conn.commit()
    

        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def ins_cart6(self):
        
       
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 
        query = ("insert into mycart (item_id,item_name,item_price) VALUES(6,'french fries',90)")
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
       
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)
    def ins_cart7(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(7,'snack wrap',100)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

      
        
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)
    def ins_cart8(self):
        
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(8,'happy meal',120)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)
    def ins_cart9(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(9,'rice meals',140)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)
    def ins_cart10(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(10,'fanta',160)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

    
        
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)
    def ins_cart11(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(11,'neapolitan',120)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def ins_cart12(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(12,'chicago',130)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

       
        
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def ins_cart13(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(13,'margerita',150)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def ins_cart14(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(14,'stuffed garlic bread',170)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def ins_cart15(self):
        
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(15,'choco lava cake',190)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

     
        
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def ins_cart16(self):
        
       
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(16,'pizza',150)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

     
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def ins_cart17(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(17,'noodles',170)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

    
        
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def ins_cart18(self):
        
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(18,'indian touch',180)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def ins_cart19(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(19,'pasta',190)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

  
        
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def ins_cart20(self):
        
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(20,'unlimited',200)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

       
        
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def ins_cart21(self):
        
       
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(21,'double chese',120)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

       
        
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def ins_cart22(self):
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(22,'whopper',130)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

        
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def ins_cart23(self):
        
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(23,'stakehouse',150)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

  
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def ins_cart24(self):
        
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(24,'rodeo',178)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

   
        
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def ins_cart25(self):
        
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(25,'bigking',180)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

  
        
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def ins_cart26(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(26,'cold cut combo',210)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

   
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def ins_cart27(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(27,'black forest ham',230)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

      
        
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def ins_cart28(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(28,'sandwich',190)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

     
        
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def ins_cart29(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(29,'chapata chana',190)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

       
        
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def ins_cart30(self):
        
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("insert into mycart (item_id,item_name,item_price) VALUES(30,'green veg',170)")
        cursor.execute(query)
        

        rows = cursor.fetchall()

      
        
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def del_cart(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=1")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def del_cart2(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=2")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def del_cart3(self):
            
       
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=3")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def del_cart4(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=4")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def del_cart5(self):
            
       
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=5")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        dominos = self.ca()
        userstable = DataTable(table=dominos)
        ca5.add_widget(userstable)
    def del_cart6(self):
            
       
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=6")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)

    def del_cart7(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=7")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)

    def del_cart8(self):
            
       
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=8")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)

    def del_cart9(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=9")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)

    def del_cart10(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=10")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        subway = self.ca()
        userstable = DataTable(table=subway)
        ca5.add_widget(userstable)

    def del_cart11(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=11")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def del_cart12(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=12")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def del_cart13(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=13")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def del_cart14(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=14")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def del_cart15(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=15")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        burgerking = self.ca()
        userstable = DataTable(table=burgerking)
        ca5.add_widget(userstable)
    def del_cart16(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=16")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def del_cart17(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=17")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def del_cart18(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=18")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def del_cart19(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=19")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def del_cart20(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=20")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        pizzahut = self.ca()
        userstable = DataTable(table=pizzahut)
        ca5.add_widget(userstable)
    def del_cart21(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=21")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def del_cart22(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=22")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def del_cart23(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=23")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def del_cart24(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=24")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def del_cart25(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=25")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        macd = self.ca()
        userstable = DataTable(table=macd)
        ca5.add_widget(userstable)
    def del_cart26(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=26")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def del_cart27(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=27")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def del_cart28(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=28")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def del_cart29(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=29")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    def del_cart30(self):
            
        ca5 = self.ids.scrn_c_content
        ca5.clear_widgets()

        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        query = ("delete from mycart where item_id=30")
        cursor.execute(query)
        
        
        rows = cursor.fetchall()

       
        conn.commit()
    

        conn.close()
        realpeprika = self.ca()
        userstable = DataTable(table=realpeprika)
        ca5.add_widget(userstable)
    
    def total(self):
            
        item_price = self.ids.totalprice
        itm = item_price
        promocode12 = self.ids.promocode12
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor()
        query = ("select sum(item_price) AS total from mycart")
        cursor.execute(query)
        itm = cursor.fetchall()
        item_price.text = str(itm[0][0])
        
        if(promocode12.text=="FIRST"):
            one=(int(item_price.text)*0.6)
            item_price.text=str(one)
        if(promocode12.text=="WONDER"):
            one=(int(item_price.text)*0.5)
            item_price.text=str(one)
           
         
        # print (promocode12.text)
        # print(item_price.text)
        
    
    def ca(self):
            
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor()

        _items = OrderedDict()
        _items['Item id'] = {}
        _items['Item name'] = {}
        _items['Price'] = {}
        item_id = []
        item_name = []
        price = []
        query = ("select *from mycart")
        cursor.execute(query)
        items = cursor.fetchall()
        for item in items:
            item_id.append(item[0])
            item_name.append(item[1])
            price.append(item[2])
        
        items_length = len(item_id)
        idx = 0
        while idx < items_length:
            _items['Item id'][idx] = item_id[idx]
            _items['Item name'][idx] = item_name[idx]
            _items['Price'][idx] = price[idx]

            idx += 1
        
        return _items
  
    def get_items(self):
        
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        _items = OrderedDict()
        _items['Item id'] = {}
        _items['Item name'] = {}
        _items['Price'] = {}
        item_id = []
        item_name = []
        price = []

        query = ("select *from dominos")
        cursor.execute(query)

        items = cursor.fetchall()

        for item in items:
            item_id.append(item[0])
            item_name.append(item[1])
            price.append(item[2])
        
        items_length = len(item_id)
        idx = 0
        while idx < items_length:
            _items['Item id'][idx] = item_id[idx]
            _items['Item name'][idx] = item_name[idx]
            _items['Price'][idx] = price[idx]

            idx += 1
        
        return _items
    def get_promo(self):
            
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        _items = OrderedDict()
        _items['Promo id'] = {}
        _items['Item name'] = {}
        _items['Discount'] = {}
        _items['Store name'] = {}
        
        promo_id = []
        item_name = []
        discount = []
        store_name = []
        
        query = ("select *from promotion")
        cursor.execute(query)

        items2 = cursor.fetchall()

        for item in items2:
            promo_id.append(item[0])
            item_name.append(item[1])
            discount.append(item[2])
            store_name.append(item[3])

        items_length = len(promo_id)
        idx = 0
        while idx < items_length:
            _items['Promo id'][idx] = promo_id[idx]
            _items['Item name'][idx] = item_name[idx]
            _items['Discount'][idx] = discount[idx]
            _items['Store name'][idx] = store_name[idx]
            

            idx += 1
        
        return _items
    def get_items2(self):
            
        conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
        cursor = conn.cursor() 

        _items = OrderedDict()
        _items['Item id'] = {}
        _items['Item name'] = {}
        _items['Price'] = {}
        item_id = []
        item_name = []
        price = []

        query = ("select *from macd")
        cursor.execute(query)

        items2 = cursor.fetchall()

        for item in items2:
            item_id.append(item[0])
            item_name.append(item[1])
            price.append(item[2])
        
        items_length = len(item_id)
        idx = 0
        while idx < items_length:
            _items['Item id'][idx] = item_id[idx]
            _items['Item name'][idx] = item_name[idx]
            _items['Price'][idx] = price[idx]

            idx += 1
        
        return _items
    def get_items3(self):
            
            conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
            cursor = conn.cursor() 

            _items = OrderedDict()
            _items['Item id'] = {}
            _items['Item name'] = {}
            _items['Price'] = {}
            item_id = []
            item_name = []
            price = []

            query = ("select *from pizzahut")
            cursor.execute(query)

            items3 = cursor.fetchall()

            for item in items3:
                item_id.append(item[0])
                item_name.append(item[1])
                price.append(item[2])
            
            items_length = len(item_id)
            idx = 0
            while idx < items_length:
                _items['Item id'][idx] = item_id[idx]
                _items['Item name'][idx] = item_name[idx]
                _items['Price'][idx] = price[idx]

                idx += 1
            
            return _items
    def get_items4(self):
            
            conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
            cursor = conn.cursor() 

            _items = OrderedDict()
            _items['Item id'] = {}
            _items['Item name'] = {}
            _items['Price'] = {}
            item_id = []
            item_name = []
            price = []

            query = ("select *from realpeprika")
            cursor.execute(query)

            items4 = cursor.fetchall()

            for item in items4:
                item_id.append(item[0])
                item_name.append(item[1])
                price.append(item[2])
            
            items_length = len(item_id)
            idx = 0
            while idx < items_length:
                _items['Item id'][idx] = item_id[idx]
                _items['Item name'][idx] = item_name[idx]
                _items['Price'][idx] = price[idx]

                idx += 1
            
            return _items
    def get_items5(self):
            
            conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
            cursor = conn.cursor() 

            _items = OrderedDict()
            _items['Item id'] = {}
            _items['Item name'] = {}
            _items['Price'] = {}
            item_id = []
            item_name = []
            price = []

            query = ("select *from burgerking")
            cursor.execute(query)

            items5 = cursor.fetchall()

            for item in items5:
                item_id.append(item[0])
                item_name.append(item[1])
                price.append(item[2])
            
            items_length = len(item_id)
            idx = 0
            while idx < items_length:
                _items['Item id'][idx] = item_id[idx]
                _items['Item name'][idx] = item_name[idx]
                _items['Price'][idx] = price[idx]

                idx += 1
            
            return _items
    def get_items6(self):
            
            conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
            cursor = conn.cursor() 

            _items = OrderedDict()
            _items['Item id'] = {}
            _items['Item name'] = {}
            _items['Price'] = {}
            item_id = []
            item_name = []
            price = []

            query = ("select *from subway")
            cursor.execute(query)

            items6 = cursor.fetchall()

            for item in items6:
                item_id.append(item[0])
                item_name.append(item[1])
                price.append(item[2])
            
            items_length = len(item_id)
            idx = 0
            while idx < items_length:
                _items['Item id'][idx] = item_id[idx]
                _items['Item name'][idx] = item_name[idx]
                _items['Price'][idx] = price[idx]

                idx += 1
            
            return _items
    def get_items7(self):
            
            conn = MySQLdb.connect(host='127.0.0.1', user='root',password='1411', database='foodmart')
            cursor = conn.cursor() 

            _items = OrderedDict()
            _items['Order id'] = {}
            _items['Name'] = {}
            _items['Phone'] = {}
            _items['Address'] = {}
            _items['Payment'] = {}
            _items['Delivery'] = {}
            _items['Promo'] = {}
            _items['Total'] = {}
                        
            ord_id = []
            name = []
            phone = []
            address = []
            payment = []
            delivery = []
            promo = []
            total = []
            

            query = "select *from orders" 
            cursor.execute(query)

            items7 = cursor.fetchall()

            for order in items7:
                
                ord_id.append(order[0])
                name.append(order[1])
                phone.append(order[2])
                address.append(order[3])
                payment.append(order[4])
                delivery.append(order[5])
                promo.append(order[6])
                total.append(order[7])
            
            items_length = len(ord_id)
            idx = 0
            while idx < items_length:
                 
                _items['Order id'][idx] = ord_id[idx] 
                _items['Name'][idx] = name[idx]
                _items['Phone'][idx] = phone[idx]
                _items['Address'][idx] = address[idx]
                _items['Payment'][idx] = payment[idx]
                _items['Delivery'][idx] = delivery[idx]
                _items['Promo'][idx] = promo[idx]
                _items['Total'][idx] = total[idx]
                

                idx += 1
            
            return _items
 
    
       
class customer_registrationApp(App):
    def build(self):
        return online_storeWindow()
if __name__=='__main__':
    customer_registrationApp().run()
