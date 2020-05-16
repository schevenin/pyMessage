from pynput.keyboard import Key, Controller as KeyboardController
import random
import time
import math


keyboard = KeyboardController()
file = open("text.txt", "r")
list_of_words = file.read().split()
percent_finished = 0


def count(words):
    return len(words)


total_words = count(list_of_words)
countdown = 3


def type(words):
    global percent_finished
    word_count = 0
    for word in words:
        for character in word:
            keyboard.type(character)
        delay = random.uniform(0, 0.5)
        time.sleep(delay)
        word_count += 1
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        if (math.ceil(word_count / total_words * 100) > percent_finished):
            percent_finished = math.ceil(word_count / total_words * 100)
            print(str(percent_finished) + "% done.")


def main():
    if input("About to type " + str(total_words) + " words.\nReady to start? ").lower() == "yes":
        for i in range(countdown):
            print("Starting in", countdown - i)
            time.sleep(1)
        #type(list_of_words)
    else:
        print("Exiting.")


if __name__ == '__main__':
    main()
