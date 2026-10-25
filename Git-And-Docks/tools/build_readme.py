"""Generates the 7 language versions of the profile README.

Run from anywhere: python Git-And-Docks/tools/build_readme.py
Edit the texts in T below, then rerun; the LATEST block is refilled by the workflow.
"""
import os
import re
import sys
from urllib.parse import quote

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
USER = "Arkomiko"
BG_D, PINK, PINK2, VIOLET = "26222b", "ffc7ec", "ff8fc8", "b983ff"
BG_L, PINK_L, VIOLET_L, TEXT_L, TEXT_D = "fff5fb", "c2408f", "8e4fe0", "3b2f40", "e9dfee"

LANGS = ["ru", "en", "be", "uk", "pl", "ja", "zh"]
FILES = {
    "ru": "README.md",
    "en": "Git-And-Docks/README/EN-en.md",
    "be": "Git-And-Docks/README/BE-by.md",
    "uk": "Git-And-Docks/README/UK-ua.md",
    "pl": "Git-And-Docks/README/PL-pl.md",
    "ja": "Git-And-Docks/README/JA-jp.md",
    "zh": "Git-And-Docks/README/ZH-cn.md",
}
NAMES = {"ru": "Русский", "en": "English", "be": "Беларуская", "uk": "Українська", "pl": "Polski", "ja": "日本語", "zh": "中文"}
STATS_LOCALE = {"ru": "ru", "en": "en", "be": "en", "uk": "uk-ua", "pl": "pl", "ja": "ja", "zh": "cn"}
STREAK_LOCALE = {"ru": "ru", "en": "en", "be": "be", "uk": "uk", "pl": "pl", "ja": "ja", "zh": "zh_Hans"}
TYPING_FONT = {"ja": "M+PLUS+Rounded+1c", "zh": "Noto+Sans+SC"}

GAMES = ["Detroit: Become Human", "Kena: Bridge of Spirits", "Mirror's Edge", "Mirror's Edge Catalyst", "Dishonored", "Black Mesa"]
ARTISTS = [
    "Monstercat", "NCS", "Virtual Riot", "Geoxor", "Chime", "Exyl", "Stonebank", "Tristam", "Pixel Terror", "Braken",
    "The Eden Project", "Sex Whales", "TULE (Lost Sky)", "Sub Urban", "Grabbitz", "Paper Skies", "Teminite", "Bossfight",
    "Apashe", "Ace Aura", "Aero Chord", "Aiobahn", "Alan Walker", "Bishu", "Bonobo", "Bad Computer", "Crankdat",
]
ANIME_EN = ["Dr. Stone", "Cyberpunk: Edgerunners", "Gate", "Bocchi the Rock!", "Birdy the Mighty: Decode",
            "The Promised Neverland", "Steins;Gate", "Death Note", "Moriarty the Patriot"]

T = {}  # per-language strings

T["ru"] = dict(
    typing=["Неважно, какого ты цвета и пола. Главное — какой ты человек по своей сути",
            "В высшей степени печально, если человек хорошо относится к тем, кто полезен ему,", "и плохо — к тем, кто бесполезен",
            "Пишу код. Учусь. Делюсь. Повторяю.", "Автоматизирую всё подряд", "Превращаю данные в решения",
            "Творю свободно и даю творить другим"],
    b_from=("Откуда", "Это так важно?"), b_since=("В коде с", "2011"), b_status=("Статус", "ищу работу"), b_views="просмотры", stats_title="Arkomiko на GitHub",
    h=["Обо мне", "Стек", "Проекты", "Статистика GitHub", "Свежие видео и треки", "Любимое", "Связь", "Поддержать"],
    about="Пишу программы и игры, создаю музыку, моделирую в 3D и рисую дизайны — стараюсь понемногу преуспевать везде. "
          "Программирование осваиваю самостоятельно с 2011 года: всё началось ещё в начальной школе с модов "
          "для J2ME-игр (Java) на кнопочных Nokia и Sony Ericsson.",
    cells=[("Программы", "Десктоп и веб: Electron, Qt, PHP, Python. Автоматизирую всё, что можно автоматизировать."),
           ("Игры", "Три проекта на Unreal Engine 5 в работе. Опыт с Unity, Godot и Source."),
           ("3D", "Моделирование в Blender и Cinema 4D, рендер в RenderMan, текстуры в Substance."),
           ("Музыка", "FL Studio и Ableton. Релизы, каверы, саундтреки к играм."),
           ("Дизайн и видео", "Интерфейсы в Figma и Adobe XD, графика в Photoshop, монтаж в Premiere Pro, After Effects, DaVinci Resolve и CapCut."),
           ("Реверс и моддинг", "Разбираюсь, как устроены движки и программы изнутри: Source, Unreal, Unity, Godot, Blender, FL Studio, Ableton.")],
    facts=[("Сейчас делаю", "три игры на Unreal Engine 5"),
           ("Изучаю", "Vue, JavaScript, TypeScript, C++, CMake, Qt, Lua"),
           ("Ищу", "работу в компании, которая делает игры или приложения. Рассматриваю предложения и коллаборации"),
           ("Цели", "устроиться туда, где нужно программировать; выпустить все свои игры; создать то, что поможет творить другим, — лейбл, программы, фреймворки"),
           ("Спрашивайте", "о чём угодно, особенно о творчестве. Помогу с любой идеей"),
           ("Направления", "frontend, backend, fullstack, геймдев, мобильная разработка, 3D, ML, дизайн"),
           ("Геймджемы", "Ludum Dare 2023"),
           ("Вне кода", "музыка, игры, рисование")],
    stack=["Рабочий уровень", "Изучаю", "Фреймворки", "Движки и 3D", "Дизайн и видео", "Музыка", "Инструменты"],
    proj=dict(
        oshi="Portable-программа для настройки макро-клавиатуры на чипе CH552 (6 клавиш и ручка-энкодер): сочетания клавиш, мультимедиа, мышь и системные действия. Пишет настройки прямо в память устройства, драйвер не нужен.",
        c2ui="Source Filmmaker в современной оболочке: читает модели, материалы, карты и сессии SFM 1:1 и редактирует их сам, не запуская sfm.exe. Интерфейс в духе библиотеки Steam и Unreal Engine 5. Разработка приостановлена.",
        music="Сайт-плеер и каталог музыки Arkomiko: релизы, техно-демки, каверы, сэмпл-паки и лицензии. Статический сайт на Astro, плеер со спектрометром на Vue, тёмная и светлая темы.",
        mili="«Мипла» — отдельное окно, которое заменяет пианоролл любой DAW. Ноты ставятся методом LARD (Left Add / Right Delete): левая кнопка ставит ноту и сразу тянет её, правая удаляет, зажатая правая стирает протяжкой. Пропускает MIDI-клавиатуру в DAW в реальном времени, управляет play / stop / BPM через плагин MiliPlain Bridge (VST3, CLAP) и работает как MIDI-проигрыватель со встроенным звуком. Паттерн перетаскивается в DAW как MIDI-клип или в папку как .mid-файл.",
        goliath="Визуальная новелла: триллер, повседневность, философия, психология. Командный проект для Windows, macOS и Linux — на мне музыка и звук.",
        ue5=("Игры на Unreal Engine 5", "Три проекта в разработке. Подробности позже.")),
    activity="Активность за последний месяц", snake="Змейка, которая ест вклад на GitHub",
    latest_note="Список обновляется автоматически.",
    fav=["Игры", "Музыка", "Аниме", "Фильмы"], more="и многие другие",
    anime=["Доктор Стоун", "Киберпанк: Бегущие по краю", "Врата: Там бьются наши воины", "Bocchi the Rock!",
           "Могучая Бёрди", "Обещанный Неверленд", "Врата Штейна", "Тетрадь смерти", "Патриотизм Мориарти"],
    films=["Интерстеллар", "Начало", "Джокер", "Зелёная миля", "Брюс Всемогущий"],
    support="Поддержка помогает выпускать новые игры, музыку и инструменты.",
)

