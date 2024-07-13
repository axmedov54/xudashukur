import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from config import BOT_TOKEN as token
from button import menyu,oqish,erkaklar,ayollar,gusl,quran1


bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

#28.06.2024 жума намозидан.05.07.2024 бомдод намозигача\n\nTong 03:45\n\nBomdod 04:40\n\nQuyosh 05:30\n\nPeshin 13:30\n\nAst 18:30\n\nShom 20:40\n\nXufton 22:20

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menyu)


@dp.message(F.text=='Xiva Navoz Vaqtlari⏲️')
async def echo_handler(message: Message) -> None:
    await message.answer(text="https://t.me/saidniyozsholikor/1624", reply_markup=menyu)
   
@dp.message(F.text=='Tongi Zikirlar🤲')
async def zikir(message: Message) -> None:
    await message.answer(text="«1)Розийту биллаҳи роббан ва бил ислами дийнан ва бимуҳаммадин соллаллоҳу алайҳи васаллама росула»\n\nМаъноси: “Аллоҳни раббим деб, Исломни диним деб, Муҳаммад алайҳиссаломни расул деб рози бўлдим”\n\n\n«2)Розийту биллаҳи роббан ва бил ислами дийнан ва бимуҳаммадин соллаллоҳу алайҳи васаллама росула», деса, унга жаннат вожиб бўлади», дедилар.\n\nМаъноси: “Аллоҳни раббим деб, Исломни диним деб, Муҳаммад алайҳиссаломни расул деб рози бўлдим”\n\n\n3)«Аллоҳумма инний асбаҳту ушҳидука ва ушҳиду ҳамалата ъаршика ва малаикатика ва жамийъа холқик, аннака анталлоҳу лаа илаҳа илла анта ваҳдака лаа шарийка лака ва анна Муҳаммадан ъабдука ва росулук»\n\nМаъноси: “Аллоҳим, албатта, мен тонг оттирдим. Сени ҳамда аршингни кўтарувчи фаришталарингни ва ҳамма халқ қилган нарсаларингни гувоҳ қилиб айтаманки, Сендан бошқа илоҳ йўқ, Муҳаммад соллаллоҳу алайҳи васаллам Сенинг банданг ва расулингдир”", reply_markup=menyu)

@dp.message(F.text=='Tungi Zikirlar🤲') 
async def zikir2(message:Message):
    await message.answer(text='«1)Амсайнаа ва амсал мулку лиллаҳи роббил ъаламийн. Аллоҳумма ас`алука хойра ҳазиҳил лайлати фатҳаҳаа ва насроҳаа ва нуроҳаа ва барокатаҳаа ва ҳудаҳаа ва аъузу бика мин шарри ма фийҳаа ва шарри маа баъдаҳаа»\n\nМаъноси: “Биз ҳам, мулк ҳам оламлар парвардигори Аллоҳники бўлган ҳолда кеч киргиздик. Эй Раббим, бу кечанинг яхшисини, фатҳ бўлишини, ғалабасини, нурини, баракасини, ҳидоятини сўрайман. Ва Сендан бу кечанинг ва бу кечадан кейингисининг ёмонлигидан паноҳ тилайман”2)Амсайнаа ва амсал мулку лиллаҳи роббил ъаламийн. Аллоҳумма ас`алука хойра ҳазиҳил лайлати фатҳаҳаа ва насроҳаа ва нуроҳаа ва барокатаҳаа ва ҳудаҳаа ва аъузу бика мин шарри ма фийҳаа ва шарри маа баъдаҳаа», деб айтсин.\n\nМаъноси: “Биз ҳам, мулк ҳам оламлар парвардигори Аллоҳники бўлган ҳолда кеч киргиздик. Эй Раббим, бу кечанинг яхшисини, фатҳ бўлишини, ғалабасини, нурини, баракасини, ҳидоятини сўрайман. Ва Сендан бу кечанинг ва бу кечадан кейингисининг ёмонлигидан паноҳ тилайман”\n\n\n3)«Аллоҳумма анта роббий ла илаҳа илла анта холақтаний ва ана ъабдука ва ана ъала ъаҳдика ва ваъдика мастатоъту аъузу бика мин шарри ма сонаъту, абуу лака биниъматика ъалаййа ва абуу бизамбий фағфирлий фаиннаҳу ла йағфируз зунуба илла анта»\n\nМаъноси: “Аллоҳим, Сен парвардигоримсан, Сендан бошқа илоҳ йўқ. Мени халқ қилдинг ва мен Сенинг қулингман. Мен Сенга берган ваъдамда ва Сенга берган аҳдимда қодир бўлганимча турибман. Қилган нарсаларимнинг ёмонидан Сенинг номинг билан паноҳ тилайман. Менга ато қилган неъматларингга иқрор бўлдим. Ва яна гуноҳларимга ҳам иқрор бўлдим. Менинг гуноҳларимни кечир. Чунки Сендан бошқаси гуноҳларни кечира олмайди”', reply_markup=menyu)
            

