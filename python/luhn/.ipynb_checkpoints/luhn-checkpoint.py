class Luhn:
    def __init__(self, card_num):
        self.state_save=card_num
        
    
    def valid(self):
        self.card_num=self.state_save.replace(" ","")
        # This test was added, because we saw many implementations
        # in which the first call to valid() worked, but the
        # second call failed().
        if len(self.card_num)<=1:
            return False
        else:
            try:
                self.card_num=[int(i) for i in self.card_num]
                for idx,num in enumerate(self.card_num[-2::-2]):
                    self.card_num[-2*(idx+1)]=(2*num-9) if 2*num>9 else 2*num
                return sum(self.card_num)%10==0
            except Exception:
                return False