T["en"] = dict(
    typing=["No matter your colour or gender — what matters is who you are at heart",
            "It is deeply sad when a person treats well those who are useful to them,", "and badly those who are not",
            "Write code. Learn. Share. Repeat.", "Automating everything in sight", "Turning data into decisions",
            "Creating freely — and helping others create"],
    b_from=("From", "Does it matter?"), b_since=("Coding since", "2011"), b_status=("Status", "open to work"), b_views="profile views", stats_title="Arkomiko on GitHub",
    h=["About", "Tech stack", "Projects", "GitHub stats", "Latest videos and tracks", "Favourites", "Contacts", "Support"],
    about="I write software and games, make music, model in 3D and draw designs — trying to get a little better at everything. "
          "Self-taught in programming since 2011: it all started in primary school with mods for J2ME (Java) games "
          "on Nokia and Sony Ericsson keypad phones.",
    cells=[("Software", "Desktop and web: Electron, Qt, PHP, Python. If it can be automated, I automate it."),
           ("Games", "Three Unreal Engine 5 projects in progress. Experience with Unity, Godot and Source."),
           ("3D", "Modelling in Blender and Cinema 4D, rendering with RenderMan, texturing in Substance."),
           ("Music", "FL Studio and Ableton. Releases, covers and game soundtracks."),
           ("Design and video", "UI in Figma and Adobe XD, graphics in Photoshop, editing in Premiere Pro, After Effects, DaVinci Resolve and CapCut."),
           ("Reverse engineering and modding", "Digging into how engines and apps work inside: Source, Unreal, Unity, Godot, Blender, FL Studio, Ableton.")],
    facts=[("Working on", "three games in Unreal Engine 5"),
           ("Learning", "Vue, JavaScript, TypeScript, C++, CMake, Qt, Lua"),
           ("Looking for", "a job at a company that makes games or apps. Open to offers and collaborations"),
           ("Goals", "join a team where programming is the job; release all my games; build things that help others create — a label, apps, frameworks"),
           ("Ask me about", "anything, especially creative stuff. Happy to help with any idea"),
           ("Areas", "frontend, backend, full-stack, game dev, mobile, 3D, ML, design"),
           ("Game jams", "Ludum Dare 2023"),
           ("Outside of code", "music, games, drawing")],
    stack=["Working knowledge", "Learning", "Frameworks", "Engines and 3D", "Design and video", "Music", "Tools"],
    proj=dict(
        oshi="Portable tool for configuring a CH552-based macro keypad (6 keys and a rotary knob): key combos, media keys, mouse and system actions. Writes settings straight to the device memory — no driver needed.",
        c2ui="Source Filmmaker in a modern shell: reads SFM models, materials, maps and sessions 1:1 and edits them itself, without ever running sfm.exe. UI inspired by the Steam library and Unreal Engine 5. Development paused.",
        music="Arkomiko's music player site and catalogue: releases, tech demos, covers, sample packs and licences. Static Astro site, Vue player with a spectrum analyser, dark and light themes.",
        mili="“Mipla” is a standalone window that replaces the piano roll of any DAW. Notes follow the LARD method (Left Add / Right Delete): left click places a note and drags it right away, right click deletes, holding right erases with a swipe. It passes a MIDI keyboard through to the DAW in real time, drives play / stop / BPM via the MiliPlain Bridge plugin (VST3, CLAP) and also works as a MIDI player with built-in sound. Drag a pattern into the DAW as a MIDI clip or into a folder as a .mid file.",
        goliath="Visual novel: thriller, slice of life, philosophy, psychology. A team project for Windows, macOS and Linux — music and sound are my part.",
        ue5=("Unreal Engine 5 games", "Three projects in development. More to come.")),
    activity="Contributions over the last month", snake="Snake eating GitHub contributions",
    latest_note="This list updates automatically.",
    fav=["Games", "Music", "Anime", "Films"], more="and many more",
    anime=ANIME_EN, films=["Interstellar", "Inception", "Joker", "The Green Mile", "Bruce Almighty"],
    support="Support helps release new games, music and tools.",
)

