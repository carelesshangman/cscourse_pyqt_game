import risar as r

r.setup()

class Kolesar: #prvic ponesrec biu imenovan Klosar ker slabo pisem :)
    def __init__(self, posX: int, posY: int):
        self.posX = posX
        self.posY = posY
        self.sprite = "kolesar.png"

class Obsatacle:
    def __init__(self, startX: int, startY: int, tiles: int):
        self.startX = startX
        self.startY = startY

k1 = Kolesar(400,340)

obstacles = []

test = r.slika(k1.posX, k1.posY, k1.sprite)
while True:
    r.odstrani(test)
    test = r.slika(k1.posX, k1.posY, k1.sprite)
    if k1.posX < 760:
        if r.desno() == True:
            k1.posX += 1
    if k1.posX > 0:
        if r.levo() == True:
            k1.posX -= 1