@dp.message(F.text=='Namoz O`qishni O`rganamiz☪️')
async def namoz2(message:Message):
  await message.answer(text='namoz o`qish',reply_markup=oqish)    

@dp.message(F.text=='Erkaklar🧔')
async def erkak(message:Message):
  await message.answer(text='namoz o`qish',reply_markup=erkaklar)

@dp.message(F.text=='Ayollar🧕')
async def ayol(message:Message):
  await message.answer(text='namoz o`qish',reply_markup=ayollar) 

#erkaklar
#22:34
@dp.message(F.text=='Bomdod')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namoz_organish_Erkaklar_5_mahal/136',caption='Bomdod Namozi Erkaklar uchun',reply_markup=erkaklar)  
 
@dp.message(F.text=='Peshin')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namoz_organish_Erkaklar_5_mahal/137',caption='Peshin Namozi Erkaklar uchun',reply_markup=erkaklar)  

@dp.message(F.text=='Asr')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namoz_organish_Erkaklar_5_mahal/138',caption='Asr Namozi Erkaklar uchun',reply_markup=erkaklar)  

@dp.message(F.text=='Shom')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namoz_organish_Erkaklar_5_mahal/139',caption='Shom Namozi Erkaklar uchun',reply_markup=erkaklar)  

@dp.message(F.text=='Xufton')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namoz_organish_Erkaklar_5_mahal/140',caption='Xufton Namozi Erkaklar uchun',reply_markup=erkaklar)  

#ayollar

@dp.message(F.text=='bomdod')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/4',caption='Bomdod Namozi Ayollar uchun',reply_markup=ayollar)  
 
@dp.message(F.text=='peshin')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/7',caption='Peshin Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='asr')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/8',caption='Asr Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='shom')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/9',caption='Shom Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='xufton')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/10',caption='Xufton Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='ortga🔙')
async def back(message:Message):
  await message.answer('asasiy menyu',reply_markup=menyu) 