T["be"] = dict(
    typing=["Няважна, якога ты колеру і полу. Галоўнае — які ты чалавек па сваёй сутнасці",
            "Вельмі сумна, калі чалавек добра ставіцца да тых, хто яму карысны,", "і дрэнна — да тых, хто бескарысны",
            "Пішу код. Вучуся. Дзялюся. Паўтараю.", "Аўтаматызую ўсё запар", "Ператвараю даныя ў рашэнні",
            "Ствараю свабодна і даю ствараць іншым"],
    b_from=("Адкуль", "Гэта так важна?"), b_since=("У кодзе з", "2011"), b_status=("Статус", "шукаю працу"), b_views="прагляды", stats_title="Arkomiko на GitHub",
    h=["Пра мяне", "Стэк", "Праекты", "Статыстыка GitHub", "Свежыя відэа і трэкі", "Любімае", "Сувязь", "Падтрымаць"],
    about="Пішу праграмы і гульні, ствараю музыку, мадэлюю ў 3D і малюю дызайны — стараюся патроху дасягаць поспеху ва ўсім. "
          "Праграмаванне асвойваю самастойна з 2011 года: усё пачалося яшчэ ў пачатковай школе з модаў "
          "для J2ME-гульняў (Java) на кнопачных Nokia і Sony Ericsson.",
    cells=[("Праграмы", "Дэсктоп і вэб: Electron, Qt, PHP, Python. Аўтаматызую ўсё, што можна аўтаматызаваць."),
           ("Гульні", "Тры праекты на Unreal Engine 5 у рабоце. Досвед з Unity, Godot і Source."),
           ("3D", "Мадэляванне ў Blender і Cinema 4D, рэндэр у RenderMan, тэкстуры ў Substance."),
           ("Музыка", "FL Studio і Ableton. Рэлізы, каверы, саўндтрэкі да гульняў."),
           ("Дызайн і відэа", "Інтэрфейсы ў Figma і Adobe XD, графіка ў Photoshop, мантаж у Premiere Pro, After Effects, DaVinci Resolve і CapCut."),
           ("Рэверс і модынг", "Разбіраюся, як уладкаваныя рухавікі і праграмы знутры: Source, Unreal, Unity, Godot, Blender, FL Studio, Ableton.")],
    facts=[("Зараз раблю", "тры гульні на Unreal Engine 5"),
           ("Вывучаю", "Vue, JavaScript, TypeScript, C++, CMake, Qt, Lua"),
           ("Шукаю", "працу ў кампаніі, якая робіць гульні або праграмы. Разглядаю прапановы і калабарацыі"),
           ("Мэты", "уладкавацца туды, дзе трэба праграмаваць; выпусціць усе свае гульні; стварыць тое, што дапаможа ствараць іншым, — лейбл, праграмы, фрэймворкі"),
           ("Пытайцеся", "пра што заўгодна, асабліва пра творчасць. Дапамагу з любой ідэяй"),
           ("Напрамкі", "frontend, backend, fullstack, геймдэў, мабільная распрацоўка, 3D, ML, дызайн"),
           ("Геймджэмы", "Ludum Dare 2023"),
           ("Па-за кодам", "музыка, гульні, маляванне")],
    stack=["Рабочы ўзровень", "Вывучаю", "Фрэймворкі", "Рухавікі і 3D", "Дызайн і відэа", "Музыка", "Інструменты"],
    proj=dict(
        oshi="Portable-праграма для наладкі макра-клавіятуры на чыпе CH552 (6 клавіш і ручка-энкодар): спалучэнні клавіш, мультымедыя, мыш і сістэмныя дзеянні. Запісвае налады проста ў памяць прылады, драйвер не патрэбны.",
        c2ui="Source Filmmaker у сучаснай абалонцы: чытае мадэлі, матэрыялы, карты і сесіі SFM 1:1 і рэдагуе іх сам, не запускаючы sfm.exe. Інтэрфейс у духу бібліятэкі Steam і Unreal Engine 5. Распрацоўка прыпынена.",
        music="Сайт-плэер і каталог музыкі Arkomiko: рэлізы, тэхна-дэма, каверы, сэмпл-пакі і ліцэнзіі. Статычны сайт на Astro, плэер са спектрометрам на Vue, цёмная і светлая тэмы.",
        mili="«Міпла» — асобнае акно, якое замяняе піяна-рол любой DAW. Ноты ставяцца метадам LARD (Left Add / Right Delete): левая кнопка ставіць ноту і адразу цягне яе, правая выдаляе, заціснутая правая сцірае працяжкай. Прапускае MIDI-клавіятуру ў DAW у рэальным часе, кіруе play / stop / BPM праз плагін MiliPlain Bridge (VST3, CLAP) і працуе як MIDI-плэер з убудаваным гукам. Патэрн перацягваецца ў DAW як MIDI-кліп або ў тэчку як .mid-файл.",
        goliath="Візуальная навела: трылер, паўсядзённасць, філасофія, псіхалогія. Камандны праект для Windows, macOS і Linux — на мне музыка і гук.",
        ue5=("Гульні на Unreal Engine 5", "Тры праекты ў распрацоўцы. Падрабязнасці пазней.")),
    activity="Актыўнасць за апошні месяц", snake="Змейка, якая есць унёсак на GitHub",
    latest_note="Спіс абнаўляецца аўтаматычна.",
    fav=["Гульні", "Музыка", "Анімэ", "Фільмы"], more="і многія іншыя",
    anime=ANIME_EN, films=["Інтэрстэлар", "Пачатак", "Джокер", "Зялёная міля", "Брус Усемагутны"],
    support="Падтрымка дапамагае выпускаць новыя гульні, музыку і інструменты.",
)

