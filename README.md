# TaskManager
---
## Лабораторная работа по предмету языки и методы программирования
### Выполнила Карпова Софья
---
Лабораторная работа выполнена с помошью бибилиотек kivy и Sqlite3.
---
Все данные приложения хранятся в базе данных data_base.db ввиде таблицы tasks:

| id | Name | Description | groups | Date_v | Time_v |
|----|------|-------------|--------|--------|--------|
| 0 | Новый год | Встретить новый год | Важное | 2018.12.31 | 22.00 |

---
### Приложение для работы с пользоавателем:
---
#### Начальный экран программы выглядит следующим образом:
![main](https://github.com/KarpovaSofya/TaskManager/blob/master/img/1.png)

#### На главном экране Доступны следущие действия:
* Show tasks - показать задачи
* Add new task - добавить новую задачу
* Find task - найти задачу
* Quit - Закрытие приложения

#### При нажатии кнопки **Show tasks** пользователь попадает в новое меню, где ему доступны следущие действия:
* Show all tasks 
* Show tasks for today 
* Show tasks for tomorrow  
* Show tasks by group  
* Show all groups 
![chooseBScreen](https://github.com/KarpovaSofya/TaskManager/blob/master/img/2.png)


##### Show all tasks - показывает все задачи пользователя
![showAllTasks](https://github.com/KarpovaSofya/TaskManager/blob/master/img/3.png)

##### Show tasks for today - показывает все задачи пользователя на сегодня
![showTasks4Today](https://github.com/KarpovaSofya/TaskManager/blob/master/img/4.png)

##### Show tasks for tomorrow - показывает все задачи пользователя на завтра
![showTasks4Tomorrow](https://github.com/KarpovaSofya/TaskManager/blob/master/img/5.png)

##### Show tasks by group - показывает все задачи пользователя данной группы
![showTasksbyGroup](https://github.com/KarpovaSofya/TaskManager/blob/master/img/6.png)

##### Для того, чтобы просмотреть все группы пользователя, есть функция **Show all groups**. (Возможно копирование текста с экрана)
![showAllGroups](https://github.com/KarpovaSofya/TaskManager/blob/master/img/7.png)

##### На всех экранах реализована функция **Back** -  возврат на экран выбора действий

---
#### При нажатии кнопки **Add new task** пользователь может добавить новое задание
В графе **Date** пользователь может ввести дату вручную или пр нажатии кнопок **Today**  и **Tomorrow** получить сегодняшнюю и завтрашнюю дату соответственно.
![byHands](https://github.com/KarpovaSofya/TaskManager/blob/master/img/10.png)
![today](https://github.com/KarpovaSofya/TaskManager/blob/master/img/8.png)
![tomorrow](https://github.com/KarpovaSofya/TaskManager/blob/master/img/8.png)

После нажатия кнопки **Add** приложение автоматически возвращается на главный экран.
Кнопка **Go to main screen** возвращает пользователя на главный экран.

---

#### При нажатии кнопки **Find task** пользователь может найти нужное задание по имени задания и дате
![find](https://github.com/KarpovaSofya/TaskManager/blob/master/img/11.png)

Если задание не будет найдено, приложение выведет сообщение **No such task**
![find2](https://github.com/KarpovaSofya/TaskManager/blob/master/img/12.png)

Кнопка **Delete** позволяет удалить найденное сообщение. Если сообщение не было найдено, пользователь не сможет её нажать (так же как и при первоначальном попадании на этот экран).
Кнопка **Back** позволяет вернуться на главный экран.
