scene.set_background_color(9)
list2 = [21, 57, 74, 99, 130, 189, 267] #ascending list
my_sprite = sprites.create(img("""
        ...................cc...
            ...............cccc63c..
            ..............c633336c..
            ..........cc.c6cc33333c.
            .........b55c6c55c33333c
            .........ff5c6c5ff33333c
            .........ff5c6c5ff6333cc
            .........b553c355c6666cc
            ..........b55355c333333c
            .........cc55555bcc3333c
            ........c5545554b55c33c.
            ........b54b4444bb5cbb..
            ........c455b4b5554c45b.
            ........c555c4c555c4c5c.
            ........c5555c5555c4c5c.
            .........ccccccccc..ccc.
    """),
    SpriteKind.player)
target = game.ask_for_number("What number?", 3)

low = 0
mid = 0
high = len(list2) - 1 #highest value of Array

def binary_search():
    global low, mid, high, list2, target
    while low <= high:
        mid = (low + high) / 2
        if list2[mid] < target: #lower list
            low = mid + 1
        elif list2[mid] > target: #upper list
            high = mid - 1
        else:
            return mid
    return -1 # if not found

found_index = binary_search()
if found_index == -1:
    my_sprite.say("sorry, I can't find your number")
else:
    my_sprite.say("found " + target + " at index " + found_index)