image work = im.Scale("work.png", 1280, 725)
image work1 = im.Scale("work1.png", 1280, 725)
image work2 = im.Scale("work2.png", 1280, 725)
image work3 = im.Scale("work3.png", 1280, 725)
image food = im.Scale("food.png", 1280, 725)
image park = im.Scale("park.png", 1280, 725)
image room = im.Scale("room.png", 1280, 725)
image police= im.Scale("police.png", 1280, 725)
image ocean1 = im.Scale("ocean1.png", 1280, 725)
image c = im.Scale("c.png", 1280, 725)
image ocean1 = im.Scale("ocean1.png", 1280, 725)
image ocean = im.Scale("ocean.png", 1280, 725)
image ocean4 = im.Scale("ocean4.png", 1280, 725)
image ocean2 = im.Scale("ocean2.png", 1280, 725)
image ocean3 = im.Scale("ocean3.png", 1280, 725)
image ocean5 = im.Scale("ocean5.png", 1280, 725)
image ocean6 = im.Scale("ocean6.png", 1280, 725)
image wine = im.Scale("wine.png", 1280, 725)
image kitchen = im.Scale("kitchen.png", 1280, 725)
image on1 = im.Scale("on1.png", 1280, 725)
image tools = im.Scale("tools.png", 700, 500)
image a = im.Scale("a.png", 1280, 725)
image b = im.Scale("b.png", 1280, 725)
image tree = im.Scale("tree.png", 1280, 725)
image tree1 = im.Scale("tree1.png", 1280, 725)
image river= im.Scale("river.png", 1280, 725)
image d = im.Scale("d.png", 1280, 725)
image e = im.Scale("e.png", 1280, 725)
image f = im.Scale("f.png", 1280, 725)
image car = im.Scale("car.png", 1280, 725)
image icon = im.Scale("icon.png", 1280, 725)
image fa = im.Scale("fa.png", 700, 500)
image zoom1 = im.Scale("zoom1.png", 1280, 725)
image sword = im.Scale("sword.png", 1280, 725)
image winebow1 = im.Scale("winebow1.png", 1280, 725)
image winebow = im.Scale("winebow.png", 1280, 725)
image jean = im.Scale("jean.png", 1280, 725)
image free = im.Scale("free.png", 1280, 725)
image gwine = im.Scale("gwine.png", 1280, 725)
image gery = im.Scale("gery.jpg", 1280, 725)


screen workroom() :
        imagemap:
            ground "work.png"  
            hotspot ((970, 486, 180, 127))  action Jump("item1")
        imagemap:
            ground "work.png"  
            hotspot ((594, 457, 167, 154))  action Jump("item4") 
        imagemap:
            ground "work.png"  
            hotspot ((964, 342, 215, 130))  action Jump("item4")
        imagemap:
            ground "work.png"  
            hotspot ((82, 65, 321, 190))  action Jump("item4")
        imagemap:
            ground "work.png"  
            hotspot ((87, 271, 359, 426))  action Jump("item4")
        imagemap:
            ground "work.png"  
            hotspot ((457, 311, 147, 156))  action Jump("item4")
        imagemap:
            ground "work.png"  
            hotspot ((593, 465, 161, 158))  action Jump("item4")
        imagemap:
            ground "work.png"  
            hotspot ((944, 205, 241, 117))  action Jump("item4")
            
screen workroom1() :
        imagemap:
            ground "work1.png"  
            hotspot ((970, 486, 180, 127))  action Jump("item3")
        imagemap:
            ground "work1.png"  
            hotspot ((594, 457, 167, 154))  action Jump("item2") 
        imagemap:
            ground "work1.png"  
            hotspot ((964, 342, 215, 130))  action Jump("item2")
        imagemap:
            ground "work1.png"  
            hotspot ((82, 65, 321, 190))  action Jump("item2")
        imagemap:
            ground "work1.png"  
            hotspot ((87, 271, 359, 426))  action Jump("item2")
        imagemap:
            ground "work1.png"  
            hotspot ((457, 311, 147, 156))  action Jump("item2")
        imagemap:
            ground "work1.png"  
            hotspot ((593, 465, 161, 158))  action Jump("item2")
        imagemap:
            ground "work1.png"  
            hotspot ((944, 205, 241, 117))  action Jump("item2")    

