import engineering_notation as ne
class engfmt:
    def __init__(self):
        pass
    def quant_to_eng(self,num,prec=2):
        return ne.EngNumber(num,precision=prec)

