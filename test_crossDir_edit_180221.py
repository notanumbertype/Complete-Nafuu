import telebot;
import time; #это нам надо для точного времени обновления
import requests; 
import os; # это надо для того, чтобы мы могли удалить старый файл html
from requests import request # это нам надо для скачивания html страницы

# тут глобальная переменная, которая будет уведомлять, что пользователь нажал /start
# мы его проверили на наличие в базе пользователей, которые уже активировали чат
startFlag = 0

# глобальная переменная для остановки отправки контента
# это начальное значение аборта
abort = 0

# Указываем токен
token = ""
bot = telebot.TeleBot(token)

dir_path = os.path.join('C:\\', 'Nafuu_parser_bot')

# точный путь файла для парса
myfilewait = dir_path + '\\WAIT.txt'

# путь до почти файла с которому мы прибавим ид пользователя
myfilequeuewait = dir_path +'\\WAIT'

# точный путь файла для записи линков
#myfilelinks = 'C:/Users/Fantom/source/repos/parser ver 1.1/parser ver 1.1/temp_links.txt'

# точный путь файла костыля
readytxt_old = dir_path +'\\READY.txt'

# путь для временного хранения пикчи
tmppath = dir_path +'\\temppic.png'

# путь до файла с общим логом
logpath = 'C:/Users/Fantom/source/repos/parser ver 1.1/parser ver 1.1/Log.txt'

# основная директория, которой мы будем приписывать названия тредов
maindir = dir_path +'\\botUsers\\'

# путь к списку пользователей
userspath = dir_path +'\\botUsers\\botUsers.txt'

# путь к файлу очереди, где записаны пользователи
queuepath = dir_path +'\\queue.txt'

# путь к файлу с информацией о пользователе и треде для парсера
infotxt = dir_path + '\\INFO.txt'

# bant, c, e, p, toy, vip, vp, vt, w, wg, wsr
bant = '\\bant.txt'
c = '\\c.txt'
e = '\\e.txt'
out = '\\out.txt'
p = '\\p.txt'
toy = '\\toy.txt'
vip = '\\vip.txt' 
vp = '\\vp.txt'
vt = '\\vt.txt'
w = '\\w.txt'
wg = '\\wg.txt'
wsr = '\\wsr.txt'

def userplace_counter(message):
    a = 0
    line = '5454'
    f = open(queuepath,"r")
    while line:    
        line = f.readline()
        a += 1
    f.close() 
    return a

# функция проверки на дэбила
def debil_func(message):
    # преобразовываем значение id из int в string
    userid = str(message.chat.id)
    
    # если чел уже начал какой-то процесс, то мы его ругаем блин☺
    if (os.path.isfile(myfilequeuewait + userid + ".txt")):
        bot.send_message(message.chat.id, "Хватит, блин, тыкать😡! Жди, когда закончится процесс обновления!")

def impatient(message):
    # это просто счетчик, чтобы показать, какой номер у типа в очереди
    a = 0
    # преобразовываем значение id из int в string
    userid = str(message.chat.id)
    
    line = '5454'
    f = open(queuepath,"r")
    while line:
        line = f.readline();
        a += 1
        if(line == ''):
            break
        # тут мы удаляем \n, чтобы не было ошибки при отправке
        line = line.strip('\n')
        if (line == userid):
            a = str(a)
            bot.send_message(message.chat.id, "Jeeeez... u touched this shi again... Жди, пожалуйста, я же тебе сейчас и так уже отправляю пички!")
            return 0
    f.close()
     
# это функция будет проверять наличие пользователя в списке приглашенных
# мб, это функция будет не нужна, но пока что пусть будет
def check_invitelist(message):
    # преобразовываем значение id из int в string
    userid = str(message.chat.id)
    f = open(userspath, 'r');
    line = '5454'
    # тут сделаем флаг, чтобы понять, нашли ли мы id пользователя в списке или нет
    flag = 0
    while line:
        line = f.readline();
        if(line == ''):
            break
        # тут мы удаляем \n, чтобы не было ошибки при отправке
        line = line.strip('\n')
        if (line == userid):
            print ("Пользователь " + userid + " есть в списке приглашенных, все ОК")
            flag = 1
    f.close()
    if (flag == 0):
        print("Пользователя " + userid + " НЕТ в списке приглашенных... Он пытается получить доступ к боту!")
        bot.send_message(message.chat.id, "Тебя НЕТ в списке приглашенных! Вот твой id: " + userid)
        bot.send_message(message.chat.id, "Если хочешь получить доступ к боту, тебе надо сообщить твой id администратору.")
        return 0

