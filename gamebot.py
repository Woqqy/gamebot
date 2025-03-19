from aiogram import Bot, Dispatcher, F
from aiogram.utils.formatting import as_marked_section, Bold
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from file_id import file_id

# Хранение токена в переменной окружения
BOT_TOKEN = "7890530869:AAGxvjv6DNHvcHEiZrF3Fgai_ULZZcB5Qh0"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def create_keyboard(buttons: list, adjust=(2,)) -> ReplyKeyboardBuilder:
    kb_builder = ReplyKeyboardBuilder()
    for button_text in buttons:
        kb_builder.add(KeyboardButton(text=button_text))
    kb_builder.adjust(*adjust)
    return kb_builder.as_markup(resize_keyboard=True)


@dp.message(Command(commands=["start"]))
async def process_command_start(message: Message):
    keyboard1 = create_keyboard(["Да", "Нет"])

    await message.answer(
        text="Для использования необходимо согласие с "
             "<a href=\"https://docs.google.com/document/d/1ZwkomdyN1s40XVC_ni50-tQLOezXryOyjlVWQ8zNkt4/edit?usp=sharing\" "
             "rel=\"nofollow\" target=\"_blank\">пользовательским соглашением</a>.",
        parse_mode="html",
        reply_markup=(keyboard1)
    )


@dp.message(lambda message: message.text.lower() in ["да", "нет"])
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "нет":
        await message.answer('Использование бота прекращено.', reply_markup=ReplyKeyboardRemove())
        # Удаляем сообщения
        for i in range(3):
            try:
                await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - i)
            except Exception as e:
                print(f"Ошибка при удалении сообщения: {e}")
    elif message.text.lower() == "да":
        resize_keyboard = True
        keyboard2 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard2)


@dp.message(F.text == 'Симуляторы')
async def process_yet(message: Message):
    keyboard3 = create_keyboard(["назад", "следующая игра"])



    await message.answer_photo(photo=file_id['rp'],
                               caption='🎮 GTA 5 Role Play (RP) 🎮 '
                                       '\n'
                                       '\nGTA 5 Role Play — это режим, где игроки становятся персонажами в живом мире, создавая уникальные истории. Вам предстоит общаться, взаимодействовать и развивать своего героя, будь то полицейский, преступник или врач.😮'
                                       '\n'
                                       '\n🛠️ Минимальные системные требования:'
                                       '\n'
                                       '\nОперационная система: Windows 8.1/10 (64-bit)'
                                       '\nПроцессор: Intel Core i5-3470 / AMD FX-8350'
                                       '\nОЗУ: 8 ГБ'
                                       '\nВидеокарта: NVIDIA GeForce GTX 660 2GB / AMD Radeon HD 7870 2GB'
                                       '\nМесто на диске: 72 ГБ'
                                       '\nDirectX: Версия 11'
                                       '\n'
                                       '\n' 'Скачать игру: https://gta5rp.com', reply_markup=keyboard3
                               )

    await message.answer_video(video=file_id['gtavid'],
                               caption='Геймлей игры')

    await message.answer_video(video=file_id['gtagif'],
                               caption='Информация будет пополняться!')


@dp.message(F.text == 'следующая игра')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "следующая игра":
        keyboard3 = create_keyboard(["назад", "следующая игра.."])
        await message.answer_photo(photo=file_id['mflight'],
                                   caption='🛫 Microsoft Flight Simulator 🛬'
                                           '\n'
                                           '\nMicrosoft Flight Simulator — это самый реалистичный авиасимулятор, позволяющий игрокам ощутить себя настоящими пилотами в виртуальном небе. Игра предлагает потрясающе детализированные ландшафты, погодные условия и сотни моделей самолётов, позволяя игрокам летать по всему миру.😮'
                                           '\n'
                                           '\n🛠️ Минимальные системные требования:'
                                           '\n'
                                           '\nОперационная система: Windows 10 (64-bit)'
                                           '\nПроцессор: Intel Core i5-4460 / AMD Ryzen 3 1200.'
                                           '\nОЗУ: 8 ГБ'
                                           '\nВидеокарта: NVIDIA GeForce GTX 770 / AMD Radeon RX 570'
                                           '\nМесто на диске: 150 ГБ'
                                           '\nDirectX: Версия 11'
                                           '\n'
                                           '\n' 'Скачать игру: https://store.steampowered.com/app/1250410/Microsoft_Flight_Simulator_40th_Anniversary_Edition/?l=russian',
                                   reply_markup=keyboard3
                                   )


    await message.answer_video(video=file_id['flightvid'],
                               caption='Геймлей игры')

    await message.answer_video(video=file_id['sigma'],
                               caption='Информация будет пополняться!')

