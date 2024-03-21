def should_hit(player_total, dealer_card_val, player_aces):
    if player_total < 12:
        return True
    elif player_aces > 0 and player_total < 18:
        return True
    elif dealer_card_val >6 and player_total <17:
        return True
    elif dealer_card_val <4 and player_total <13:
        return True
    else:
        return False
    
def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    if player_total < 12:
        return True
    elif player_high_aces > 0 and player_total < 18:
        return True
    elif dealer_total > 6 and player_total <17:
        return True
    elif dealer_total <4 and player_total <13:
        return True
    else:
        return False