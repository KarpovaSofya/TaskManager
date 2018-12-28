from bs4 import BeautifulSoup
import re
import requests
import sqlite3
import kivy
import sys
import datetime
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown

tasks = sqlite3.connect("database.db")  #подключаем базу данных
cursor = tasks.cursor()

def get_today_date():
	s=''
	for i in str(datetime.date.today()).split('-'):
		s = s + i + '.'
	return (s[:-1])

def get_tomorrow_date():
	s=''
	for i in str(datetime.date.today()+datetime.timedelta(days=1)).split('-'):
		s = s + i + '.'
	return (s[:-1])

today = get_today_date()
tomorrow = get_tomorrow_date()

class MainScreen(Screen):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)

	def go2showTaskScreen(self,*args): 
		self.manager.current = 'showTaskScreen'

	def go2addScreen(self,*args): 
		self.manager.current = 'addScreen'

	def go2chooseBScreen(self,*args): 
		self.manager.current = 'chooseBScreen'

	def quit_press(self):
		sys.exit()


class ShowScreen(Screen):

	def __init__(self, **kwargs):
		super(ShowScreen, self).__init__(**kwargs)

	def show_all_tasks(self):
		t = ''
		sql = "SELECT * FROM tasks"
		for row in cursor.execute(sql):
			t = t+'\n**Задача:** ' + row[1] + '\n\n**Описание:** '+row[2]+'\n\n**Категория:** ' + row[3]+'\n\n**Дата:** ' + row[4]+'\n\n**Время:** ' + row[5]+'\n\n=======================\n'
		self.ids['text'].text = t

	def go2chooseBScreen(self,*args):
		self.manager.current = 'chooseBScreen'
		self.ids['text'].text = ''

class AddScreen(Screen):

	def __init__(self, **kwargs):
		super(AddScreen, self).__init__(**kwargs)

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'

	def add_new_task(self, name, description, date_v, time_v, groups):
		sql = 'INSERT INTO tasks (name, description, date_v, time_v, groups) VALUES (?,?,?,?,?)'
		cursor.execute(sql, (name.capitalize(), description.capitalize(), date_v, time_v, groups.capitalize()))
		tasks.commit()
		self.go2mainScreen()

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'
		self.ids['name'].text = ''
		self.ids['description'].text = ''
		self.ids['date'].text = ''
		self.ids['time'].text = ''
		self.ids['groups'].text = ''

	def today(self):
		self.ids['date'].text = today

	def tomorrow(self):
		self.ids['date'].text = tomorrow


class ShowTaskScreen(Screen):

	def __init__(self, **kwargs):
		super(ShowTaskScreen, self).__init__(**kwargs)

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'

	def find_task(self, name, date):
		sql = "SELECT * FROM tasks WHERE name=:name AND date_v=:date_v"
		cursor.execute(sql, {"name": name.capitalize(),"date_v": date})
		task = cursor.fetchall()
		if task == []:
			t = "No such task"
			self.ids['delete_btn'].disabled = True
		else:
			t = '\n**Задача:** ' + task[0][1] + '\n\n**Описание:** '+task[0][2]+'\n\n**Категория:** ' + task[0][3]+'\n\n**Дата:** ' + task[0][4]+'\n\n**Время:** ' + task[0][5]+'\n\n\n'
			self.ids['delete_btn'].disabled = False
		self.ids['text'].text = t

#	def change_task(self,name,date):

	def delete_task(self,name,date):
		sql = "DELETE FROM tasks WHERE name= '" + name.capitalize() + "' AND date_v= '" + date +"'"
		cursor.execute(sql)
		tasks.commit()
		self.ids['text'].text = ""
		self.ids['name'].text = ''
		self.ids['date'].text = ''


class ChooseBScreen(Screen):

	def __init__(self, **kwargs):
		super(ChooseBScreen, self).__init__(**kwargs)

	def go2showScreen(self,*args): 
		self.manager.current = 'showScreen'

	def go2tasks4todayScreen(self,*args): 
		self.manager.current = 'tasks4todayScreen'

	def go2tasks4tomorrowScreen(self,*args): 
		self.manager.current = 'tasks4tomorrowScreen'

	def go2tasksByGroup(self,*args): 
		self.manager.current = 'tasksByGroupScreen'

	def go2allGroupsScreen(self,*args): 
		self.manager.current = 'allGroupsScreen'

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'