@dp.message(F.text == 'следующая игра..')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "следующая игра..":
        keyboard3 = create_keyboard(["назад"])
        await message.answer_photo(photo=file_id['goatsim'],
                                   caption='🐐 Goat Simulator 3 🐐'
                                           '\n'
                                           '\nGoat Simulator 3 — это абсурдный и весёлый симулятор козла, разработанный шведской студией Coffee Stain Studios. Игра продолжает традицию хаоса и разрушения, заложенную в предыдущих частях серии, предлагая ещё больше возможностей для креативного беспорядка.😮'
                                           '\n'
                                           '\n🛠️ Минимальные системные требования:'
                                           '\n'
                                           '\nОперационная система: Windows 10 (64-bit)'
                                           '\nПроцессор: Intel Core i5-2300 / AMD FX-6300'
                                           '\nОЗУ: 8 ГБ'
                                           '\nВидеокарта: NVIDIA GeForce GTX 960 / AMD Radeon R9 280'
                                           '\nМесто на диске: 25 ГБ'
                                           '\nDirectX: Версия 11'
                                           '\n'
                                           '\n' 'Скачать игру: Steam',
                                   reply_markup=keyboard3
                                   )

        await message.answer_video(video=file_id['goatvid'],
                                   caption='Геймлей игры')

        await message.answer_video(video=file_id['medvejonok'],
                                   caption='Информация будет пополняться!')



@dp.message(F.text == 'назад')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)

@dp.message(F.text == 'Хорроры')
async def process_yet(message: Message):
    keyboard3 = create_keyboard(["назад", "следуйущая игра"])

    await message.answer_photo(photo=file_id['fnaf'],
                               caption='🧸 Five Nights at Freddys 🧸'
                                       '\n'
                                       '\nFive Nights at Freddys — это культовая хоррор-игра, которая покорила сердца миллионов геймеров своей атмосферой напряжения и страха. Игрок берет на себя роль ночного охранника в пиццерии Freddy Fazbear’s Pizza, где ночью оживают аниматроники, и ваша задача — выжить пять ночей подряд.😮'
                                       '\n'
                                       '\n🛠️ Минимальные системные требования:'
                                       '\n'
                                       '\nОперационная система: Windows XP/Vista/7/8/10'
                                       '\nПроцессор: 2 ГГц'
                                       '\nОЗУ: 1 ГБ'
                                       '\nВидеокарта: с поддержкой OpenGL 2.1'
                                       '\nМесто на диске: 250 МБ'
                                       '\nDirectX: Версия 9.0c'
                                       '\n'
                                       '\n' 'Скачать игру: https://store.steampowered.com/app/319510/Five_Nights_at_Freddys/', reply_markup=keyboard3
                               )

    await message.answer_video(video=file_id['fnafvid'],
                               caption='Геймлей игры')

    await message.answer_video(video=file_id['fnafgif'],
                               caption='Информация будет пополняться!')


