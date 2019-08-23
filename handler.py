from telegram.ext import CommandHandler, MessageHandler, Filters

def start(bot, update):
    mensagem = "CARA NA BOA, OU TU FALA QUEM TU É AGORA... OU TU.. EU VOU TE CAÇAR, ENTENDEU? E TU ACHA QUE EU TO TI-TIP-TE CHAMAN... IRMÃO, EU VOU ARREBENTAR A SUA VIDA IRMÃO. EU NÃO TENHO MAIS PROPÓSITO PARA VIVER A NÃO SER TE - - FO-DER CARA. MANO... TÁ FERRADO CARA"
    bot.send_message(chat_id=update.message.chat_id, text=mensagem)

def check_message(bot, update):
    corrected_words = list()

    message = update.message.text.split()
    message_id = update.message.message_id

    for word in message:
        if 'u' in word or 'ú' in word or 'U' in word or 'Ú' in word:
            word = word.replace('u', 'v')
            word = word.replace('ú', 'v')
            word = word.replace('U', 'V')
            word = word.replace('Ú', 'V')
            word = word + '*'
            corrected_words.append(word)

            corrected_string = ', '.join(corrected_words)

    if corrected_words:
        bot.send_message(update.message.chat_id, corrected_string, reply_to_message_id=message_id)

HANDLERS = [
    CommandHandler('start', start),
    #MessageHandler(Filters.text, check_message),
]
