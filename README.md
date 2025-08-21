# Как установить:

1. Если у вас нет Python, то установите его. Проверить наличие Python можно прописав в CMD `pip --version`. Если вам выводится версия, значит у вас уже установлен Python и вы можете переходить к пункту №2.
Как установить Python:
1.1 Переходите на https://www.python.org/downloads/ и качаете последнюю версию.
1.2 Ставите галочку напротив Add Python to PATH и нажимаете Customize Installation
1.3 Следующие пункты оставляете на значении по умолчанию.
2. После этого вам нужно установить используемую библиотеку requests. Открываете командную строку и пишете `pip install requests`. Если вас просят прописать определённую команду, пишете её и потом заново устанавливаете requests.
3. Открываете лаунчер IDLE Python (либо любой другой редактор кода если у вас есть), открываете файл main.py (File -> Open), который нужно скачать из репозитории и нажимаете F5 чтобы запустить код.

Если у вас начала появляться информация об уровнях, то код работает. Результат будет в той же директории, что находится файл main.py. Результат будет заноситься в с каждым уровнем data-temp.json, так что вы можете выключать код во время работы (но есть шанс, что из-за этого вы можете потерять прогресс). С каждым запуском программы данные в data-temp.json добавляются в data.json. Не рекомендуется прекращать работу кода до того, как в консоль будет выведено `data and data-temp were succesfully merged`, иначе вы потеряете все данные.

Каждые 10 тыс. уровней будет создаваться резервная копия в директории bckp, с названием `data (Длина массива).json`. При желании вы можете изменить частоту бекапов, изменив 7 строчку на `BACKUP_FREQ = [Число]`

Также в файл `exist_levels.json` будут заноситься уровни, айди которых был сгенерировал и уже оказался в скане.

# Как загрузить уже существующие данные:

Качаете JSON файл из открытых источников, перемещаете в директорию с main.py и переименовываете в data.json. Если вы хотите вставить те данные с 1.9 миллионом уровней, то скачать их можно отсюда: https://mega.nz/file/fpRXEIRS#NZy50tf42sHdme184pM-7ilpQrMRsW7VWH7OBPCXEW4

en:

# How to install:

1. If you don't have Python, install it. You can check if Python is installed by typing `pip --version` in CMD. If a version number is displayed, Python is already installed and you can proceed to step 2.
How to install Python:
1.1 Go to https://www.python.org/downloads/ and download the latest version.
1.2 Check the box next to Add Python to PATH and click Customize Installation.
1.3 Leave the following items at their default values.
2. Next, you need to install the requests library. Open the command line and type pip install requests. If you are asked to enter a specific command, type it and then reinstall requests.
3. Open the IDLE Python launcher (or any other code editor you have), open the main.py file (File -> Open), which you need to download from the repository, and press F5 to run the code.

If information about the levels starts to appear, the code is working. The result will be in the same directory as the main.py file. The result will be recorded in data-temp.json with each level, so you can turn off the code while it is running (but there is a chance that you may lose progress because of this). Each time the program is run, the data in data-temp.json is added to data.json. It is not recommended to stop the code before the console displays `data and data-temp were successfully merged`, otherwise you will lose all data.

Every 10,000 levels, a backup copy will be created in the bckp directory, named `data (array length).json`. If desired, you can change the backup frequency by changing line 7 to `BACKUP_FREQ = [Number]`

Also, levels whose IDs have been generated and are already in the scan will be entered into the `exist_levels.json` file.

# How to load existing data:

Download the JSON file from open sources, move it to the directory with main.py, and rename it to data.json. If you want to insert data with 1.9 million levels, you can download it from here: https://mega.nz/file/fpRXEIRS#NZy50tf42sHdme184pM-7ilpQrMRsW7VWH7OBPCXEW4