@dp.message(F.text == 'следуйущая игра')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "следуйущая игра":
        keyboard3 = create_keyboard(["назад", "следующая игра."])
        await message.answer_photo(photo=file_id['misside'],
                                   caption='📚 Misside 📚'
                                           '\n'
                                           '\nMisside — это визуальная новелла, жанр интерактивной литературы, где игрок участвует в развитии сюжета, принимая решения за главного героя. Эта игра особенно привлекательна для любителей романтических историй и драм, предлагая множество вариантов развития событий и разнообразные концовки.😮'
                                           '\n'
                                           '\n🛠️ Минимальные системные требования:'
                                           '\n'
                                           '\nПлатформа: ПК, мобильные устройства (Android, iOS)'
                                           '\nЖанр: Визуальная новелла, интерактивная история.'
                                           '\nТехнические требования: Обычно невысокие, главное — наличие устройства с экраном и возможностью запуска приложений'
                                           '\n'
                                           '\n' 'Скачать игру: PlayMarket, AppStore, Steam',
                                   reply_markup=keyboard3
                                   )

        await message.answer_video(video=file_id['misvid'],
                                   caption='Геймлей игры')

        await message.answer_video(video=file_id['misgif'],
                                   caption='Информация будет пополняться!')


@dp.message(F.text == 'следующая игра.')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "следующая игра.":
        keyboard3 = create_keyboard(["назад"])
        await message.answer_photo(photo=file_id['silenthill'],
                                   caption='🌀 Silent Hill 2 🌀'
                                           '\n'
                                           '\nSilent Hill 2 — это культовый психологический хоррор, разработанный Konami и выпущенный в 2001 году. Игра считается одним из лучших представителей жанра благодаря своей глубокой атмосфере, запутанному сюжету и символизму, который заставляет задуматься о человеческой природе и страхах..😮'
                                           '\n'
                                           '\n🛠️ Минимальные системные требования:'
                                           '\n'
                                           '\nОперационная система: Windows XP/Vista/7/8/10'
                                           '\nПроцессор: Intel Pentium III / AMD Athlon'
                                           '\nОЗУ: 128 МБ'
                                           '\nВидеокарта: DirectX 8.1 совместимая видеокарта'
                                           '\nМесто на диске: 1.4 ГБ'
                                           '\nDirectX: Версия 8.1'
                                           '\n'
                                           '\n' 'Скачать игру: Steam',
                                   reply_markup=keyboard3
                                   )

        await message.answer_video(video=file_id['silentvid'],
                                   caption='Геймлей игры')

        await message.answer_video(video=file_id['silentgif'],
                                   caption='Информация будет пополняться!')

@dp.message(F.text == 'назад')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)


@dp.message(F.text == 'Экшен')
async def process_yet(message: Message):
    keyboard3 = create_keyboard(["назад", "как обойти блокировку?"])
    await message.answer_photo(photo=file_id['colda'],
                               caption='🎮 Call of Duty 🎮'
                                       '\n'
                                       '\nCall of Duty — это легендарная серия шутеров от первого лица, известная своими динамичными боевыми действиями, захватывающими кампаниями и напряженными мультиплеерными сражениями. Игроки погружаются в эпичные битвы, происходящие в различных исторических эпохах и современных конфликтах.😮'
                                       '\n'
                                       '\n🛠️ Минимальные системные требования:'
                                       '\n'
                                       '\nОперационная система: Windows 10 (64-bit)'
                                       '\nПроцессор: Intel Core i3-4340 / AMD FX-6300'
                                       '\nОЗУ: 8 ГБ'
                                       '\nВидеокарта: NVIDIA GeForce GTX 670 / AMD Radeon HD 7950'
                                       '\nМесто на диске: 175 ГБ'
                                       '\nDirectX: Версия 12'
                                       '\n'
                                       '\n' 'Скачать игру: https://store.steampowered.com/app/1938090/Call_of_Duty/?l=russian'
                                       '\n'
                                       '\n🥶НЕДОСТУПНО В РОССИИ🥶',
                               reply_markup=keyboard3
                               )

    await message.answer_video(video=file_id['coldavid'],
                               caption='Геймлей игры')

    await message.answer_video(video=file_id['coldagif'],
                               caption='Информация будет пополняться!')



