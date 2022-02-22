import discord
import wheelCollection
import wheel
import time
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()  # initialize discord client.
currentTime = time.localtime()  # initialize time object
TOKEN = os.getenv('DISCORD_TOKEN')  # save token
wheelLibrary = wheelCollection.wheelCollection()  # create wheel library
bot = commands.Bot(command_prefix='w.')  # initialize command prefix.


@client.event
async def on_ready():
    print(client.user, "has logged on")


# @client.event
@bot.command()
async def info(message):
    """
    Gets info.
    command: w.info
    :param message: message.
    :return: print server, author, and message id.
    """

    print("info", time.strftime("%H:%M:%S", currentTime))

    await message.send(message.guild)
    await message.send(message.author)
    await message.send(message.message.id)


@bot.command()
async def insert(message, arg1, *arg2):
    """
    creates a wheel.
    command: w.insert 'wheel_name' 'list_element_1', 'list_element_2', 'list_element_n'
    :param arg1: name of wheel
    :param arg2: elements of wheel.
    :param message: command
    :return: returns either that the wheel name is already used or wheel made successfully
    """

    print("creating wheel", time.strftime("%H:%M:%S", currentTime))

    cWheel = wheel.myWheel(arg1, list(arg2))  # create instance of wheel.

    if wheelLibrary.addWheel(cWheel):  # add wheel to library.
        await message.channel.send("wheel name already used!")
    else:
        await message.channel.send("wheel made successfully!")


@bot.command()
async def delete(message, arg1):
    """
    removes a new wheel.
    command: w.delete 'wheel_name'
    :param arg1: name of wheel
    :param message: command
    :return: returns either that the wheel name is already used or wheel made successfully
    """

    print("destroying wheel", time.strftime("%H:%M:%S", currentTime))

    if wheelLibrary.removeWheel(arg1):  # add wheel to library.
        await message.channel.send("wheel does not exists!")
    else:
        await message.channel.send("wheel removed successfully!")


@bot.command()
async def spin(message, arg1):
    """
    Spins a wheel in the library.
    command: w.spin 'wheel_name'
    :param arg1: name of wheel
    :param message: command.
    :return: Spins wheel: arg1 or returns wheel does not exist.
    """

    print("spinning elements", time.strftime("%H:%M:%S", currentTime))

    if wheelLibrary.inLibrary(arg1) < 0:
        await message.channel.send("wheel does not exists!")
    else:
        await message.channel.send(wheelLibrary.spinWheel(arg1))


@bot.command()
async def add(message, arg1, *arg2):
    """
    add element to wheel name.
    command: w.add 'wheel_name' 'wheel_name' 'list_element_1', 'list_element_2', 'list_element_n'
    :param arg1: name of wheel
    :param arg2: elements
    :param message: command.
    :return: Spins wheel: arg1 or returns wheel does not exist.
    """

    print("adding elements", time.strftime("%H:%M:%S", currentTime))

    if wheelLibrary.inLibrary(arg1) < 0:
        await message.channel.send("wheel does not exists!")
    else:
        await message.channel.send(wheelLibrary.addElements(arg1, list(arg2)))


@bot.command()
async def remove(message, arg1, *arg2):
    """
    add element to wheel name.
    command: w.add 'wheel_name' 'wheel_name' 'list_element_1', 'list_element_2', 'list_element_n'
    :param arg1: name of wheel
    :param arg2: elements
    :param message: command.
    :return: Spins wheel: arg1 or returns wheel does not exist.
    """

    print("removing elements", time.strftime("%H:%M:%S", currentTime))

    if wheelLibrary.inLibrary(arg1) < 0:
        await message.channel.send("wheel does not exists!")
    else:
        await message.channel.send(wheelLibrary.removeElements(arg1, list(arg2)))

@bot.command()
async def showAll(message):
    """
    show all wheel names.
    command: w.showAll
    :param message: command.
    :return: Spins wheel: arg1 or returns wheel does not exist.
    """

    print("printing wheels", time.strftime("%H:%M:%S", currentTime))


@bot.command()
async def show(message, arg1):
    """
    show wheel elements.
    command: w.show 'wheel_name'
    :param arg1: name of wheel
    :param arg2: elements
    :param message: command.
    :return: Spins wheel: arg1 or returns wheel does not exist.
    """

    print("printing wheel", time.strftime("%H:%M:%S", currentTime))


if __name__ == "__main__":
    bot.run(TOKEN)
