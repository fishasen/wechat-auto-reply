from wxpy import *

bot=Bot()

#my_friend=bot.friends().search('asen',sex=MALE)
#my_friend = ensure_one(bot.search('asen'))
tuling = Tuling(api_key='a97254251ac44affa169b767794a296f')
friends=bot.friends()
group=bot.groups().search('鹤立鸭群')
@bot.register(friends,group)
def reply_my_friend(msg):
    #return '收到消息: {} ({})'.format(msg.text, msg.type)

    tuling.do_reply(msg)


embed()