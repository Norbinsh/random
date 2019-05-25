#!/usr/bin/env python3
"""This is meant as an experimental POC, ***do not*** use this for any production environments as is.

Will place a randomly generated password at the clipboard for easy paste as needed.

Password complexity as well as key combination can be configured.
"""

import os
import sys
import string
import pyperclip
import random
from configparser import ConfigParser
from pynput import keyboard

base_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_path, "config.ini")

if os.path.exists(config_path):
    config = ConfigParser()
    config.read(config_path)
else:
    print("Couldn't find config, Exiting.")
    sys.exit(1)

keys_combination = {eval('keyboard.Key.' + x) for x in config['clipboard_copying']['keys_combination'].split(',')}

password_length = config['password_generating']['length']

mixture_level = config['password_generating']['mixture_level']

possible_password_chars = {'0': string.ascii_lowercase, '1': string.ascii_lowercase + string.ascii_uppercase,
                           '2': string.ascii_lowercase + string.ascii_uppercase + string.digits,
                           '3': string.ascii_lowercase + string.ascii_uppercase + string.digits + '@#$%'}

legitimate_chars = possible_password_chars[mixture_level]

active_keys = set()


def on_press(key):
    if key in keys_combination:
        active_keys.add(key)
        if all(k in active_keys for k in keys_combination):
            to_clipboard()


def on_release(key):
    try:
        active_keys.remove(key)
    except KeyError:
        pass


def to_clipboard():
    pyperclip.copy(generate_password())


def generate_password():
    return ''.join(random.sample(legitimate_chars, len(legitimate_chars)))[:int(password_length)]


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print(on_press)
    listener.join()
