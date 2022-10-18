import hikari, json




bot = hikari.GatewayBot(token="MTAyODY4MDAzNDEwNzUzMTI4NA.G0eCHS.r6EKCgTftShmdNG9dtoGm-y_9kK4a4pCpFCysI")

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    # If a non-bot user sends a message "hk.ping", respond with "Pong!"
    # We check there is actually content first, if no message content exists,
    # we would get None' here.
    if event.is_bot or not event.content:
        return

    if event.content.startswith("Приветик"):
        await event.message.respond("Привет")

    if event.content.startswith("ку"):
        await event.message.respond("Ну ти і кукушка")

    if event.content.startswith("Бот, владік красава?"):
        await event.message.respond("Да, він машина")


    if event.content.startswith("Картинка"):
        imgURL = event.content.split(' ')
        await event.message.respond(f'https://api.lorem.space/image/%7BimgURL[1]%7D?w=150&h=150%27')


bot.run()