#!/usr/bin/env python3



import requests
import wget
def api_pull():
    choice= input("What Pokemon would you like a picture of? ").lower()
    poke_api = (f'https://pokeapi.co/api/v2/pokemon/{choice}/')
    return poke_api # the value of url must be a valid url concatenated with user input!
def json_conv(api_pull):
    poke_api = requests.get(api_pull)
    json2python = poke_api.json()
    return json2python # the value of json2python is the whole dictionary of bulbasaur!
def api_slice(json_conv):
    poke_pic = json_conv["sprites"]["front_default"]# code goes here!
    return poke_pic # the value of poke_pic must be the URL of the "front_default" image!
def wget_pic(api_slice):
    url = api_slice
    wget.download(url, "/home/student/mycode/pokemon.png" )
    # image must be saved to /home/student/mycode
def main():
    wget_pic(api_slice(json_conv(api_pull())))
main()
