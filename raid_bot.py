# -*- coding: utf-8 -*-
#--------------------[ МОДУЛИ ]------
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
#------------- [ CONNECT ] -----------
token = "0e7a9421621cb9c315b0d8acfe7b26f510ba34ef4029cc3a282858d5f4150fabc370e81c9763c4d52820e" #token group
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