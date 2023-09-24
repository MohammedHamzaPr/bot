import telebot
from telebot import types
from time import sleep
token = '6259659318:AAE8dKyM-cBR1yK1sNci28Gu2X12qIJwwL8'
bot = telebot.TeleBot(token)

bog_bounty = types.InlineKeyboardButton('اصتياد ثغرة', callback_data='bog_bounty')
programing = types.InlineKeyboardButton('برمجة', callback_data='programing')
photoshop = types.InlineKeyboardButton('فوتوشوب', callback_data='photochop')
call = types.InlineKeyboardButton('استشارة', callback_data='call')

@bot.message_handler(commands=['start'])
def start(message):
    b = types.InlineKeyboardMarkup()
    b.row_width=1
    b.add(bog_bounty)
    b.add(programing)
    b.add(photoshop)
    b.add(call)
    bot.reply_to(message,'حدد ماذا تريد',reply_markup=b)

@bot.callback_query_handler(lambda call:True)   

def pro(call):
    if call.data == 'programing':
        desktop = types.InlineKeyboardButton('برمجة تطبيقات سطح المكتب', callback_data='desktop')
        telegrab_bot = types.InlineKeyboardButton('برمجة بوتات تيليجرام', callback_data='telegrab_bot')
        web = types.InlineKeyboardButton(' برمجة موقع ويب', callback_data='web')
        android = types.InlineKeyboardButton('برمجة تطبيق هاتف', callback_data='android')
        anythink = types.InlineKeyboardButton('برمجة اداة او تطبيق معين', callback_data='anythink')
        programing_buttons = types.InlineKeyboardMarkup()
        programing_buttons.row_width=4
        programing_buttons.add(desktop)
        programing_buttons.add(telegrab_bot)
        programing_buttons.add(web)
        programing_buttons.add(android)
        programing_buttons.add(anythink)
        bot.edit_message_text(chat_id=call.message.chat.id,text='حدد ماذا تريد',message_id=call.message.message_id,reply_markup=programing_buttons)
    
    elif call.data == 'desktop':
        shup = types.InlineKeyboardButton('شراء الخدمة',callback_data='shup')
        last = types.InlineKeyboardMarkup()
        last.row_width = 1
        last.add(shup)
        bot.edit_message_text('خدمة برمجة تطبيقات سطح المكتب توفر لك تطبيقًا مخصصًا وقويًا يعمل على أنظمة الكمبيوتر الشخصية، مما يمكنك من تلبية احتياجات عملك أو مشروعك بكفاءة. نقدم تطبيقات تتميز بواجهات مستخدم سهلة الاستخدام وأداء متميز، مع إمكانية توسيعها وتخصيصها حسب احتياجاتك الفريدة. تتيح لك هذه الخدمة تحقيق أهدافك بسرعة وكفاءة على أجهزة سطح المكتب.',call.message.chat.id,call.message.message_id,reply_markup=last)

    elif call.data == 'android':
        shup = types.InlineKeyboardButton('شراء الخدمة',callback_data='shup')
        last = types.InlineKeyboardMarkup()
        last.row_width = 1
        last.add(shup)
        bot.edit_message_text('خدمة بيع تطبيقات الهاتف تقدم لك مجموعة متنوعة من التطبيقات المبتكرة والمفيدة لأنظمة تشغيل الهواتف الذكية. يمكنك تصفح متجرنا الرقمي للعثور على تطبيقات تلبي احتياجاتك، سواء كنت بحاجة إلى تطبيقات للترفيه، التعليم، الصحة، أو أي مجال آخر. تطبيقاتنا تتميز بواجهات سهلة الاستخدام وأداء ممتاز، مع دعم فني ممتاز وتحديثات منتظمة لضمان استمرارية العمل. نحن هنا لتلبية احتياجاتك وجعل تجربة استخدام التطبيقات أكثر سهولة ومتعة',call.message.chat.id,call.message.message_id,reply_markup=last)

    elif call.data == 'web':
        shup = types.InlineKeyboardButton('شراء الخدمة',callback_data='shup')
        last = types.InlineKeyboardMarkup()
        last.row_width = 1
        last.add(shup)
        bot.edit_message_text('خدمة برمجة مواقع مخصصة تقدم لك موقعًا أو تطبيقًا ويب فريدًا وجاذبًا يلبي احتياجاتك وأهدافك على الإنترنت، مع تصميم جذاب وأمان ممتاز ودعم مستمر',call.message.chat.id,call.message.message_id,reply_markup=last)

bot.polling()