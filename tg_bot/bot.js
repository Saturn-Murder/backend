const TelegramAPI = require("node-telegram-bot-api")
const token = '6227029117:AAH_hpycXzA1-QIXggh2COl99fcP1JAUJ70';

const bot = new TelegramAPI(token,{
    polling: true
})

const listMat = ['хуй', 'блять', 'гандон', 'залупа', 'пенис', 'хер', 'вагина', 'сука', 'пидор', 'пизда']

bot.on('text', async (msg) =>{
    console.log(msg.text.toLowerCase())
    console.log(msg.text.replace('?','').replace('!','').replace(',','').replace('.','').toLowerCase())
    msg.text.replace('?','').replace('!','').replace(',','').replace('.','').split(' ').forEach(async val =>{
        if(listMat.includes(val.toLowerCase())){
            bot.banChatMember(msg.chat.id,msg.from.id)
            bot.deleteMessage(msg.chat.id,msg.message_id)
            await wait(10000)
            await bot.unbanChatMember(msg.chat.id,msg.from.id)
            console.log(msg.from.username,' unbaned')
        }
    })
    if(msg.text == '/stop' && msg.from.username == 'Dovi_t'){
        process.exit(0);
    }
})
 
function wait(time) {
    return new Promise(resolve => {
        setTimeout(resolve, time);
    });
}

