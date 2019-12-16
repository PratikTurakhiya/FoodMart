import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from collections import OrderedDict
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.video import Video

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

class superadmin(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        content = self.ids.scrn_user_contents
        superadmin = self.get_users()
        userstable = DataTable(table=superadmin)
        content.add_widget(userstable)

        stores = self.ids.scrn_store_contents
        store_registration = self.get_stores()
        userstable = DataTable(table=store_registration)
        stores.add_widget(userstable)

    def change_screen(self, instance):
        if instance.text == 'LOGIN':
            self.ids.srn_mgn_main.current = 'top_main_screen'
            info = self.ids.info
            info.text = 'LOGIN'
        else:
            self.ids.scrn_mngr.current = 'scrn_log_content'
            info = self.ids.info
            info.text = 'LOGIN'
        
    def change_dash_main(self, instance):
        if instance.text == 'Exit Dash':
            self.ids.srn_mgn_main.current = 'top_main_screen'
            info = self.ids.info
            info.text = 'LOGIN'
        else:
            self.ids.srn_mgn_main.current = 'sec_main_screen'

    def change_screen2(self, instance):
        if instance.text == 'MENU':
            self.ids.scrn_admin_mngr.current = 'scrn_cust_content'
        elif instance.text == 'Admin Users':
            self.ids.scrn_admin_mngr.current = 'scrn_user_content'
        else:
            self.ids.scrn_admin_mngr.current = 'scrn_store_content'
            
    def change_store_screen(self, instance):

        if instance.text == 'Remove Store':
            self.ids.scrn_store_mngr.current = 'scrn_store_delete'
            infostore = self.ids.infostore
            infostore.text = ''
        else:
            pass
    def change_entry_screen(self, instance):
        if instance.text == 'Add User':
            self.ids.scrn_entry_mngr.current = 'scrn_entry_content'
            infouser = self.ids.infouser
            infouser.text = ''
        elif instance.text == 'Update User':
            self.ids.scrn_entry_mngr.current = 'scrn_entry2_content'
            infouser = self.ids.infouser
            infouser.text = ''
        else:
            self.ids.scrn_entry_mngr.current = 'scrn_entry3_content'
            infouser = self.ids.infouser
            infouser.text = ''
    def get_users(self):

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _users = OrderedDict()
        _users['User no.'] = {}
        _users['Name'] = {}
        _users['Username'] = {}
        _users['Password'] = {}
        _users['Designation'] = {}
        sup_id = []
        name = []
        username = []
        password = []
        designation = []

        query = ("select *from superadmin")
        cursor.execute(query)

        users = cursor.fetchall()

        for user in users:
            sup_id.append(user[0])
            name.append(user[1])
            username.append(user[2])
            pwd = user[3]
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            password.append(pwd)
            designation.append(user[4])

        users_length = len(sup_id)
        idx = 0
        while idx < users_length:
            _users['User no.'][idx] = sup_id[idx]
            _users['Name'][idx] = name[idx]
            _users['Username'][idx] = username[idx]
            _users['Password'][idx] = password[idx]
            _users['Designation'][idx] = designation[idx]

            idx += 1
        
        return _users

    def add_user_fields(self):

        add_user = self.ids.scrn_user_contents
        add_user.clear_widgets()

        name = self.ids.fname_field1
        username = self.ids.user_field1
        password = self.ids.pass_field1
        designation = self.ids.des_field1

        infouser = self.ids.infouser

        first = name.text
        use = username.text
        pwd = password.text
        des = designation.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if first == '' or use == '' or pwd == '' or des == '':
            infouser.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if  not len(pwd) >= 8:
                infouser.text = '[color=#FF0000]Password should be greater than 8 characters[/color]'
            else:
                infouser.text = '[color=#00FF00]user successfully added[/color]'
                query = ("insert into superadmin(name,username,password,designation) VALUES('%s','%s','%s','%s')" %(str(first),str(use),str(pwd),str(des)))
                cursor.execute(query)
                
                rows = cursor.fetchall()

                for users in rows:
                    
                    first = users[1]
                    use = users[2]
                    pwd = users[3]
                    des = users[4]

            conn.commit()
            conn.close()

        superadmin = self.get_users()
        userstable = DataTable(table=superadmin)
        add_user.add_widget(userstable)

        if  not len(pwd) >= 8:
            password.text = ''
        else:
            name.text = ''
            username.text = ''
            password.text = ''
            designation.text = 'select'

    def update_user(self):

        update_user = self.ids.scrn_user_contents
        update_user.clear_widgets()

        sup_id = self.ids.user_field2
        username = self.ids.username_field2
        password = self.ids.pass_field2
        designation = self.ids.des_field2

        infouser = self.ids.infouser

        user = sup_id.text
        use = username.text
        pwd = password.text
        des = designation.text

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        if use == '' or pwd == '' or des == '' or user == '':
            infouser.text = '[color=#FF0000]Please enter required fields[/color]'
        else:
            if  not len(pwd) >= 8:
                infouser.text = '[color=#FF0000]Password should be greater than 8 characters[/color]'
            else:
                infouser.text = '[color=#00FF00]user successfully updated[/color]'

                query = "UPDATE superadmin SET username= '%s',password='%s',designation= '%s' WHERE sup_id= %d" %(str(use),str(pwd),str(des),int(user))
                cursor.execute(query)
            
                rows = cursor.fetchall()

                for users in rows:
                    
                    user = users[1]
                    use = users[2]
                    pwd = users[3]
                    des = users[4]

            conn.commit()
            conn.close()

        superadmin = self.get_users()
        userstable = DataTable(table=superadmin)
        update_user.add_widget(userstable)

        if  not len(pwd) >= 8:
            password.text = ''
        else:
            sup_id.text = ''
            username.text = ''
            password.text = ''
            designation.text = 'select'
    
    def delete_user(self):

        remove = self.ids.scrn_user_contents
        remove.clear_widgets()

        sup_id = self.ids.user_id_field3
        user = sup_id.text

        infouser = self.ids.infouser

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 
        if user == '':
            infouser.text = '[color=#FF0000]Please enter user number to be removed[/color]'
        else:
            infouser.text = '[color=#00FF00]user successfully removed[/color]'
            query = "DELETE FROM superadmin WHERE sup_id = %d" %(int(user))
            cursor.execute(query)
        
            conn.commit()
            conn.close()

        superadmin = self.get_users()
        userstable = DataTable(table=superadmin)
        remove.add_widget(userstable)

        sup_id.text = ''

    def validate_storeuser(self, instance):
        user_id = self.ids.user_field
        password = self.ids.pass_field

        info = self.ids.info

        uname = user_id.text
        pas = password.text 

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 
        
        query = ("select * from superadmin WHERE username='%s' AND password='%s'" %(str(uname),str(pas)))
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:

            if  ([uname == row[2] and pas == row[3]]):
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
    
    def get_stores(self):

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 

        _stores = OrderedDict()
        _stores['Store No'] = {}
        _stores['Store Name'] = {}
        _stores['Branch'] = {}
        _stores['Address'] = {}
        _stores['Email Address'] = {}
        _stores['Phone No'] = {}
        _stores['Store Type'] = {}
        _stores['Store Description'] = {}
        store_id = []
        storename = []
        store_branch = []
        address = []
        email = []
        phone_no = []
        store_type = []
        store_type_des = []

        query = ("select *from store_registration")
        cursor.execute(query)

        stores = cursor.fetchall()

        for sto in stores:

            store_id.append(sto[0])
            storename.append(sto[1])
            store_branch.append(sto[2])
            address.append(sto[3])
            email.append(sto[4])
            phone_no.append(sto[5])
            store_type.append(sto[6])
            store_type_des.append(sto[7])
        
        stores_length = len(store_id)
        idx = 0
        while idx < stores_length:
            _stores['Store No'][idx] = store_id[idx]
            _stores['Store Name'][idx] = storename[idx]
            _stores['Branch'][idx] = store_branch[idx]
            _stores['Address'][idx] = address[idx]
            _stores['Email Address'][idx] = email[idx]
            _stores['Phone No'][idx] = phone_no[idx]
            _stores['Store Type'][idx] = store_type[idx]
            _stores['Store Description'][idx] = store_type_des[idx]

            idx += 1
        
        return _stores

    def delete_store(self):

        remove = self.ids.scrn_store_contents
        remove.clear_widgets()

        store_id = self.ids.store_id_field3
        store = store_id.text

        infostore = self.ids.infostore

        conn = MySQLdb.connect(host='localhost', user='root',password='ssalironnie', database='foodmart')
        cursor = conn.cursor() 
        if store == '':
            infostore.text = '[color=#FF0000]Please enter user number to be removed[/color]'
        else:
            infostore.text = '[color=#00FF00]user successfully removed[/color]'
        
            query = "DELETE FROM store_registration WHERE store_id = %d" %(int(store))
            cursor.execute(query)
        
            conn.commit()
            conn.close()

        store_registration = self.get_stores()
        userstable = DataTable(table=store_registration)
        remove.add_widget(userstable)

        store_id.text = ''
        # try:
        #     store_id.text == int(store_id.text)
        # except ValueError:
        #     infostore.text = '[color=#FF0000]Enter Numbers only[/color]'

class superadminApp(App):
    def build(self):
        return superadmin()
if __name__=='__main__':
    superadminApp().run()   