#isllar
@dp.message(F.text=='Allohnig 99 Ismi')
async def ism(message:Message):
  await message.answer('Alloh\nar-Rahmon\nar-Rahiym\nal-Malik\nal-Quddus\nas-Salom\nal-Mo‘min\nal-Muhaymin\nal-Aziz\nal-Jabbor\nal-Mutakabbir\nal-Xoliq\nal-Bori’\nal-Musavvir\nal-G‘affor\nal-Qahhor\nal-Vahhob\nar-Razzoq\nal-Fattoh\nal-Aliym\nal-Qobiz\nal-Bosit\nal-Xofiz\nar-Rofe’\nal-Mu’izz\nal-Muzill\nas-Samiy’\nal-Basiyr\nal-Hakam\nal-Adl\nal-Latiyf\nal-Xabiyr\nal-Haliym\nal-Aziym\nal-G‘afur\nash-Shakur\nal-Aliy\nal-Kabiyr\nal-Hafiyz\nal-Muqiyt\nal-Hasiyb\nal-Jaliyl\nal-Kariym\nar-Raqiyb\nal-Mujiyb\nal-Vose’\nal-Hakiym\nal-Vadud\nal-Majiyd\nal-Bo’is\nash-Shahiyd\nal-Haq\nal-Vakiyl\nal-Qaviy\nal-Matiyn\nal-Valiy\nal-Hamiyd\nal-Muhsiy\nal-Mubdi’\nal-Mu’iyd\nal-Muhyi\nal-Mumiyt\nal-Hayy\nal-Qayyum\nal-Vojid\nal-Mojid\nal-Vohid\nas-Somad\nal-Qodir\nal-Muqtadir\nal-Muqaddim\nal-Muaxxir\nal-Avval\nal-Oxir\naz-Zohir\nal-Botin\nal-Voliy\nal-Muta’oliy\nal-Barr\nat-Tavvob\nal-Muntaqim\nal-Afuvv\nar-Ra`uf\nal-Molikul mulk\nZul jaloli val ikrom\nal-Muqsit\nal-Jome’\nal-G‘aniy\nal-Mug‘niy\nal-Mone’\naz-Zorr\nan-Nofe’\nan-Nur\nal-Hodiy\nal-Badiy’\nal-Boqiy\nal-Voris\nar-Rashiyd\nas-Sabur',reply_markup=menyu)

#Taxorat
@dp.message(F.text=='Taxorat Olish Tartibi🚿')
async def back(message:Message):
  await message.answer_video(video='https://t.me/Namoz_organish_Erkaklar_5_mahal/134',caption='Taxorat Olish',reply_markup=menyu) 

@dp.message(F.text=='G`usl Olish Tartibi🚿')
async def namoz2(message:Message):
  await message.answer(text='G`usl qilish',reply_markup=gusl)    

@dp.message(F.text=='erkaklar🧔')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namoz_organish_Erkaklar_5_mahal/133',caption='Erkaklar G`usl Olish',reply_markup=gusl)

@dp.message(F.text=='ayollar🧕')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/3',caption='Ayllar G`usl Olish',reply_markup=gusl) 


@dp.message(F.text=='ortga⬅️')
async def back(message:Message):
  await message.answer('Namoz O`qish',reply_markup=oqish) 


#01:48
#quran
#12:10
@dp.message(F.text=='Quran Audio🫀')
async def quran(message:Message):
  await message.answer(text='Quran Audio',reply_markup=quran1)  



@dp.message(F.text=='Al-Fatiha')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/2', reply_markup=quran1)

@dp.message(F.text=='Al-Baqarah')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/3', reply_markup=quran1)

@dp.message(F.text=='Al-Imran')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/4', reply_markup=quran1)

@dp.message(F.text=='An-Nisa')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/5', reply_markup=quran1)

@dp.message(F.text=='Al-Maidah')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/6', reply_markup=quran1)

@dp.message(F.text=='Al-Anam')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/7', reply_markup=quran1)

@dp.message(F.text=='Al-Araf')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/8', reply_markup=quran1)

@dp.message(F.text=='Al-Anfal')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/9', reply_markup=quran1)

@dp.message(F.text=='At-Tawbah')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/10', reply_markup=quran1)

@dp.message(F.text=='Yunus')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/11', reply_markup=quran1)

@dp.message(F.text=='Hud')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/12', reply_markup=quran1)

@dp.message(F.text=='Yusuf')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/13', reply_markup=quran1)

@dp.message(F.text=='Ar-Rad')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/14', reply_markup=quran1)

@dp.message(F.text=='Ibrahim')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/15', reply_markup=quran1)

@dp.message(F.text=='Al-Hijr')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/16', reply_markup=quran1)

@dp.message(F.text=='An-Nahl')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/17', reply_markup=quran1)

@dp.message(F.text=='Al-Isra')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/18', reply_markup=quran1)

@dp.message(F.text=='Al-Kahf')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/19', reply_markup=quran1)

@dp.message(F.text=='Maryam')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/20', reply_markup=quran1)

@dp.message(F.text=='Ta-Ha')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/21', reply_markup=quran1)

@dp.message(F.text=='Al-Anbiya')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/22', reply_markup=quran)