class Tasks4todayScreen(Screen):

	def __init__(self, **kwargs):
		super(Tasks4todayScreen, self).__init__(**kwargs)

	def go2chooseBScreen(self,*args):
		self.manager.current = 'chooseBScreen'
		self.ids['text'].text = ''

	def find_task4today(self):
		t = ''
		sql = "SELECT * FROM tasks WHERE date_v=:date_v"
		for row in cursor.execute(sql, {"date_v": today}):
			if row != []:
				t = t+'\n**Задача:** ' + row[1] + '\n\n**Описание:** '+row[2]+'\n\n**Категория:** ' + row[3]+'\n\n**Дата:** ' + row[4]+'\n\n**Время:** ' + row[5]+'\n\n=======================\n'
		if t == []:
			t = "No such task"
		else:
			self.ids['text'].text = t


class Tasks4tomorrowScreen(Screen):

	def __init__(self, **kwargs):
		super(Tasks4tomorrowScreen, self).__init__(**kwargs)

	def go2chooseBScreen(self,*args):
		self.manager.current = 'chooseBScreen'
		self.ids['text'].text = ''

	def find_task4tomorrow(self):
		t = ''
		sql = "SELECT * FROM tasks WHERE date_v=:date_v"
		for row in cursor.execute(sql, {"date_v": tomorrow}):
			if row != []:
				t = t+'\n**Задача:** ' + row[1] + '\n\n**Описание:** '+row[2]+'\n\n**Категория:** ' + row[3]+'\n\n**Дата:** ' + row[4]+'\n\n**Время:** ' + row[5]+'\n\n=======================\n'
		if t == []:
			t = "No such task"
		else:
			self.ids['text'].text = t

class TasksByGroupScreen(Screen):

	def __init__(self, **kwargs):
		super(TasksByGroupScreen, self).__init__(**kwargs)

	def go2chooseBScreen(self,*args):
		self.manager.current = 'chooseBScreen'
		self.ids['text'].text = ''

	def find_task_by_group(self):
		groups = self.ids['input_g'].text.capitalize()
		t = ''
		sql = "SELECT * FROM tasks WHERE groups=:groups"
		cursor.execute(sql, {"groups": groups})
		task = cursor.fetchall()
		if task == []:
			t = "No such task"
		else:
			t = t + '\n**Задача:** ' + task[0][1] + '\n\n**Описание:** '+task[0][2]+'\n\n**Категория:** ' + task[0][3]+'\n\n**Дата:** ' + task[0][4]+'\n\n**Время:** ' + task[0][5]+'\n\n=======================\n'
		self.ids['text'].text = t

class AllGroupsScreen(Screen):

	def __init__(self, **kwargs):
		super(AllGroupsScreen, self).__init__(**kwargs)

	def go2chooseBScreen(self,*args):
		self.manager.current = 'chooseBScreen'
		self.ids['all_groups'].text = ''

	def show_all_groups(self):
		t = ''
		sql = "SELECT * FROM tasks"
		for row in cursor.execute(sql):
			t = t +row[3]+'\n'
		self.ids['all_groups'].text = t


class TaskManager(App):
	def build(self):
		root = ScreenManager()
		mainScreen = MainScreen(name='mainScreen')
		showScreen = ShowScreen(name='showScreen')
		addScreen = AddScreen(name='addScreen')
		chooseBScreen = ChooseBScreen(name='chooseBScreen')
		showTaskScreen = ShowTaskScreen(name='showTaskScreen')
		tasksByGroupScreen = TasksByGroupScreen(name='tasksByGroupScreen')
		tasks4tomorrowScreen = Tasks4tomorrowScreen(name='tasks4tomorrowScreen')
		tasks4todayScreen = Tasks4todayScreen(name='tasks4todayScreen')
		allGroupsScreen = AllGroupsScreen(name='allGroupsScreen')

		root.add_widget(mainScreen)
		root.add_widget(showScreen)
		root.add_widget(addScreen)
		root.add_widget(chooseBScreen)
		root.add_widget(showTaskScreen)
		root.add_widget(tasksByGroupScreen)
		root.add_widget(tasks4tomorrowScreen)
		root.add_widget(tasks4todayScreen)
		root.add_widget(allGroupsScreen)

		return root

if __name__ == '__main__':
	TaskManager().run()