label run3:
            ""
            scene background
            ""
            $ renpy.music.queue("audio/chr3.mp3", channel="sound_effect")
            scene ocean2
            "ตอน สรุปคดีฆาตรกรรม"
            show chr_d13 at left
            s "{cps=10}ทุกคนไม่เห็นโดมะแล้วเขาหายไปไหน{/cps}"
            hide chr_d13 at left
                    
            scene background
            "{cps=10}หลังจากอิจิ โซมะพูดเสร็จก็ไฟดับทั้งอควาเรียม{/cps}"
            j "{cps=10}ไฟดับ ทุกคนระวัง{/cps}"
            f "{cps=10}เกิดอะไรขึ้นอีก{/cps}"
            b "{cps=10}ทุกคนอยู่ใกล้กันไว้{/cps}"
            n "{cps=10}ไม่นะะะ กรี๊ดดดด{/cps}"
            
            c "{cps=10}ใจเย็นๆ และอยู่ในความสงบด้วยซิโรริ นานะ{/cps}"
            j "{cps=10}ซิโรริ นานะ หยุดวิ่งในที่มืดเดี๋ยวนี้ ในห้องนี้มีคนร้ายอยู่{/cps}"
            "{cps=10} หลังจากซิโรริ นานะส่งเสียงกรีดร้องก็ได้วิ่งหนีไปโดยไม่ฟังคำเตือนของผู้อื่น 
            พร้อมกับเล็บเรืองแสงจากมือของตัวซิโรริ นานะ{/cps}"
            c "{cps=10}ยาสุโอะ ไปเปิดเบรกเกอร์เร็ว{/cps}"
            b "{cps=10}จะรีบไปเปิดเดี๋ยวนี้{/cps}"
            j "{cps=10}มาอาระ หานานะ จากในที่มืดและปกป้องเขา{/cps}"
            o "{cps=10}ค่ะ นานะจังคุณอยู่ไหน{/cps}"
            n "{cps=10}อยู่นี่ อยู่นี่{/cps}"
            c "{cps=10}(ยาสุโอะ เร็วๆเข้า){/cps}"
            z "{cps=10}ครึ่ก ครึ่ก ครึ่ก{/cps}" 
            n "{cps=10}กรี๊ดดดด{/cps}"                     
            j "{cps=10}คนร้ายอยู่ตรงไหน{/cps}"
            z "{cps=10}ครึ่ก ครึ่ก ครึ่ก ตุบ{/cps}!"
            c "{cps=10}(นี้มันเสียงกระป๋องน้ำจากที่โต๊ะนิ){/cps}"
            
            "{cps=10}หลังจากได้ยินเสียงของคนร้ายที่หลบหนีไปจากที่มืด ไฟก็ได้สว่างขึ้นอีกครั้ง{/cps}"
            scene ocean3
            "{cps=10}ซิโรริ นานะ ตายโดยมีดที่ปัดหลังเอาไว้แล้วล้มลงตรงที่ไม่ไกลจากโต๊ะข้างๆ{/cps}"
            show chr_b1 at right
            g "{cps=10}ก ก ก ก กรี๊ด{/cps}"
            hide chr_b1 at right
            show chr_f12 at left
            j "{cps=10}เสร็จกันเรามาช้าไป{/cps}"
            show chr_h3 at right
            show chr_f13 at left
            hide chr_f12 at left
            o "{cps=10}ขอโทษด้วย ที่ตามเธอกลับมาไม่ทัน เธอวิ่งออกไปเร็วมาก{/cps}"
            show chr_h1 at right
            hide chr_h3 at right
            show chr_f12 at left
            hide chr_f13 at left
            j "{cps=10}เหตุการณ์เกิดขึ้นเร็วมาก ไม่มีใครคาดคิดว่าเธอจะวิ่งออกไปยังงั้น{/cps}"
            hide chr_h1 at right
            show chr_h3 at right
            hide chr_f12 at left
            show chr_f13 at left
            o "{cps=10}ค่ะ{/cps}"
            hide chr_h3 at right
            hide chr_f13 at left
            "หลังจากที่ไฟสว่างขึ้นอีกครั้ง ทุกคนก็ได้มารวม ตัวกันใกล้ๆ ศพของ ซิโรริ นานะ"
            show chr_f12 at left
            j "{cps=10}แล้วนี่คืออะไร{/cps}"
            show chr_h4 at right
            show chr_f13 at left
            hide chr_f12 at left
            o "{cps=10}มันคือเล็บปลอมค่ะไว้สำหรับตกแต่งตรงเล็บค่ะ{/cps}"
            show chr_b1 at right
            hide chr_h4 at right
            g "{cps=10}แต่หนูเห็นแสงที่ตรงเล็บด้วย{/cps}"
            show chr_f12 at left
            hide chr_f13 at left
            j "{cps=10}แสดงว่าคนร้ายได้ใส่ฟอสฟอรัสในยาทาเล็บก่อนให้นานะสินะ{/cps}"
            show chr_h1 at right
            hide chr_b1 at right
            show chr_f13 at left
            hide chr_f12 at left
            o "{cps=10}แล้วใครเป็นคนสั่งให้เลขาของคุณคิวจู โดมะ ส่งน้ำยาทาเล็บให้เธอกัน{/cps}"
            hide chr_h1 at right
            show chr_f12 at left
            hide chr_f13 at left
            j "{cps=10}อืมก็จริงนะ หรือไม่ก็สลับน้ำยาทาเล็บก็เป็นไปได้{/cps}"
            show chr_f13 at left
            hide chr_f12 at left
            show chr_a2
            b "{cps=10}ผมมาแล้ว และเปิดเบรกเกอร์แล้วครับ{/cps}"
            hide chr_f13 at left
            show chr_a3
            hide chr_a2
            c "{cps=10}ขอบคุณมากยาสุโอะ แต่เหมือนมันจะช้าไป{/cps}"
            show chr_a2
            hide chr_a3
            b "{cps=10}ขอโทษจริงๆที่ไปเปิดเบรกเกอร์ไม่ทัน{/cps}"
            show chr_a3
            hide chr_a2
            c "{cps=10}ไม่เป็นไร ยาสุโอะ ดูเหมือนว่าคนร้ายจะอยู่ในกลุ่มนี้แน่ๆ 
            เพราะว่าคนร้ายเข้าหาตัวนานะได้เร็วเกินไปในช่วงระยะเวลาสั้นๆ ขนาดนี้โดยที่ไม่มีใครตัว{/cps}"
            show chr_a2
            hide chr_a3
            b "{cps=10}ก็จริง แต่พวกเราจะรู้ว่าใครเป็นคนร้ายกัน{/cps}"
            show chr_a3
            hide chr_a2
            show chr_c13 at left
            hide chr_k12 at left
            m "{cps=10}เกิดอะไรขึ้นครับทุกคน หะ นานะตายแล้วหรอ{/cps}"
            show chr_i13 at left
            hide chr_c13 at left
            f "{cps=10}อย่ามาตอแหล โดมะ แกสินะเป็นคนร้ายที่ฆ่าคุณนานะ คุณจูโคโร่ และคุณคิวจู  สินะ{/cps}"
            show chr_c11 at left
            hide chr_i13 at left  
            m "{cps=10}แต่ผมไปเข้าห้องน้ำแค่แปปเดี๋ยว ก็ให้ผมเป็นคนร้ายแล้ว 
            มันสมเหตุสมผลไหม พูดอะไรบ้างสิครับ คุณ อิจิ{/cps}"
            show chr_d12 at left
            hide chr_c11 at left
            s "{cps=10}แล้วทำไมนายไม่บอกฉัน หรือว่าแกเป็นคนร้ายเพราะไม่พอใจที่ฉันคนนี้ไม่เพิ่มตำแหน่งและเงินเดือนให้สินะ{/cps}"
            show chr_c11 at left
            hide chr_d12 at left 
            m "{cps=10}จะเป็นแบบนั้นได้ไงครับ ทุกคนผมไม่ใช่คนร้ายแน่นอน{/cps}"
            show chr_l11 at left
            hide chr_c11 at left 
            u "{cps=10}แล้วจะเป็นใครอีกล่ะที่เป็นคนร้ายหลังจากที่นานะ ตายไปได้สักพัก ถึงพึ่งปรากฏตัวออกมา{/cps}"
            show chr_e13 at left
            hide chr_l11 at left
            t "{cps=10}ผมว่าโดมะไม่ใช่คนร้ายนะ เพราะว่าถ้าหลบหนีไปแล้ว โดมะที่เป็นคนร้ายคงไม่เลือกมาในเวลาอย่างตอนนี้ 
            เพราะจะโดนส่งสัยเปล่าๆ แถมเขายังไม่มีอาการเหนื่อยหอบเลยด้วย{/cps}"
            hide chr_e13 at left
            show chr_b1 at right
            hide chr_h1 at right
            g "{cps=10}จริงค่ะ เพราะมีร่องรอยต่อสู้ขัดขืนกับคนร้าย 
            ถ้าโดมะเป็นคนร้ายต้องมีอาการเหนื่อยล้าบ้าง{/cps}"
            show chr_d12 at left
            hide chr_b1 at right
            s "{cps=10}ยังงั้นหรอ ขอโทษจริงๆนะ โดมะ{/cps}"
            show chr_c12 at left
            hide chr_d12 at left
            m "{cps=10}ไม่เป็นไรครับ แค่คุณอิจิและทุกคนอย่ามาเข้าใจผมผิดก็พอแล้วครับ{/cps}"
            hide chr_c12 at left
            c "{cps=10}ตอนนี้พวกเราควรจะมาสังเกตว่าคนร้ายที่หนีไปเป็นใครกันแน่ ที่แอบแฝงอยู่ในกลุ่ม{/cps}"
            show chr_a2
            hide chr_a3
            b "{cps=10}โอเคเข้าใจแล้ว  แต่ว่า %(c)s คุณกระตือรือร้นถึงขั้นที่ปากระป๋องน้ำใส่คนร้ายเลยเหรอ{/cps}"
            show chr_a3
            hide chr_a2
            c "{cps=10}ไม่ใช่ผมปากระป๋องน้ำใส่ แต่คนร้ายเดินไปชนโต๊ะที่มีกระป๋องน้ำอยู่เลยกระเด็นต่างหาก{/cps}"
            show chr_a2
            hide chr_a3
            b "{cps=10}ถ้างั้นคนร้ายก็มีรอยน้ำเปื้อนเสื้อผ้าจากกระป๋องน้ำที่ตกสินะ{/cps}"
            show chr_a3
            hide chr_a2
            c "{cps=10}ใช่มีความเป็นไปได้ รีบตามหาตัวให้เจอกัน{/cps}"
            hide chr_a2
            "{cps=10}นักสืบและผู้ช่วยนักสืบ เริ่มตามหาคนที่มีรอยน้ำเปื้อนบนเสื้อผ้า{/cps}"
            
            " เวลาผ่านไปสักพัก หลังจากที่นักสืบและผู้ช่วยนักสืบเริ่มสังเกตุ 
            ผู้รอดชีวิตคนอื่นด้วยสายตา ก็พบหนึ่งในผู้รอดชีวิตที่มีบางอย่างผิดปกติ"
            scene jean
            b "{cps=10}ไม่จริงใช่มั้ย{/cps}"
            c "{cps=10}น่าจะใช่เพราะเขาเป็นคนเดียวที่มีรอยน้ำ{/cps}"
            b  "{cps=10}แต่ไม่มีหลักฐานส่งถึงเขาเลยนะ{/cps}"
            c  "{cps=10}พวกเราต้องหาหลักฐานในบริเวณนี้เพิ่มอีกหน่อย 
            ถ้าไม่มีก็ให้คิดว่าเป็นคนร้ายไว้ก่อนเลย{/cps}"
            b  "{cps=10}โอเค{/cps}"
            
            "หลังจากที่นักสืบและผู้ช่วยนักสืบเริ่มส่งสัย ก็ได้ค้นหาหลักฐานจนมั่นใจแล้วว่าใครเป็นคนร้าย
	และ กำลังจะเปิดเผยความจริง ก็เหตุการณ์แปลกประหลาดขึ้น"
            z "{cps=10}เสียงกดปุ่ม{/cps}"
            
            scene ocean4
            "ฉากน้ำท่วมจากอควาเลี่ยม"
            j "{cps=10}ร ระเบิดเหรอเนี่ย!{/cps}"
            o "{cps=10}ทุกคนระวัง{/cps}"
            "อควาเรียมที่น้ำท่วมพร้อมกับไพ่เลข 4 5 6 ที่ลอยขึ้นมากับน้ำ"
            show chr_a2
            b  "{cps=10}ทุกคนยังปลอดภัยอยู่ไหม{/cps}"
            show chr_a3
            hide chr_a2
            show chr_f12 at left
            j  "{cps=10}ยังปลอดภัยอยู่ แต่สถานการณ์ไม่ค่อยดีเท่าไร{/cps}"
            show chr_f13 at left
            hide chr_f12 at left
            show chr_h2 at right
            o "{cps=10}ยังปลอดภัยอยู่ค่ะ{/cps}"
            show chr_b3 at right
            hide chr_h2 at right
            g "{cps=10}ยังปลอดภัยอยู่ค่ะ{/cps}"
            show chr_e13 at left
            hide chr_f13 at left
            show chr_b1 at right
            hide chr_b3 at right
            t "{cps=10}ยังปลอดภัยอยู่ แต่ผมเกือบจะจมน้ำแล้วครับ{/cps}"
            show chr_c13 at left
            hide chr_e13 at left
            m "{cps=10}ยังปลอดภัยอยู่ครับ คุณอิจิอยู่ไหนครับ ช่วยตอบด้วย{/cps}"
            show chr_d11 at left
            hide chr_c13 at left
            s "{cps=10}ทำไม ทำไม ต้องเกิดเรื่องแบบนี้ขึ้นด้วย{/cps}"
            show chr_i11 at left
            hide chr_d11 at left
            f "{cps=10}ช่วยด้วยผมว่ายน้ำไม่เป็น{/cps}"
            show chr_l12 at left
            hide chr_i11 at left
            u "{cps=10}เดี๋ยวฉันช่วยคุณเอง{/cps}"      
            show chr_i14 at left
            hide chr_l12 at left
            f "{cps=10}ขอบคุณมากครับ{/cps}"
            show chr_l12 at left
            hide chr_i14 at left
            u "{cps=10}ไม่เป็นไร{/cps}"
            show chr_l13 at left
            hide chr_l12 at left
            show chr_a2
            hide chr_a3
            b "{cps=10}ดูนี่สิครับ{/cps}"
            show chr_a3
            hide chr_a2
            show chr_h4 at right
            hide chr_b1 at right
            o "{cps=10}นี่คนร้ายคิดจะเก็บคุณเนด้งย่ง คุณนิวาราและคุณโรคุ 3 คนพร้อมกันในทีเดียวเลยสิน่ะ{/cps}"
            show chr_l14 at left
            hide chr_l13 at left
            hide chr_h4 at right
            u "{cps=10}แปลว่าเรารอดจากการฆ่าแล้วสิน่ะ{/cps}"
            hide chr_l14 at left
            show chr_b1 at right
            g "{cps=10}ใช่ค่ะ{/cps}"
            show chr_c13 at left
            hide chr_b1 at right
            m "{cps=10}จะรอดหรือไม่รอดก็ออกจากตรงนี้ก่อนไหม{/cps}"
            show chr_f12 at left
            hide chr_c13 at left
            j "{cps=10}ก็จริง แต่ผมสังเกตมานานแล้วว่าคุณ %(c)s อยู่ไหนกัน{/cps}"
            show chr_f13 at left
            hide chr_f12 at left
            c "{cps=10}อยู่นี่ครับ  ผมเจอทางออกจากใต้น้ำครับ 
            โดยการดำน้ำออกไปแล้วขึ้นฝั่งตรงตึกดูดาวของอควาเรียมครับps}"
            show chr_f12 at left
            hide chr_f13 at left
            j "{cps=10}เยี่ยมเลย ทุกคนกลั่นหายใจ แล้วเริ่มดำน้ำกัน{/cps}"
            show chr_i11 at left
            hide chr_f12 at left
            f "{cps=10}อีกแล้วเหรอ{/cps}"
            show chr_l12 at left
            hide chr_i11 at left
            u "{cps=10}ไม่เป็นไร แค่คุณกลั่นหายใจก็พอ{/cps}"
            show chr_i11 at left
            hide chr_l12 at left
            f "{cps=10}โอ เค ครับ{/cps}"
            hide chr_a3
            hide chr_i11 at left
            z "เสียงน้ำ"
            jump give
