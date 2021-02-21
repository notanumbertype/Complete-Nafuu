#include <cstdio> // для ф-ии подсчета колва символов feof (аналог: ferror)
//#include <cstring>
#include <string> // это можно было бы юзать, если бы я хотел массив символов везде ставить,
//но стринги удобнее ) тут есть strlen на длину и прочее...
#include <iostream>
#ifdef __unix__
#include <unistd.h>
#elif _WIN32
#include <Windows.h>
#endif

#include <fstream>
#include <vector>     // надо, чтобы я мог записать строки в векторы, потом их сравнить
#include <filesystem> // чтобы мы могли удалять файлы
//#include "anal.h"

using namespace std;

// тут создам глобальную константу на весь файл парсера
const string globalDir = "H:/Arch_moe_bot/";

/*
НЕ ЗАБЫТЬ ДОБАВИТЬ ЗНАК СОБАКИ В КОНЕЦ ФАЙЛА!"!!!!!!!!1
*/

/*
*
view-source_https___archive.nyafuu.org_c_.html*

ренейм файла сырья
parsetext.html

 ключик
class="html-attribute-value">thread_image_box</span>"&gt;</span>*

*/

class anal // определяем класс
{
public:
    void getter(string fname, string fname1, string user_id, string thread)
    {
        char simb;                // символ из файла
        char probel = (char)32;   // пробел для стопа
        char kavichki = (char)34; // кавычки для стопа тоже
        char dog = (char)64;      // знак собаки для конца файла
        string tempString;        // временная строка для сравнения с ключом
        string str = fname1;      // ключ к парсу линка (ключевая фраза, которая нам говорит, где копать)))
        string resString;         // конечная линка (выводим пока что на экран)
        string temper;            // временная переменная для меня (чтобы я понимал, что кладется в ячейку после 149 итераций)
        //str.erase(0, 1); // удаляем \n из начала

        // это путь, куда будет сохраняться файл (сырье)
        string parsetext = globalDir + "botUsers" + "/" + user_id + "/" + fname;
        cout << parsetext << endl;
        // это путь к треду, с которым мы будем сравнивать значения из парсера
        string thread_path = globalDir + "botUsers" + "/" + user_id + "/" + thread;
        cout << thread_path << endl;
        //тут мы дописываем путь до tmplinks в папке для каждого пользователя
        //string tmpstr = "C:/Users/Fantom/source/repos/parser ver 1.1/parser ver 1.1/botUsers/" + user_id + "/" + "tmplinks.txt";
        string tmpstr = globalDir + "botUsers" + "/" + user_id + "/" + "tmplinks.txt";

        ifstream file;
        file.open(parsetext);
        /*
        while (!file) // проверка на пажилого
         {
             file.open(fname);
             Sleep(10000);
         }
         */

        //ofstream file54; // поток для записи
        //file54.open("res_links.txt");

        ofstream file54;
        file54.open(tmpstr, ios_base::app); // открываем файл для записи в конец

        /*
        while (!file54) // проверка на пажилого
        {
            file54.open("res_links.txt");
            Sleep(10000);
        }
        */

        cout << "ФАЙЛ ОТКРЫТ!" << endl;

        //while (file.get(simb) && i < count)
        if (file.is_open()) // открыл ли файл или нет
        {
            //while (file.get(simb)) //&& i < count) ??
            while (file >> simb && simb != dog)
            {
                //cout << "прошли 1 вайл" << endl;
                while (simb != probel && simb != dog) // пока нам не встретился пробел
                {
                    //cout << simb << endl;
                    //cout << "прошли 2 вайл" << endl;
                    tempString.push_back(simb); // вставляем в конец временной строки символ
                    file.get(simb);             // добираем следующий символ
                }

                if (simb == dog)
                {
                    break;
                }

                //tempString.replace(str.begin()-1, str.end(), ".");
                //tempString.pop_back(); // удаляем последний знак
                //tempString.erase(tempString.size() - 1, 1);

                //cout << tempString << endl;
                //cout << tempString << endl;
                //cout << str << endl;

                //file54 << str << str;

                //file54.close();

                //cout << tempString << endl;

                if (tempString == str) // СРАВНИЕВАЕМ СТРОКИ
                {
                    cout << "МЫ ВНУТРИ!" << endl;
                    cout << tempString << endl;

                    // надо как-то скипнуть 9 букв
                    // ОШИБКА ЛИБО ТУТ, ЛИБО В "СРАВНИВАЕМ СТРОКИ!"
                    for (int i = 0; i < 9; i++)
                    {
                        //cout << "крутимся в цикле" << endl;
                        file.get(simb);
                        temper.push_back(simb);
                    }
                    // выводим последнее значение символа
                    //cout << simb << endl;
                    // временный мусорный буфер
                    //cout << temper << endl;
                    //file.get(simb);
                    if (simb == kavichki)
                    {
                        file.get(simb);
                        while (simb != kavichki)
                        {
                            resString.push_back(simb); // вставляем в конец результирующей строки символ
                            file.get(simb);            // добираем следующий символ
                        }

                        cout << resString << endl;
                        file54 << resString << "\n"; // ВЫВОДИМ ЛИНКИ В ФАЙЛ с переносом строки

                        resString.clear(); // отчистчаем рез стринг
                    }
                    tempString.clear(); // чистим временную строку
                }
                else
                {
                    tempString.clear(); // чистим временную строку
                }
            }
            file.close();   // закрываем файл
            file54.close(); // закрываем файл
        }
    }

