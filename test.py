import keyboard,player,monster,time,random,loading

monster_lv1 = ['슬라임','좀비','스켈레톤']
monster_lv5 = ['고블린','망령','구울']
monster_lv10 = ['뱀파이어','늑대인간','고스트']
monster_lv15 = ['하피','사이클롭스','자이언트']


def vattle(player:player.Adventurer,monster: monster.Monster):
    while True:
        player.choice()
        monster.choice()

        # 서로가 공격할 때
        if player.state == 0 and monster.state == 0:
            monster.now_hp -= player.attack()
            player.now_hp -= monster.attack()
        
        # 플레이어는 방어, 몬스터는 공격
        elif player.state == 1 and monster.state == 0:
            result = monster.attack()
            player.defense(result,monster)

        # 플레이어는 공격, 몬스터는 방어
        elif player.state == 0 and monster.state == 1:
            result = player.attack()
            monster.defense(result,player)

        # 서로가 방어할 때
        elif player.state == 1 and monster.state == 1:
            player.print_message("서로 방패를 들고 경계하고 있다.")
            time.sleep(1)
            continue
        
        # 플레이어가 사망할 때
        if player.life(): break
        elif monster.life():
            player.now_hp = player.max_hp
            break


def get_monster(player:player.Adventurer,hunting_gorund):
    value = random.randint(1,100)%3
    mob = 0
    loading.loding()
    if(hunting_gorund==0):
        mob = monster.Monster(monster_lv1[value],1)
        time.sleep(2)
        vattle(player,mob)
    elif(hunting_gorund==1):
        mob = monster.Monster(monster_lv5[value],5)
        time.sleep(2)
        vattle(player,mob)
    elif(hunting_gorund==2):
        mob = monster.Monster(monster_lv10[value],10)
        time.sleep(2)
        vattle(player,mob)
    elif(hunting_gorund==3):
        mob = monster.Monster(monster_lv15[value],15)
        time.sleep(2)
        vattle(player,mob)

def hunting(player: player.Adventurer,hunting_ground):
    while True :
        player.print_message("몬스터 발견!\n K = 전투 || L = 도망")
        if keyboard.read_key()=="k" or keyboard.read_key()=="K":
            get_monster(player,hunting_ground)
            time.sleep(0.5)
        elif keyboard.read_key()=="l" or keyboard.read_key()=="L":
            time.sleep(0.5)
            return 0
        else : continue