# функция, которая будет проверять, есть ли папка на пользователя или нет
# если да, то она спросит, хочет ли человек ее сохранить или создать новую
def check_user_data(message):
    # это путь к папке с файлами на пользователя
    # преобразовываем значение id из int в string
    userid = str(message.chat.id)
    user_path = maindir + userid # пример:'C:/Users/Fantom/source/repos/parser ver 1.1/parser ver 1.1/botUsers/771330279'
   
    '''
    # проверка на наличие пользователя в базе
    
    '''
    if os.path.isdir(user_path): # НЕ ПУТАТЬ C os.path.isfile!!!!!
        bot.send_message(message.chat.id, "Ты уже пользовался мной... вот твой id = " + userid)
        print ("Пользователь " + userid + " уже есть в базе...")
    else:
        # если пользователя нет, заводим папку на пользователя
        os.mkdir(user_path)
        # далее создаем лог на пользователя
        f = open(user_path + '/LOG.txt', 'w')
        f.close()
        # создаем файлы под все треды
        f = open(user_path + bant, 'w')
        f.close()
        f = open(user_path + c, 'w')
        f.close()
        f = open(user_path + e, 'w')
        f.close()
        f = open(user_path + out, 'w')
        f.close()
        f = open(user_path + p, 'w')
        f.close()
        f = open(user_path + toy, 'w')
        f.close()
        f = open(user_path + vip, 'w')
        f.close()
        f = open(user_path + vp, 'w')
        f.close()
        f = open(user_path + vt, 'w')
        f.close()
        f = open(user_path + w, 'w')
        f.close()
        f = open(user_path + wg, 'w')
        f.close()
        f = open(user_path + wsr, 'w')
        f.close()
        print("Этого пользователя не было в базе... создал все папки и файлы")


"""
# функция, которая будет создавать файл аборт тхт в
# директории пользователя, чтобы не произошел сбой блин (
def abort(message):
    # преобразовываем значение id из int в string
    userid = str(message.chat.id)
    # тут мы создаем путь пользователя, где хранятся треды, логи и тмплинкс
    user_path = maindir + userid # 'C:/Users/Fantom/source/repos/parser ver 1.1/parser ver 1.1/botUsers/771330279'
    # создаем файл реди тхт
    abort_path = user_path + "/" + "ABORT.txt"
    f = open(abort_path, 'w')
    f.close()

"""


