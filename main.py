#pygame 2.4.0dev2, SDL 2.26.4-x64
import pygame as p

white = (232, 232, 232)
activekeys = []
#debug = False
#path = __file__
#path = path[-3:]
p.init()

fps = 60
fpsms = (1000/60)
mov = (5/fps)

height , width = 480, 720

screen = p.display.set_mode([width , height])

Running = True
clock = p.time.Clock()

icon = p.image.load("Lib\icon.ico").convert()
p.display.set_icon(icon)
p.display.set_caption('the game')

class Player():
    def __init__(self):
        self.h = 128
        self.health = 100
        self.plyrx = 0
        self.plyry = height / 2
        self.w = 64
        self.plyrimg = p.image.load("Lib/tempchar.bmp").convert_alpha()
    def jump():
        pass
    def movef():
        self.plyrx += (mov * fps)
    def moveb():
        self.plyrx -= (mov * fps)
                

#match __name__:
#    case "__main__":
#        pass
#    case _:
#        exit()
    
#match path:
#   case ".py":
#        debug = True
#    case "pyw":
#        pass

plyr = Player()

while Running:
    screen.blit(plyr.plyrimg, (plyr.plyrx, plyr.plyry))
    p.display.flip()
    screen.fill(white)
    evnt = p.event.poll()
    match evnt.type:
        case p.KEYDOWN:
            #print(evnt.key)
            activekeys.append(evnt.key)
        case p.KEYUP:
            activekeys.remove(evnt.key)
        case p.QUIT:
            p.quit()
            Running = False
            break
        case _:
            pass
    for x in activekeys:
        match x:
            case 27:
                p.quit()
                Running = False
                break
            case 1073741903:
                plyr.movef()
            case 1073741904:
                plyr.moveb()
            case 1073741906:
                plyr.jump = True
            #case 1073741905:
            #    plyry -= (mov * fps)
            case 1073741922:
                plyr.__init__()
            case _:
                pass
    clock.tick(60)
