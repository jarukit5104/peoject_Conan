label gery: 
                    scene work
                    image co = Text("ช่วงสรุปผล", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                    show co
                    ""
                    hide co
                    show chr_2 at right
                    "{cps=10}สวัสดีผู้เล่น ตอนแรกสนุกไหม{/cps}"
                    "{cps=10}ขออธิบายตอนแรกในการนับคะแนน 
                    ว่าโดยการนับคะแนนมาจากโชว์รูปหรือหลักฐานเพื่อได้คะแนนออกมาอย่างละ1คะแนนแบบง่ายๆนะครับ{/cps}"
                    jump TL
label TL:
                    $ thing = []
                    if f1 == True:
                       $ thing.append("ขนนก")
                    else:
                        jump TL1
label TL1:
                    if f3 == True:
                        $ thing.append("รูปดาบ")
                    else:
                        jump TL2
label TL2:
                    if f4 == True:
                       $ thing.append("รูปดอกไม้")
                    else:
                        jump TL3
label TL3:
                    if f6 == True:
                        $ thing.append("ร่องรอย")
                    else:
                        jump TL4
label TL4:
                    if f7 == True:
                       $ thing.append("สัญลักษณ์อินฟินิตี้")
                    else:
                        jump TL6
label TL5:
                    if f8 == True: 
                       $ thing.append("เครื่องมือ")
                    else:
                        jump TL6
label TL6:
                    if f9 == True:      
                        $ thing.append("แว่นขยาย")
                    else:
                        jump TL7

label TL7:
                    "{cps=10}ส่วนโชว์คะแนนรวมที่ได้มาเดี๋ยวจะโชว์หลังจากผมไปนะ{/cps}"
                    "{cps=10}เจอกันในตอนหน้านะ{/cps}"
                    hide chr_2 at right
                    if tool_y == 1:
                        image c1 = Text("สรุปหาหลักฐานไปแล้ว 0/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c1
                        jump sec
                    if tool_y == 2:
                        image c2 = Text("สรุปหาหลักฐานไปแล้ว 1/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c2
                        "[thing[0]]]"
                        jump sec
                    if tool_y == 3:
                        image c3 = Text("สรุปหาหลักฐานไปแล้ว 2/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c3
                        "[thing[0]], [thing[1]]"
                        jump sec
                    if tool_y == 4:
                        image c4 = Text("สรุปหาหลักฐานไปแล้ว 3/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c4
                        "[thing[0]], [thing[1]], [thing[2]]"
                        jump sec
                    if tool_y == 5:
                        image c5 = Text("สรุปหาหลักฐานไปแล้ว 4/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c5
                        "[thing[0]], [thing[1]], [thing[2]], [thing[3]]"
                        jump sec
                    if tool_y == 6:
                        image c6 = Text("สรุปหาหลักฐานไปแล้ว 5/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c6
                        "[thing[0]], [thing[1]], [thing[2]], [thing[3]], [thing[4]]"
                        jump sec
                    if tool_y == 7:
                        image c7 = Text("สรุปหาหลักฐานไปแล้ว 6/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c7
                        "[thing[0]], [thing[1]], [thing[2]], [thing[3]], [thing[4]], [thing[5]]"
                        jump sec
                    if tool_y == 8:
                        image c8 = Text("สรุปหาหลักฐานไปแล้ว 7/7", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show c8
                        "[thing[0]], [thing[1]], [thing[2]], [thing[3]], [thing[4]], [thing[5]], [thing[6]]"
                        jump sec