T["uk"] = dict(
    typing=["Неважливо, якого ти кольору і статі. Головне — яка ти людина по своїй суті",
            "Надзвичайно сумно, коли людина добре ставиться до тих, хто їй корисний,", "і погано — до тих, хто некорисний",
            "Пишу код. Вчуся. Ділюся. Повторюю.", "Автоматизую все підряд", "Перетворюю дані на рішення",
            "Творю вільно і даю творити іншим"],
    b_from=("Звідки", "Це так важливо?"), b_since=("У коді з", "2011"), b_status=("Статус", "шукаю роботу"), b_views="перегляди", stats_title="Arkomiko на GitHub",
    h=["Про мене", "Стек", "Проєкти", "Статистика GitHub", "Свіжі відео та треки", "Улюблене", "Зв'язок", "Підтримати"],
    about="Пишу програми та ігри, створюю музику, моделюю в 3D і малюю дизайни — намагаюся потроху встигати всюди. "
          "Програмування опановую самостійно з 2011 року: усе почалося ще в початковій школі з модів "
          "для J2ME-ігор (Java) на кнопкових Nokia та Sony Ericsson.",
    cells=[("Програми", "Десктоп і веб: Electron, Qt, PHP, Python. Автоматизую все, що можна автоматизувати."),
           ("Ігри", "Три проєкти на Unreal Engine 5 у роботі. Досвід з Unity, Godot і Source."),
           ("3D", "Моделювання в Blender і Cinema 4D, рендер у RenderMan, текстури в Substance."),
           ("Музика", "FL Studio та Ableton. Релізи, кавери, саундтреки до ігор."),
           ("Дизайн і відео", "Інтерфейси у Figma та Adobe XD, графіка в Photoshop, монтаж у Premiere Pro, After Effects, DaVinci Resolve та CapCut."),
           ("Реверс і модинг", "Розбираюся, як влаштовані рушії та програми зсередини: Source, Unreal, Unity, Godot, Blender, FL Studio, Ableton.")],
    facts=[("Зараз роблю", "три гри на Unreal Engine 5"),
           ("Вивчаю", "Vue, JavaScript, TypeScript, C++, CMake, Qt, Lua"),
           ("Шукаю", "роботу в компанії, яка робить ігри або застосунки. Розглядаю пропозиції та колаборації"),
           ("Цілі", "влаштуватися туди, де потрібно програмувати; випустити всі свої ігри; створити те, що допоможе творити іншим, — лейбл, програми, фреймворки"),
           ("Питайте", "про що завгодно, особливо про творчість. Допоможу з будь-якою ідеєю"),
           ("Напрями", "frontend, backend, fullstack, геймдев, мобільна розробка, 3D, ML, дизайн"),
           ("Геймджеми", "Ludum Dare 2023"),
           ("Поза кодом", "музика, ігри, малювання")],
    stack=["Робочий рівень", "Вивчаю", "Фреймворки", "Рушії та 3D", "Дизайн і відео", "Музика", "Інструменти"],
    proj=dict(
        oshi="Portable-програма для налаштування макроклавіатури на чипі CH552 (6 клавіш і ручка-енкодер): поєднання клавіш, мультимедіа, миша та системні дії. Записує налаштування прямо в пам'ять пристрою, драйвер не потрібен.",
        c2ui="Source Filmmaker у сучасній оболонці: читає моделі, матеріали, мапи та сесії SFM 1:1 і редагує їх сам, не запускаючи sfm.exe. Інтерфейс у дусі бібліотеки Steam та Unreal Engine 5. Розробку призупинено.",
        music="Сайт-плеєр і каталог музики Arkomiko: релізи, техно-демо, кавери, семпл-паки та ліцензії. Статичний сайт на Astro, плеєр зі спектрометром на Vue, темна та світла теми.",
        mili="«Мипла» — окреме вікно, яке замінює піаноролл будь-якої DAW. Ноти ставляться методом LARD (Left Add / Right Delete): ліва кнопка ставить ноту й одразу тягне її, права видаляє, затиснута права стирає протяжкою. Пропускає MIDI-клавіатуру в DAW у реальному часі, керує play / stop / BPM через плагін MiliPlain Bridge (VST3, CLAP) і працює як MIDI-програвач із вбудованим звуком. Патерн перетягується в DAW як MIDI-кліп або в теку як .mid-файл.",
        goliath="Візуальна новела: трилер, повсякденність, філософія, психологія. Командний проєкт для Windows, macOS і Linux — на мені музика та звук.",
        ue5=("Ігри на Unreal Engine 5", "Три проєкти в розробці. Подробиці згодом.")),
    activity="Активність за останній місяць", snake="Змійка, яка їсть внесок на GitHub",
    latest_note="Список оновлюється автоматично.",
    fav=["Ігри", "Музика", "Аніме", "Фільми"], more="та багато інших",
    anime=ANIME_EN, films=["Інтерстеллар", "Початок", "Джокер", "Зелена миля", "Брюс Всемогутній"],
    support="Підтримка допомагає випускати нові ігри, музику та інструменти.",
)

T["pl"] = dict(
    typing=["Nieważne, jakiego jesteś koloru i płci. Liczy się to, jakim jesteś człowiekiem",
            "To wielki smutek, gdy ktoś dobrze traktuje tych, którzy są mu przydatni,", "a źle tych, którzy są bezużyteczni",
            "Piszę kod. Uczę się. Dzielę się. Powtarzam.", "Automatyzuję wszystko, co się da", "Zamieniam dane w decyzje",
            "Tworzę swobodnie i pozwalam tworzyć innym"],
    b_from=("Skąd", "Czy to takie ważne?"), b_since=("Programowanie od", "2011"), b_status=("Status", "szukam pracy"), b_views="wyświetlenia", stats_title="Arkomiko na GitHubie",
    h=["O mnie", "Stack", "Projekty", "Statystyki GitHub", "Najnowsze filmy i utwory", "Ulubione", "Kontakt", "Wsparcie"],
    about="Piszę programy i gry, tworzę muzykę, modeluję w 3D i projektuję grafiki — staram się po trochu rozwijać we wszystkim. "
          "Programowania uczę się samodzielnie od 2011 roku: wszystko zaczęło się jeszcze w podstawówce od modów "
          "do gier J2ME (Java) na telefony z klawiaturą Nokia i Sony Ericsson.",
    cells=[("Programy", "Desktop i web: Electron, Qt, PHP, Python. Automatyzuję wszystko, co się da."),
           ("Gry", "Trzy projekty na Unreal Engine 5 w toku. Doświadczenie z Unity, Godot i Source."),
           ("3D", "Modelowanie w Blenderze i Cinema 4D, rendering w RenderMan, tekstury w Substance."),
           ("Muzyka", "FL Studio i Ableton. Wydania, covery, soundtracki do gier."),
           ("Design i wideo", "Interfejsy w Figmie i Adobe XD, grafika w Photoshopie, montaż w Premiere Pro, After Effects, DaVinci Resolve i CapCut."),
           ("Reverse engineering i modding", "Rozbieram silniki i programy, żeby zrozumieć, jak działają od środka: Source, Unreal, Unity, Godot, Blender, FL Studio, Ableton.")],
    facts=[("Teraz tworzę", "trzy gry na Unreal Engine 5"),
           ("Uczę się", "Vue, JavaScript, TypeScript, C++, CMake, Qt, Lua"),
           ("Szukam", "pracy w firmie, która tworzy gry lub aplikacje. Rozważam oferty i współpracę"),
           ("Cele", "praca tam, gdzie się programuje; wydanie wszystkich moich gier; stworzenie czegoś, co pomoże tworzyć innym — wytwórni, programów, frameworków"),
           ("Pytaj", "o cokolwiek, zwłaszcza o twórczość. Pomogę z każdym pomysłem"),
           ("Kierunki", "frontend, backend, fullstack, gamedev, aplikacje mobilne, 3D, ML, design"),
           ("Game jamy", "Ludum Dare 2023"),
           ("Poza kodem", "muzyka, gry, rysowanie")],
    stack=["Poziom roboczy", "Uczę się", "Frameworki", "Silniki i 3D", "Design i wideo", "Muzyka", "Narzędzia"],
    proj=dict(
        oshi="Przenośny program do konfiguracji klawiatury makro na układzie CH552 (6 klawiszy i pokrętło): skróty klawiszowe, multimedia, mysz i akcje systemowe. Zapisuje ustawienia bezpośrednio w pamięci urządzenia — bez sterowników.",
        c2ui="Source Filmmaker w nowoczesnej odsłonie: wczytuje modele, materiały, mapy i sesje SFM 1:1 i sam je edytuje, bez uruchamiania sfm.exe. Interfejs w stylu biblioteki Steam i Unreal Engine 5. Prace wstrzymane.",
        music="Strona-odtwarzacz i katalog muzyki Arkomiko: wydania, dema, covery, sample packi i licencje. Statyczna strona na Astro, odtwarzacz ze spektrometrem na Vue, motyw ciemny i jasny.",
        mili="„Mipla” to osobne okno, które zastępuje piano roll dowolnego DAW. Nuty wstawia się metodą LARD (Left Add / Right Delete): lewy przycisk stawia nutę i od razu ją przeciąga, prawy usuwa, przytrzymany prawy ściera pociągnięciem. Przepuszcza klawiaturę MIDI do DAW w czasie rzeczywistym, steruje play / stop / BPM przez wtyczkę MiliPlain Bridge (VST3, CLAP) i działa jako odtwarzacz MIDI z wbudowanym dźwiękiem. Wzorzec przeciąga się do DAW jako klip MIDI albo do folderu jako plik .mid.",
        goliath="Powieść wizualna: thriller, okruchy życia, filozofia, psychologia. Projekt zespołowy na Windows, macOS i Linux — moja działka to muzyka i dźwięk.",
        ue5=("Gry na Unreal Engine 5", "Trzy projekty w produkcji. Szczegóły później.")),
    activity="Aktywność z ostatniego miesiąca", snake="Wąż zjadający kontrybucje na GitHubie",
    latest_note="Lista aktualizuje się automatycznie.",
    fav=["Gry", "Muzyka", "Anime", "Filmy"], more="i wielu innych",
    anime=ANIME_EN, films=["Interstellar", "Incepcja", "Joker", "Zielona mila", "Bruce Wszechmogący"],
    support="Wsparcie pomaga wydawać nowe gry, muzykę i narzędzia.",
)

