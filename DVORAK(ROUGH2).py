#####################################################################
# author: Taylor DeMent  
# date: 5/1/2024    
# description: A ROUGH program that converts QWERTY keystrokes
# to DVORAK in a while loop (currently buggy)
#####################################################################
import keyboard

def ChangeKeyInput():
    if keyboard.is_pressed("q"):
        print("'")

    if keyboard.is_pressed("w"):
        print(",")

    if keyboard.is_pressed("e"):
        print(".")

    if keyboard.is_pressed("r"):
        print("p")

    if keyboard.is_pressed("t"):
        print("y")
        
    if keyboard.is_pressed("y"):
        print("f")

    if keyboard.is_pressed("u"):
        print("g")

    if keyboard.is_pressed("i"):
        print("c")

    if keyboard.is_pressed("o"):
        print("r")

    if keyboard.is_pressed("p"):
        print("l")

    if keyboard.is_pressed("a"):
        print("a")

    if keyboard.is_pressed("s"):
        print("o")

    if keyboard.is_pressed("d"):
        print("e")

    if keyboard.is_pressed("f"):
        print("u")

    if keyboard.is_pressed("g"):
        print("i")

    if keyboard.is_pressed("h"):
        print("d")

    if keyboard.is_pressed("j"):
        print("h")

    if keyboard.is_pressed("k"):
        print("t")

    if keyboard.is_pressed("l"):
        print("n")

    if keyboard.is_pressed(";"):
        print("s")

    if keyboard.is_pressed("z"):
        print(";")

    if keyboard.is_pressed("x"):
        print("q")

    if keyboard.is_pressed("c"):
        print("j")

    if keyboard.is_pressed("v"):
        print("k")

    if keyboard.is_pressed("b"):
        print("x")

    if keyboard.is_pressed("n"):
        print("b")

    if keyboard.is_pressed("m"):
        print("m")

    if keyboard.is_pressed(","):
        print("w")

    if keyboard.is_pressed("."):
        print("v")

    if keyboard.is_pressed("/"):
        print("z")
   
typing_loop = True

while True:
    ChangeKeyInput()

    









    