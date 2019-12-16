import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from collections import OrderedDict
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

# from kivy.uix.popup import Popup
# # from KivyCalendar import DatePicker
# from kivy.core.window import Window

# Window.clearcolor = (0.5, 0.5, 0.5, 1)
# Window.size = (400, 250)

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
            table_data.append({'text':str(t),'size_hint_y':None,'height':35,'bcolor':(.06,.45,.45,1)})

        for r in range(rows_len):
            for t in col_titles:
                table_data.append({'text':str(products[t][r]),'size_hint_y':None,'height':25,'bcolor':(.06,.25,.25,1)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

class online_storeWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        content = self.ids.scrn_user_contents
        store_admin_user = self.get_users()
        userstable = DataTable(table=store_admin_user)
        content.add_widget(userstable)

        item_scrn = self.ids.scrn_item_contents
        items = self.get_items()
        userstable = DataTable(table=items)
        item_scrn.add_widget(userstable)

        boys_scrn = self.ids.scrn_deliboy_contents
        deliveryboys = self.get_boys()
        userstable = DataTable(table=deliveryboys)
        boys_scrn.add_widget(userstable)

        promo_scrn = self.ids.scrn_promo_contents
        promotions = self.get_promo_items()
        userstable = DataTable(table=promotions)
        promo_scrn.add_widget(userstable)

        ord_scrn = self.ids.scrn_ord_contents
        orders = self.get_orders()
        userstable = DataTable(table=orders)
        ord_scrn.add_widget(userstable)

        ord_cancel = self.ids.scrn_ord_cancel
        orders = self.get_cancelled_orders()
        userstable = DataTable(table=orders)
        ord_cancel.add_widget(userstable)

        ord_delivered = self.ids.scrn_ord_control_del
        orders = self.get_delivered_orders()
        userstable = DataTable(table=orders)
        ord_delivered.add_widget(userstable)

        ord_out_deliver = self.ids.scrn_ord_control_out
        orders = self.get_outofdeliver_orders()
        userstable = DataTable(table=orders)
        ord_out_deliver.add_widget(userstable)

        deli_scrn = self.ids.scrn_deli_contents
        delivery = self.get_delivery()
        userstable = DataTable(table=delivery)
        deli_scrn.add_widget(userstable)

        complaint_scrn = self.ids.scrn_comp_content
        complaints = self.get_complaints()
        userstable = DataTable(table=complaints)
        complaint_scrn.add_widget(userstable)

        feed_scrn = self.ids.scrn_feed_content
        complaints = self.get_feedback()
        userstable = DataTable(table=complaints)
        feed_scrn.add_widget(userstable)
    
    # def setDate(self):
    #     self.cal = CalendarWidget(as_popup=True)
    #     self.popup = Popup(title='Calendar', content=self.cal, size_hint=(1, 1))
    #     self.popup.open()
    
    def change_order_control_screen(self, instance):
        if instance.text == 'Out For Delivery':
            self.ids.scrn_ord_cont.current = 'scrn_ord_control_out'
        elif instance.text == 'Delivered':
            self.ids.scrn_ord_cont.current = 'scrn_ord_control_del'
        elif instance.text == 'Order Manage':
            self.ids.scrn_ord_cont.current = 'scrn_ord_content_manage'
        else:
            self.ids.scrn_ord_cont.current = 'scrn_ord_cancel'

    def change_screen(self, instance):
        if instance.text == 'REGISTRATION':
            self.ids.scrn_mngr.current = 'scrn_reg_content'
        elif instance.text == 'LOGIN':
            self.ids.scrn_mngr.current = 'scrn_log_content'
        else:
            self.ids.scrn_mngr.current = 'scrn_mall_content'

    def change_dash_main(self, instance):
        if instance.text == 'Exit Dash':
            self.ids.srn_mgn_main.current = 'top_main_screen'
            info = self.ids.info
            info.text = 'LOGIN'
        else:
            self.ids.srn_mgn_main.current = 'sec_main_screen'

    def change_entry_screen(self, instance):
        if instance.text == 'Add User':
            self.ids.scrn_entry_mngr.current = 'scrn_entry_content'
            info2 = self.ids.info2
            info2.text = ''
        elif instance.text == 'Update User':
            self.ids.scrn_entry_mngr.current = 'scrn_entry2_content'
            info2 = self.ids.info2
            info2.text = ''
        else:
            self.ids.scrn_entry_mngr.current = 'scrn_entry3_content'
            info2 = self.ids.info2
            info2.text = ''

    def change_item_entry_screen(self, instance):
        if instance.text == 'Add Item':
            self.ids.scrn_item_entry.current = 'scrn_item'
            infoitem = self.ids.infoitem
            infoitem.text = ''
        elif instance.text == 'Update Item':
            self.ids.scrn_item_entry.current = 'scrn_update'
            infoitem = self.ids.infoitem
            infoitem.text = ''
        else:
            self.ids.scrn_item_entry.current = 'scrn_delete'
            infoitem = self.ids.infoitem
            infoitem.text = ''

    def change_order_screen(self, instance):
        if instance.text == 'update status':
            self.ids.scrn_ord_view.current = 'scrn_del_delete'
            inforder = self.ids.inforder
            inforder.text = ''
        else:
            self.ids.scrn_ord_view.current = 'scrn_ord_delete'
            inforder = self.ids.inforder
            inforder.text = ''

    def change_promo_screen(self, instance):
        if instance.text == 'Add Promo Item':
            self.ids.scrn_promo_add_item.current = 'scrn_promo_add'
            infopromo = self.ids.infopromo
            infopromo.text = ''
        elif instance.text =='Update Promo Item':
            self.ids.scrn_promo_add_item.current = 'scrn_promo_update'
            infopromo = self.ids.infopromo
            infopromo.text = ''
        else:
            self.ids.scrn_promo_add_item.current = 'scrn_promo_delete'
            infopromo = self.ids.infopromo
            infopromo.text = ''

    def change_delivery_screen(self, instance):
        if instance.text == 'Assign Delivery':
            self.ids.scrn_delivery_boy.current = 'scrn_deli_add'
            infodeli = self.ids.infodeli
            infodeli.text = ''
        elif instance.text =='Update Delivery':
            self.ids.scrn_delivery_boy.current = 'scrn_deli_update'
            infodeli = self.ids.infodeli
            infodeli.text = ''
        else:
            self.ids.scrn_delivery_boy.current = 'scrn_deli_delete'
            infodeli = self.ids.infodeli
            infodeli.text = ''
    
    def change_deliveryboy_screen(self, instance):
        if instance.text == 'Add Delivery Boy':
            self.ids.deliveryboy.current = 'dboy_add'
            infoboy = self.ids.infoboy
            infoboy.text = ''
        elif instance.text =='Update Delivery Boy':
            self.ids.deliveryboy.current = 'dboy_update'
            infoboy = self.ids.infoboy
            infoboy.text = ''
        else:
            self.ids.deliveryboy.current = 'dboy_delete'
            infoboy = self.ids.infoboy
            infoboy.text = ''

    def change_screen2(self, instance):
        if instance.text == 'MENU':
            self.ids.scrn_admin_mngr.current = 'scrn_dash_content'
        elif instance.text == 'Manage Items':
            self.ids.scrn_admin_mngr.current = 'scrn_item_content'
        elif instance.text == 'Manage Store Users':
            self.ids.scrn_admin_mngr.current = 'scrn_user_content'
        elif instance.text == 'Manage Orders':
            self.ids.scrn_admin_mngr.current = 'scrn_ord_content'
        elif instance.text == 'Manage Promotions':
            self.ids.scrn_admin_mngr.current = 'scrn_promo_content'
        elif instance.text == 'Manage Deliveries':
            self.ids.scrn_admin_mngr.current = 'scrn_deli_content'
        elif instance.text == 'Manage Delivery Boys':
            self.ids.scrn_admin_mngr.current = 'scrn_deliboy_content'
        elif instance.text == 'View Complaints':
            self.ids.scrn_admin_mngr.current = 'scrn_comp_content'
        else:
            self.ids.scrn_admin_mngr.current = 'scrn_feed_content'

    def get_delivery(self):
        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _delis= OrderedDict()
        _delis['Delivery No'] = {}
        _delis['Delivery Date'] = {}
        _delis['Delivery Boy'] = {}
        _delis['Order No'] = {}
        _delis['Customer'] = {}
        _delis['Item Name'] = {}
        delivery_id = []
        delivery_date = []
        fname = []
        ord_id = []
        lname = []
        item_name = []

        query = "SELECT d.delivery_id,d.delivery_date,b.fname,O.ord_id,C.lname,I.item_name FROM orders O,customer_registration C,delivery d,deliveryboys b,items I WHERE d.ord_id = O.ord_id and d.del_boy_id = b.del_boy_id and O.cust_id = C.cust_id and O.item_id = I.item_id"
        cursor.execute(query)

        delis = cursor.fetchall()

        for deli in delis:

            delivery_id.append(deli[0])
            delivery_date.append(deli[1])
            fname.append(deli[2])
            ord_id.append(deli[3])
            lname.append(deli[4])
            item_name.append(deli[5])

        delis_length = len(delivery_id)
        idx = 0
        while idx < delis_length:
            _delis['Delivery No'][idx] = delivery_id[idx]
            _delis['Delivery Date'][idx] = delivery_date[idx]
            _delis['Delivery Boy'][idx] = fname[idx]

            _delis['Order No'][idx] = ord_id[idx]

            _delis['Customer'][idx] = lname[idx]
            _delis['Item Name'][idx] = item_name[idx]

            idx += 1
        return  _delis

    def get_orders(self):
        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _ords = OrderedDict()
        _ords['Order No'] = {}
        _ords['Order Date'] = {}
        _ords['Quantity'] = {}
        _ords['First Name'] = {}
        _ords['Last Name'] = {}
        _ords['Item Name'] = {}
        _ords['Status'] = {}
        ord_id = []
        ord_date = []
        quantity = []
        fname = []
        lname = []
        item_name = []
        status = []

        query = "SELECT orders.ord_id,orders.ord_date,orders.quantity,C.fname,C.lname,I.item_name,orders.status FROM orders,customer_registration C,items I WHERE orders.cust_id = C.cust_id and orders.item_id = I.item_id"
        cursor.execute(query)

        ords = cursor.fetchall()

        for order in ords:
            ord_id.append(order[0])
            ord_date.append(order[1])
            quantity.append(order[2])
            fname.append(order[3])
            lname.append(order[4])
            item_name.append(order[5])
            status.append(order[6])
        
        ords_length = len(ord_id)
        idx = 0
        while idx < ords_length:
            _ords['Order No'][idx] = ord_id[idx]
            _ords['Order Date'][idx] = ord_date[idx]
            _ords['Quantity'][idx] = quantity[idx]
            _ords['First Name'][idx] = fname[idx]
            _ords['Last Name'][idx] = lname[idx]
            _ords['Item Name'][idx] = item_name[idx]
            _ords['Status'][idx] = status[idx]

            idx += 1
        
        return  _ords

    def get_cancelled_orders(self):
        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _ords = OrderedDict()
        _ords['Order No'] = {}
        _ords['Order Date'] = {}
        _ords['Quantity'] = {}
        _ords['First Name'] = {}
        _ords['Last Name'] = {}
        _ords['Item Name'] = {}
        _ords['Status'] = {}
        ord_id = []
        ord_date = []
        quantity = []
        fname = []
        lname = []
        item_name = []
        status = []

        query = "SELECT orders.ord_id,orders.ord_date,orders.quantity,C.fname,C.lname,I.item_name,orders.status FROM orders,customer_registration C,items I WHERE orders.cust_id = C.cust_id and orders.item_id = I.item_id and orders.status = 'cancelled'"
        cursor.execute(query)

        ords = cursor.fetchall()

        for order in ords:
            ord_id.append(order[0])
            ord_date.append(order[1])
            quantity.append(order[2])
            fname.append(order[3])
            lname.append(order[4])
            item_name.append(order[5])
            status.append(order[6])
        
        ords_length = len(ord_id)
        idx = 0
        while idx < ords_length:
            _ords['Order No'][idx] = ord_id[idx]
            _ords['Order Date'][idx] = ord_date[idx]
            _ords['Quantity'][idx] = quantity[idx]
            _ords['First Name'][idx] = fname[idx]
            _ords['Last Name'][idx] = lname[idx]
            _ords['Item Name'][idx] = item_name[idx]
            _ords['Status'][idx] = status[idx]

            idx += 1
        
        return  _ords

    def get_delivered_orders(self):
        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _ords = OrderedDict()
        _ords['Order No'] = {}
        _ords['Order Date'] = {}
        _ords['Quantity'] = {}
        _ords['First Name'] = {}
        _ords['Last Name'] = {}
        _ords['Item Name'] = {}
        _ords['Status'] = {}
        ord_id = []
        ord_date = []
        quantity = []
        fname = []
        lname = []
        item_name = []
        status = []

        query = "SELECT orders.ord_id,orders.ord_date,orders.quantity,C.fname,C.lname,I.item_name,orders.status FROM orders,customer_registration C,items I WHERE orders.cust_id = C.cust_id and orders.item_id = I.item_id and orders.status = 'delivered'"
        cursor.execute(query)

        ords = cursor.fetchall()

        for order in ords:
            ord_id.append(order[0])
            ord_date.append(order[1])
            quantity.append(order[2])
            fname.append(order[3])
            lname.append(order[4])
            item_name.append(order[5])
            status.append(order[6])
        
        ords_length = len(ord_id)
        idx = 0
        while idx < ords_length:
            _ords['Order No'][idx] = ord_id[idx]
            _ords['Order Date'][idx] = ord_date[idx]
            _ords['Quantity'][idx] = quantity[idx]
            _ords['First Name'][idx] = fname[idx]
            _ords['Last Name'][idx] = lname[idx]
            _ords['Item Name'][idx] = item_name[idx]
            _ords['Status'][idx] = status[idx]

            idx += 1
        
        return  _ords

    def get_outofdeliver_orders(self):

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _ords = OrderedDict()
        _ords['Order No'] = {}
        _ords['Order Date'] = {}
        _ords['Quantity'] = {}
        _ords['First Name'] = {}
        _ords['Last Name'] = {}
        _ords['Item Name'] = {}
        _ords['Status'] = {}
        ord_id = []
        ord_date = []
        quantity = []
        fname = []
        lname = []
        item_name = []
        status = []

        query = "SELECT orders.ord_id,orders.ord_date,orders.quantity,C.fname,C.lname,I.item_name,orders.status FROM orders,customer_registration C,items I WHERE orders.cust_id = C.cust_id and orders.item_id = I.item_id and orders.status = 'out for delivery'"
        cursor.execute(query)

        ords = cursor.fetchall()

        for order in ords:
            ord_id.append(order[0])
            ord_date.append(order[1])
            quantity.append(order[2])
            fname.append(order[3])
            lname.append(order[4])
            item_name.append(order[5])
            status.append(order[6])
        
        ords_length = len(ord_id)
        idx = 0
        while idx < ords_length:
            _ords['Order No'][idx] = ord_id[idx]
            _ords['Order Date'][idx] = ord_date[idx]
            _ords['Quantity'][idx] = quantity[idx]
            _ords['First Name'][idx] = fname[idx]
            _ords['Last Name'][idx] = lname[idx]
            _ords['Item Name'][idx] = item_name[idx]
            _ords['Status'][idx] = status[idx]

            idx += 1
        
        return  _ords

    def get_promo_items(self):
        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _promos = OrderedDict()
        _promos['Promo No'] = {}
        _promos['Start Date'] = {}
        _promos['End Date'] = {}
        _promos['Promo code'] = {}
        _promos['Discount(%)'] = {}
        _promos['Item Name'] = {}
        promo_id = []
        promo_start_date = []
        promo_end_date = []
        promo_code = []
        discount = []
        item_name = []

        query = "SELECT P.promo_id,P.promo_start_date,P.promo_end_date,P.promo_code,P.discount,items.item_name FROM items,promotions P WHERE items.item_id = P.item_id"
        cursor.execute(query)

        promos = cursor.fetchall()

        for promo in promos:

            promo_id.append(promo[0])
            promo_start_date.append(promo[1])
            promo_end_date.append(promo[2])
            promo_code.append(promo[3])
            discount.append(promo[4])
            item_name.append(promo[5])

        promos_length = len(promo_id)
        idx = 0
        while idx < promos_length:
            _promos['Promo No'][idx] = promo_id[idx]
            _promos['Start Date'][idx] = promo_start_date[idx]
            _promos['End Date'][idx] = promo_end_date[idx]
            _promos['Promo code'][idx] = promo_code[idx]
            _promos['Discount(%)'][idx] = discount[idx]
            _promos['Item Name'][idx] = item_name[idx]

            idx += 1
        
        return _promos

    def get_boys(self):
        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _boys = OrderedDict()
        _boys['Delivery Boy No'] = {}
        _boys['First Name'] = {}
        _boys['Last Name'] = {}
        _boys['Email'] = {}
        _boys['Address'] = {}
        _boys['Phone_no'] = {}
        _boys['Service Area'] = {}
        del_boy_id = []
        fname = []
        lname = []
        email = []
        address = []
        phone_no = []
        area_of_service = []

        query = ("select *from deliveryboys")
        cursor.execute(query)

        boys = cursor.fetchall()

        for boy in boys:
            del_boy_id.append(boy[0])
            fname.append(boy[1])
            lname.append(boy[2])
            email.append(boy[3])
            address.append(boy[4])
            phone_no.append(boy[5])
            area_of_service.append(boy[6])
        
        boys_length = len(del_boy_id)
        idx = 0
        while idx < boys_length:
            _boys['Delivery Boy No'][idx] = del_boy_id[idx]
            _boys['First Name'][idx] = fname[idx]
            _boys['Last Name'][idx] = lname[idx]
            _boys['Email'][idx] = email[idx]
            _boys['Address'][idx] = address[idx]
            _boys['Phone_no'][idx] = phone_no[idx]
            _boys['Service Area'][idx] = area_of_service[idx]

            idx += 1
        
        return _boys

    def get_users(self):

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _users = OrderedDict()
        _users['User no.'] = {}
        _users['First Name'] = {}
        _users['Last Name'] = {}
        _users['Username'] = {}
        _users['Password'] = {}
        _users['Designation'] = {}
        _users['Department'] = {}
        user_id = []
        fname = []
        lname = []
        username = []
        password = []
        designation = []
        department = []

        query = ("select *from store_admin_user")
        cursor.execute(query)

        users = cursor.fetchall()

        for user in users:
            user_id.append(user[0])
            fname.append(user[1])
            lname.append(user[2])
            username.append(user[3])
            pwd = user[4]
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            password.append(pwd)
            designation.append(user[5])
            department.append(user[6])
        
        users_length = len(user_id)
        idx = 0
        while idx < users_length:
            _users['User no.'][idx] = user_id[idx]
            _users['First Name'][idx] = fname[idx]
            _users['Last Name'][idx] = lname[idx]
            _users['Username'][idx] = username[idx]
            _users['Password'][idx] = password[idx]
            _users['Designation'][idx] = designation[idx]
            _users['Department'][idx] = department[idx]

            idx += 1
        
        return _users

    def get_items(self):

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _items = OrderedDict()
        _items['Item No'] = {}
        _items['Item Name'] = {}
        _items['Description'] = {}
        _items['Category'] = {}
        _items['Subcategory'] = {}
        _items['Quantity'] = {}
        _items['Price'] = {}
        _items['Promo Status'] = {}
        item_id = []
        item_name = []
        description = []
        category = []
        subcategory = []
        quantity = []
        price = []
        promo_status = []

        query = "Select *from items"
        cursor.execute(query)

        items = cursor.fetchall()

        for item in items:
            item_id.append(item[0])
            item_name.append(item[1])
            description.append(item[2])
            category.append(item[3])
            subcategory.append(item[4])
            quantity.append(item[5])
            price.append(item[6])
            promo_status.append(item[7])
        
        items_length = len(item_id)
        idx = 0
        while idx < items_length:
            _items['Item No'][idx] = item_id[idx]
            _items['Item Name'][idx] = item_name[idx]
            _items['Description'][idx] = description[idx]
            _items['Category'][idx] = category[idx]
            _items['Subcategory'][idx] = subcategory[idx]
            _items['Quantity'][idx] = quantity[idx]
            _items['Price'][idx] = price[idx]
            _items['Promo Status'][idx] = promo_status[idx]

            idx += 1
        
        return _items

    def get_complaints(self):

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _comp = OrderedDict()
        _comp['Order no'] = {}
        _comp['Item'] = {}
        _comp['Issue about item'] = {}
        _comp['Order Date'] = {}
        _comp['Customer'] = {}
        ord_id = []
        item_name = []
        issue = []
        ord_date = []
        fname = []

        query = ("select O.ord_id,I.item_name,comp.issue,O.ord_date,C.fname from orders O,items I,complaints comp,customer_registration C where O.ord_id = O.ord_id and O.item_id = I.item_id and C.cust_id = comp.cust_id and O.cust_id = C.cust_id")
        cursor.execute(query)

        comps = cursor.fetchall()

        for comp in comps:
            ord_id.append(comp[0])
            item_name.append(comp[1])
            issue.append(comp[2])
            ord_date.append(comp[3])
            fname.append(comp[4])
        
        comps_length = len(ord_id)
        idx = 0
        while idx < comps_length:
            _comp['Order no'][idx] = ord_id[idx]
            _comp['Item'][idx] = item_name[idx]
            _comp['Issue about item'][idx] = issue[idx]
            _comp['Order Date'][idx] = ord_date[idx]
            _comp['Customer'][idx] = fname[idx]

            idx += 1
        
        return _comp

    def get_feedback(self):

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _comp = OrderedDict()
        _comp['Order no'] = {}
        _comp['Item'] = {}
        _comp['Rate(/5)'] = {}
        _comp['Customer'] = {}
        ord_id = []
        item_name = []
        rate = []
        fname = []

        query = ("select O.ord_id,I.item_name,comp.rate,C.fname from orders O,items I,complaints comp,customer_registration C where O.ord_id = O.ord_id and O.item_id = I.item_id and C.cust_id = comp.cust_id and O.cust_id = C.cust_id")
        cursor.execute(query)

        comps = cursor.fetchall()

        for comp in comps:
            ord_id.append(comp[0])
            item_name.append(comp[1])
            rate.append(comp[2])
            fname.append(comp[3])
        
        comps_length = len(ord_id)
        idx = 0
        while idx < comps_length:
            _comp['Order no'][idx] = ord_id[idx]
            _comp['Item'][idx] = item_name[idx]
            _comp['Rate(/5)'][idx] = rate[idx]
            _comp['Customer'][idx] = fname[idx]

            idx += 1
        
        return _comp

    def add_dboy_fields(self):

        boys_scrn = self.ids.scrn_deliboy_contents
        boys_scrn.clear_widgets()
        
        fname = self.ids.fname_field_boy
        lname = self.ids.lname_field_boy
        email = self.ids.email_field_boy
        address = self.ids.address_field_boy
        phone_no = self.ids.phone_field_boy
        area_of_service = self.ids.area_field_boy

        infoboy = self.ids.infoboy

        first = fname.text
        last = lname.text
        mail = email.text
        add = address.text
        phone = phone_no.text
        area = area_of_service.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if first == '' or last == '' or mail == '' or add == '' or area == '':
            infoboy.text = '[color=#FF0000]Required fields can not be left empty[/color]'
        elif not mail.endswith(".com") or not mail.find("@"):
            infoboy.text = '[color=#FF0000]Invalid email address[/color]'
        elif not len(phone) == 10:
            infoboy.text = '[color=#FF0000]Phone number should be 10 digits[/color]'
        else:
            infoboy.text = '[color=#00FF00]Delivery boy successfully added[/color]'
            query = ("insert into deliveryboys(fname,lname,email,address,phone_no,area_of_service) VALUES('%s','%s','%s','%s','%d','%s')" %(str(first),str(last),str(mail),str(add),int(phone),str(area)))
            cursor.execute(query)
            
            rows = cursor.fetchall()

            for users in rows:
                
                first = users[1]
                last = users[2]
                mail = users[3]
                add = users[4]
                phone = users[5]
                area = users[6]

        conn.commit()
        conn.close()

        deliveryboys = self.get_boys()
        userstable = DataTable(table=deliveryboys)
        boys_scrn.add_widget(userstable)

        if not mail.endswith(".com") or not mail.find("@"):
            email.text = ''
        elif not len(phone) == 10:
            phone_no.text = ''
        else:
            fname.text = ''
            lname.text = ''
            email.text = '' 
            address.text = ''
            phone_no.text = ''

    def update_dboy_fields(self):

        boys_scrn = self.ids.scrn_deliboy_contents
        boys_scrn.clear_widgets()
        
        del_boy_id = self.ids.dboy_field_no
        fname = self.ids.fname_field_boy2
        lname = self.ids.lname_field_boy2
        email = self.ids.email_field_boy2
        address = self.ids.address_field_boy2
        phone_no = self.ids.phone_field_boy2
        area_of_service = self.ids.area_field_boy2

        infoboy = self.ids.infoboy

        delNo = del_boy_id.text
        first = fname.text
        last = lname.text
        mail = email.text
        add = address.text
        phone = phone_no.text
        area = area_of_service.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if first == '' or last == '' or mail == '' or add == '' or area == '':
            infoboy.text = '[color=#FF0000]Required fields can not be left empty[/color]'
        elif not mail.endswith(".com") or not mail.find("@"):
            infoboy.text = '[color=#FF0000]Invalid email address[/color]'
        elif not len(phone) == 10:
            infoboy.text = '[color=#FF0000]Phone number should be 10 digits[/color]'
        else:
            infoboy.text = '[color=#00FF00]Delivery boy successfully updated[/color]'
            query = "UPDATE deliveryboys SET fname= '%s',lname= '%s',email= '%s',address= '%s',phone_no= %d,area_of_service= '%s' WHERE del_boy_id = %d" %(str(first),str(last),str(mail),str(add),int(phone),str(area),int(delNo))
            cursor.execute(query)
            
            rows = cursor.fetchall()

            for users in rows:
                
                delNo = users[0]
                first = users[1]
                last = users[2]
                mail = users[3]
                add = users[4]
                phone = users[5]
                area = users[6]

        conn.commit()
        conn.close()

        deliveryboys = self.get_boys()
        userstable = DataTable(table=deliveryboys)
        boys_scrn.add_widget(userstable)

        if not mail.endswith(".com") or not mail.find("@"):
            email.text = ''
        elif not len(phone) == 10:
            phone_no.text = ''
        else:
            del_boy_id.text = ''
            fname.text = ''
            lname.text = ''
            email.text = '' 
            address.text = ''
            phone_no.text = ''
            area_of_service.text = 'select'
    
    def delete_delivery_boy(self):

        boys_scrn = self.ids.scrn_deliboy_contents
        boys_scrn.clear_widgets()

        del_boy_id = self.ids.fname_field_boy3
        boy = del_boy_id.text

        infoboy = self.ids.infoboy

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 
        
        if boy == '':
            infoboy.text = '[color=#FF0000]Please Enter delivery boy number[/color]'
        else:
            infoboy.text = '[color=#00FF00]Delvery boy Successfully removed[/color]'
            query = "DELETE FROM deliveryboys WHERE del_boy_id = %d" %(int(boy))
            cursor.execute(query)
        
        conn.commit()
        conn.close()

        deliveryboys = self.get_boys()
        userstable = DataTable(table=deliveryboys)
        boys_scrn.add_widget(userstable)

        if boy == '':
            del_boy_id.text = ''
        else:
            del_boy_id.text = ''

    def add_delivery(self):

        deli_scrn = self.ids.scrn_deli_contents
        deli_scrn.clear_widgets()

        delivery_date = self.ids.date_field2
        del_boy_id = self.ids.dboy_field2
        ord_id = self.ids.orderNo_field2

        infodeli = self.ids.infodeli

        date = delivery_date.text
        ordNo = ord_id.text
        dboy = del_boy_id.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if ordNo == '' or dboy == '':
            infodeli.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if date == '':
                infodeli.text = '[color=#FF0000]Delivery date should higher than todays date[/color]'
            else:
                infodeli.text = '[color=#00FF00]Delivery assigned successfully[/color]'

                query = "insert into delivery(delivery_date,ord_id,del_boy_id) VALUES('%s','%d','%d')" %(str(date),int(ordNo),int(dboy))
                cursor.execute(query)

                rows = cursor.fetchall()

                for deli in rows:
                    
                    date = deli[1]
                    dboy = deli[2]
                    ordNo = deli[3]

            conn.commit()
            conn.close()

        delivery = self.get_delivery()
        userstable = DataTable(table=delivery)
        deli_scrn.add_widget(userstable)

        if date == '':
            delivery_date.text = ''
        else:
            delivery_date.text = ''
            del_boy_id.text = ''
            ord_id.text = ''

    def update_delivery(self):

        deli_scrn = self.ids.scrn_deli_contents
        deli_scrn.clear_widgets()

        delivery_id = self.ids.delivery_update_field3
        delivery_date = self.ids.date_field3
        ord_id = self.ids.orderNo_field3
        del_boy_id = self.ids.dboy_field3

        infodeli = self.ids.infodeli

        deliNo = delivery_id.text

        date = delivery_date.text
        order = ord_id.text
        dboy = del_boy_id.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if order == '' or dboy == '':
            infodeli.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if date == '':
                infodeli.text = '[color=#FF0000]Delivery date should not be higher than todays date[/color]'
            else:
                infodeli.text = '[color=#00FF00]Delivery assigned successfully[/color]'

                query = "UPDATE delivery SET delivery_date= '%s',ord_id= %d,del_boy_id= %d WHERE delivery_id= %d" %(str(date),int(order),int(dboy),int(deliNo))
                cursor.execute(query)

                rows = cursor.fetchall()

                for deli in rows:
                    
                    deliNo = deli[0]
                    date = deli[1]
                    order = deli[2]
                    dboy = deli[3]

            conn.commit()
            conn.close()

        delivery = self.get_delivery()
        userstable = DataTable(table=delivery)
        deli_scrn.add_widget(userstable) 

        if date == '':
            delivery_date.text = ''
        else:
            delivery_id.text = ''
            delivery_date.text = ''
            ord_id.text = ''
            del_boy_id.text = ''

    def delete_delivery(self):

        deli_scrn = self.ids.scrn_deli_contents
        deli_scrn.clear_widgets()

        delivery_id = self.ids.date_field4
        deli = delivery_id.text

        infodeli = self.ids.infodeli

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if deli == '':
                infodeli.text = '[color=#FF0000]Enter delivery number to be deleted[/color]'
        else:
            infodeli.text = '[color=#00FF00]Delivery successfully[/color]'
    
            query = "DELETE FROM delivery WHERE delivery_id = %d" %(int(deli))
            cursor.execute(query)
        
            conn.commit()
            conn.close()

        delivery = self.get_delivery()
        userstable = DataTable(table=delivery)
        deli_scrn.add_widget(userstable)

        if deli == '':
                delivery_id.text = ''
        else:
            delivery_id.text = ''

    def add_promo_item_fields(self):

        promo_scrn = self.ids.scrn_promo_contents
        promo_scrn.clear_widgets()

        promo_start_date = self.ids.start_promo_field
        promo_end_date = self.ids.end_promo_field
        promo_code = self.ids.code_promo_field
        discount = self.ids.discount_field
        item_id = self.ids.item_promo_field

        infopromo = self.ids.infopromo
        
        item_promo = item_id.text
        start = promo_start_date.text
        end = promo_end_date.text
        code = promo_code.text
        dis = discount.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if item_promo == '' or start == '' or end == '' or code == '':
            infopromo.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if dis == '':
                infopromo.text = '[color=#FF0000]Discount can not be the same as the current discount[/color]'
            else:
                infopromo.text = '[color=#00FF00]Item successfully on promotion[/color]'

                query = "insert into promotions(item_id,promo_start_date,promo_end_date,promo_code,discount) VALUES('%d','%s','%s','%s','%d')" %(int(item_promo),str(start),str(end),str(code),int(dis))
                cursor.execute(query)

                rows = cursor.fetchall()

                for users in rows:

                    item_promo = users[1]
                    start = users[2]
                    end = users[3]
                    code = users[4]
                    dis = users[5]

            conn.commit()
            conn.close()

        promotions = self.get_promo_items()
        userstable = DataTable(table=promotions)
        promo_scrn.add_widget(userstable)

        if dis == '':
            discount.text = ''
        else:
            promo_start_date.text = ''
            promo_end_date.text = ''
            promo_code.text = '' 
            discount.text = ''
            item_id.text = ''

    def promo_update_item(self):

        promo_scrn = self.ids.scrn_promo_contents
        promo_scrn.clear_widgets()

        promo_id = self.ids.promo_field_update
        promo_start_date = self.ids.start_promo_update
        promo_end_date = self.ids.end_promo_update
        discount = self.ids.discount_field_update

        infopromo = self.ids.infopromo

        promoNo = promo_id.text
        start = promo_start_date.text
        end = promo_end_date.text
        dis = discount.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if promoNo == '' or start == '' or end == '':
            infopromo.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if dis == '':
                infopromo.text = '[color=#FF0000]Discount can not be the same as the current discount[/color]'
            else:
                infopromo.text = '[color=#00FF00]Item successfully updated on promotion[/color]'

                query = "UPDATE promotions SET promo_start_date= '%s',promo_end_date= '%s',discount= %d WHERE promo_id= %d" %(str(start),str(end),int(dis),int(promoNo))
                cursor.execute(query)

                rows = cursor.fetchall()

                for users in rows:
                    
                    promoNo = users[0]
                    start = users[1]
                    end = users[2]
                    dis = users[4]

            conn.commit()
            conn.close()

        promotions = self.get_promo_items()
        userstable = DataTable(table=promotions)
        promo_scrn.add_widget(userstable)

        if dis == '':
            discount.text = ''
        else:
            promo_id.text = ''
            promo_start_date.text = ''
            promo_end_date.text = ''
            discount.text = ''

    def delete_promo_item(self):

        promo_scrn = self.ids.scrn_promo_contents
        promo_scrn.clear_widgets()

        promo_id = self.ids.promo_id_field2

        infopromo = self.ids.infopromo


        promo = promo_id.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if promo == '':
            infopromo.text = '[color=#FF0000]Please enter promotional item number to be removed[/color]'
        else:
            infopromo.text = '[color=#00FF00]promotional item is successfully removed[/color]'
        
            query = "DELETE FROM promotions WHERE promo_id = %d" %(int(promo))
            cursor.execute(query)
        
            conn.commit()
            conn.close()

        promotions = self.get_promo_items()
        userstable = DataTable(table=promotions)
        promo_scrn.add_widget(userstable)

        promo_id.text = ''

    def add_item_fields(self):

        item_scrn = self.ids.scrn_item_contents
        item_scrn.clear_widgets()
    
        item_name = self.ids.item_field1
        description = self.ids.desc_field1
        category = self.ids.cat_field1
        subcategory = self.ids.subcat_field1
        quantity = self.ids.qty_field1
        price = self.ids.price_field1
        promo_status = self.ids.promo_status_field1

        infoitem = self.ids.infoitem

        item = item_name.text
        desc = description.text
        cat = category.text
        subcat = subcategory.text
        qty = quantity.text
        px = price.text
        promo = promo_status.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if item == '' or desc == '' or cat == '' or subcat == '' or qty == '' or promo == '':
            infoitem.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if px == '':
                infoitem.text = '[color=#FF0000]Price can not be the same as the current price[/color]'
            else:
                infoitem.text = '[color=#00FF00]Item successfully added[/color]'

                query = ("insert into items(item_name,description,category,subcategory,quantity,price,promo_status) VALUES('%s','%s','%s','%s','%d','%d','%s')" %(str(item),str(desc),str(cat),str(subcat),int(qty),int(px),str(promo)))
                cursor.execute(query)
                
                rows = cursor.fetchall()

                for users in rows:
                    
                    item = users[1]
                    desc = users[2]
                    cat = users[3]
                    subcat = users[4]
                    qty = users[5]
                    px = users[6]
                    promo = users[7]

            conn.commit()
            conn.close()

        items = self.get_items()
        userstable = DataTable(table=items)
        item_scrn.add_widget(userstable)

        if px == '':
            price.text = ''
        else:
            item_name.text = ''
            description.text = ''
            category.text = 'select' 
            subcategory.text = 'select'
            quantity.text = ''
            price.text = ''
            promo_status.text = 'select'

    def update_item(self):

        update_item = self.ids.scrn_item_contents
        update_item.clear_widgets()
    
        item_id = self.ids.item_id_field2
        quantity = self.ids.qty_field2
        price = self.ids.price_field2
        promo_status = self.ids.promo_status_field2

        infoitem = self.ids.infoitem

        item_no = item_id.text
        qty = quantity.text
        px = price.text
        promo = promo_status.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if item_no == '' or qty == '' or promo == '':
            infoitem.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if px == '':
                infoitem.text = '[color=#FF0000]Price can not be Greater the current price[/color]'
            else:
                infoitem.text = '[color=#00FF00]Item successfully updated[/color]'

                query = "UPDATE items SET quantity= %d,price= %d,promo_status= '%s' WHERE item_id= %d" %(int(qty),int(px),str(promo),int(item_no))
                cursor.execute(query)
                
                rows = cursor.fetchall()

                for users in rows:
                    
                    item_no = users[0]
                    qty = users[5]
                    px = users[6]
                    promo = users[7]

            conn.commit()
            conn.close()

        items = self.get_items()
        userstable = DataTable(table=items)
        update_item.add_widget(userstable)

        if px == '':
            price.text = ''
        else:
            item_id.text = ''
            quantity.text = ''
            price.text = ''
            promo_status.text = 'select'

    def delete_item(self):

        delete_item = self.ids.scrn_item_contents
        delete_item.clear_widgets()

        item_id = self.ids.item_id_field3

        infoitem = self.ids.infoitem

        item = item_id.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if item == '':
            infoitem.text = '[color=#FF0000]Please enter item number to be removed[/color]'
        else:
            infoitem.text = '[color=#00FF00]item successfully removed[/color]'
        
            query = "DELETE FROM items WHERE item_id = %d" %(int(item))
            cursor.execute(query)
        
            conn.commit()
            conn.close()

        items = self.get_items()
        userstable = DataTable(table=items)
        delete_item.add_widget(userstable)

        item_id.text = ''

    def add_user_fields(self):

        add_user = self.ids.scrn_user_contents
        add_user.clear_widgets()

        fname = self.ids.fname_field1
        lname = self.ids.lname_field1
        username = self.ids.user_field1
        password = self.ids.pass_field1
        designation = self.ids.des_field1
        department = self.ids.depart_field1

        info2 = self.ids.info2

        first = fname.text
        last = lname.text
        use = username.text
        pwd = password.text
        des = designation.text
        depart = department.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if first == '' or last == '' or use == '' or pwd == '' or des == '' or depart == '':
            info2.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if  not len(pwd) >= 8:
                info2.text = '[color=#FF0000]Password should be greater than 8 characters[/color]'
            else:
                info2.text = '[color=#00FF00]user successfully added[/color]'
                query = ("insert into store_admin_user(fname,lname,username,password,designation,department) VALUES('%s','%s','%s','%s','%s','%s')" %(str(first),str(last),str(use),str(pwd),str(des),str(depart)))
                cursor.execute(query)
                
                rows = cursor.fetchall()

                for users in rows:
                    
                    first = users[1]
                    last = users[2]
                    use = users[3]
                    pwd = users[4]
                    des = users[5]
                    depart = users[6]

            conn.commit()
            conn.close()

        store_admin_user = self.get_users()
        userstable = DataTable(table=store_admin_user)
        add_user.add_widget(userstable)

        if  not len(pwd) >= 8:
            password.text = ''
        else:
            fname.text = ''
            lname.text = ''
            username.text = ''
            password.text = ''
            designation.text = 'select'
            department.text = 'select'

    def update_user(self):

        update_user = self.ids.scrn_user_contents
        update_user.clear_widgets()

        user_id = self.ids.user_field2
        username = self.ids.username_field2
        password = self.ids.pass_field2
        designation = self.ids.des_field2
        department = self.ids.depart_field2

        info2 = self.ids.info2

        user_no = user_id.text
        use = username.text
        pwd = password.text
        des = designation.text
        depart = department.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if use == '' or pwd == '' or des == '' or depart == '':
            info2.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if  not len(pwd) >= 8:
                info2.text = '[color=#FF0000]Password should be greater than 8 characters[/color]'
            else:
                info2.text = '[color=#00FF00]user successfully updated[/color]'

                query = "UPDATE store_admin_user SET username= '%s',password='%s',designation= '%s', department= '%s' WHERE user_id= %d" %(str(use),str(pwd),str(des),str(depart),int(user_no))
                cursor.execute(query)
            
                rows = cursor.fetchall()

                for users in rows:
                    
                    user_no = users[0]
                    use = users[3]
                    pwd = users[4]
                    des = users[5]
                    depart = users[6]

            conn.commit()
            conn.close()

        store_admin_user = self.get_users()
        userstable = DataTable(table=store_admin_user)
        update_user.add_widget(userstable)

        if  not len(pwd) >= 8:
            password.text = ''
        else:
            user_id.text = ''
            username.text = ''
            password.text = ''
            designation.text = 'select'
            department.text = 'select'
    
    def delete_user(self):

        remove = self.ids.scrn_user_contents
        remove.clear_widgets()

        user_id = self.ids.user_id_field3
        user = user_id.text

        info2 = self.ids.info2

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 
        
        if user == '':
            info2.text = '[color=#FF0000]Please enter user number to be removed[/color]'
        else:
            info2.text = '[color=#00FF00]user successfully removed[/color]'

            query = "DELETE FROM store_admin_user WHERE user_id = %d" %(int(user))
            cursor.execute(query)
        
            conn.commit()
            conn.close()

        store_admin_user = self.get_users()
        userstable = DataTable(table=store_admin_user)
        remove.add_widget(userstable)

        user_id.text = ''

    # def delete_order(self):

    #     ord_scrn = self.ids.scrn_ord_contents
    #     ord_scrn.clear_widgets()

    #     ord_id = self.ids.ord_id_field2
    #     order = ord_id.text

    #     inforder = self.ids.inforder

    #     conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
    #     cursor = conn.cursor() 
        
    #     if order == '':
    #         inforder.text = '[color=#FF0000]Please enter order number to be deleted[/color]'
    #     else:
    #         inforder.text = '[color=#00FF00]Order successfully deleted[/color]'
    #         query = "DELETE FROM orders WHERE ord_id = %d" %(int(order))
    #         cursor.execute(query)
        
    #     conn.commit()
    #     conn.close()

    #     orders = self.get_orders()
    #     userstable = DataTable(table=orders)
    #     ord_scrn.add_widget(userstable)

    #     if order == '':
    #         ord_id.text = ''
    #     else:
    #         ord_id.text = ''

    def update_order_status(self):
        ord_scrn = self.ids.scrn_ord_contents
        ord_scrn.clear_widgets()

        ord_out_deliver = self.ids.scrn_ord_control_out
        ord_out_deliver.clear_widgets()

        ord_delivered = self.ids.scrn_ord_control_del
        ord_delivered.clear_widgets()

        ord_cancel = self.ids.scrn_ord_cancel
        ord_cancel.clear_widgets()

        ord_id = self.ids.status_field2
        status = self.ids.order_status

        inforder = self.ids.inforder

        ordo = ord_id.text
        sta = status.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 
        if ordo == '' or sta == '':
            inforder.text = '[color=#FF0000]Required field can not be empty[/color]'
        else:
            inforder.text = '[color=#00FF00]Order Status successfully updated[/color]'

            query = "UPDATE orders SET status= '%s' WHERE ord_id= %d" %(str(sta),int(ordo))
            cursor.execute(query)

            rows = cursor.fetchall()

            for ods in rows:

                ordo = ods[0]
                sta = ods[8]
            
        conn.commit()
        conn.close()

        orders = self.get_orders()
        userstable = DataTable(table=orders)
        ord_scrn.add_widget(userstable)

        orders = self.get_outofdeliver_orders()
        userstable = DataTable(table=orders)
        ord_out_deliver.add_widget(userstable)

        orders = self.get_delivered_orders()
        userstable = DataTable(table=orders)
        ord_delivered.add_widget(userstable)

        orders = self.get_cancelled_orders()
        userstable = DataTable(table=orders)
        ord_cancel.add_widget(userstable)

        if ordo == '' or sta =='':
            ord_id.text= ''
            status.text= 'select'
        else:
            ord_id.text= ''
            status.text= 'select'

    def validate_storeuser(self, instance):
        user_id = self.ids.user_field
        password = self.ids.pass_field

        info = self.ids.info

        uname = user_id.text
        pas = password.text 

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 
        
        query = ("select * from store_admin_user WHERE username='%s' AND password='%s'" %(str(uname),str(pas)))
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:

            if  ([uname == row[3] and pas == row[4]]):
                if instance.text == 'Sign In':
                    self.ids.srn_mgn_main.current = 'top_main_screen'
                else:
                    self.ids.srn_mgn_main.current = 'sec_main_screen'

        if  uname == '' or pas == '':
            info.text = '[color=#FF0000]username and/ or password required[/color]'
        else:
            info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'

        conn.commit()
        conn.close()

        user_id.text = ''
        password.text = ''

    def register_store(self, instance):

        storename = self.ids.store_field
        store_branch = self.ids.branch_field
        address = self.ids.address_field1
        email= self.ids.email_field1
        phone_no = self.ids.phone_field1
        store_type = self.ids.type_field
        store_type_des = self.ids.des_field

        info = self.ids.info_field

        store = storename.text
        branch = store_branch.text
        add = address.text
        mail = email.text
        phone = phone_no.text
        typ = store_type.text
        des = store_type_des.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if store == '' or branch == '' or add == '' or mail == '' or phone == '' or typ == '' or des == '':
            info.text = '[color=#FF0000]Given fields should not be empty[/color]'
        elif not mail.endswith(".com") or not mail.find("@"):
            info.text = '[color=#FF0000]Invalid email address[/color]'
        elif  not len(phone) == 10:
            info.text = '[color=#FF0000]The Phone Number Should be 10 digits[/color]'
        else:

            query = ("insert into store_registration (storename,store_branch,address,email,phone_no,store_type,store_type_des) VALUES('%s','%s','%s','%s','%s','%s','%s')" %(str(store),str(branch),str(add),str(mail),str(phone),str(typ),str(des)))
            cursor.execute(query)
            
            rows = cursor.fetchall()

            for users in rows:
                
                store = users[1]
                branch = users[2]
                add = users[3]
                mail = users[4]
                phone = users[5]
                typ = users[6]
                des = users[7]
                
            conn.commit()
            conn.close()
            self.ids.scrn_mngr.current = 'scrn_log_content'

        if not mail.endswith(".com") or not mail.find("@"):
            email.text = ''
        elif not len(phone) == 10:
            phone_no.text = ''
        else:
            storename.text = ''
            store_branch.text = ''
            address.text = ''
            email.text = ''
            phone_no.text = ''
            store_type.text = ''
            store_type_des.text = ''

class online_storeApp(App):
    def build(self):

        return online_storeWindow()

if __name__=='__main__':
    online_storeApp().run()   