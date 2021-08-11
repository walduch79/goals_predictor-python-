last_twenty = int(input("Number of goals scored in last twenty games: "))
last_five = int(input("Number of goals scored in last five games: "))

av_20 = float(last_twenty / 20)
av_5 = float(last_five / 5)

print(f"{av_20} is average goals per match in last 20 games")
print(f"{av_5} is average goals per match in last 5 games")

pre_index = float(av_20 - av_5)
print(f"prediction index is : {pre_index}")

def get_pre():
    if pre_index >= -0.35 and pre_index <= 0.35 :
        print(f"Value of {pre_index} seems to be neutral, avoid this match!")
    elif pre_index < -0.35 :
        print(f"It is very likely that there will be less goals than {av_5} scored this time!")
    else:
        print(f"In this case more goals than {av_5} is quite possible today!")

get_pre()

print("GOOD LUCK PAL !!! ")