T["ja"] = dict(
    typing=["肌の色も性別も関係ない。大切なのは、その人の本質だ",
            "役に立つ人には優しく、役に立たない人には冷たくする――それは何より悲しいことだ",
            "コードを書く。学ぶ。共有する。繰り返す。", "なんでも自動化する", "データを決断に変える",
            "自由に創り、みんなが創れる場をつくる"],
    b_from=("出身", "それって大事？"), b_since=("コード歴", "2011年から"), b_status=("ステータス", "求職中"), b_views="閲覧数", stats_title="ArkomikoのGitHub統計",
    h=["自己紹介", "技術スタック", "プロジェクト", "GitHub統計", "最新の動画・楽曲", "お気に入り", "連絡先", "支援"],
    about="プログラムやゲームを作り、音楽を制作し、3Dモデリングやデザインも手がけています。どの分野でも少しずつ上達するのが目標です。"
          "プログラミングは2011年から独学で、小学生の頃にNokiaやSony Ericssonのガラケー向けJ2ME（Java）ゲームを改造したのが始まりでした。",
    cells=[("ソフトウェア", "デスクトップとWeb：Electron、Qt、PHP、Python。自動化できるものはすべて自動化します。"),
           ("ゲーム", "Unreal Engine 5で3本のゲームを開発中。Unity、Godot、Sourceの経験もあります。"),
           ("3D", "BlenderとCinema 4Dでモデリング、RenderManでレンダリング、Substanceでテクスチャ制作。"),
           ("音楽", "FL StudioとAbleton。オリジナル曲、カバー、ゲームのサウンドトラック。"),
           ("デザイン・映像", "FigmaとAdobe XDでUI、Photoshopでグラフィック、Premiere Pro・After Effects・DaVinci Resolve・CapCutで映像編集。"),
           ("リバースエンジニアリング・MOD", "エンジンやソフトの内部構造を探るのが好きです：Source、Unreal、Unity、Godot、Blender、FL Studio、Ableton。")],
    facts=[("開発中", "Unreal Engine 5で3本のゲーム"),
           ("学習中", "Vue、JavaScript、TypeScript、C++、CMake、Qt、Lua"),
           ("探しているもの", "ゲームやアプリを開発する会社での仕事。オファーやコラボも歓迎です"),
           ("目標", "プログラミングの仕事に就くこと、自分のゲームをすべてリリースすること、レーベル・ツール・フレームワークなど誰かの創作を支えるものを作ること"),
           ("気軽にどうぞ", "何でも聞いてください。特に創作の話なら大歓迎。どんなアイデアでもお手伝いします"),
           ("分野", "フロントエンド、バックエンド、フルスタック、ゲーム開発、モバイル、3D、ML、デザイン"),
           ("ゲームジャム", "Ludum Dare 2023"),
           ("コード以外", "音楽、ゲーム、お絵描き")],
    stack=["実務レベル", "学習中", "フレームワーク", "エンジン・3D", "デザイン・映像", "音楽", "ツール"],
    proj=dict(
        oshi="CH552チップ搭載のマクロキーパッド（6キー＋ロータリーノブ）を設定するポータブルツール。キーの組み合わせ、メディア操作、マウス、システム操作を割り当て、設定をデバイスのメモリに直接書き込みます。ドライバー不要。",
        c2ui="Source Filmmakerをモダンな外観で。SFMのモデル、マテリアル、マップ、セッションを1:1で読み込み、sfm.exeを起動せずに編集します。UIはSteamライブラリとUnreal Engine 5がモチーフ。開発は一時停止中。",
        music="Arkomikoの音楽プレイヤー兼カタログサイト。リリース、デモ、カバー、サンプルパック、ライセンス情報を掲載。Astroの静的サイトに、スペクトラム表示付きのVueプレイヤー。ダーク／ライトテーマ対応。",
        mili="「ミプラ」は、あらゆるDAWのピアノロールを置き換える独立ウィンドウ。ノートはLARD方式（Left Add / Right Delete）で入力：左クリックで配置してそのままドラッグ、右クリックで削除、右ボタンを押したままなぞると消去。MIDIキーボードの信号をリアルタイムでDAWへ中継し、プラグインMiliPlain Bridge（VST3・CLAP）でDAWの再生／停止／BPMを操作・同期します。内蔵音源付きのMIDIプレイヤーとしても動作。パターンはDAWへドラッグするとMIDIクリップに、フォルダへドラッグすると.midファイルになります。",
        goliath="ビジュアルノベル（スリラー／日常／哲学／心理）。Windows・macOS・Linux向けのチーム制作で、音楽とサウンドを担当。",
        ue5=("Unreal Engine 5のゲーム", "3本を開発中。詳細は後日。")),
    activity="直近1か月のアクティビティ", snake="GitHubのコントリビューションを食べるヘビ",
    latest_note="このリストは自動で更新されます。",
    fav=["ゲーム", "音楽", "アニメ", "映画"], more="ほか多数",
    anime=["Dr.STONE", "サイバーパンク エッジランナーズ", "GATE 自衛隊 彼の地にて、斯く戦えり", "ぼっち・ざ・ろっく！",
           "鉄腕バーディー DECODE", "約束のネバーランド", "シュタインズ・ゲート", "DEATH NOTE", "憂国のモリアーティ"],
    films=["インターステラー", "インセプション", "ジョーカー", "グリーンマイル", "ブルース・オールマイティ"],
    support="ご支援は新しいゲーム、音楽、ツールの制作に使われます。",
)

