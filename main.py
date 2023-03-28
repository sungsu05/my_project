import time,player,opening,view


print("당신의 이름을 입력해주세요 : ",end='')
name = input()
opening.oppening()

men = player.Adventurer(name)
time.sleep(2)
view.move(men)
