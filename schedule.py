from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from datetime import datetime
import sqlite3

Builder.load_string('''
<Schedule>:
    id: main_win
    orientation:'vertical'
    padding:10
    spacing:10
    Label:
        text:'GRAFIK - CZERWIEC 2023' 
        bold: True
        font_size:20
        color: '#76b5c5'
        size_hint: 1, 0.2
    RecycleView:
        viewclass: 'CustomLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 5
            default_size: (None,250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5

<CustomLabel@Label>:
    bcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
''')

class Schedule(BoxLayout):
    def __init__(self,table='', **kwargs):
        super().__init__(**kwargs)

        current_datetime = datetime.now()
        current_month = current_datetime.strftime("%B")



        data = {
            'Poniedziałek':{0:(''),1:('05.06' +'  8 - 16'),2:('12.06' +'  8 - 16'),3:('19.06' +'  8 - 16'), 4:('26.06' +'  8 - 16')},
            'Wtorek':{0:(''),1:('06.06' +'  8 - 16'),2:('13.06' +'  8 - 16'),3:('20.06' +'  8 - 16'), 4:('27.06' +'  8 - 16')},
            'Środa':{0:(''),1:('07.06' +'  7 - 17'),2:('14.06' +'  7 - 17'),3:('21.06' +'  7 - 17'), 4:('28.06' +'  7 - 17')},
            'Czwartek': {0: ('01.06' +'  8 - 16'), 1: ('08.06' +'  WOLNE'), 2: ('15.06' +'  8 - 16'), 3: ('22.06' +'  8 - 16'), 4:('29.06' +'  8 - 16')},
            'Piątek': {0: ('02.06' +'  8 - 14'), 1: ('09.06' +'  8 - 14'), 2: ('16.06' +'  8 - 14'), 3: ('23.06' +'  8 - 14'), 4:('30.06' +'  8 - 14')},
            'Sobota': {0: ('03.06'+'  WOLNE'), 1: ('10.06'+'  WOLNE'), 2: ('17.06' +'  8 - 14'), 3: ('24.06'+'  WOLNE'), 4:('')},
            'Niedziela': {0:('04.06'+'  WOLNE'), 1: ('11.06'+'  WOLNE'), 2: ('18.06'+'  WOLNE'), 3: ('25.06'+'  WOLNE'),  4:('')},
        } #data store

        column_titles = [x for x in data.keys()]
        rows_length = len(data[column_titles[0]])
        self.columns = len(column_titles)

        table_data = []
        for y in column_titles:
            table_data.append({'text':str(y), 'size_hint_y':None,'height':50,'bcolor':(.05,.15,.30,1)})

        for z in range(rows_length):
            for y in column_titles:
                table_data.append({'text':str(data[y][z]),'size_hint_y':None,'height':40,'bcolor':(.06,.25,.40,1)})

        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

class ScheduleApp(App):
    def build(self):
        return Schedule()

if __name__=='__main__':
    ScheduleApp().run()