T["zh"] = dict(
    typing=["无论肤色与性别，重要的是你本质上是怎样的人",
            "只善待对自己有用的人，而冷待无用之人，这是最可悲的事",
            "写代码。学习。分享。重复。", "把一切都自动化", "把数据变成决策", "自由创作，也让他人自由创作"],
    b_from=("来自", "这很重要吗？"), b_since=("编程始于", "2011"), b_status=("状态", "求职中"), b_views="访问量", stats_title="Arkomiko 的 GitHub 统计",
    h=["关于我", "技术栈", "项目", "GitHub统计", "最新视频与音乐", "我的最爱", "联系方式", "支持我"],
    about="我写程序、做游戏、创作音乐、做3D建模，也画设计稿——每个领域都想一点点做得更好。"
          "2011年开始自学编程：最初是在小学时为诺基亚和索尼爱立信按键手机修改J2ME（Java）游戏。",
    cells=[("软件", "桌面与Web：Electron、Qt、PHP、Python。能自动化的，我都会自动化。"),
           ("游戏", "正在用Unreal Engine 5开发三款游戏。也用过Unity、Godot和Source。"),
           ("3D", "用Blender和Cinema 4D建模，用RenderMan渲染，用Substance制作材质。"),
           ("音乐", "FL Studio与Ableton。原创、Cover和游戏配乐。"),
           ("设计与视频", "用Figma和Adobe XD做界面，用Photoshop做图形，用Premiere Pro、After Effects、DaVinci Resolve和CapCut剪辑视频。"),
           ("逆向与Mod", "喜欢研究引擎和软件的内部原理：Source、Unreal、Unity、Godot、Blender、FL Studio、Ableton。")],
    facts=[("正在做", "用Unreal Engine 5开发三款游戏"),
           ("正在学", "Vue、JavaScript、TypeScript、C++、CMake、Qt、Lua"),
           ("寻找", "游戏或应用开发公司的工作机会，也欢迎合作邀约"),
           ("目标", "找到一份编程工作；发布自己所有的游戏；创造能帮助他人创作的东西——厂牌、软件、框架"),
           ("欢迎提问", "什么都可以问，尤其是创作相关的。任何想法我都乐意帮忙"),
           ("方向", "前端、后端、全栈、游戏开发、移动开发、3D、机器学习、设计"),
           ("Game Jam", "Ludum Dare 2023"),
           ("代码之外", "音乐、游戏、绘画")],
    stack=["熟练使用", "正在学习", "框架", "引擎与3D", "设计与视频", "音乐", "工具"],
    proj=dict(
        oshi="用于配置CH552芯片宏键盘（6个按键＋旋钮）的便携工具：快捷键、多媒体、鼠标和系统操作。设置直接写入设备内存，无需驱动。",
        c2ui="现代外壳下的Source Filmmaker：1:1读取SFM的模型、材质、地图和会话并直接编辑，无需运行sfm.exe。界面风格参考Steam库和Unreal Engine 5。开发已暂停。",
        music="Arkomiko的音乐播放与作品目录网站：发行作品、技术演示、Cover、采样包和授权信息。基于Astro的静态站点，Vue播放器带频谱显示，支持深色和浅色主题。",
        mili="「Mipla」是一个独立窗口，可替代任何DAW的钢琴卷帘。音符采用LARD方式（Left Add / Right Delete）输入：左键放置音符并立即拖动，右键删除，按住右键划过即可擦除。它能把MIDI键盘信号实时传入DAW，通过MiliPlain Bridge插件（VST3、CLAP）控制并同步DAW的播放、停止和BPM，也能作为自带音源的MIDI播放器使用。Pattern可直接拖进DAW成为MIDI片段，或拖到文件夹生成.mid文件。",
        goliath="视觉小说：惊悚、日常、哲学、心理。面向Windows、macOS和Linux的团队作品，我负责音乐与音效。",
        ue5=("Unreal Engine 5游戏", "三个项目开发中，详情稍后公布。")),
    activity="最近一个月的贡献", snake="吃掉GitHub贡献格子的贪吃蛇",
    latest_note="此列表自动更新。",
    fav=["游戏", "音乐", "动画", "电影"], more="等等",
    anime=["石纪元", "赛博朋克：边缘行者", "GATE 奇幻自卫队", "孤独摇滚！", "铁腕Birdy DECODE",
           "约定的梦幻岛", "命运石之门", "死亡笔记", "忧国的莫里亚蒂"],
    films=["星际穿越", "盗梦空间", "小丑", "绿里奇迹", "冒牌天神"],
    support="你的支持将用于制作新的游戏、音乐和工具。",
)