    long simstrCount(string fname) //ф-я, которая считает кол-во символов
    {
        long strcounter = 0; // счетчик
        long simcounter = 0; //
        //FILE * f1 = fopen("archive.nyafuu.org.html", "r"); // это указатель на объект, чтобы распознать поток
        ifstream f1; // экзэмпляр класса ifstream для чтения файла
        f1.open(fname);

        if (!f1) // проверка на пажилого
        {
            cout << "can't open file \n";
        }
        //ищем кол-во символов
        while (!f1.eof())
        {
            string str;
            getline(f1, str);
            strcounter++;
        }
        f1.close();
        char ch;
        f1.open(fname);
        while (f1 >> ch)
        {
            simcounter++;
        }
        f1.close(); // закрываем файл

        //либо вот так
        /*
        streampos begin, end;
        ifstream myfile("example.txt");
        begin = myfile.tellg();
        myfile.seekg(0, ios::end);
        end = myfile.tellg();
        myfile.close();
        cout << "Length: " << (end - begin) << " symbols.\n";
        */

        //fclose(f1);

        cout << "Кол-во символов в файле = " << simcounter << "\n"
             << "Кол-во строк в файле = " << strcounter << "\n";
        return strcounter;
    }

    //на вход принимаем кол-во символов в файле
    void simPrint(long count, string fname) // метод, который выведет все символы из файла
    {
        char simb;  // символ из файла
        ifstream f; // экзэмпляр класса ifstream для чтения файла
        f.open(fname);

        if (!f) // проверка на пажилого
        {
            cout << "can't open file \n";
        }
        cout << "\n Вот, что сейчас в файле: \n";
        int i = 0;       // счетчик
        if (f.is_open()) // открыл ли файл или нет
        {
            while (f.get(simb) && i < count)
            {
                cout << simb;
                i++;
            }
            f.close(); // закрываем файл
        }
    }
    // этим методом можем мы сравниваем все полученные пики на наличие их в базе, если нет таких же, то добавляем
    void picBase_compare(string user_id, string thread)
    {
        // это путь к файлу с тредом на конкретного пользователя
        string thread_path = globalDir + "botUsers" + "/" + user_id + "/" + thread + ".txt";
        // это путь к файлу с тмп линками, чтобы их изменить и отправить уже в бота
        string tmpstr = globalDir + "botUsers" + "/" + user_id + "/" + "tmplinks.txt";

        string foolstr; // строка, чтобы пикать строки из базы
        string linkstr; // строка, чтобы пикать строки из темпа

        // создаем 2 вектора
        vector<string> vTmp;  // вектор файла с тмп линк
        vector<string> vBase; // вектор базы на тред

        ifstream fBase_read;  // файл с базой на тред на чтение
        ofstream fBase_write; // файл с базой на тред на запись

        ofstream f_write;
        //f_write.open(tmpstr);
        ifstream f_read;
        //f_read.open(tmpstr);

        // КОРОЧЕ, МНЕ НАДОЕЛО НАД ЭТИМ ДУМАТЬ. БУДУ ДЕЛАТЬ ЧЕРЕЗ VECTOR
        // допустим, будим юзать его как контейнер.
        // запишем в него данные из tmp файла с линками, потом будем сравнивать
        // с вектором из файла с базой = > удалим одинаковые из tmp
        // в отдельном блоке пробежимся по базе и tmp и удалим, где-то добавим

        // считаем данные из файла тмп в вектор
        f_read.open(tmpstr); // файл с темп линками
        while (!f_read.eof())
        {
            // пропихиваем в конец вектора полученные значения из тмп файла
            string str;
            getline(f_read, str);
            vTmp.push_back(str);
        }
        f_read.close();

        fBase_read.open(thread_path); // открываем базу с линками на конкр. тред для сравнения
        while (!fBase_read.eof())
        {
            // пропихиваем в конец вектора полученные значения из базофайла файла
            string str;
            getline(fBase_read, str);
            vBase.push_back(str);
        }
        fBase_read.close();

        // проверяем, если тред-база пустая, то записываем сразу туда тмп
        if (vBase.empty())
        {
            fBase_write.open(thread_path);
            for (int i = 0; i < vTmp.size(); i++)
            {
                fBase_write << vTmp[i] << "\n";
            }
            fBase_write.close();
        }
        // А ВОТ НА ИНАЧЕ ОСНОВНОЕ ДЕЙСТВИЕ
        else
        {
            for (int i = 0; i < vBase.size(); i++)
            {
                for (int j = 0; j < vTmp.size(); j++)
                {
                    // если находим одинаковые строки, то удаляем из tmp
                    if (vTmp[j] == vBase[i])
                    {
                        cout << "Совпала строка!" << endl;
                        cout << vTmp[j] << "\n\n";
                        vTmp.erase(vTmp.begin() + j); // указываем итератором, что надо удалять
                    }
                }
            }
        }
        cout << "Работа закончена, все сравнили, вот конечный тпмшник: " << endl;
        // выводим исправленный тпмшник
        for (int i = 0; i < vTmp.size(); i++)
        {
            cout << vTmp[i] << "\n";
        }
        cout << "Обновляю тмп в файл... " << endl;

        //remove(tmpstr.c_str()); // удаляем старый тмпшник
        f_write.open(tmpstr, ios_base::trunc); // удалить содержимое файла, если он существует
        f_write.close();

        f_write.open(tmpstr);
        for (int i = 0; i < vTmp.size(); i++)
        {
            f_write << vTmp[i] << "\n";
        }
        f_write.close();

        // тут открываем файл тред-базы, чтобы туда в конец дописать файлы
        fBase_write.open(thread_path, ios_base::app); // открываем файл для записи в конец
        // дописываем в конец обновленный тмп
        for (int i = 0; i < vTmp.size(); i++)
        {
            fBase_write << vTmp[i] << "\n";
        }
    }
};