# ОСНОВНАЯ ФУНКЦИЯ
def update_nafuu(message, source, thread):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2
    
    # преобразовываем значение id из int в string
    userid = str(message.chat.id)
    
    # тут мы создаем путь пользователя, где хранятся треды, логи и тмплинкс
    user_path = maindir + userid # 'C:/Users/Fantom/source/repos/parser ver 1.1/parser ver 1.1/botUsers/771330279'
    
    # для начала мы проверяем, есть ли хоть кто-то в очереди
    if (os.stat(queuepath).st_size == 0):
        # если очередь пустая, то мы сразу вписываем себя в очередь
        # и сразу создаем файл с именет вайт + ид
            # записываю пользователя в очередь
            # для этого мы открывает файл очереди на запись в конец
            # и дозаписываем туда пользователя
            qfile = open(queuepath, "a")
            qfile.write(userid + "\n")
            qfile.close()
            f = open(myfilequeuewait + userid + ".txt", 'w')
            f.close()
    else:
        # записываю пользователя в очередь
        # для этого мы открывает файл очереди на запись в конец
        # и дозаписываем туда пользователя
        qfile = open(queuepath, "a")
        qfile.write(userid + "\n")
        qfile.close()
    
    # пока не существует файла с название типа WAIT771330279, мы ждем
    while not os.path.isfile(myfilequeuewait + userid + ".txt"):
        time.sleep(1)
        
    # пока есть костыль на ожидание другого пользователя, то
    # то ждем
    #print("Жду пока исчезнет файл WAIT...")
    #while os.path.isfile(myfilewait):
    #    time.sleep(1)
        
    # если не существует файла костыля, то все ОК    
    #if not os.path.isfile(myfilewait):
    #    print('Все ОК, ФАЙЛА "WAIT" НЕТ !')
    
    # если этот файл увидит питон, то будет ждать, пока закончится один процесс
    # значит, что еще один пользователь сейчас запустил скрипт
    #wait_file = open(myfilewait, 'w')
    #wait_file.close()


    print("Начинаю обновление...")
    
    # создаем файл реди тхт
    #abort_path = user_path + "/" + "ABORT.txt"
        
    #print("Проверка на наличие файла ABORT...")
    
    # дефайним, что пользователь еще не нажал аборот
    #if os.path.isfile(abort_path):
    #    os.remove(abort_path)
    
    #print("Файла ABORT нет!...")
    
    # это то, откуда мы будем брать ссылки для конечной отправки 
    myfilelinks = user_path + "\\tmplinks.txt"
    
    # создаем путь под файл реди тхт
    #readytxt = user_path + '/READY.txt'
    # временная мера, чтобы в момент, когда мы будем записывать id и тред в файл,
    # он не стартанул парсер
     # ТУТ ЩА НАВАЛИВАЮ ПРОСТО ГРЯЗЬ
    # СКАЧИВАЮ 3 РАЗА РАЗНЫЕ СТРАНИЦЫ С САЙТА
    # 3 ФАЙЛА ЗАПИСЫВАЮ РАЗНЫМИ ИМЕНАМИ
    # а в парсере мы 3 раза пробегаемся по циклу)
    
    # ссылки на страницы (просто пажилой позор)
    sauce1 = source
    sauce2 = source + 'page/2/'
    sauce3 = source + 'page/3/'
    
    # путь к файлу 1
    myfile1 = user_path + '\\parsetext1.html'
    # путь к файлу 2
    myfile2 = user_path + '\\parsetext2.html'
    # путь к файлу 3
    myfile3 = user_path + '\\parsetext3.html'
    
    print("Удаляю файл со старыми тмп и старые файлы хтмл...")        
    
    if os.path.isfile(myfilelinks):
        os.remove(myfilelinks)
        
    # если существует файл (html), если да, то его удаляет
    if os.path.isfile(myfile1):
        os.remove(myfile1)
    
    # если существует файл (html), если да, то его удаляет
    if os.path.isfile(myfile2):
        os.remove(myfile2)
        
    # если существует файл (html), если да, то его удаляет
    if os.path.isfile(myfile3):
        os.remove(myfile3)
    
    print("Скачиваю новые страницы...")
        
    try:
        # скачиваем html страницу
        t = request('GET', sauce1).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("Ошибка в подключении... ")
        raise SystemExit(e)
    
    # создаем, (если не можем открыть), файл и записываем туда html
    with open(myfile1, 'w', encoding='utf-8') as f:
        f.write(t)
        
    try:
        # скачиваем html страницу
        t = request('GET', sauce2).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("Ошибка в подключении... ")
        raise SystemExit(e)

    # создаем, (если не можем открыть), файл и записываем туда html
    with open(myfile2, 'w', encoding='utf-8') as f:
        f.write(t)
        
    try:
        # скачиваем html страницу
        t = request('GET', sauce3).text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print("Ошибка в подключении... ")
        raise SystemExit(e)

    # создаем, (если не можем открыть), файл и записываем туда html
    with open(myfile3, 'w', encoding='utf-8') as f:
        f.write(t)
        
    # На выходе получаем 3 файла для парса
    
    print("Скачал html страницы. ")
    
    # по нашей анальной задумке дописываем @ в конец
    # это надо, чтобы парсер знал, когда остановиться 
    with open(myfile1, 'a', encoding='utf-8') as f:
        f.write('@')
    with open(myfile2, 'a', encoding='utf-8') as f:
        f.write('@')
    with open(myfile3, 'a', encoding='utf-8') as f:
        f.write('@')
    
    # теперь нам надо сделать костыль для парсера
    # создаем файл READY.txt 
    # если этот файл увидит парсер, то начнет парсинг по хтмэльке 
    my_file = open(readytxt_old, 'w')
    my_file.close()
    
    file = open(infotxt , 'a') #дозапись в файл
    file.write(userid + '\n')
    file.write(thread + '\n')
    file.close()

    
    # после этого происходит парсинг
    ########################
    ########################
    ########################
    
    print('Начинаю сон на 2 секунды...')
    # Сон на 2 секунды
    time.sleep(2)
    
    print('Жду парсер...')
    
    # это сделано на всякий случай, если парсер не уложится в отведенные 10сек
    # то бот будет просто ждать удаления файла READY.txt
    while os.path.isfile(readytxt_old):
        time.sleep(1)
        
    # если не существует файла костыля, то все ОК    
    if not os.path.isfile(readytxt_old):
        print('Все ОК, костыля нет!')
   
    # Сон на 1 секунду
    print('Сплю еще секундочку...')
    time.sleep(1)
    
    ######ОСНОВНОЕ ДЕЙСТВИЕ######
    # ЕСЛИ РАЗМЕР ПИКА >= 10МБ, ТО
    # ТО ВСЕ КРАШИТСЯ
    # ПОТОМУ ЧТО БОТ БОЛЬШЕ НЕ МОЖЕТ ОТПРАВИТЬ
    
    # Открыли файл
    #with open(myfilelinks, 'r') as linkf: 
      #  pass
    linkf = open(myfilelinks, "r")
    # Пока есть строки, делаем:
    line = '5454'
    # Устанавливаем курсор на начало файла
    #linkf.seek(0)
    while line:
        #if os.path.isfile(abort_path):
        #        bot.send_message(message.chat.id, 'Ты написал ABORT ...=> Завершаю обновления....')
        #        time.sleep(1)
        #        break
        # Прочитать строку
        line = linkf.readline()
        #ТУТ НАДО СДЕЛАТЬ ПРОВЕРКУ НА КОНЕЦ файла сразу
        if(line == ''):
            break
        # тут мы удаляем \n, чтобы не было ошибки при отправке
        line = line.strip('\n')
        # ОПЯТЬ КОСТЫЛЬ НА ПРОВЕРКУ РАЗМЕРА ФАЙЛА
        # Сначала скачиваем пик, потом его будем удалять☺
        # скачали пик
        try:
            r = requests.get(line)
        except Exception as e:
            print(e)
            print("Попалось исключение, поэтому мы его скипаем...")
            continue
        
        # тут пытался написать обработчик ошибки 400 
        # получилось так себе (
        #if r.getcode() == 400:
        #    print("ОШИБКА 400... не могу скачать ссылку... пропускаю пикчу...")
        #    continue
        # записали его в файл
        with open(tmppath, 'wb') as f: 
            f.write(r.content)
        info = os.stat(tmppath)
        #сравнили размер файла в байтах с макс размером пика
        print(info.st_size)
        if info.st_size >= 5242880:
            print(line)
            print(info.st_size)
            print("Размер файла привышает максимальный для отправки!")
            # удаляем файл
            os.remove(tmppath)
            continue
        # удаляем файл
        os.remove(tmppath)
        # тут мы узнаем расширение (тип) файла (png, jpg - как фото, а gif - как видео)
        # пикаем ласт 3 символа из строки
        type = line[-3:]
        # если гиф, то:
        if (type == 'gif'):
            print(line)
            print("Это гифа!")
            #if os.path.isfile(abort_path):
            #    bot.send_message(message.chat.id, 'Ты написал ABORT ...=> Завершаю обновления....')
            #    time.sleep(1)
            #    break
            #Присылаем гиф пользователю
            # ловим исключения апи
            try:
                bot.send_video(message.chat.id, line, None, 'gif')
            except Exception as e:
                print(e)
                print("Попалось исключение, поэтому мы его скипаем...")
                continue
            # Проверяем, нажал ли пользователь /abort
            #if os.path.isfile(abort_path):
            #    bot.send_message(message.chat.id, 'Ты написал ABORT ...=> Завершаю обновления....')
            #    time.sleep(1)
            #    break
            
        elif (type == 'ebm'): # Это значит, что я присылаю вебм
              print(line)
              print("Это webm!")
              print("Скипаю...")
              continue
              #Присылаем вебм пользователю
              #bot.send_video(message.chat.id, line, None, 'wemb')
              #time.sleep(1)
              #if (abort == 1):
                #bot.send_message(message.chat.id, 'Ты написал ABORT ...=> Завершаю обновления....')
                #time.sleep(1)
                #break
        else:
            print(line)
            #if os.path.isfile(abort_path):
            #    bot.send_message(message.chat.id, 'Ты написал ABORT ...=> Завершаю обновления....')
            #    time.sleep(1)
            #    break
            #Присылаем пик пользователю
             # ловим исключения апи
            try:
                bot.send_photo(message.chat.id, line)
            except Exception as e:
                print(e)
                print("Попалось исключение, поэтому мы его скипаем...")
                continue
            # Сон на 1 секунду
            time.sleep(1)
            #if os.path.isfile(abort_path):
            #    bot.send_message(message.chat.id, 'Ты написал ABORT ...=> Завершаю обновления....')
            #    time.sleep(1)
            #    break
    # удаляем темп тхт
    # Закрываем указатель на этот файл
    linkf.close()
    #if os.path.isfile(myfilelinks):
    #    os.remove(myfilelinks)
    #os.remove(myfilelinks)
    bot.send_message(message.chat.id, 'Пока это все, что есть 🤗')
    print("рассчет окончен!")
    #print("Удаляю файл WAIT...")
    print("Удаляю пользователя из очереди...")
    
    # удаляем файл
    os.remove(myfilequeuewait + userid + ".txt")
    
    # откываю файл с очередью
    f = open(queuepath,"r")
    # читаю все строки
    lines = f.readlines()
    f.close()
    f = open(queuepath,"w")
    for line in lines:
        # если нашли ид, то записываем в файл все, кроме него
        if line!= userid +"\n":
            f.write(line)
    f.close()
    
    print("Беру следующего из очереди...")
    
    # если в очереди так никого и нет, то
    if (os.stat(queuepath).st_size == 0):
        print("Очередь пуста!")
        
    else:
        # теперь добираем чела из очереди
        f = open(queuepath, "r")
        line = f.readline()
        line = line.strip("\n")
        f.close()
    
        # а вот тут мы уже создаем следующий файл вайт + ид 
        f = open(myfilequeuewait + line + ".txt", 'w')
        f.close()
        time.sleep(1)
    
    #os.remove(myfilewait)
    #print("Удаляю файл ABORT...")
    #os.remove(abort_path)