def shield_text(s):
    return quote(s.replace("-", "--").replace("_", "__"), safe="")


def badge(label, message, color=PINK, style="flat-square", logo=None):
    url = f"https://img.shields.io/badge/{shield_text(label)}-{shield_text(message)}-{color}?style={style}&labelColor={BG_D}"
    if logo:
        url += f"&logo={logo}&logoColor={PINK}"
    return url


def tag(name, logo=None):
    """Small dark badge with a single text segment, used for tech under project cards and stack extras."""
    url = f"https://img.shields.io/badge/{shield_text(name)}-{BG_D}?style=flat-square"
    if logo:
        url += f"&logo={logo}&logoColor={PINK}"
    return f'<img src="{url}" alt="{name}">'


def picture(dark, light, alt, attrs=""):
    return (f'<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="{dark}">\n'
            f'  <source media="(prefers-color-scheme: light)" srcset="{light}">\n'
            f'  <img src="{dark}" alt="{alt}"{attrs}>\n</picture>')


def typing(lang, color):
    t = T[lang]
    font = TYPING_FONT.get(lang, "Comfortaa")
    lines = ";".join(quote(l, safe="") for l in t["typing"])
    return (f"https://readme-typing-svg.demolab.com?font={font}&weight=600&size=17&duration=4000&pause=1500"
            f"&color={color}&center=true&vCenter=true&width=880&height=42&lines={lines}")


def skills(icons):
    return f'<img src="https://skillicons.dev/icons?i={icons}&perline=10" alt="{icons.replace(",", ", ")}">'


