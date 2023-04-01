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

width, height = 720, 720

screen = p.display.set_mode([width, height])

Running = True
#jump = False
#up = False
#down = False
clock = p.time.Clock()

icon = p.image.load("Lib\icon.ico").convert()
p.display.set_icon(icon)
p.display.set_caption('the game')
#bg = p.image.load("Lib\bg.jpg").convert()

class Player:
    def __init__(self):
        self.w = 64
        self.h = 128
        self.plyrx = 0
        self.plyry = height/2
        self.plyrimg = p.image.load("Lib/tempchar.bmp").convert()
    def scale(self):
        self.plyrimg = p.transform.smoothscale(self.plyrimg, (self.w, self.h)).convert()
    def jump(self):
        pass
        #empty for now
        
plyr = Player()

match __name__:
    case "__main__":
        pass
    case _:
        exit()
    
#match path:
#   case ".py":
#        debug = True
#    case "pyw":
#        pass

while Running:
    screen.blit(plyr.plyrimg, (plyr.plyrx, plyr.plyry))
    p.display.flip()
    screen.fill(white)
    evnt = p.event.poll()
    match evnt.type:
        case p.KEYDOWN:
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
            case 127:
                plyr.w -= 2
                plyr.scale()
            case 1073741898:
                plyr.h += 2
                plyr.scale()
            case 1073741901:
                plyr.h -= 2
                plyr.scale()
            case 1073741902:
                plyr.w += 2
                plyr.scale()
            case 1073741903:
                plyr.plyrx += (mov * fps)
            case 1073741904:
                plyr.plyrx -= (mov * fps)
            case 1073741906:
                #plyr.jump()
                pass
            #case 1073741905:
            #    plyr.plyry -= (mov * fps)
            case 1073741922:
                plyr.plyrx = 0
                plyr.plyry = height/2
                plyr.w = 64
                plyr.h = 128
                plyr.plyrimg = p.image.load("Lib/tempchar.bmp").convert()
            case _:
                pass
    clock.tick(60)