@dp.message(F.text=='Al-Hajj')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/23', reply_markup=quran1)

@dp.message(F.text=='Al-Muminun')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/24', reply_markup=quran1)

@dp.message(F.text=='An-Nur')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/25', reply_markup=quran1)

@dp.message(F.text=='Al-Furqan')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/26', reply_markup=quran1)

@dp.message(F.text=='Ash-Shuara')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/27', reply_markup=quran1)

@dp.message(F.text=='An-Naml')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/28', reply_markup=quran1)

@dp.message(F.text=='Al-Qasas')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/29', reply_markup=quran1)

@dp.message(F.text=='Al-Ankabut')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/30', reply_markup=quran1)

@dp.message(F.text=='Ar-Rum')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/31', reply_markup=quran1)

@dp.message(F.text=='Luqman')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/32', reply_markup=quran1)

@dp.message(F.text=='As-Sajda')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/33', reply_markup=quran1)

@dp.message(F.text=='Al-Ahzab')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/34', reply_markup=quran1)

@dp.message(F.text=='Saba')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/35', reply_markup=quran1)

@dp.message(F.text=='Fatir')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/36', reply_markup=quran1)

@dp.message(F.text=='Ya-Sin')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/37', reply_markup=quran1)

@dp.message(F.text=='As-Saffat')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/38', reply_markup=quran1)

@dp.message(F.text=='Sad')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/39', reply_markup=quran1)

@dp.message(F.text=='Az-Zumar')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/40', reply_markup=quran1)

@dp.message(F.text=='Ghafir')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/41', reply_markup=quran1)

@dp.message(F.text=='Fussilat')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/42', reply_markup=quran)

@dp.message(F.text=='Ash-Shura')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/43', reply_markup=quran1)

@dp.message(F.text=='Az-Zukhruf')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/44', reply_markup=quran1)

@dp.message(F.text=='Ad-Dukhan')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/45', reply_markup=quran1)

@dp.message(F.text=='Al-Jathiya')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/46', reply_markup=quran1)

@dp.message(F.text=='Al-Ahqaf')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/47', reply_markup=quran1)

@dp.message(F.text=='Muhammad')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/48', reply_markup=quran1)

@dp.message(F.text=='Al-Fath')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/49', reply_markup=quran1)

@dp.message(F.text=='Al-Hujurat')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/50', reply_markup=quran1)

@dp.message(F.text=='Qaf')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/51', reply_markup=quran1)

@dp.message(F.text=='Adh-Dhariyat')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/52', reply_markup=quran1)

@dp.message(F.text=='At-Tur')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/53', reply_markup=quran)

@dp.message(F.text=='An-Najm')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/54', reply_markup=quran1)

@dp.message(F.text=='Al-Qamar')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/55', reply_markup=quran1)

@dp.message(F.text=='Ar-Rahman')
async def quran(message:Message):
  await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/56', reply_markup=quran1)

@dp.message(F.text=='Al-Waqia')
async def quran(message:Message):
  await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/57', reply_markup=quran1)

@dp.message(F.text=='Al-Hadid')
async def quran(message:Message):
  await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/58', reply_markup=quran1)

@dp.message(F.text=='Al-Mujadila')
async def quran(message:Message):
   await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/59', reply_markup=quran1)

@dp.message(F.text=='Al-Hashr')
async def quran(message:Message):
  await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/60', reply_markup=quran1)

@dp.message(F.text=='Al-Mumtahina')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/61', reply_markup=quran1)

@dp.message(F.text=='As-Saff')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/62', reply_markup=quran1)

@dp.message(F.text=='Al-Jumua')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/63', reply_markup=quran1)

@dp.message(F.text=='Al-Munafiqun')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/64', reply_markup=quran1)

@dp.message(F.text=='At-Taghabun')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/65', reply_markup=quran1)

@dp.message(F.text=='At-Talaq')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/66', reply_markup=quran1)

@dp.message(F.text=='At-Tahrim')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/67', reply_markup=quran1)

@dp.message(F.text=='Al-Mulk')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/68', reply_markup=quran1)