int main()
{
    setlocale(LC_ALL, "rus");
    /*
    string s; // сюда будем класть считанные строки
    ifstream file("krol.html"); // файл из которого читаем (для линукс путь будет выглядеть по другому)

    while (getline(file, s)) { // пока не достигнут конец файла класть очередную строку в переменную (s)
        cout << s << endl; // выводим на экран
        s += "\n"; // что нибудь делаем со строкой например я добавляю плюсик в конце каждой строки
        cout << s << endl; // и снова вывожу на экран но уже модифицированную строку (без записи ее в файл)
    }

    file.close(); // обязательно закрываем файл что бы не повредить его

    */

    anal krol; // создаем экземпляр класса анал

    int kolvo;
    string string_user;   // ID пользователя
    string string_thread; // НАЗВАНИЕ ТРЕДА
    //string string1 = "parsetext.html"; // путь (название файла для парса)

    string stringtext1 = "parsetext1.html"; // путь (название файла для парса)
    string stringtext2 = "parsetext2.html"; // путь (название файла для парса)
    string stringtext3 = "parsetext3.html"; // путь (название файла для парса)

    string string2;                               //= 'class="html - attribute - value">thread_image_box</span>" & gt; < / span>';
    string readystring = globalDir + "READY.txt"; // стирнг для удаления реди тээкстэ
    string infostr = globalDir + "INFO.txt";      // стринг для получаения id и треда

    // тут мы просто получаем ключ для парса из файла (потому что вижла дурак блин☺)
    ifstream f;
    f.open(globalDir + "example.txt");
    while (!f.eof())
    {
        getline(f, string2);
    }
    f.close();
    //ifstream f1; // для проверки хтмльки

    //ifstream f2; // для проверки линк-базы
    cout << string2 << "vivod" << endl;

    ifstream fREADY;
    // файл, который создаст питон, чтобы дать понять парсеру, что была закачана хтмэлька + создан файл под запись линков

    //const char* name;
    //cout << "Введите кол-во символов, которое нужно вывести из файла: " << endl;
    //cin >> kolvo;
    //cout << "Введите название (путь) файла: " << endl;
    //getline(cin, string1, '*');
    //cout << string1 << endl;

    //cout << "Введите КЛЮЧ к парсу линка: " << endl;
    //getline(cin, string2, '*');
    //cout << string2 << endl;
    //kolvo = krol.simCount(string1); // получаем значение counter

    while (true)
    {
        fREADY.open(readystring); // пытаемся открыть файл

        while (!fREADY) // пока не существует хтмльки и линк-базы - спим (10c)
        {
            cout << "Жду файл 'READY'... " << endl;
#ifdef __unix__
            usleep(10000000); // sleeping in microseconds (unistd.h)
#elif _WIN32
            Sleep(10000); // sleeping in miliseconds (Windows.h)
#endif
            fREADY.open(readystring); // пытаемся открыть файл
        }

        fREADY.close();

        // тут мы получаем папку юзера и значение треда
        fREADY.open(infostr);
        cout << infostr << endl;
        getline(fREADY, string_user);
        getline(fREADY, string_thread);
        fREADY.close();

        cout << stringtext1 << " " << string2 << endl;
        cout << stringtext2 << " " << string2 << endl;
        cout << stringtext3 << " " << string2 << endl;

        cout << string_user << " " << string_thread << endl;

        // Из-за того, что файл с темп линками не хранился, а каждый раз удалялся и записывался заново,
        // я понял, что надо сразу открывать файл потом закрывать
        string tmpstr = globalDir + "botUsers" + "/" + string_user + "/" + "tmplinks.txt";
        ofstream file54;
        file54.close();

        // парметры, которые принимает функция getter:
        // 1) путь (название файла для парса)
        // 2) ключ для парса из файла (example.txt)
        // 3) ID пользователя
        // 4) НАЗВАНИЕ ТРЕДА

        krol.getter(stringtext1, string2, string_user, string_thread);
        krol.getter(stringtext2, string2, string_user, string_thread);
        krol.getter(stringtext3, string2, string_user, string_thread);

        // ВОТ ТУТ ДОЛЖЕН БЫТЬ ОТЛОВ ПОВТОРЯЕМОСТИ ССЫЛОК В КАЖДОМ ТРЕДЕ

        cout << "Цикл завершен!" << endl;

        cout << "Делаю проверку на совпадения тпшки и тред-базы..." << endl;
        krol.picBase_compare(string_user, string_thread);

        cout << "\n\n";
        cout << "Проверка завершена... файлы обновлены." << endl;

        remove(readystring.c_str()); // удаляем readystring

        cout << "ФАЙЛ 'READY.txt' удален. "
             << "\n";

        remove(infostr.c_str()); // удаляем INFO.txt
        cout << "ФАЙЛ 'INFO.txt' удален. "
             << "\n\n";
    }

    //krol.simPrint(kolvo, string1); // производим печать всего файла
    cout << "\n";

    //class="html-attribute-value">thread_image_box</span>"&gt;</span>.

    //
    system("pause");
    return 0;
}