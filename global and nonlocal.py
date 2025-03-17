from global_scope import greeting

total_fruits=0

def play_level():
    level_fruits=0
    def collect_fruits():
        nonlocal level_fruits
        level_fruits+=(total_fruits+ 3)
    collect_fruits()# this initiates the update of level_fruits
    print(f"player you have {level_fruits}")# but what does this do
    global total_fruits
    total_fruits+=level_fruits

play_level()
print(f"this is {total_fruits}")
play_level()
print(f"this is {total_fruits}")
play_level()
print(f"this is{total_fruits}")
play_level()
print(f"this is {total_fruits}")

print(f"the final fruits={total_fruits}")
greeting("Charles")