# Метод под команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    check_user_data(message)
    print(message)
    print(message.chat.id)
    global startFlag
    if (startFlag == 0):
        bot.send_message(message.chat.id, 'Ты написал мне "start". Так давай начнем!😒')
        bot.send_message(message.chat.id, 'Напиши мне "/help", чтобы узнать, что я умею🧠')
        # Сон на 1 секунду
        time.sleep(1)
        bot.send_message(message.chat.id, 'Если хочешь закончить программу, то пришли /abort (Это пока что в бета-тестировании...)')
        startFlag = 1
    else:
        print("Пользователь нажал /start, хотя уже был в базе.")
   
@bot.message_handler(commands=['help'])
def help_message(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    
    print(message)
    print(message.chat.id)
    bot.send_message(message.chat.id, '/bant - International/Random🔞 **(worst place on earth)\n/c - Anime/Cute **(sometimes mature content)\n/e - Ecchi🔞\n/out - Outdoors\n/p - Photography\n/toy - Toys\n/vip - Very Impotent Posers\n/vp - Pokémon\n/vt - Virtual YouTubers\n/w - Anime/Wallpapers **(mpbile-pc)\n/wg - Wallpapers/General **(mpbile-pc)\n/wsr - Worksafe Requests')

"""
@bot.message_handler(commands=['abort'])
def abort_command(message):
    print('Пользователь завершил программу')
    print("Заврешаю цикл...")
    # СОЗДАЕМ КОСТЫЛБ ... ДА, опять.. (
    # при вызове аборта мы создаем файл ABORT.TXT
    abort(message)
"""
    
@bot.message_handler(commands=['bant'])
def update_bant(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1    
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2
    
    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)
    # тут проверяем, идут ли сейчас обновления или нет, если да, то ругаем чела
    #debil_func(message)
    print("Пользователь нажал /bant...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    source = 'https://archive.nyafuu.org/bant/'
    thread = "bant" # название треда
    update_nafuu(message, source, thread)
    
@bot.message_handler(commands=['c'])
def update_c(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2
    
    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /c...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    source = 'https://archive.nyafuu.org/c/'
    thread = "c" # название треда
    update_nafuu(message, source, thread)

@bot.message_handler(commands=['e'])
def update_e(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /e...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/e/'
    thread = "e" # название треда
    update_nafuu(message, source, thread)
    
@bot.message_handler(commands=['out'])
def update_out(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1    
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2
    
    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)
    # тут проверяем, идут ли сейчас обновления или нет, если да, то ругаем чела
    #debil_func(message)
    print("Пользователь нажал /out...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    source = 'https://archive.nyafuu.org/out/'
    thread = "out" # название треда
    update_nafuu(message, source, thread)
    
@bot.message_handler(commands=['p'])
def update_p(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /p...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/p/'
    thread = "p" # название треда
    update_nafuu(message, source, thread)
    
@bot.message_handler(commands=['toy'])
def update_toy(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /toy...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/toy/'
    thread = "toy" # название треда
    update_nafuu(message, source, thread)

@bot.message_handler(commands=['vip'])
def update_vip(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /vip...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/vip/'
    thread = "vip" # название треда
    update_nafuu(message, source, thread)

@bot.message_handler(commands=['vp'])
def update_vp(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /vp...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/vp/'
    thread = "vp" # название треда
    update_nafuu(message, source, thread)

@bot.message_handler(commands=['vt'])
def update_vt(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /vt...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/vt/'
    thread = "vt" # название треда
    update_nafuu(message, source, thread)

@bot.message_handler(commands=['w'])
def update_v(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /w...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/w/'
    thread = "w" # название треда
    update_nafuu(message, source, thread)

@bot.message_handler(commands=['wg'])
def update_vg(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /wg...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place) 
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/wg/'
    thread = "wg" # название треда
    update_nafuu(message, source, thread)

@bot.message_handler(commands=['wsr'])
def update_wsr(message):
    # тут мы делаем защиту, чтобы незванный гость не смог использовать бота
    a = 1
    a = check_invitelist(message)
    if (a == 0):
        return 1
    # проверяем, нажимал ли чел уже эту кнопку или нет
    # флаг на проверку дурака
    foolflag = 1
    # если он у нас есть в списке, то он его хейтит
    foolflag = impatient(message)
    if (foolflag == 0):
        return 2

    # тут будет функция, которая просто считает, каким в очереди будет пользователь
    place = userplace_counter(message)
    place = str(place)    
    print("Пользователь нажал /wsr...")
    bot.send_message(message.chat.id, 'Обновление займет некоторое время... wait pls☺')
    bot.send_message(message.chat.id, 'Твое место в очереди: ' + place)
    if (place == '1'):
        bot.send_message(message.chat.id, 'О, в очереди перед тобой никого нет... отправляю тебе пикчи...')
    print("Пользователь нажал апдейт...")
    #timing = time.time() # создаем экзэмпляр time
    source = 'https://archive.nyafuu.org/wsr/'
    thread = "wsr" # название треда
    update_nafuu(message, source, thread)
# Это нужно для того, чтобы все время опрашивать бота на наличие сообщений от пользователя        
bot.polling(none_stop=True, interval=0)
input()