import random,os,keyboard,time

class MainStatus:
    # 상수
    MAX_HP, DAMAGE, ARMOR, MAX_EXP, CRITICAL= 100, 20, 10, 100, 0.15
    MAX_MP,MAGIC_POWER = MAX_HP, DAMAGE*2
    CLASS = "모험가"

    #생성자
    def __init__(self,name,level=1):
        #이름,레벨,경험치 조정
        self.name, self.level, self.now_exp = name, level, 0
        #레벨에 따른  스탯 보정
        self.level_up()

        self.print_message(f"초보 {self.CLASS},{self.name}의 여정이 시작된다.")

    def level_up(self):
       self.max_hp = self.MAX_HP * self.level
       self.now_hp = self.max_hp
       self.damage = self.DAMAGE * self.level
       self.critical = self.CRITICAL + (self.level/100)
       self.armor = self.ARMOR * self.level
       self.max_exp = self.MAX_EXP * self.level
       self.max_mp = self.MAX_MP* self.level
       self.now_mp = self.max_mp
       self.magic_power = self.MAGIC_POWER
       self.state = 0
        # 공격 = 0
        # 방어 = 1
        # 스킬 = 2~
    
    ## 비례법칙을 이용한, 체력 게이지바
    def bar(self,max,now):
        try :
            bar = 30
            now = round(now/max*bar)
            return "■" * now + "□"*(bar-now)
        except ZeroDivisionError:
            return "■" * now + "□"*(bar-now)
    
    def print_info(func):
        def info(self,*args):
            os. system('cls')
            string = "─" * 100+"\n"
            # 상단 라인
            string += f"체력 : {self.bar(self.max_hp,self.now_hp)}   ({self.max_hp}/{self.now_hp})\n"
            # info
            message = func(self,*args)
            # 메시지
            string += f"\n{message}\n\n"+"─" * 100
            #메시지 출력과, 하단 라인 출력
            print(string)
        return info
    
    @print_info
    def print_message(self, s):
        return s

    #공격
    def attack(self):
        random_value = random.uniform(0,1)
        #자신의 크리티컬 확률이, 랜덤값 보다 크다면 
        if(random_value < self.critical):
            critical_damage = random.randint(self.damage*2,self.damage*3)
            self.print_message(f'{self.name}의 크리티컬 어택!! 피해량 [{critical_damage}]')
            time.sleep(1)
            return critical_damage
        else:
            value = int(self.damage*0.20)
            damage = random.randint(self.damage-value,self.damage+value)
            self.print_message(f'{self.name}의 어택! 피해량 [{damage}]')
            time.sleep(1)
            return damage
    
   # 공격 방어    
    def defense(self,value,target):
        n = int(self.armor*0.20)
        random_value = (random.randint(self.armor-n,self.armor+n)*2) - value
        if 0 >= random_value:
            self.now_hp -= abs(random_value)
            self.print_message(f"상대방의 공격을 막아냈습니다. 감소된 받은 피해량 [{abs(random_value)}]")
            time.sleep(1)
        else:
            self.print_message(f"반격! 반격 데미지[{random_value}]")
            time.sleep(1)
            target.now_hp -= abs(random_value)
        
#######################################################################################################################################
#######################################################################################################################################

