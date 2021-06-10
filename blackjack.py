#################################                 
#               팀 15           #                 
#        이유진 정유찬 최종인        #                 
#   Ver 1.2.0, relese 2021.6.4. #
#################################

#룰 설명(기본적으론 강의시간에 만든 블랙잭과 같음)
#추가기능
#1. 베팅금액 설정 - 기존에는 무조건 하나의 칩만 걸 수 있었지만 원하는 대로 칩을 걸 수 있도록 수정
#2. 더블다운 - 무한정 카드를 새로 뽑는데신 딱 한장만 더 뽑고 더이상 뽑지 못하지만 베팅 금액을 두배로 올릴 수 있음
#3. 서렌더 - 처음 카드 두장을 받았을 때 가망이 없을 것이라 생각하면 기권을 하고 베팅 금액의 절반을 돌려 받음


from cardgame import *
from member import *

def blackjack():
    print("Welcome to Softopia Casino")
    username, tries, wins, chips, members = login(load_members())
    play = 0
    win = 0
    bet = 0
    deck = fresh_deck()
    while True:
        print("----------")
        #베팅금액 입력
        while bet <= 0 :
            try:
                bet = int(input("How much do you want to bet : "))
            except ValueError:
                print("Not Number")
                bet = 1
        
        print("You bet",bet,"chips.")
        chips -= bet
        play += 1
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        #show_cards(직접 구현한 카드모양 표시, 카드 리스트를 인자로 받음)
        show_cards([('?', '?'), (dealer[1][0], dealer[1][1])], "My cards are:")
        show_cards(player, "Your cards are:")
        score_dealer = count_score(dealer)
        score_player = count_score(player)
        print("your score:",score_player)

        choice = ''

        #블랙잭(한번에 승리)   
        if score_player == 21:
            print("Blackjack! You won.")
            chips += bet*2
            win+=1
        #계속 진행  
        else:

            ###플레이어 차례 버스트가 아니라면 계속 진행 할 수 있음
            while score_player < 21:

                if len(player) == 2 :
                    print("Hit:h DoubleDown:d Stand(stay):s Surrender:surrender")
                else:
                    print("Hit:h DoubleDown:d Stand(stay):s")

                choice = input("choice : ")
                
                #Hit 한장 더 뽑음
                if choice == 'h':
                    card, deck = hit(deck)
                    player.append(card)
                    score_player = count_score(player)
                    show_cards_motion([card], "New Card!!", 0.3)
                    time.sleep(0.5)
                    show_cards(player, "Your cards are:")
                    print("your score:",score_player)
                #Double down 베팅금액을 두배로 하고 딱 한장만 더 뽑고 차례를 넘김
                if choice == 'd':
                    chips-= bet
                    bet = bet*2
                    print("The betting amount is doubled to", bet)
                    
                    card, deck = hit(deck)
                    player.append(card)
                    score_player = count_score(player)
                    show_cards_motion([card], "New Card!!", 0.3)
                    time.sleep(0.5)
                    show_cards(player, "Your cards are:")
                    print("your score:",score_player)
                    break;
                #Stand(stay) 카드 뽑기를 멈추고 딜러에게 차례를 넘김
                if choice == 's':
                    break;
                #Surrender 기권
                if choice == 'surrender' and len(player) == 2:
                    print("You choose to surrender.")
                    break;

            ###딜러 차례
            #플레이어 기권(패배)
            if choice == 'surrender':
                    #베팅금액의 절반을 돌려 받음
                    print("Returns",int(bet/2),"chip(s)")
                    chips += int(bet/2)
            #플레리어 버스트(패배)    
            elif score_player > 21:
                print("You bust! I won.")
            #비교(누가 더 21에 가까운지)    
            else:
                #딜러가 16이 넘을때까지 계속 뽑음 
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                print("my score:",score_dealer)
                
                #딜러 버스트(승리)
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += bet*2
                    win +=1
                #무승부
                elif score_dealer == score_player:
                    print("We draw.")
                #플레이어가 더 높음(승리)
                elif score_dealer < score_player:
                    print("You won.")
                    chips += bet*2
                    win += 1
                #딜러가 더 높음(패배)
                else:
                    print("I won.")
                    
        print("Chips =", chips)
        draw_chips(chips)
        
        if not more("Play more? (y/n) "):
            break
        
    print("----------")
    print("You played", play, "games and won", win, "of them")
    print("Your winning percentage today is", "{0:.1f}".format((win/play)*100), "%")
    tries += play
    wins += win
    members[username] = (members[username][0], tries, wins, chips)
    store_members(members)
    show_top5(members)
    print("Bye!")

blackjack()