def build(lang):
    t = T[lang]
    root = lang == "ru"
    a = "Git-And-Docks/assets/" if root else "../assets/"
    h = t["h"]

    # language switcher: current language highlighted, others link to their files
    switch = []
    for l in LANGS:
        target = FILES[l] if root else ("../../README.md" if l == "ru" else os.path.basename(FILES[l]))
        if l == lang:
            switch.append(f'<img src="https://img.shields.io/badge/{shield_text(NAMES[l])}-{PINK}?style=for-the-badge" alt="{NAMES[l]}">')
        else:
            switch.append(f'<a href="{target}"><img src="https://img.shields.io/badge/{shield_text(NAMES[l])}-{BG_D}?style=for-the-badge" alt="{NAMES[l]}"></a>')

    views = (f"https://visitor-badge.laobi.icu/badge?page_id={USER}.{USER}&left_color=%23{BG_D}&right_color=%23{VIOLET}"
             f"&left_text={quote(t['b_views'], safe='')}")
    top_badges = " ".join([
        f'<img src="{badge(*t["b_from"])}" alt="{t["b_from"][0]}: {t["b_from"][1]}">',
        f'<img src="{badge(*t["b_since"])}" alt="{t["b_since"][0]} {t["b_since"][1]}">',
        f'<img src="{badge(*t["b_status"], color=VIOLET)}" alt="{t["b_status"][0]}: {t["b_status"][1]}">',
        f'<img src="{views}" alt="{t["b_views"]}">',
    ])

    cells = t["cells"]
    rows = []
    for i in range(0, 6, 3):
        tds = "".join(f'\n<td width="33%" valign="top"><b>{c[0]}</b><br><sub>{c[1]}</sub></td>' for c in cells[i:i + 3])
        rows.append(f"<tr>{tds}\n</tr>")
    what = "<table>\n" + "\n".join(rows) + "\n</table>"
    facts = "\n".join(f"- **{k}:** {v}" for k, v in t["facts"])

    s = t["stack"]
    stack_rows = [
        (s[0], skills("php,html,py"), [tag("SQL")]),
        (s[1], skills("js,ts,vue,cpp,cmake,lua"), []),
        (s[2], skills("electron,qt,bootstrap"), []),
        (s[3], skills("unreal,unity,godot,blender"), [tag("Source", "valve"), tag("Cinema 4D", "cinema4d"), tag("RenderMan")]),
        (s[4], skills("figma,ps,pr,ae,xd"), [tag("Substance"), tag("DaVinci Resolve", "davinciresolve"), tag("CapCut")]),
        (s[5], skills("ableton"), [tag("FL Studio")]),
        (s[6], skills("git,docker,visualstudio,vscode,idea,phpstorm"), [tag("draw.io", "diagramsdotnet")]),
    ]
    stack = "<table>\n" + "\n".join(
        f'<tr>\n<td width="170"><b>{name}</b></td>\n<td>{icons}{"<br>" + " ".join(extra) if extra else ""}</td>\n</tr>'
        for name, icons, extra in stack_rows) + "\n</table>"

    p = t["proj"]
    gh = f"https://github.com/{USER}/"

    def card(title, url, text, tags):
        head = f'<a href="{url}">{title}</a>' if url else title
        return (f'<td width="50%" valign="top">\n<h3>{head}</h3>\n{text}\n<br><br>\n'
                f'{" ".join(tags)}\n</td>')

    projects = "<table>\n<tr>\n" + "\n".join([
        card("OshiMakiKey Studio", gh + "OshiMakiKey-Studio", p["oshi"], [tag("C#", "dotnet"), tag(".NET 8"), tag("USB HID"), tag("Windows")]),
        card("SFM C2UI", gh + "SFM_C2UI", p["c2ui"], [tag("Python", "python"), tag("Qt 6", "qt"), tag("OpenGL", "opengl"), tag("Source Filmmaker", "valve")]),
    ]) + "\n</tr>\n<tr>\n" + "\n".join([
        card("Arkomiko.Music", gh + "Arkomiko.Music", p["music"], [tag("Astro", "astro"), tag("Vue 3", "vuedotjs"), tag("TypeScript", "typescript")]),
        card("MiliPlain", gh + "MiliPlain", p["mili"], [tag("MIDI"), tag("VST3"), tag("CLAP"), tag("LARD")]),
    ]) + "\n</tr>\n<tr>\n" + "\n".join([
        card("Goliath Child", "https://handakote.itch.io/goliathchild", p["goliath"], [tag("itch.io", "itchdotio"), tag("Visual Novel")]),
        card(p["ue5"][0], None, p["ue5"][1], [tag("Unreal Engine 5", "unrealengine"), tag("C++", "cplusplus")]),
    ]) + "\n</tr>\n</table>"

    def stats_url(dark):
        c = (dict(bg=BG_D, title=PINK, text=TEXT_D, icon=VIOLET, ring=PINK2) if dark
             else dict(bg=BG_L, title=PINK_L, text=TEXT_L, icon=VIOLET_L, ring="e0479e"))
        return (f"bg_color={c['bg']}&title_color={c['title']}&text_color={c['text']}&icon_color={c['icon']}"
                f"&ring_color={c['ring']}&hide_border=true&border_radius=12&locale={STATS_LOCALE[lang]}")

    rs = "https://github-readme-stats.vercel.app/api"
    stats_card = picture(f"{rs}?username={USER}&show_icons=true&include_all_commits=true&custom_title={quote(t['stats_title'], safe='')}&{stats_url(True)}",
                         f"{rs}?username={USER}&show_icons=true&include_all_commits=true&custom_title={quote(t['stats_title'], safe='')}&{stats_url(False)}",
                         "GitHub stats", ' height="180"')
    langs_card = picture(f"{rs}/top-langs/?username={USER}&layout=compact&langs_count=8&{stats_url(True)}",
                         f"{rs}/top-langs/?username={USER}&layout=compact&langs_count=8&{stats_url(False)}",
                         "Top languages", ' height="180"')
    sk = f"https://streak-stats.demolab.com?user={USER}&locale={STREAK_LOCALE[lang]}&border_radius=12&hide_border=true"
    streak = picture(
        f"{sk}&background={BG_D}&ring={PINK2}&fire={PINK2}&currStreakNum={PINK}&sideNums={PINK}&currStreakLabel={VIOLET}&sideLabels={TEXT_D}&dates=a99bb0&stroke=4a3f52",
        f"{sk}&background={BG_L}&ring=e0479e&fire=e0479e&currStreakNum={PINK_L}&sideNums={PINK_L}&currStreakLabel={VIOLET_L}&sideLabels={TEXT_L}&dates=7a6a80&stroke=f0d6e8",
        "GitHub streak")
    tr = f"https://github-trophies.vercel.app/?username={USER}&no-frame=true&no-bg=true&margin-w=6&row=1&column=7"
    trophies = picture(f"{tr}&theme=radical", f"{tr}&theme=flat", "GitHub trophies")
    ag = (f"https://activity-graph.vercel.app/graph?username={USER}&area=true&hide_border=true&radius=12"
          f"&custom_title={quote(t['activity'], safe='')}")
    activity = picture(
        f"{ag}&bg_color={BG_D}&color={TEXT_D}&title_color={PINK}&line={VIOLET}&point={PINK}&area_color={VIOLET}",
        f"{ag}&bg_color={BG_L}&color={TEXT_L}&title_color={PINK_L}&line=e0479e&point={VIOLET_L}&area_color=f9a8d4",
        t["activity"], ' width="100%"')
    raw = f"https://raw.githubusercontent.com/{USER}/{USER}/output/"
    snake = picture(raw + "snake-dark.svg", raw + "snake-light.svg", t["snake"], ' width="100%"')

    def fav_block(title, items):
        return f"<details>\n<summary><b>{title}</b></summary>\n\n" + "\n".join(f"- {x}" for x in items) + "\n\n</details>"

    fav = "\n\n".join([
        fav_block(t["fav"][0], GAMES),
        fav_block(t["fav"][1], [", ".join(ARTISTS) + f" {t['more']}"]),
        fav_block(t["fav"][2], t["anime"]),
        fav_block(t["fav"][3], t["films"]),
    ])

    def link_badge(name, url, logo, value=None):
        img = f"https://img.shields.io/badge/{shield_text(value or name)}-{BG_D}?style=for-the-badge&logo={logo}&logoColor={PINK}"
        return f'<a href="{url}"><img src="{img}" alt="{name}"></a>'

    contacts = " ".join([
        link_badge("Email", "mailto:Arikomika@gmail.com", "gmail", "Email"),
        link_badge("Telegram", "https://t.me/arkomiko_gr", "telegram"),
        link_badge("VK", "https://vk.com/arkomiko", "vk"),
        link_badge("X", "https://x.com/arkomiko21299", "x"),
        link_badge("YouTube", "https://www.youtube.com/@Arkomiko", "youtube"),
        link_badge("Arkomiko Music", "https://www.youtube.com/@arkomiko_music", "youtube"),
        link_badge("Twitch", "https://www.twitch.tv/arkomiko", "twitch"),
        link_badge("TikTok", "https://www.tiktok.com/@arkomiko_tt", "tiktok"),
        link_badge("SoundCloud", "https://soundcloud.com/arkomiko", "soundcloud"),
    ])
    support = " ".join([
        link_badge("Boosty", "https://boosty.to/arkomiko", "boosty"),
        link_badge("Ko-fi", "https://ko-fi.com/arkomiko", "kofi"),
    ])

    logo = picture(a + "logo-dark.svg", a + "logo-light.svg", "Arkomiko", ' width="760"')
    typing_pic = picture(typing(lang, "FFC7EC"), typing(lang, "C2408F"), t["typing"][2], ' width="100%"')
    footer = ("https://capsule-render.vercel.app/api?type=waving&color=0:ffc7ec,50:ff8fc8,100:b983ff"
              "&height=110&section=footer")

    return f"""<div align="center">

{logo}

{typing_pic}

{" ".join(switch)}

{top_badges}

</div>

## {h[0]}

{t["about"]}

{what}

{facts}

## {h[1]}

{stack}

## {h[2]}

{projects}

## {h[3]}

<div align="center">

{stats_card}
{langs_card}

{streak}

{trophies}

{activity}

{snake}

</div>

## {h[4]}

<!-- LATEST:START -->
<!-- LATEST:END -->

<sub>{t["latest_note"]}</sub>

## {h[5]}

{fav}

## {h[6]}

<div align="center">

{contacts}

</div>

## {h[7]}

{t["support"]}

<div align="center">

{support}

<img src="{footer}" alt="" width="100%">

</div>
"""


LATEST = re.compile(r"<!-- LATEST:START -->.*?<!-- LATEST:END -->", re.S)


if __name__ == "__main__":
    for lang in LANGS:
        path = os.path.join(ROOT, FILES[lang])
        os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
        text = build(lang)
        # keep whatever the "Latest videos and tracks" workflow has already filled in
        if os.path.exists(path):
            old = LATEST.search(open(path, encoding="utf-8").read())
            if old:
                text = LATEST.sub(lambda _: old.group(0), text)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("wrote", FILES[lang])
