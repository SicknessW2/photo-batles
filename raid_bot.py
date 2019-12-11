# -*- coding: utf-8 -*-
#--------------------[ МОДУЛИ ]------
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
#------------- [ CONNECT ] -----------
token = "990f3c165cbc368b89d526714130101d532b27a62f4633ec342e00a18f1c64b9aaf6e0cac390293ef7071" #token group
group_id = "186306570"# ID group
vk_session = vk_api.VkApi(token = token) # Обработка access_token
longpoll = VkBotLongPoll(vk_session, group_id) # Данные для работы в сообществе
vk = vk_session.get_api()
#------------[ VARIBLE ]------------

color = [VkKeyboardColor.POSITIVE,VkKeyboardColor.PRIMARY,VkKeyboardColor.DEFAULT,VkKeyboardColor.NEGATIVE]

def create_keyboard(response):
	if True:
		keyboard = VkKeyboard(one_time=False)
		
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_line()
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))
		keyboard.add_button('WWWwwww vkbot.ru', color=random.choice(color))

	keyboard = keyboard.get_keyboard()
	return keyboard

#------------[ COMMANDS ] ----------
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
    	response = event.obj.text
    	keyboard = create_keyboard(response)
    	
    	while True:    		
    		vk.messages.send(
    		peer_id=event.obj.peer_id,
    		random_id = 0,
    		 sticker_id = '163',
    		 keyboard= keyboard
    		)
    		vk.messages.send(peer_id=event.obj.peer_id,random_id = 0, message = 'Чел ты...Чел ты...Чел ты...'*70,keyboard= keyboard)
    		vk.messages.send(
    		peer_id=event.obj.peer_id,
    		random_id = 0,
    		keyboard= keyboard,
    		message= '😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱😳🤪😵😡😠🤬😷🤒🤕🤢🤮🤧😇🤠🤥🤫🤭🧐🤓😈👿🤡👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👶🧒👦👧🧑👨👱‍♂🧔👩👱‍♀🧓👴👵👨‍⚕👩‍⚕👨‍🎓👩‍🎓👨‍🏫👩‍🏫👨‍⚖👩‍⚖👨‍🌾👩‍🌾👨‍🍳👩‍🍳👨‍🔧👩‍🔧👨‍🏭👩‍🏭👨‍💼👮‍♂👨‍🚀👷‍♂👷‍♀🕵‍♂🕵‍♂🎅🧙‍♀🧚‍♂🎅💃🏃‍♀🧘‍♀🧘‍♂🧘‍♂🐈🐅🐅🐅🐩🐶🐱🐈🐥🦆🐸🐊🍐🍒🍓🍑🍏🍋🍓🍄🍆🥑🍆🐣🦆🦆🦉🐸🐤🐓🦆🐸🐸🦉🦆🦆🦉🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🎙🎙🎙🎙😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱😳🤪😵😡😠🤬😷🤒🤕🤢🤮🤧😇🤠🤥🤫🤭🧐🤓😈👿🤡👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👶🧒👦👧🧑👨👱‍♂🧔👩👱‍♀🧓👴👵👨‍⚕👩‍⚕👨‍🎓👩‍🎓👨‍🏫👩‍🏫👨‍⚖👩‍⚖👨‍🌾👩‍🌾👨‍🍳👩‍🍳👨‍🔧👩‍🔧👨‍🏭👩‍🏭👨‍💼👮‍♂👨‍🚀👷‍♂👷‍♀🕵‍♂🕵‍♂🎅🧙‍♀🧚‍♂🎅💃🏃‍♀🧘‍♀🧘‍♂🧘‍♂🐈🐅🐅🐅🐩🐶🐱🐈🐥🦆🐸🐊🍐🍒🍓🍑🍏🍋🍓🍄🍆🥑🍆🐣🦆🦆🦉🐸🐤🐓🦆🐸🐸🦉🦆🦆🦉🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🎙🎙😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪😫😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱😳🤪😵😡😠🤬😷🤒🤕🤢🤮🤧😇🤠🤥🤫🤭🧐🤓😈👿🤡👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👶🧒👦👧🧑👨👱‍♂🧔👩👱‍♀🧓👴👵👨‍⚕👩‍⚕👨‍🎓👩‍🎓👨‍🏫👩‍🏫👨‍⚖👩‍⚖👨‍🌾👩‍🌾👨‍🍳👩‍🍳👨‍🔧👩‍🔧👨‍🏭👩‍🏭👨‍💼👮‍♂👨‍🚀👷‍♂👷‍♀🕵‍♂🕵‍♂🎅🧙‍♀🧚‍♂🎅💃🏃‍♀🧘‍♀🧘‍♂🧘‍♂🐈🐅🐅🐅🐩🐶🐱🐈🐥🦆🐸🐊🍐🍒🍓🍑🍏🍋🍓🍄🍆🥑🍆🐣🦆🦆🦉🐸🐤🐓🦆🐸🐸🦉🦆🦆🦉🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🎙🎙'*2,
    		attachment = 'wall-179382817_135'
    		)