@dp.message(F.text == 'назад')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)


@dp.message(F.text == 'Ролевые игры')
async def process_yet(message: Message):
    keyboard3 = create_keyboard(["назад", "следующая игра...", "как обойти блокировку?"])
    await message.answer_photo(photo=file_id['skyrim'],
                               caption='🐉 The Elder Scrolls V: Skyrim 🐉'
                                       '\n'
                                       '\nThe Elder Scrolls V: Skyrim — это культовая ролевая игра, созданная студией Bethesda Game Studios, которая перенесёт вас в огромный открытый мир, полный приключений, драконов и древних тайн. Игроки берут на себя роль Драконорождённого, способного поглощать души драконов и использовать их силу для борьбы с угрозой, нависшей над Скайримом.😮'
                                       '\n'
                                       '\n🛠️ Минимальные системные требования:'
                                       '\n'
                                       '\nОперационная система: Windows 7/8/10 (64-bit)'
                                       '\nПроцессор: Intel Core i5-750 / AMD Phenom II X4 945'
                                       '\nОЗУ: 8 ГБ'
                                       '\nВидеокарта: NVIDIA GeForce GTX 470 / AMD Radeon HD 7870'
                                       '\nМесто на диске: 12 ГБ'
                                       '\nDirectX: Версия 11'
                                       '\n'
                                       '\n' 'Скачать игру: https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/?l=russian'
                                       '\n'
                                       '\n🥶НЕДОСТУПНО В РОССИИ🥶',
                               reply_markup=keyboard3
                               )

    await message.answer_video(video=file_id['skyrimvid'],
                               caption='Геймлей игры')

    await message.answer_video(video=file_id['skyrimgif'],
                               caption='Информация будет пополняться!')

@dp.message(F.text == 'следующая игра...')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "следующая игра...":
        keyboard3 = create_keyboard(["назад", "слеедующая игра"])
        await message.answer_photo(photo=file_id['elder'],
                                   caption='🔥 Elden Ring 🔥'
                                           '\n'
                                           '\nElden Ring — это action-RPG, разработанная японской студией FromSoftware, известной своими играми серии Dark Souls и Bloodborne. Игра была выпущена в феврале 2022 года и быстро завоевала популярность среди поклонников жанра.😮'
                                           '\n'
                                           '\n🛠️ Минимальные системные требования:'
                                           '\n'
                                           '\nОперационная система: Windows 10 (64-bit)'
                                           '\nПроцессор: Intel Core i5-8400 / AMD Ryzen 3 3300X'
                                           '\nОЗУ: 12 ГБ'
                                           '\nВидеокарта: NVIDIA GeForce GTX 1060 / AMD Radeon RX 580'
                                           '\nМесто на диске: 60 ГБ'
                                           '\nDirectX: Версия 12'
                                           '\n'
                                           '\n' 'Скачать игру: Steam',
                                   reply_markup=keyboard3
                                   )

    await message.answer_video(video=file_id['eldervid'],
                               caption='Геймлей игры')

    await message.answer_video(video=file_id['eldergif'],
                               caption='Информация будет пополняться!')

@dp.message(F.text == 'слеедующая игра')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "слеедующая игра":
        keyboard3 = create_keyboard(["назад"])
        await message.answer_photo(photo=file_id['souls'],
                                   caption='🔥 Dark Souls 🔥'
                                           '\n'
                                           '\nDark Souls — это культовая action-RPG, разработанная японской студией FromSoftware и выпущенная в 2011 году. Игра известна своей сложной боевой системой, мрачной атмосферой и захватывающим миром, полным тайн и опасностей.😮'
                                           '\n'
                                           '\n🛠️ Минимальные системные требования:'
                                           '\n'
                                           '\nОперационная система: Windows XP SP3 / Vista SP2 / 7 SP1'
                                           '\nПроцессор: Intel Core 2 Duo E6850 / AMD Phenom II X2 545'
                                           '\nОЗУ: 2 ГБ'
                                           '\nВидеокарта: GeForce 9800 GT / ATI Radeon HD 4870'
                                           '\nМесто на диске: 16 ГБ'
                                           '\nDirectX: Версия 9.0c'
                                           '\n'
                                           '\n' 'Скачать игру: Steam',
                                   reply_markup=keyboard3
                                   )

        await message.answer_video(video=file_id['soulsvid'],
                                   caption='Геймлей игры')

        await message.answer_video(video=file_id['soulsgif'],
                                   caption='Информация будет пополняться!')



