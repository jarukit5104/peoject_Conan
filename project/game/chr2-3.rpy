                label see:
                    menu : 
                        c"   "
                        "ไปดูใกล้ๆ":
                            jump see1
                        "บอกเตือนกับทุกคน":
                            jump see2
                                                       
                label see1:
                    c "{cps=10}นี่มันหน้าไม้ ระวังนะครับ คุณจิกิตะ{/cps}"
                    "{cps=10}จิกิตะ ฮาจิโตะ ได้เหยียบอะไรบางอย่าง แล้วพร้อมอะไรบางพุ่งไปหาจิกิตะ ฮาจิโตะ แต่หลบได้{/cps}"
                    show chr_e13 at left
                    t "{cps=10}เส้นเอ็น ? ลูกธนู ?{/cps}"
                    hide chr_e13 at left
                    show chr_f12 at left
                    j "{cps=10}ยิงจากตรงทางไหน{/cps}"
                    hide chr_f12 at left
                    c "พวกเราออกจากที่นี่นะ"
                    show chr_f12 at left
                    j "{cps=10}โอเค{/cps}"
                    hide chr_f12 at left
                    jump run2
                
                label see2:
                    c "{cps=10}ทุกคนระวังนะครับเห็นบนชั้นไวน์ตรงนั้นไม่รู้ว่ามันคืออะไร{/cps}"
                    show chr_f12 at left
                    j "{cps=10}อะไรเหรอ{/cps}"
                    hide chr_f12 at left
                    show chr_f13 at left
                    show chr_a2 
                    b "{cps=10}เดี๋ยวดูให้นะครับ{/cps}"
                    hide chr_a2 
                    "{cps=10}จิกิตะ ฮาจิโตะ ได้เหยียบอะไรบางอย่างแบบรีบร้อน แล้วพร้อมอะไรบางพุ่งไปหาคุณจิกิตะ ฮาจิโตะ ทำให้คุณจิกิตะได้บาดเจ็บตรงไหล่{/cps}"
                    hide chr_f13 at left
                    show chr_f12 at left
                    show chr_a3
                    t "{cps=10}อ๊ากก เจ็บจัด!! ที่มัน ลูกธนู ?{/cps}"
                    hide chr_f12 at left
                    show chr_f13 at left
                    show chr_a2  
                    hide chr_a3
                    b "{cps=10}เป็นอะไรไหม{/cps}"
                    hide chr_f13 at left
                    show chr_e13 at left
                    show chr_a3 
                    hide chr_a2
                    t "{cps=10}แค่โดนลูกธนูเฉียดๆนะครับ{/cps}"
                    hide chr_a3
                    hide chr_e13 at left
                    show chr_f12 at left
                    j "{cps=10}ยิงออกจากชั้นไวน์ที่คุณ %(c)s บอก{/cps}"
                    hide chr_f12 at left
                    call screen Winebow
                label wb1:
                            scene winebow11
                            label wi:
                                scene winebow
                                show 8 
                                c "{cps=10}ไพ่เลข 8 นั่นเหรอ{/cps}"
                                $ f2 = True
                                hide 8
                                jump wb2
                label wb2:
                    show chr_a2
                    b "{cps=10}ตรงนี้ครับ{/cps}"
                    "{cps=10}ทุกคนที่นั้นได้เห็นหน้าไม้หลังชั้นไวน์ตรงทางข้างหลังตัวของจิกิตะ ฮาจิโตะที่อยู่ไม่ไกลมากพร้อมกับ เลข 8{/cps}"
                    b "{cps=10}เลข 8 ก็ไปแล้วต่อไปก็ซิโรริ นานะ{/cps}"
                    hide chr_a2
                    show chr_a3
                    c "{cps=10}ต้องรีบกลับหาซิโรริ นานะโดยเร็ว{/cps}"
                    show chr_f12 at left
                    j "{cps=10}โอเค{/cps}"
                    hide chr_f12 at left
                    hide  chr_a3
                    jump run2
                
                label run2:
                    scene ocean2
                    "{cps=10}หลังจากทุกคนที่ไปห้องเก็บไวน์ได้กลับจุดที่รวมตัวที่เดิม{/cps}"
                    show chr_c14 at left
                    m "{cps=10}เกิดอะไรขึ้นครับพวกคุณ{/cps}"
                    hide chr_c14 at left
                    show chr_f12 at left
                    j "{cps=10}จูโคโร่ อาคายุยได้วางกับดักใส่คุณจิกิตะ ฮาจิโตะ แต่โชคดีที่เขาหลบได้ แต่คนต่อไปคือ ซิโรริ นานะ{/cps}"
                    hide chr_f12 at left
                    show chr_d14 at left
                    s "{cps=10}งั้นผมเฝ้าซิโรริ นานะ เอง เพราะไม่อย่าให้คนตายมาจากผมอีก{/cps}"
                    hide chr_d14 at left
                    show chr_j4 at right
                    n "{cps=10}เป็นคุณสินะ เป็นตัวต้นเหตุที่ทำให้ทุกคนต้องตาย{/cps}"
                    show chr_j3 at right
                    hide chr_j4 at right
                    show chr_a2
                    b "{cps=10}ใจเย็นก่อนนะครับ เดี๋ยวพวกผู้ชายยกเว้นโดมะ และอิจิ ไปหาจูโคโร่ อาคายุยก่อน{/cps}"
                    show chr_a3 
                    hide chr_a2
                    c "{cps=10}ผมไปเอาเครื่องดื่มให้กับทุกคนเอง{/cps}"
                    "{cps=10}หลังจากทุกคนแยกย้ายทำหน้าที่เวลาสักพัก %(c)sแจกน้ำเปล่าให้กับทุกคน{/cps}"
                    c "{cps=10}นี้ครับน้ำเปล่าสำหรับทุกคน{/cps}"
                    show chr_j4 at right
                    hide chr_j3 at right
                    n "{cps=10}ขอบคุณค่ะ{/cps}"
                    show chr_i11 at left
                    hide chr_j4 at right
                    f "{cps=10}ขอบคุณครับ{/cps}"
                    hide chr_i11 at left
                    show chr_l12 at left
                    u "{cps=10}แล้วมีเบียร์ไหม{/cps}"
                    hide chr_l12 at left
                    show chr_l13 at left
                    c "{cps=10}มีครับจะมีคนเอาเบียร์เพิ่มหริอน้ำเปล่าไหม{/cps}"
                    hide chr_l13 at left
                    show chr_c13 at left
                    m "{cps=10}ผมเอาน้ำเปล่า{/cps}"
                    hide chr_c13 at left
                    show chr_d13 at left
                    s "{cps=10}ผมเบียร์ครับ{/cps}"
                    hide chr_d13 at left
                    c "{cps=10}โอเคครับเดี๋ยวเอาที่ห้องครัวก่อนนะครับ{/cps}"
                    show chr_l12 at left
                    u "{cps=10}รีบเร็วเข้าล่ะ อยากดื่มเบียร์ใจจะขาดแล้ว{/cps}"
                    hide chr_l12 at left

                    
                    scene kitchen
                    "{cps=10}%(c)s บังเอิญเห็นจิกิตะ ฮาจิโตะ ชิมพริกป่นที่ห้องครัว{/cps}"
                    c "{cps=10}คุณฮาจิโตะ ทำอะไรเหรอ ถ้าน้ำแร่ก็ในตู้เย็นชั้นล่างนะครับ{/cps}"
                    show chr_e13 at left
                    t "{cps=10} อ่อ งานอดิเรกชิมเครื่องปรุงนะครับ และขอบคุณที่บอกนะครับ{/cps}"
                    " {cps=10}%(c)s ได้สังเกตเห็นอาการผิดปกติและลนลานของจิกิตะ ฮาจิโตะ{/cps}"
                    hide chr_e13 at left
                    show chr_e12 at left
                    c "{cps=10}ไม่เป็นไรนะครับ อืมเอาน้ำกระป๋องไปให้ยาสุโอะกับสารวัตรดีกว่า
                          อือ คุณฮาจิโตะ ช่วย ถือน้ำกับผมหน่อยได้ไหม{/cps}"
                    hide chr_e12 at left
                    show chr_e13 at left
                    t "{cps=10}ได้สิครับ{/cps}"
                    hide chr_e13 at left
                    
                    scene ocean2
                    "{cps=10}%(c)s และจิกิตะ ฮาจิโตะ ได้แจกน้ำให้ทุกคนที่เหลือ{/cps}"
                    c "{cps=10}นี่สิน้ำกระป๋องหลังจากเครียดคดีอยู่ตอนนี้จริงๆ{/cps}"
                    show chr_a2
                    b "{cps=10}ใช่ครับ{/cps}"
                    show chr_a3
                    show chr_f12 at left
                    hide chr_a2
                    j "{cps=10}พวกนายชอบเครื่องดื่มนี้จริงๆ{/cps}"
                    show chr_f13 at left
                    hide chr_f12 at left
                    show chr_a2
                    hide chr_a3
                    b "{cps=10}ก็ใช่สิครับ เวลาแบบนี้ต้องคลายเครียดก่อนคนร้ายลงมือทำอะไรเพิ่มอีก{/cps}" 
                    show chr_i11 at left
                    hide chr_f13 at left
                    show chr_a3
                    hide chr_a2
                    f "{cps=10}พวกคุณสบายใจจริงๆ เลยน่ะ{/cps}"      
                    show chr_l12 at left
                    hide chr_i11 at left
                    u "เ{cps=10}อาน่า ก็ดีกว่านั่งเฉยๆรอความตายหรอกน่า{/cps}"
                    show chr_i11 at left
                    hide chr_l12 at left
                    f "{cps=10}ก็จริงนะครับ{/cps}"
                    show chr_e13 at left
                    hide chr_i11 at left
                    t "{cps=10}คงไม่น่าเร็วๆนี้หรอกนะ{/cps}"
                    "{cps=10}หลังจากพูดคุยไม่นานก็เกิดเรื่องบางอย่างขึ้น{/cps}"
                    show chr_d13 at left
                    hide chr_e13 at left
                    s "{cps=10}แล้วโดมะหายไปไหนทุกคนเห็นเขาไหม{/cps}"
                    show chr_l13 at left
                    hide chr_d13 at left
                    u "{cps=10}ไม่เห็นนะครับ{/cps}"
                    hide chr_l13 at left
                    show chr_h1 at right
                    o "{cps=10}ไม่เห็นเลยค่ะ{/cps}"
                    show chr_b1 at right
                    hide chr_h1 at right
                    g "{cps=10}หนูด้วยค่ะ{/cps}"
                    show chr_d13 at left
                    hide chr_b1 at right
                    s "{cps=10}ทุกคนไม่เห็นโดมะแล้วเขาหายไปไหน{/cps}"
                    hide chr_a2
                    hide chr_d13 at left
                    
                    scene background
                    "{cps=10}หลังจากอิจิ โซมะพูดเสร็จก็ไฟดับทั้งอควาเรียม{/cps}"
                    j "{cps=10}ไฟดับ ทุกคนระวัง{/cps}"
                    f "{cps=10}เกิดอะไรขึ้นอีก{/cps}"
                    b "{cps=10}ทุกคนอยู่ใกล้กันไว้{/cps}"
                    n "{cps=10}ไม่นะะะ กรี๊ดดดด{/cps}"
                    
                    scene work
                    image do = Text("ช่วงสรุปผล", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                    show do
                    ""
                    hide do
                    show chr_2 at right
                    "{cps=10}เจอกันอีกแล้ว ตอนที่2เรื่องราวกำลังเริ่มเข้มขันขึ้น{/cps}"
                    "{cps=10}ขออธิบายตอนสองในการนับคะแนน 
                    ว่าโดยการนับคะแนนมาจากผู้คุยกับบุคคลผู้ต้องสงสัยและหาหลักฐานเล็กน้อยนะครับ{/cps}"
                    "{cps=10}นับคะแนนจะบุคคลไปเรื่อยๆจะได้คะแนนตามที่คุยไว้หรือจะไม่มีคะแนนบางบุคคลก็ได้นะครับ{/cps}"
                    jump sp
                label sp:
                    $ lol = 1
                    $ pe= []
                    if s1 == True:
                        $ pe.append("โดมะ นิโตะ")
                        $ lol +=1
                    else:
                        jump sp1
                label sp1:
                    if s2 == True:
                        $ pe.append("มาอาระ นากิซัน")
                        $ lol +=1
                    else:
                        jump sp2
                label sp2:
                    if s3 == True:
                        $ pe.append("เนด้งย่ง โดเซบ้า")
                        $ lol +=1
                    else:
                        jump sp3
                label sp3:
                    if s4 == True:
                        $ pe.append("นิวารา ชิโกะ")
                        $ lol +=1
                    else:
                        jump sp4
                label sp4:
                    if s5 == True:
                        $ pe.append("โรคุ ดุกิ")
                        $ lol +=1
                    else:
                        jump sp5
                label sp5:
                    if s6 == True:
                        $ pe.append("จิกิตะ ฮาจิโตะ")
                        $ lol +=1
                    else:
                        jump sp6
                label sp6:   
                    "{cps=10}ส่วนโชว์คะแนนรวมที่ได้มาเดี๋ยวจะโชว์หลังจากผมไปเช่นเคย{/cps}"
                    "{cps=10}เจอกันในตอนหน้านะ{/cps}"
                    hide chr_2 at right
                    $ renpy.music.stop(channel="sound_effect")
                    if   ser_y == 1:
                        image d1 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 0/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d1
                        jump run4
                    if   ser_y == 2:
                        image d2 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 1/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d2
                        jump run4
                    if   ser_y == 3:
                        image d3 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 2/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d3
                        jump run4
                    if   ser_y == 4:
                        image d4 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 3/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d4
                        jump run4
                    if   ser_y == 5:
                        image d5 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 4/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d5
                        jump run4
                    if   ser_y == 6:
                        image d6 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 5/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d6
                        jump run4
                    if   ser_y == 7:
                        image d7 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 6/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d7
                        jump run4
                    if   ser_y == 8:
                        image d8 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 7/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d8
                        jump run4
                    if   ser_y == 9:
                        image d9 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 8/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d9
                    if   ser_y == 10:
                        image d10 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 9/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d10
                        jump run4
                    if   ser_y == 11:
                        image d11 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 10/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d11
                        jump run4
                    if   ser_y == 12:
                        image d12 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 11/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d12
                        jump run4
                    if   ser_y == 13:
                        image d13 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว12/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d13
                        jump run4
                    if   ser_y == 14:
                        image d14 = Text("สรุปสอบถามผู้คนที่สอบถามไปแล้ว 13/13", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show d14
                        jump run4
                label run4:
                    if   lol == 2:
                        "[pe[0]]"
                        jump run3
                    if   lol == 3:
                        "[pe[0]],[pe[1]]"
                        jump run3
                    if   lol == 4:
                        "[pe[0]],[pe[1]],[pe[2]]"
                        jump run3
                    if   lol == 5:
                        "[pe[0]],[pe[1]],[pe[2]],[pe[3]]"
                        jump run3
                    if   lol == 6:
                        "[pe[0]],[pe[1]],[pe[2]],[pe[3]],[pe[4]]"
                        jump run3
                    if   lol == 7:
                        "[pe[0]],[pe[1]],[pe[2]],[pe[3]],[pe[4]],[pe[5]]"
                        jump run3
                    else:
                        ""
                        jump run3
