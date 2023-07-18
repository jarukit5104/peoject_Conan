﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("เจ้าหน้าที่โจ")
define s = Character("อิจิ โซมะ")
define b = Character("ผู้ช่วย ยาสุโอะ")
define c = Character("c") 
define d = Character("ชายปริศนา")
define j = Character("สารวัตรทาเครุ")
define h = Character("ชายปริศนา")
define e = Character("จูโยว อิจิโตะ") 
define t = Character("จิกิตะ ฮาจิโตะ")
define z = Character("???")
define n = Character("ซิโรริ นานะ")
define r = Character("คนใกล้ตัวของอิจิ โซมะ")
define m = Character("โดมะ นิโตะ")
define o = Character("มาอาระ นากิซัน")
define f = Character("เนด้งย่ง โดเซบ้า")
define g = Character("นิวารา ชิโกะ")
define u = Character("โรคุ ดุกิ")
define v = Character("ทุกคน")
define l = Character("พวกผู้หญิง")

init:
    $ click_count = 0
    $ max_clicks = 4
    $ f1 = False
    $ f2 = False
    $ f3 = False
    $ f4 = False
    $ f5 = False
    $ f6 = False
    $ f7 = False
    $ f8 = False
    $ f9 = False
    $ s1 = False
    $ s2 = False
    $ s3 = False
    $ s4 = False
    $ s5 = False
    $ s6 = False
    $ s7 = False
    $ ok1 = False
    $ ok2 = False
    $ ok3 = False
    $ ok4 = False
    $ ok5 = False
    $ ok6 = False
    $ end_y = 1
    $ renpy.music.register_channel("sound_effect", mixer="sfx")

# The game starts here.

