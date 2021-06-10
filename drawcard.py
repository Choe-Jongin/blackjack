import time


class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    GRAY = '\033[90m'
    BRIGHTBLUE = '\033[94m'
# https://sosomemo.tistory.com/59

#1   ┏━━━━━━━━━━━┓ 
#2   ┃ A         ┃    
#3   ┃           ┃ 
#4   ┃           ┃ 
#5   ┃     ♠     ┃ 
#6   ┃           ┃  
#7   ┃           ┃ 
#8   ┃           ┃ 
#9   ┗━━━━━━━━━━━┛
#   ♠ ︎♣ ♥︎ ♦︎
def draw_card_by_line(card, line):
    s = '?'
    r = card[1]
    if card[0] == "Spade":
        s = '♠'
        print(Colors.BLACK, end = '')
    elif card[0] == "Heart":
        s = '♥︎'
        print(Colors.RED, end = '')
    elif card[0] == "Diamond":
        s = '♦'
        print(Colors.RED, end = '')
    elif card[0] == "Club":
        s = '♣'
        print(Colors.BLACK, end = '')
    else:
        print(Colors.BRIGHTBLUE, end = '')
        
    if line == 1:
        print("┏━━━━━━━━━━━┓",sep='', end ='')
    if line == 2:
        if r != 10 :
            print("┃",r,"          ┃",sep='', end = '')  #2
        else:
            print("┃",r,"         ┃",sep='', end = '')  #2 
    if line == 3:
        if r == 'A':
            print("┃           ┃",sep='', end='')
        elif r == 2:
            print("┃           ┃",sep='', end='')
        elif r == 3:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 4 :
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 5:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 6:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 7:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 8:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 9:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 10:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 'J' or r == 'Q' or r == 'K':
            print("┃           ┃",sep='', end='')
        else:
            print("┃x x x x x x┃",sep='', end='')
            
    elif line == 4:
        if r == 'A':
            print("┃           ┃",sep='', end='')
        elif r == 2:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 3:
            print("┃           ┃",sep='', end='')
        elif r == 4:
            print("┃           ┃",sep='', end='')
        elif r == 5:
            print("┃           ┃",sep='', end='')
        elif r == 6:
            print("┃           ┃",sep='', end='')
        elif r == 7:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 8:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 9:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 10:
            print("┃  ",s,"  ",s,"  ",s,"  ┃",sep='', end='')
        elif r == 'J' or r == 'Q' or r == 'K':
            print("┃           ┃",sep='', end='')
        else:
            print("┃ x x x x x ┃",sep='', end='')
            
    elif line == 5:
        if r == 'A':
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 2:
            print("┃           ┃",sep='', end='')
        elif r == 3:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 4:
            print("┃           ┃",sep='', end='')
        elif r == 5:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 6:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 7:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 8:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 9:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 10:
            print("┃           ┃",sep='', end='')
        elif r == 'J' or r == 'Q' or r == 'K':
            print("┃           ┃",sep='', end='')
        else:
            print("┃x x x x x x┃",sep='', end='')
        
    elif line == 6:
        if r == 'A':
            print("┃           ┃",sep='', end='')
        elif r == 2:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 3:
            print("┃           ┃",sep='', end='')
        elif r == 4:
            print("┃           ┃",sep='', end='')
        elif r == 5:
            print("┃           ┃",sep='', end='')
        elif r == 6:
            print("┃           ┃",sep='', end='')
        elif r == 7:
            print("┃           ┃",sep='', end='')
        elif r == 8:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 9:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 10:
            print("┃  ",s,"  ",s,"  ",s,"  ┃",sep='', end='')
        elif r == 'J' or r == 'Q' or r == 'K':
            print("┃           ┃",sep='', end='')
        else:
            print("┃ x x x x x ┃",sep='', end='')

    elif line == 7:   
        
        if r == 'A':
            print("┃           ┃",sep='', end='')
        elif r == 2:
            print("┃           ┃",sep='', end='')
        elif r == 3:
            print("┃     ",s,"     ┃",sep='', end='')
        elif r == 4:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 5:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 6:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 7:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 8:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 9:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 10:
            print("┃  ",s,"     ",s,"  ┃",sep='', end='')
        elif r == 'J' or r == 'Q' or r == 'K':
            print("┃           ┃",sep='', end='')
        else:
            print("┃x x x x x x┃",sep='', end='')
            
    elif line == 8:
        if r != 10 :
            print("┃          ",r,"┃",sep='', end = '')
        else:
            print("┃         ",r,"┃",sep='', end = '')
            
    elif line == 9:
        print("┗━━━━━━━━━━━┛",sep='', end ='')
        
    print(Colors.RESET, end = '')

def draw_cards_motion(cards,sec):
    
    timeq = sec/9
    time.sleep(timeq)
    
    for r in range(1,10):
        for c in cards:
           draw_card_by_line(c,r)
        print("")
        time.sleep(timeq)

def draw_cards(cards):
    draw_cards_motion(cards,0.18)

