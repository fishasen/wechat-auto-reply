from wxpy import *

bot=Bot()

#my_friend=bot.friends().search('asen',sex=MALE)
#my_friend = ensure_one(bot.search('asen'))
xiaoi = XiaoI('32WPFjlNaxua', 'YBxl0PO00crP8L8MbBYH')
friends=bot.friends()
#group=bot.groups().search('鹤立鸭群')
@bot.register(friends)
def reply_my_friend(msg):
    #return '收到消息: {} ({})'.format(msg.text, msg.type)

    xiaoi.do_reply(msg)


embed()