@dp.message(F.text == 'назад')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)

@dp.message(lambda message: message.text.lower() in ["назад", "как обойти блокировку?"])
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "как обойти блокировку?":
        keyboard3 = create_keyboard(["назад"])
        await message.answer_photo(photo=file_id['vpn'],
                                   caption='Как обойти блокировку игр? 🎮'
                                           '\n'
                                           '\n1. VPN 🌐 — меняет IP, открывая доступ.'
                                           '\n2. DNS 🔄 — смени на Google DNS или Cloudflare.'
                                           '\n3. Tor 🧅 — для анонимности.'
                                           '\n4. Прокси 🔗 — скрывает твой IP.'
                                           '\n'
                                           '\n🎁 Рефералка со скидкой на VPN:'
                                           '\n👉 https://t.me/siriusvpnbot?start=R_n3lbuo 👈 '
                                           '\n'
                                           '\nИграй без границ! 🚀',
                                   reply_markup=keyboard3
                                   )


@dp.message(lambda message: message.text.lower() in ["назад", "как обойти блокировку?"])
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры",
             "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)
    elif message.text.lower() == "как обойти блокировку?":
        keyboard3 = create_keyboard(["назад"])
        await message.answer_photo(photo=file_id['vpn'],
                                   caption='Как обойти блокировку игр? 🎮'
                                           '\n'
                                           '\n1. VPN 🌐 — меняет IP, открывая доступ.'
                                           '\n2. DNS 🔄 — смени на Google DNS или Cloudflare.'
                                           '\n3. Tor 🧅 — для анонимности.'
                                           '\n4. Прокси 🔗 — скрывает твой IP.'
                                           '\n'
                                           '\n🎁 Рефералка со скидкой на VPN:'
                                           '\n👉 https://t.me/siriusvpnbot?start=R_n3lbuo 👈 '
                                           '\n'
                                           '\nИграй без границ! 🚀',
                                   reply_markup=keyboard3
                                   )


@dp.message(F.text == 'Как обойти блокировку?')
async def process_yet(message: Message):
    keyboard3 = create_keyboard(["назад"])
    await message.answer_photo(photo=file_id['vpn'],
                               caption='Как обойти блокировку игр? 🎮'
                                       '\n'
                                       '\n1. VPN 🌐 — меняет IP, открывая доступ.'
                                       '\n2. DNS 🔄 — смени на Google DNS или Cloudflare.'
                                       '\n3. Tor 🧅 — для анонимности.'
                                       '\n4. Прокси 🔗 — скрывает твой IP.'
                                       '\n'
                                       '\n🎁 Рефералка со скидкой на VPN:'
                                       '\n👉 https://t.me/siriusvpnbot?start=R_n3lbuo 👈 '
                                       '\n'
                                       '\nИграй без границ! 🚀',
                               reply_markup=keyboard3
                               )


@dp.message(F.text == 'назад')
async def process_yes_no(message: Message, bot: Bot):
    if message.text.lower() == "назад":
        keyboard71 = create_keyboard(
            ["Симуляторы", "Хорроры", "Ролевые игры", "Как обойти блокировку?"])
        await message.answer("Выберите жанр необходимой игры", reply_markup=keyboard71)




if __name__ == "__main__":
    dp.run_polling(bot)
