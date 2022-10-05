#!/bin/python3
#Rey Rivera
#Interview Question
#
#
#Translator Dictionary
#

english2spanish = {"hello":"hola","world":"mundo"}

def translate(userInput):
    userInput.lower();
    if userInput in english2spanish:
        print(english2spanish[userInput])
    else:
        print("Word not found in dictionary")

translate("hello")
translate("world")