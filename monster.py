import player,os,random,time

class Monster(player.MainStatus):
    CLASS = "몬스터"
    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.max_hp = 60 * level
        self.now_hp = self.max_hp
        self.damage = 7*level
        self.armor = 3*level
        self.critical = 0.7 +(level/100)
        self.exp = 15 * level
        self.state = 0
        # 공격 = 0
        # 방어 = 1
        # 스킬 = 2~
        self.print_message(f"{self.CLASS},{self.name}등장!!")
    
    def print_info(func):
        def info(self,*args):
            os. system('cls')
            string = "─" * 100+"\n"
            # 상단 라인
            string += f"체력 : {self.bar(self.max_hp,self.now_hp)}   ({self.max_hp}/{self.now_hp})\n"
            # 체력 게이지 바
            string += f"| 이름 : {self.name} | 직업 : {self.CLASS} | lv {self.level} | Attack {self.damage} | Defense {self. armor} |"
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
    
    #생존 여부
    def life(self,target):
        if self.now_hp > 0: return False # 몬스터가 살아있다면 

        #몬스터가 죽었다면
        self.print_message(f"{self.CLASS} {self.name}를 처치 했다!! {self.exp} 경험치 획득!")
        time.sleep(1)
        target.get_exp(self.exp)
        return True
    
    #행동 선택
    def choice(self):
        # 공격 = 0
        # 방어 = 1
        # 스킬 = 2~
        random_value = random.randint(1,10)%2
        if random_value :
            self.state = 0
        else :
            self.sate = 1