# player  모험가
class Adventurer(MainStatus):
    def print_info(func):
        def info(self,*args):
            os. system('cls')
            string = "─" * 100+"\n"
            # 상단 라인
            string += f"체력 : {self.bar(self.max_hp,self.now_hp)}   ({self.max_hp}/{self.now_hp})\n"
            string += f"마나 : {self.bar(self.max_mp,self.now_mp)}   ({self.max_mp}/{self.now_mp})\n"
            # 체력 게이지 바
            string += f"| 이름 : {self.name} | 직업 : {self.CLASS} | lv {self.level} | exp {self.max_exp}/{self.now_exp} | Attack {self.damage} | Defense {self. armor} |"
            # info
            message = func(self,*args)
            # 메시지
            string += f"\n{message}\n\n"+"─" * 100
            #메시지 출력과, 하단 라인 출력
            print(string)
        return info
    @print_info
    def print_message(self, s):
        return s
    
    def class_level_up(self,player: MainStatus):
        self.print_message("전직 조건을 충족했습니다! \n K = 기사  L = 자객")
        while True:
            if keyboard.read_key()=="k" or keyboard.read_key()=="K" :
                temp_name = self.name
                temp_level = self.level
                #player = Knight(temp_name,temp_level)
                break
            elif keyboard.read_key()=="l" or keyboard.read_key()=="L":
                temp_name = self.name
                temp_level = self.level
                #player = Assassin(temp_name,temp_level)
                break

    def get_exp(self,value):
        self.now_exp += value
        while self.now_exp >= self.max_exp:
            self.now_exp -= self.max_exp
            self.level_up()
            self.level += 1

    
    def life(self):
        if self.now_hp>0 : return False
        else :
            self.print_message(f"사망하셨습니다. 레벨이 감소됩니다.")
            time.sleep(1)
            self.level -= 1
            if 0 >= self.level : self.level = 1
            self.level_up()
            return True
    #행동 선택
    def choice(self):
        self.print_message("K키를 눌러 공격합니다, L키를 눌러 방어합니다.1,2,3, 숫자를 눌러 스킬을 사용합니다.\n 보유스킬[Q] : 모험가의 끈기!")
        while True:
            if keyboard.read_key()=="k" or keyboard.read_key()=="K" :
                self.state = 0
                # 공격 = 0
                # 방어 = 1
                # 스킬 = 2~
                break
            elif keyboard.read_key()=="l" or keyboard.read_key()=="L":
                self.state = 1
                break
            elif keyboard.read_key()=="q" or keyboard.read_key()=="Q":
                if(self.now_mp>30):
                    self.state = 1
                    self.now_mp -= 30
                    self.now_hp += random.randint(10,30)
                    if(self.now_hp>self.max_hp): self.now_hp = self.max_hp
                    self.print_message("모험가의 끈기를 사용하셨습니다.  일정수치량 체력이 회복됩니다. 방패를 들어 올립니다.")
                    time.sleep(0.5)
                    break
                else:
                    self.print_message("K키를 눌러 공격합니다, L키를 눌러 방어합니다.1,2,3, 숫자를 눌러 스킬을 사용합니다.\n보유스킬[1] : 모험가의 끈기!\n마나가 부족합니다.")
                    time.sleep(0.5)
                    continue
            else :
                continue 


#######################################################################################################################################
#######################################################################################################################################
            
#기사
class Knight(Adventurer):
    #상수 재 정의
    MAX_HP, DAMAGE, ARMOR, MAX_EXP, CRITICAL = 150, 15, 40, 150, 0.8
    MAX_MP,MAGIC_POWER = MAX_HP, DAMAGE*2
    CLASS = "기사"
    #생성자 재 정의
    def __init__(self,name,level=1):
        #이름,레벨,경험치 조정
        self.name, self.level, self.now_exp = name, level, 0
        #레벨에 따른  스탯 보정
        self.level_up()

        self.print_message(f"{self.CLASS} 전직!! ,{name}이 새로운 스킬을 획득했다.")


#######################################################################################################################################
#######################################################################################################################################


#자객
class Assassin(Adventurer):
    #상수 재 정의
    MAX_HP, DAMAGE, ARMOR, MAX_EXP, CRITICAL = 80, 15, 40, 150, 0.8
    MAX_MP,MAGIC_POWER = MAX_HP, DAMAGE*2
    CLASS = "기사"
    #생성자 재 정의
    def __init__(self,name,level=1):
        #이름,레벨,경험치 조정
        self.name, self.level, self.now_exp = name, level, 0
        #레벨에 따른  스탯 보정
        self.level_up()
        self.print_message(f"{self.CLASS} 전직!! ,{name}이 새로운 스킬을 획득했다.")

