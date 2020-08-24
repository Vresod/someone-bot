# someone bot

this discord bot tags a random person whenever a message tags the bot. unless you remove some of the code it will automatically change its nickname to "someone".

## how use??????

for users: if "@someone" is in your message then it replies to your message with a random person in your server/guild

for admins: install the discord.py module via pip, put a discord bot token in a file called `tokenfile`, and run `./main.py`. if you want the bot to include other bots in its user pool then use `./main.py includeBots`. if you want the bot to not change its nickname to "someone" every time it turns on or joins a server use `./main.py dontChangeNick`. if you want the bot to not say the message that triggered the bot use `./main.py dontSayMessage`. these options can be used together.

for admins (who dont have server hardware): https://discord.com/api/oauth2/authorize?client_id=747243680271827064&permissions=67108864&scope=bot is the default instance of the bot. it is run by me, Vresod, the developer of the script. it uses none of the command line flags (meaning it will change its nickname every time it turns on, won't include bots in its user pool, and will say the message of whoever summoned the bot)

## why??????

reference to discord 2018 april fools joke, [Discord now has @someone](https://www.youtube.com/watch?v=BeG5FqTpl9U). 