@dp.message(F.text=='Al-Qalam')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/69', reply_markup=quran1)

@dp.message(F.text=='Al-Haqqa')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/70', reply_markup=quran1)

@dp.message(F.text=='Al-Maarij')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/71', reply_markup=quran1)

@dp.message(F.text=='Nuh')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/72', reply_markup=quran1)

@dp.message(F.text=='Al-Jinn')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/73', reply_markup=quran1)

@dp.message(F.text=='Al-Muzzammil')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/74', reply_markup=quran1)

@dp.message(F.text=='Al-Muddathir')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/75', reply_markup=quran1)

@dp.message(F.text=='Al-Qiyama')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/76', reply_markup=quran1)

@dp.message(F.text=='Al-Insan')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/77', reply_markup=quran1)

@dp.message(F.text=='Al-Mursalat')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/78', reply_markup=quran1)

@dp.message(F.text=='An-Naba')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/79', reply_markup=quran1)

@dp.message(F.text=='An-Naziat')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/83', reply_markup=quran1)

@dp.message(F.text=='Abasa')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/84', reply_markup=quran1)

@dp.message(F.text=='At-Takwir')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/85', reply_markup=quran1)

@dp.message(F.text=='Al-Buruj')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/86', reply_markup=quran1)

@dp.message(F.text=='At-Tariq')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/87', reply_markup=quran1)

@dp.message(F.text=='Al-Ala')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/88', reply_markup=quran1)

@dp.message(F.text=='Al-Ghashiyah')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/89', reply_markup=quran1)

@dp.message(F.text=='Al-Fajr')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/90', reply_markup=quran1)

@dp.message(F.text=='Al-Balad')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/91', reply_markup=quran1)

@dp.message(F.text=='Ash-Shams')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/92', reply_markup=quran1)

@dp.message(F.text=='Al-Layl')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/93', reply_markup=quran1)

@dp.message(F.text=='Ad-Duha')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/94', reply_markup=quran1)

@dp.message(F.text=='Ash-Sharh')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/95', reply_markup=quran1)

@dp.message(F.text=='At-Tin')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/96', reply_markup=quran1)

@dp.message(F.text=='Al-Alaq')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/97', reply_markup=quran1)

@dp.message(F.text=='Al-Qadr')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/98', reply_markup=quran1)

@dp.message(F.text=='Al-Bayyina')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/99', reply_markup=quran1)

@dp.message(F.text=='Az-Zalzala')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/100', reply_markup=quran1)

@dp.message(F.text=='Al-Adiyat')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/101', reply_markup=quran1)

@dp.message(F.text=='Al-Qaria')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/102', reply_markup=quran1)

@dp.message(F.text=='At-Takathur')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/103', reply_markup=quran1)

@dp.message(F.text=='Al-Asr')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/104', reply_markup=quran1)

@dp.message(F.text=='Al-Humaza')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/105', reply_markup=quran1)

@dp.message(F.text=='Al-Fil')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/106', reply_markup=quran1)

@dp.message(F.text=='Quraish')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/107', reply_markup=quran1)

@dp.message(F.text=='Al-Maun')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/108', reply_markup=quran1)

@dp.message(F.text=='Al-Kawthar')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/109', reply_markup=quran1)

@dp.message(F.text=='Al-Kafirun')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/110', reply_markup=quran1)

@dp.message(F.text=='An-Nasr')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/111', reply_markup=quran1)

@dp.message(F.text=='Al-Masad')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/112', reply_markup=quran1)

@dp.message(F.text=='Al-Ikhlas')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/113', reply_markup=quran1)

@dp.message(F.text=='Al-Falaq')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/114', reply_markup=quran1)

@dp.message(F.text=='An-Nas')
async def quran(message:Message):
    await message.answer_audio(audio='https://t.me/yasseraldosari_mp3/115', reply_markup=quran1)


@dp.message(F.text=='ortga<-')
async def back(message:Message):
  await message.answer('Asossiy menyu',reply_markup=menyu) 

#15:45


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Tugadi")