screen workroom2() :
        imagemap:
            ground "work2.png"  
            hotspot ((618, 158, 44, 38))  action Jump("item9")
        imagemap:
            ground "work2.png"  
            hotspot ((594, 457, 167, 154))  action Jump("item6") 
        imagemap:
            ground "work2.png"  
            hotspot ((964, 342, 215, 130))  action Jump("item6")
        imagemap:
            ground "work2.png"  
            hotspot ((82, 65, 321, 190))  action Jump("item6")
        imagemap:
            ground "work2.png"  
            hotspot ((87, 271, 359, 426))  action Jump("item6")
        imagemap:
            ground "work2.png"  
            hotspot ((457, 311, 147, 156))  action Jump("item6")
        imagemap:
            ground "work2.png"  
            hotspot ((593, 465, 161, 158))  action Jump("item6")
        imagemap:
            ground "work2.png"  
            hotspot ((944, 205, 241, 117))  action Jump("item6")

screen workroom3() :
        imagemap:
            ground "work2.png"  
            hotspot ((618, 158, 44, 38))  action Jump("item10")
        imagemap:
            ground "work3.png"  
            hotspot ((970, 486, 180, 127))  action Jump("item7")
        imagemap:
            ground "work3.png"  
            hotspot ((594, 457, 167, 154))  action Jump("item8") 
        imagemap:
            ground "work3.png"  
            hotspot ((964, 342, 215, 130))  action Jump("item8")
        imagemap:
            ground "work3.png"  
            hotspot ((82, 65, 321, 190))  action Jump("item8")
        imagemap:
            ground "work3.png"  
            hotspot ((87, 271, 359, 426))  action Jump("item8")
        imagemap:
            ground "work3.png"  
            hotspot ((593, 465, 161, 158))  action Jump("item8")
        imagemap:
            ground "work3.png"  
            hotspot ((944, 205, 241, 117))  action Jump("item8")
            
screen Tree() :
        imagemap:
            ground "tree1.png"  
            hotspot ((463, 73, 34, 39))  action Jump("tree1")
        imagemap:
            ground "tree1.png"  
            hotspot ((4, 8, 242, 353))  action Jump("tree2")
        imagemap:
            ground "tree1.png"  
            hotspot ((9, 386, 1271, 283))  action Jump("tree3")
        imagemap:
            ground "tree1.png"  
            hotspot ((663, 7, 617, 233))  action Jump("tree3")    

screen Tree1() :
        imagemap:
            ground "tree1.png"  
            hotspot ((463, 73, 34, 39))  action Jump("tree4")
        imagemap:
            ground "tree1.png"  
            hotspot ((4, 8, 242, 353))  action Jump("tree6")
        imagemap:
            ground "tree1.png"  
            hotspot ((9, 386, 1271, 283))  action Jump("tree7")
        imagemap:
            ground "tree1.png"  
            hotspot ((663, 7, 617, 233))  action Jump("tree7")
            
            
screen House1() :
        imagemap:
            ground "rooom1.png"  
            hotspot ((493, 53, 58, 44))  action Jump("rooom1")
        imagemap:
            ground "rooom1.png"  
            hotspot ((0, 1, 478, 366))  action Jump("rooom2")
        imagemap:
            ground "rooom1.png"  
            hotspot ((0, 422, 1277, 295))  action Jump("rooom2")
        imagemap:
            ground "rooom1.png"  
            hotspot ((1, 398, 34, 27))  action Jump("rooom3")
            

screen Winebow() :
        imagemap:
            ground "winebow1.png"  
            hotspot ((0, 0, 1279, 717))  action Jump("wb1")


            