#①②⑤⑩⑳㉕㊿
coin = [1,2,5,10,20,25,50]                #동전의 종류(오름차순이여야 에러가 안남)
#과제 함수
def draw_chips(chips):

    #cache
    memoization = {coin[0] : [coin[0]]}

    #내부함수
    def inner_legal_payment(n):

        #basis
        if n <= 0:      #양수를 검사하게 될 경우 논리상
            return []   #이 조건을 만족할 일은 없지만 safey를 위해 넣은 구문

        #가능한 동전 조합들을 모두 담을 리스트(2차원 리스트)
        a = []

        #캐시에 n에 대한 값이 저장되어 있으면 다시 분기하지 않고 캐싱함
        if n in memoization.keys():
            return memoization[n]

        #캐싱되지 않았을 경우 조합을 직접 찾아냄
        for c in coin:
            if n < c :      #n이 동전 보다 작은 값이면 비교 할 필요 없음
                break
            if n == c :     #n이 동전과 같다면 해당 동전을 반환하고 끝
                a.append([c])
                break;
            if n > c:       #n이 동전(c) 보다 크면 n에서 c를 뺸 값을 재귀호출
                inner_legal_payment(n-c)
                if n-c in memoization.keys():        #가능한 조합이 있으면
                    a.append([c] + memoization[n-c]) #c와 n-c의 반환값을 합침
                else :  #가능한 조합이 없으면(ex: 2,5,7로는 3을 만들지 못한다.)
                    pass#a에 조합이 들어가지 않고 None을 반환함.신경쓸 필요 없음

        if a == [] :
            return None

        #a에 들어있는 동전 조합들 중 가장 길이 짧은 조합의 인덱스를 찾음
        minindex = 0
        for i in range(len(a)):
            if len(a[i]) <= len(a[minindex]) :
                minindex = i

        #캐시에 저장하고 그 값을 반환
        memoization[n] = a[minindex]
        return memoization[n]
    
    #금액이 너무 크면 재귀함수 호출 제한에 걸려서 좀 줄여야함 
    exceedchip = 0
    while(chips > 555):
        chips -= coin[len(coin)-1]
        exceedchip += 1
    
    chiplist = inner_legal_payment(chips)
    
    for i in coin:
        if chiplist.count(i) <= 0 :
            continue
        
        if i == 1:
            print(Colors.BLACK, end='')
            print("⓵ x ", end='')
        elif i == 2:
            print(Colors.YELLOW, end='')
            print("⓶ x ", end='')
        elif i == 5:
            print(Colors.RED, end='')
            print("⓹ x ", end='')
        elif i == 10:
            print(Colors.BRIGHTBLUE, end='')
            print("⓾ x ", end='')
        elif i == 20:
            print(Colors.GRAY, end='')
            print("⑳ x ", end='')
        elif i == 25:
            print(Colors.GREEN, end='')
            print("㉕x ", end='')
        elif i == 50:
            print(Colors.BLUE, end='')
            print("㊿x ", end='')
        
        print(Colors.RESET, end = '')
        
        if i == coin[len(coin)-1]:
            print(chiplist.count(i)+exceedchip)
        else:
            print(chiplist.count(i))
        
            
#한 장씩 출력 이젠 안 씀 
#1   ┏━━━━━━━━━━━┓ 
#2   ┃ A         ┃    
#3   ┃           ┃ 
#4   ┃           ┃ 
#5   ┃     ♠     ┃ 
#6   ┃           ┃  
#7   ┃           ┃ 
#8   ┃           ┃ 
#9   ┗━━━━━━━━━━━┛
#   ♠ ︎♣ ♥︎ ♦︎
def draw_card(card):
    s = '?'
    r = card[1]
    if card[0] == "Spade":
        s = '♠'
    elif card[0] == "Heart":
        s = '♥︎'
    elif card[0] == "Diamond":
        s = '♦'
    elif card[0] == "Club":
        s = '♣'
   
    print("┏━━━━━━━━━━━┓",sep='')       #1
    if r != 10 :
        print("┃",r,"          ┃",sep='')  #2
    else:
        print("┃",r,"         ┃",sep='')  #2
        
    if r == 'A':
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
    elif r == 2:
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
    elif r == 3:
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
    elif r == 4:
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
    elif r == 5:
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
    elif r == 6:
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃           ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃           ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
    elif r == 7:
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃           ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
    elif r == 8:
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
    elif r == 9:
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
    elif r == 10:
        print("┃  ",s,"     ",s,"  ┃",sep='')
        print("┃  ",s,"  ",s,"  ",s,"  ┃",sep='')
        print("┃           ┃",sep='')
        print("┃  ",s,"  ",s,"  ",s,"  ┃",sep='')
        print("┃  ",s,"     ",s,"  ┃",sep='')
    elif r == 'J':
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
    elif r == 'Q':
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
    elif r == 'K':
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
        print("┃     ",s,"     ┃",sep='')
        print("┃           ┃",sep='')
        print("┃           ┃",sep='')
    else:
        print("┃x x x x x x┃",sep='')
        print("┃ x x x x x ┃",sep='')
        print("┃x x x x x x┃",sep='')
        print("┃ x x x x x ┃",sep='')
        print("┃x x x x x x┃",sep='')
    
    if r != 10 :
        print("┃          ",r,"┃",sep='')      #8
    else:
        print("┃         ",r,"┃",sep='')      #8
    print("┗━━━━━━━━━━━┛",sep='')      #9


        