label start:     
        $ renpy.music.queue("audio/chr1.mp3", channel="sound_effect")

        scene background
        "ตอน  คดีฆาตรกรรมที่แปลกประหลาด"
        scene a
        "{cps=10}เมืองโตเกียว
        ณ โตเกียวทาว์ เมืองที่มีผู้คนพลุ่งพล่าน ในโรงแรมแห่งหนึ่ง ในชั้นที่4 มีห้องหนึ่งที่มีเสียงโทรศัพท์ดัง
        ได้ปลุกคนผู้หนึ่งให้ลุกขึ้นจากที่นอน{/cps}" 
        scene b
        "{cps=10}ชายปริศนารับโทรศัพท์{/cps}"
        h "{cps=10}สวัสดีครับ ใครครับ ที่นี่คือสำนักงานสุดยอดนักสืบ{/cps}"
        j  "{cps=10}ผม สารวัตรทาเครุ อิโตะ อยากจ้างให้มาช่วยสืบสวนคดีหน่อยครับ{/cps}"
        show king at left
        show queen at right
        hide king at left
        hide queen at right
        h "{cps=10}อยากให้ช่วยสืบคดีงั้นเหรอ? แล้วคดีเกี่ยวกับอะไรล่ะครับ{/cps}"
        j "{cps=10}จากที่ทางตำรวจตรวจสอบ น่าจะเป็นคดีต่อเนื่อง เกิดขึ้นมาแล้ว2 คดี
        ในสถานที่เกิดเหตุมีวัตถุพยานที่คาดว่าคนร้ายทิ้งไว้ มีลักษณะสิ่งของคล้ายคลึงกันทั้ง 2 คดี{/cps}"
        h  "{cps=10}อืม คดีฆาตกรรมสินะ{/cps}"
        j   "{cps=10}คุณรู้ได้ยังไง แต่ที่คุณคิดก็ไม่ผิดหรอก เพียงแต่ว่าเหยื่อในเหตุการณ์ทั้ง2คดี ยังมีชีวิตอยู่{/cps}"
        h  "{cps=10}อืม.. คาดการณ์ผิดไปหน่อยสินะ{/cps}"
        j  "{cps=10}คุณนี้สุดยอดจริงๆ สมกับเป็นสุดยอดนักสืบผู้มีชื่อเสียง แห่งเอกชน
            ที่สามารถสรุปเกี่ยวกับคดีว่าเป็นคดีอะไร จากการฟังที่ 
            ผมบอกไปแค่ไม่เท่าไร {/cps}"
        j    "{cps=10}คุณนี้สุดยอดจริงๆ ผมขอฟังชื่อคุณอีกสักครั้ง จากปากคุณเองได้มั้ย{/cps}"
        $ c = renpy.input("โปรดตั้งชื่อของคุณก่อนเริ่มเกม(ชื่อภาษาไทยเท่านั้น)")
        $ c = c.strip()
        $  tool_y = 1
        $  inf_y = 1
        c "{cps=10}หึหึ งั้นฟังให้ดี ข้าชื่อ %(c)s ผู้ที่เป็นสุดยอดนักสืบ ยังไงล่ะ{/cps}"
        j "{cps=10}ขอบคุณมากที่ยอมทำตามคำขอของผม ส่วนรายละเอียดเพิ่มเติมเราจะมาคุยที่สำนักงานตำรวจ{/cps}"
    
        label go:
                    menu : 
                        c"   "
                        "ตกลง ผมจะไปสำนักงานของผมก่อน แล้วไปพร้อมกับผู้ช่วย ":
                            jump go1
                        "โอเค ผมจะรีบไปสำนักงานตำรวจ พร้อมกับผู้ช่วยทันที":
                            jump go2
                                         
        label name:
            menu : 
                c"   "
                "บอกชื่อแบบจริงจัง":
                    jump name1
                "บอกชื่อแบบสบายๆ":
                    jump name2
        
        label serr:  
            $  ser_y = 1
            $  ser1_y = False
            $  ser2_y = False
            $  ser3_y = False
            $  ser4_y = False
            $  ser5_y = False
            $  ser6_y = False
            $  ser7_y = False
            $ na = ["โดมะ นิโตะ", "มาอาระ นากิซัน","เนด้งย่ง โดเซบ้า","นิวารา ชิโกะ","โรคุ ดุกิ","ซิโรริ นานะ","จิกิตะ ฮาจิโตะ"]
            $ na1 = renpy.random.choice(na)
            $ na.remove(na1)
            $ na2 = renpy.random.choice(na)
            $ na.remove(na2)
            $ na3 = renpy.random.choice(na)
            $ na.remove(na3)
            $ na4 = renpy.random.choice(na)
            $ na.remove(na4)
            $ na5 = renpy.random.choice(na)
            $ na.remove(na5)
            $ na6 = renpy.random.choice(na)
            $ na.remove(na6)
            $ na7 = renpy.random.choice(na)
            label ser:
                menu : 
                    c "{cps=10}สอบหาข้อมูลแต่ละบุคคล แต่จะเริ่มถามคนไหนดี{/cps}"
                    "[na1]"if ser1_y == False:
                            $ ser1_y = True
                            if na1=="โดมะ นิโตะ":
                                    jump ser1
                            if na1=="มาอาระ นากิซัน":
                                    jump ser2
                            if na1=="เนด้งย่ง โดเซบ้า":
                                    jump ser3
                            if na1=="นิวารา ชิโกะ":
                                    jump ser4
                            if na1=="โรคุ ดุกิ":
                                    jump ser5
                            if na1=="ซิโรริ นานะ":
                                    jump ser6
                            else:
                                    jump ser7
                    "[na2]"if ser2_y == False:
                            $ ser2_y = True
                            if na2=="โดมะ นิโตะ":
                                    jump ser1
                            if na2=="มาอาระ นากิซัน":
                                    jump ser2
                            if na2=="เนด้งย่ง โดเซบ้า":
                                    jump ser3
                            if na2=="นิวารา ชิโกะ":
                                    jump ser4
                            if na2=="โรคุ ดุกิ":
                                    jump ser5
                            if na2=="ซิโรริ นานะ":
                                    jump ser6
                            else:
                                    jump ser7
                    "[na3]"if ser3_y == False:
                            $ ser3_y = True
                            if na3=="โดมะ นิโตะ":
                                    jump ser1
                            if na3=="มาอาระ นากิซัน":
                                    jump ser2
                            if na3=="เนด้งย่ง โดเซบ้า":
                                    jump ser3
                            if na3=="นิวารา ชิโกะ":
                                    jump ser4
                            if na3=="โรคุ ดุกิ":
                                     jump ser5
                            if na3=="ซิโรริ นานะ":
                                    jump ser6
                            else:
                                    jump ser7
                    "[na4]"if ser4_y == False:
                            $ ser4_y = True
                            if na4=="โดมะ นิโตะ":
                                    jump ser1
                            if na4=="มาอาระ นากิซัน":
                                    jump ser2
                            if na4=="เนด้งย่ง โดเซบ้า":
                                    jump ser3
                            if na4=="นิวารา ชิโกะ":
                                    jump ser4
                            if na4=="โรคุ ดุกิ":
                                    jump ser5
                            if na4=="ซิโรริ นานะ":
                                    jump ser6
                            else:
                                    jump ser7 
                    "ถัดไป":
                           jump ser9
                    "ไม่มีเรื่องที่จะสอบถามแล้ว":
                           jump ser8
            label ser9:
                menu:
                    c "{cps=10}สอบหาข้อมูลแต่ละบุคคล แต่จะเริ่มถามคนไหนดี{/cps}"
                    "[na5]"if ser5_y == False:
                            $ ser5_y = True
                            if na5=="โดมะ นิโตะ":
                                    jump ser1
                            if na5=="มาอาระ นากิซัน":
                                    jump ser2
                            if na5=="เนด้งย่ง โดเซบ้า":
                                    jump ser3
                            if na5=="นิวารา ชิโกะ":
                                    jump ser4
                            if na5=="โรคุ ดุกิ":
                                    jump ser5
                            if na5=="ซิโรริ นานะ":
                                    jump ser6
                            else:
                                    jump ser7
                    "[na6]"if ser6_y == False:
                            $ ser6_y = True
                            if na6=="โดมะ นิโตะ":
                                    jump ser1
                            if na6=="มาอาระ นากิซัน":
                                    jump ser2
                            if na6=="เนด้งย่ง โดเซบ้า":
                                    jump ser3
                            if na6=="นิวารา ชิโกะ":
                                    jump ser4
                            if na6=="โรคุ ดุกิ":
                                    jump ser5
                            if na6=="ซิโรริ นานะ":
                                    jump ser6
                            else:
                                    jump ser7
                    "[na7]"if ser7_y == False:
                            $ ser7_y = True
                            if na7=="โดมะ นิโตะ":
                                    jump ser1
                            if na7=="มาอาระ นากิซัน":
                                    jump ser2
                            if na7=="เนด้งย่ง โดเซบ้า":
                                    jump ser3
                            if na7=="นิวารา ชิโกะ":
                                    jump ser4
                            if na7=="โรคุ ดุกิ":
                                    jump ser5
                            if na7=="ซิโรริ นานะ":
                                    jump ser6
                            else:
                                    jump ser7
                    "ไม่มีเรื่องที่จะสอบถามแล้ว":
                           jump ser8
                    "ย้อนกลับ":
                           jump ser
            label ser1: 
                $  make1_y = False
                $  make2_y = False
                $  make3_y = False
                $ ma = ["ทำงานอะไรมา ก่อนจะมาที่นี้", "มาที่นี่ทำไม","หมดเรื่องที่จะถามแล้ว ระวังตัวด้วยล่ะ"]
                $ ma1 = renpy.random.choice(ma)
                $ ma.remove(ma1)
                $ ma2= renpy.random.choice(ma)
                $ ma.remove(ma2)
                $ ma3= renpy.random.choice(ma)
                
                label s1:
                    menu : 
                        c""
                        "[ma1]"if make1_y == False:
                            $ make1_y = True
                            if ma1=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make1
                            if ma1=="มาที่นี่ทำไม":
                                jump make2
                            else:
                                jump make3
                        "[ma2]"if make2_y ==False:
                            $ make2_y = True
                            if ma2=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make1
                            if ma2=="มาที่นี่ทำไม":
                                jump make2
                            else:
                                jump make3
                            jump make2
                        "[ma3]"if make3_y == False:
                            $ make3_y = True
                            if ma3=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make1
                            if ma3=="มาที่นี่ทำไม":
                                jump make2
                            else:
                                jump make3
                        
            label make1:
                    $ s1 = True
                    $  ser_y += 1
                    c "{cps=10}คุณโดมะ ทำงานเกี่ยวกับอะไรเหรอครับ{/cps}"
                    show chr_c3
                    m "{cps=10}ทำงานเป็นผู้ช่วยเซฟของอิจิ โซมะ ที่ร้านอาหารครับ{/cps}"
                    hide chr_c3
                    jump s1
            label make2: 
                    $ s1 = True
                    $  ser_y += 1
                    c "{cps=10}คุณโดมะ มาทำอะไรที่นี้กับโซมะ{/cps}"
                    show chr_c3
                    m "{cps=10}ผมได้จดหมายของเลขาของ คุณ คิวจู โดมะส่งถึงผมกับคุณอิจิ โซมะ{/cps}"
                    m "{cps=10}เห็นเขาบอกว่าอยากให้มาขยายร้านของเราที่นี่หน่อย{/cps}"
                    m "{cps=10}ทำให้พวกเรามาคุยธุระกับที่นี่นะครับ{/cps}"
                    hide chr_c3
                    jump s1
            label make3:
                    $ s1 = True
                    show chr_c3
                    m "{cps=10}จะระวังตัวครับ และจะดูแลคุณโซมะให้ได้เลยครับ{/cps}"
                    hide chr_c3
                    c "{cps=10}คนต่อไป{/cps}"
                    jump ser
                    
            label ser2: 
                $  make4_y = False
                $  make5_y = False
                $  make6_y = False
                $ ma = ["ทำงานอะไรมา ก่อนจะมาที่นี้", "มาที่นี่ทำไม","หมดเรื่องที่จะถามแล้ว ระวังตัวด้วยล่ะ"]
                $ ma1 = renpy.random.choice(ma)
                $ ma.remove(ma1)
                $ ma2= renpy.random.choice(ma)
                $ ma.remove(ma2)
                $ ma3= renpy.random.choice(ma)
                
                label s2:
                    menu : 
                        c""
                        "[ma1]"if make4_y == False:
                            $ make4_y = True
                            if ma1=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make4
                            if ma1=="มาที่นี่ทำไม":
                                jump make5
                            else:
                                jump make6
                        "[ma2]"if make5_y ==False:
                            $ make5_y = True
                            if ma2=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make4
                            if ma2=="มาที่นี่ทำไม":
                                jump make5
                            else:
                                jump make6
                        "[ma3]"if make6_y == False:
                            $ make6_y = True
                            if ma3=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make4
                            if ma3=="มาที่นี่ทำไม":
                                jump make5
                            else:
                                jump make6
                        
            label make4: 
                    $ s2 = True
                    $  ser_y += 1
                    c "{cps=10}คุณมาอาระ มาทำอะไรที่นี้ล่ะ{/cps}"          
                    show chr_h1
                    o "{cps=10}เป็นนักเขียนนิยายในชีวิตและประสบการณ์ของฉันเองค่ะ ที่ติดอันดับท็อป1 ใน100 รายการเลยนะค่ะ{/cps}"
                    hide chr_h1
                    c "{cps=10}สุดยอดเลยนะครับ{/cps}" 
                    show chr_h4
                    o "{cps=10}แน่นอนอยู่แล้วค่ะ เพราะเก่งยังไงล่ะค่ะ{/cps}"
                    hide chr_h4
                    c "{cps=10}คุณนี้มั่นหน้าตัวเองจริงๆ เลยน่ะครับ{/cps}" 
                    hide chr_h1
                    jump s2
            label make5: 
                    $ s2 = True
                    $  ser_y += 1
                    c "{cps=10}คุณมาอาระ มาทำอะไรที่นี้ล่ะ{/cps}"
                    show chr_h1
                    o "{cps=10}เขาเชิญฉันให้มาเขียนบทบรรยายเกี่ยวกับสถานที่นี้ ฉันเลยว่าจะขายหนังสือนิยายของฉันที่นี่นะค่ะ{/cps}" 
                    o "{cps=10}เลยมาเจรจาธุรกิจนะค่ะ{/cps}"  
                    hide chr_h1
                    c "{cps=10}โอเค{/cps}"
                    show chr_h1
                    o "{cps=10}มีคำถามไหมค่ะ{/cps}"  
                    hide chr_h1
                    jump s2
            label make6:
                    $ s2 = True
                    c "{cps=10}ไม่มีอะไรแล้วครับ{/cps}"
                    show chr_h1
                    o "{cps=10}โอเคค่ะ{/cps}" 
                    hide chr_h1
                    c "{cps=10}คนต่อไป{/cps}"
                    jump ser
                    
            label ser3: 
                $  make7_y = False
                $  make8_y = False
                $  make9_y = False
                $ ma = ["ทำงานอะไรมา ก่อนจะมาที่นี้", "มาที่นี่ทำไม","หมดเรื่องที่จะถามแล้ว ระวังตัวด้วยล่ะ"]
                $ ma1 = renpy.random.choice(ma)
                $ ma.remove(ma1)
                $ ma2= renpy.random.choice(ma)
                $ ma.remove(ma2)
                $ ma3= renpy.random.choice(ma)
                label s3:
                    menu : 
                        c""
                        "[ma1]"if make7_y == False:
                            $ make7_y = True
                            if ma1=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make7
                            if ma1=="มาที่นี่ทำไม":
                                jump make8
                            else:
                                jump make9
                        "[ma2]"if make8_y ==False:
                            $ make8_y = True
                            if ma2=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make7
                            if ma2=="มาที่นี่ทำไม":
                                jump make8
                            else:
                                jump make9
                        "[ma3]"if make9_y == False:
                            $ make9_y = True
                            if ma3=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make7
                            if ma3=="มาที่นี่ทำไม":
                                jump make8
                            else:
                                jump make9
                        
            label make7: 
                    $ s3 = True
                    $  ser_y += 1
                    c "{cps=10}คุณเนด้งย่ง ทำงานเกี่ยวกับอะไรเหรอครับ{/cps}"
                    show chr_i2
                    f "{cps=10}เป็นนักวิจารณ์อาหารและวิจารณ์เรื่องไวน์เป็นพิเศษ{/cps}"
                    hide chr_i2
                    jump s3
            label make8: 
                    $ s3 = True
                    $  ser_y += 1
                    c "{cps=10}คุณเนด้งย่ง มาทำอะไรที่นี้ล่ะ{/cps}"
                    show chr_i2
                    f "{cps=10}มาเช็คสินค้าไวน์ว่าได้มาตรฐานตามที่คุณคิวจู โดมะร้องขอมาครับ{/cps}"
                    hide chr_i2
                    show chr_f2
                    j "{cps=10}แน่ใจนะ ว่ามาเช็คไวน์เพราะว่าไม่มีใครมาด้วยเลย{/cps}"
                    hide chr_f2
                    show chr_i2
                    f "{cps=10}ความแตกซะแล้ว ความจริงมาชิมไวน์ที่นี่ด้วยล่ะ{/cps}"
                    hide chr_i2
                    jump s3
            label make9:
                    $ s3 = True
                    c "{cps=10}ไม่มีอะไรสอบถามแล้วครับ{/cps}"
                    show chr_i2
                    f "{cps=10}โอเคครับ{/cps}"
                    hide chr_i2
                    c "{cps=10}คนต่อไป{/cps}"
                    jump ser
                    
            label ser4: 
                $  make10_y = False
                $  make11_y = False
                $  make12_y = False
                $ ma = ["ทำงานอะไรมา ก่อนจะมาที่นี้", "มาที่นี่ทำไม","หมดเรื่องที่จะถามแล้ว ระวังตัวด้วยล่ะ"]
                $ ma1 = renpy.random.choice(ma)
                $ ma.remove(ma1)
                $ ma2= renpy.random.choice(ma)
                $ ma.remove(ma2)
                $ ma3= renpy.random.choice(ma)
                label s4:
                    menu : 
                        c""
                        "[ma1]"if make10_y == False:
                            $ make10_y = True
                            if ma1=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make10
                            if ma1=="มาที่นี่ทำไม":
                                jump make11
                            else:
                                jump make12
                        "[ma2]"if make11_y ==False:
                            $ make11_y = True
                            if ma2=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make10
                            if ma2=="มาที่นี่ทำไม":
                                jump make11
                            else:
                                jump make12
                        "[ma3]"if make12_y == False:
                            $ make12_y = True
                            if ma3=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make10
                            if ma3=="มาที่นี่ทำไม":
                                jump make11
                            else:
                                jump make12
                        
            label make10: 
                    $ s4 = True
                    $  ser_y += 1
                    c "{cps=10}คุณนิวารา ทำงานเกี่ยวกับอะไรเหรอครับ{/cps}"
                    show chr_b2
                    g "{cps=10}ป ป เป็น จิตรกรค่ะ{/cps}"
                    hide chr_b2
                    c "{cps=10}ดูคุณกลัวๆนะครับ{/cps}"
                    show chr_b2
                    g "{cps=10}ไม่มีอะไร แค่หนาวๆค่ะ{/cps}"
                    hide chr_b2
                    jump s4
            label make11: 
                    $ s4 = True
                    $  ser_y += 1
                    c "{cps=10}คุณนิวารา มาทำอะไรที่นี้ล่ะ{/cps}"
                    show chr_b2
                    g "{cps=10}เขาให้หนูมาโปรโมทอควาเรียมผ่านการวาดภาพของหนู ที่เป็นจิตรกรชื่อดัง 
                    เลยมาเจรจากับเขาเพื่อจะปฏิเสธข้อเสนอของเขาค่ะ{/cps}"
                    hide chr_b2
                    c "{cps=10}แล้วทำไมไม่ปฏิเสธทางอีเมลที่ได้รับข้อความล่ะครับ/cps}"
                    show chr_b2
                    g "{cps=10}ปฏิเสธไปแล้วค่ะ แต่เขาไม่ฟัง 
                    บอกว่าลงชื่อหนูในผู้เขาสมัครวาดภาพอควาเรียมไว้แล้ว เลยต้องมาคุยกับเขาค่ะ{/cps}"
                    hide chr_b2
                    c "{cps=10}โอเคครับ เข้าใจเรื่องราวแล้ว{/cps}"
                    jump s4
            label make12:
                    $ s4 = True
                    c "{cps=10}ไม่มีอะไรแล้วครับ{/cps}"
                    show chr_b2
                    g "{cps=10}โอเคค่ะ{/cps}" 
                    hide chr_b2
                    c "{cps=10}คนต่อไป{/cps}"
                    jump ser

            label ser5: 
                $  make13_y = False
                $  make14_y = False
                $  make15_y = False
                $ ma = ["ทำงานอะไรมา ก่อนจะมาที่นี้", "มาที่นี่ทำไม","หมดเรื่องที่จะถามแล้ว ระวังตัวด้วยล่ะ"]
                $ ma1 = renpy.random.choice(ma)
                $ ma.remove(ma1)
                $ ma2= renpy.random.choice(ma)
                $ ma.remove(ma2)
                $ ma3= renpy.random.choice(ma)
                label s5:
                    menu : 
                        c""
                        "[ma1]"if make13_y == False:
                            $ make13_y = True
                            if ma1=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make13
                            if ma1=="มาที่นี่ทำไม":
                                jump make14
                            else:
                                jump make15
                        "[ma2]"if make14_y ==False:
                            $ make14_y = True
                            if ma2=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make13
                            if ma2=="มาที่นี่ทำไม":
                                jump make14
                            else:
                                jump make15
                        "[ma3]"if make15_y == False:
                            $ make15_y = True
                            if ma3=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make13
                            if ma3=="มาที่นี่ทำไม":
                                jump make14
                            else:
                                jump make15
                        
            label make13: 
                    $ s5 = True
                    $  ser_y += 1
                    c "{cps=10}คุณโรคุ ทำงานเกี่ยวกับอะไรเหรอครับ{/cps}"
                    show chr_l2
                    u "{cps=10}เป็นนักถ่ายรูปอิสระครับ ผมชื่อดังมากเลยน่ะ{/cps}"
                    hide chr_l2
                    jump s5
            label make14: 
                    $ s5 = True
                    $  ser_y += 1
                    c "{cps=10}คุณโรคุ มาทำอะไรที่นี้ล่ะ{/cps}"
                    show chr_l2
                    u "{cps=10} เขาให้มาถ่ายภาพอควาเรียมเผยแพร่ผ่านทีวีที่เขาเคยสัมภาษณ์นะครับ 
                    เขาบอกว่าจะไปออกรายการอีกรอบ{/cps}"
                    u "{cps=10}แต่สุดท้ายก็เป็นแบบนี้{/cps}"
                    hide chr_l2
                    c "{cps=10}โอเคครับ{/cps}"
                    jump s5
            label make15:
                    $ s5 = True
                    c "{cps=10}ไม่มีอะไรแล้วครับ{/cps}"
                    show chr_l2
                    u "{cps=10}โอเคครับ{/cps}"
                    hide chr_l2
                    c "{cps=10}คนต่อไป{/cps}"
                    jump ser
             
            label ser6: 
                $  make16_y = False
                $  make17_y = False
                $  make18_y = False
                $ ma = ["ทำงานอะไรมา ก่อนจะมาที่นี้", "มาที่นี่ทำไม","หมดเรื่องที่จะถามแล้ว ระวังตัวด้วยล่ะ"]
                $ ma1 = renpy.random.choice(ma)
                $ ma.remove(ma1)
                $ ma2= renpy.random.choice(ma)
                $ ma.remove(ma2)
                $ ma3= renpy.random.choice(ma)
                label s6:
                    menu : 
                        c""
                        "[ma1]"if make16_y == False:
                            $ make16_y = True
                            if ma1=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make16
                            if ma1=="มาที่นี่ทำไม":
                                jump make17
                            else:
                                jump make18
                        "[ma2]"if make17_y ==False:
                            $ make17_y = True
                            if ma2=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make16
                            if ma2=="มาที่นี่ทำไม":
                                jump make17
                            else:
                                jump make18
                        "[ma3]"if make18_y == False:
                            $ make18_y = True
                            if ma3=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make16
                            if ma3=="มาที่นี่ทำไม":
                                jump make17
                            else:
                                jump make18
                        
            label make16: 
                    c "{cps=10}คุณซิโรริ ทำงานเกี่ยวกับอะไรเหรอครับ{/cps}"
                    show chr_j2
                    n "{cps=10}เป็นนางแบบค่ะ ในชื่อซิโรริ นานะ ผู้เป็นคนน่ารักและเรียบร้อยค่ะ{/cps}"
                    hide chr_j2
                    jump s6
            label make17: 
                    c "{cps=10}คุณซิโรริ มาทำอะไรที่นี้ล่ะ{/cps}"
                    show chr_j2
                    n "{cps=10}เขาให้หนูมาโปรโมทอควาเรียมของเขาทางออนไลน์และทีวี เลยมาเจรจากับเขา{/cps}"
                    n "{cps=10}แน่นอนหนูทั้งเก่งและน่ารักยังไงล่ะ{/cps}"
                    hide chr_j2
                    jump s6
            label make18: 
                    c "{cps=10}ไม่มีอะไรแล้วครับ{/cps}"
                    show chr_j2
                    g "{cps=10}โอเคค่ะ{/cps}"
                    hide chr_j2
                    c "{cps=10}คนต่อไป{/cps}"
                    jump ser
                    
            label ser7: 
                $  make19_y = False
                $  make20_y = False
                $  make21_y = False
                $ ma = ["ทำงานอะไรมา ก่อนจะมาที่นี้", "มาที่นี่ทำไม","หมดเรื่องที่จะถามแล้ว ระวังตัวด้วยล่ะ"]
                $ ma1 = renpy.random.choice(ma)
                $ ma.remove(ma1)
                $ ma2= renpy.random.choice(ma)
                $ ma.remove(ma2)
                $ ma3= renpy.random.choice(ma)
                
                label s7:
                    menu : 
                        c""
                        "[ma1]"if make19_y == False:
                            $ make19_y = True
                            if ma1=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make19
                            if ma1=="มาที่นี่ทำไม":
                                jump make20
                            else:
                                jump make21
                        "[ma2]"if make20_y ==False:
                            $ make20_y = True
                            if ma2=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make19
                            if ma2=="มาที่นี่ทำไม":
                                jump make20
                            else:
                                jump make21
                            jump make2
                        "[ma3]"if make21_y == False:
                            $ make21_y = True
                            if ma3=="ทำงานอะไรมา ก่อนจะมาที่นี้":
                                jump make19
                            if ma3=="มาที่นี่ทำไม":
                                jump make20
                            else:
                                jump make21
                        
            label make19:
                    $ s6 = True
                    $ ser_y += 1
                    c "{cps=10}คุณจิกิตะ ทำงานเกี่ยวกับอะไรเหรอครับ{/cps}"
                    show chr_e1
                    t "{cps=10}ผมเป็นผู้เชี่ยวชาญไวน์ครับ{/cps}"
                    hide chr_e1
                    jump s7
            label make20: 
                    $ s6 = True
                    $ ser_y += 2
                    c "{cps=10}คุณจิกิตะ มาทำอะไรที่นี้ล่ะ{/cps}"
                    show chr_e1
                    t "{cps=10}ผมจะมาปฏิเสธกับคิวจู โดมะ
                    เพราะว่าผมจะต้องไปที่บ้านเกิดตัวเองที่บ้านนอกเพื่อหมักไวน์ของผมต่อครับ{/cps}"
                    hide chr_e1
                    show chr_f2
                    j "งั้นก็สรุปมาเจรจากับคิวจู โดมะ สินะ"
                    hide chr_f2
                    jump s7
            label make21:
                    $ s6 = True
                    c "{cps=10}ไม่มีอะไรแล้วครับ{/cps}"
                    show chr_e1
                    t "{cps=10}โอเคค่ะ{/cps}"
                    hide chr_e1
                    c "{cps=10}คนต่อไป{/cps}"
                    jump ser                
            label who:                    
                    menu : 
                        c"คนนั้นคือ... "
                        "โดมะ นิโตะ"if s1 == True:
                                $ ok1 = True
                                jump w1
                        "มาอาระ นากิซัน"if s2 == True:
                                $ ok2 = True
                                jump w2
                        "นิวารา ชิโกะ"if s4 == True:
                                $ ok4 = True
                                jump w3
                        "โรคุ ดุกิ"if s5 == True:
                                $ ok5 = True
                                jump w4
                        "จิกิตะ ฮาจิโตะ"if s6 == True:
                                $ ok6 = True
                                jump who2
                        "เนด้งย่ง โดเซบ้า"if s3 == True:
                                $ ok3 = True
                                jump w5        
            label w1:
                $ end_y += 1
                show chr_c3
                m "ทำไมผมเป็นคนร้ายไปได้ล่ะ
                แต่ผมยังไม่ได้ทำอะไรเลย"
                hide chr_c3
                c "เพราะว่าคุณคือผู้ต้องสงสัยของเหตุการณ์ทั้งหมดไงล่ะ"
                show chr_c3
                m "เหตุผลมีแค่นี้เหรอ แล้วไหนล่ะ หลักฐานที่บ่งชี้ว่าผมเป็นคนร้าย"
                hide chr_c3
                
                menu : 
                        c"นั้นก็คือ... "                                     
                        "ลูกธนู"if f1 == True:
                            jump wh1
                        "ไม่มีหลักฐาน":
                            jump wh2
            label wh1:
                $ end_y += 1
                show chr_c1
                m "นี่ไม่ได้เกี่ยวข้องกับผมเลยครับ"
                hide chr_c1
                c "นี่คือหลักฐานที่ใช้มัดตัวคุณไงล่ะ"
                show chr_c1
                m "นี่ไม่ใช่ของผม ถ้าไม่รู้จริงอย่ามาใส่ร้ายกันมั่ว"
                hide chr_c1
                c "ไม่จริง เป็นไปไม่ได้ ก็ทุกอบ่างบ่งชี้มาที่คุณนี้หน่า"
                jump ed1
            label wh2:
                show chr_c1
                m "นี่ไม่ได้เกี่ยวข้องกับผมเลยครับ"
                hide chr_c1
                show chr_f3
                j "คุณนักสืบ คุณแน่ใจได้ยังไงทั้งที่ไม่มีหลักฐานอะไรเลย"
                hide chr_f3
                c "คนนี้ล่ะ คนร้ายแน่นอน สัญชาตญาณของผมมันร่ำร้อง"
                show chr_f3
                j "! ! ! !"
                hide chr_f3
                jump ed2 
            label w2:
                $ end_y += 1
                show chr_h1
                o "...คุณพูดบ้าอะไรของคุณเนื้ย"
                o "ทำไมฉันถึงเป็นคนร้ายไปได้ล่ะ"
                hide chr_h1
                c "เพราะว่าคุณคือผู้ต้องสงสัยของเหตุการณ์ทั้งหมดไงล่ะ"
                show chr_h1
                o "เหตุผลมีแค่นี้เหรอ แล้วไหนล่ะ หลักฐานที่บ่งชี้ว่าฉันเป็นคนร้าย"
                hide chr_h1
                menu : 
                        c"นั้นก็คือ... "
                        
                        "ไพ่เลข 8"if f2 == True:
                            jump wh3
                        "ไม่มีหลักฐาน":
                            jump wh4
            label wh3:
                $ end_y += 1
                show chr_h3
                o "นี่ไม่ได้เกี่ยวข้องกับฉันเลยค่ะ"
                hide chr_h3
                c "นี่คือหลักฐานที่ใช้มัดตัวคุณไงล่ะ"
                show chr_h3
                o "นี่ไม่ใช่ของผม ถ้าไม่รู้จริงอย่ามาใส่ร้ายกันมั่ว"
                hide chr_h3
                c "ไม่จริง เป็นไปไม่ได้ ก็ทุกอบ่างบ่งชี้มาที่คุณนี้หน่า"
                jump ed1
            label wh4:
                show chr_h3
                o "นี่ไม่ได้เกี่ยวข้องกับฉันเลยค่ะ"
                hide chr_h3
                show chr_f3
                j "คุณนักสืบ คุณแน่ใจได้ยังไงทั้งที่ไม่มีหลักฐานอะไรเลย"
                hide chr_f3
                c "คนนี้ล่ะ คนร้ายแน่นอน สัญชาตญาณของผมมันร่ำร้อง"
                show chr_f3
                j "! ! ! !"
                hide chr_f3
                jump ed2 
            label w3:
                $ end_y += 1
                show chr_b3
                g "ทำไมหนูถึงเป็นคนร้ายไปได้ล่ะ"
                hide chr_b3
                c "เพราะว่าคุณคือผู้ต้องสงสัยของเหตุการณ์ทั้งหมดไงล่ะ"
                show chr_b3
                g "เหตุผลมีแค่นี้เหรอ แล้วไหนล่ะ หลักฐานที่บ่งชี้ว่าหนูเป็นคนร้าย"
                hide chr_b3
                menu : 
                        c"นั้นก็คือ... "
                        
                        "ดอกไม้สีขาว"if f3 == True:
                            jump wh5
                        "ไม่มีหลักฐาน":
                            jump wh6
            label wh5:
                $ end_y += 1
                show chr_b2
                g "นี่ไม่ได้เกี่ยวข้องกับฉันเลยค่ะ"
                hide chr_b2
                c "นี่คือหลักฐานที่ใช้มัดตัวคุณไงล่ะ"
                show chr_b2
                g "นี่ไม่ใช่ของผม ถ้าไม่รู้จริงอย่ามาใส่ร้ายกันมั่ว"
                hide chr_b2
                c "ไม่จริง เป็นไปไม่ได้ ก็ทุกอบ่างบ่งชี้มาที่คุณนี้หน่า"
                jump ed1
            label wh6:
                show chr_b2
                g "นี่ไม่ได้เกี่ยวข้องกับฉันเลยค่ะ"
                hide chr_b2
                show chr_f3
                j "คุณนักสืบ คุณแน่ใจได้ยังไงทั้งที่ไม่มีหลักฐานอะไรเลย"
                hide chr_f3
                c "คนนี้ล่ะ คนร้ายแน่นอน สัญชาตญาณของผมมันร่ำร้อง"
                show chr_f3
                j "! ! ! !"
                hide chr_f3
                jump ed2  
            label w4:
                $ end_y += 1
                show chr_l3
                u "ทำไมผมเป็นคนร้ายไปได้ล่ะ"
                hide chr_l3
                c "เพราะว่าคุณคือผู้ต้องสงสัยของเหตุการณ์ทั้งหมดไงล่ะ"
                show chr_l3
                u "เหตุผลมีแค่นี้เหรอ แล้วไหนล่ะ หลักฐานที่บ่งชี้ว่าผมเป็นคนร้าย"
                hide chr_l3
                menu : 
                        c"นั้นก็คือ... "
                        
                        "ไพ่รูปคิง"if f4 == True:
                            jump wh7
                        "ไม่มีหลักฐาน":
                            jump wh8
            label wh7:
                $ end_y += 1
                show chr_l1
                u "นี่ไม่ได้เกี่ยวข้องกับผมเลยครับ"
                hide chr_l1
                c "นี่คือหลักฐานที่ใช้มัดตัวคุณไงล่ะ"
                show chr_l1
                u "นี่ไม่ใช่ของผม ถ้าไม่รู้จริงอย่ามาใส่ร้ายกันมั่ว"
                hide chr_l1
                c "ไม่จริง เป็นไปไม่ได้ ก็ทุกอบ่างบ่งชี้มาที่คุณนี้หน่า"
                jump ed1
            label wh8:
                show chr_l1
                u "นี่ไม่ได้เกี่ยวข้องกับผมเลยครับ"
                hide chr_l1
                show chr_f3
                j "คุณนักสืบ คุณแน่ใจได้ยังไงทั้งที่ไม่มีหลักฐานอะไรเลย"
                hide chr_f3
                c "คนนี้ล่ะ คนร้ายแน่นอน สัญชาตญาณของผมมันร่ำร้อง"
                show chr_f3
                j "! ! ! !"
                hide chr_f3
                jump ed2  
            label w5:
                $ end_y += 1
                show chr_i1
                f "ทำไมผมเป็นคนร้ายไปได้ล่ะ"
                hide chr_i1
                c "เพราะว่าคุณคือผู้ต้องสงสัยของเหตุการณ์ทั้งหมดไงล่ะ"
                show chr_i1
                f "เหตุผลมีแค่นี้เหรอ แล้วไหนล่ะ หลักฐานที่บ่งชี้ว่าผมเป็นคนร้าย"
                hide chr_i1
                menu : 
                        c"นั้นก็คือ... "
                        
                        "หัวจุนไวน์"if f5 == True:
                            jump wh9
                        "ไม่มีหลักฐาน":
                            jump wh10
            label wh9:
                $ end_y += 1
                show chr_i1
                f "นี่ไม่ได้เกี่ยวข้องกับผมเลยครับ"
                hide chr_i1
                c "นี่คือหลักฐานที่ใช้มัดตัวคุณไงล่ะ"
                show chr_i1
                f "นี่ไม่ใช่ของผม ถ้าไม่รู้จริงอย่ามาใส่ร้ายกันมั่ว"
                hide chr_i1
                c "ไม่จริง เป็นไปไม่ได้ ก็ทุกอบ่างบ่งชี้มาที่คุณนี้หน่า"
                jump ed1
            label wh10:
                show chr_i1
                f "นี่ไม่ได้เกี่ยวข้องกับผมเลยครับ"
                hide chr_i1
                show chr_f3
                j "คุณนักสืบ คุณแน่ใจได้ยังไงทั้งที่ไม่มีหลักฐานอะไรเลย"
                hide chr_f3
                c "คนนี้ล่ะ คนร้ายแน่นอน สัญชาตญาณของผมมันร่ำร้อง"
                show chr_f3
                j "! ! ! !"
                hide chr_f3
                jump ed2  
        label end:
                    scene work
                    image eo = Text("ช่วงสรุปผล", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                    show eo
                    ""
                    hide eo
                    show chr_2 at right
                    "{cps=10}สวัสดีผู้เล่น สนุกไหม{/cps}"
                    "{cps=10}ขออธิบายตอนสุดท้ายในการนับคะแนน 
                    ว่าโดยการนับคะแนนมาจากการระบุคนร้ายกับโชว์หลักฐาน/cps}"
                    $ te= []
                    if ok1 == True:
                        $ te.append("โดมะ นิโตะ")
                    else:
                        jump l1
        label l1:
                        if ok2 == True:
                            $ te.append("มาอาระ นากิซัน")
                        else:
                            jump l2
        label l2:
                        if ok3 == True:
                            $ te.append("เนด้งย่ง โดเซบ้า")
                        else:
                            jump l3
        label l3:
                        if ok4 == True:
                            $ te.append("นิวารา ชิโกะ")
                        else:
                            jump l4
        label l4:
                        if ok5 == True:
                            $ te.append("โรคุ ดุกิ")
                        else:
                            jump l5
        label l5:
                        if ok6 == True:
                            $ te.append("จิกิตะ ฮาจิโตะ")
                        else:
                            jump l6
        label l6:                    
                    "{cps=10}ส่วนโชว์คะแนนรวมที่ได้มาเดี๋ยวจะโชว์หลังจากผมไปนะ{/cps}"
                    "{cps=10}บายบาย{/cps}"
                    hide chr_2 at right
                    if end_y == 2:
                        image e1 = Text("สรุปผล 1/5", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show e1
                        "[te[0]]"
                        jump end1
                    if end_y == 3:
                        image e2 = Text("สรุปผล 2/5", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show e2
                        "[te[0]]"
                        jump end1
                    if end_y == 4:
                        image e3 = Text("สรุปผล 3/5", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show e3
                        "[te[0]]"
                        jump end1
                    if end_y == 5:
                        image e4 = Text("สรุปผล 4/5", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show e4
                        "[te[0]]"
                        jump end1
                    if end_y == 6:
                        image e5 = Text("สรุปผล 5/5", color="#cdfffc", size=48, xpos=0.5, ypos=0.5)
                        show e5
                        "[te[0]]"
                        jump end1
        
        label end1:
            ""
            hide e1
            "ขอบคุณที่มาเล่นกันนะครับ"
        return
