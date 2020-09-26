from manimlib.imports import *

class SquareEqualCubes(Scene):
    def construct(self):
        self.write_equation()
        self.calculate_LHS_RHS()

    def write_equation(self):
        theorem = TextMobject("Number Theory: Nicomachus's Theorem").to_edge(UP)
        title = TextMobject('The ', 'square of the sum', ' is equal to the ', 'sum of the cubes').shift(2*UP)
        equation = TexMobject('(1+2+3+....+n)^2', '=', '1^3 +2^3 + 3^3 +....+n^3')
        method = TextMobject("A Visual Proof").shift(2*DOWN)

        box_LHS1 = SurroundingRectangle(title[1]).set_color(GREEN)
        box_RHS1 = SurroundingRectangle(title[3]).set_color(RED)
        box_LHS2 = SurroundingRectangle(equation[0]).set_color(GREEN)
        box_RHS2 = SurroundingRectangle(equation[2]).set_color(RED)

        self.play(
            Write(theorem),
            run_time = 2
        )
        self.play(
            Write(title),
            run_time = 2
        )
        self.wait(2)

        self.play(
            Write(equation),
            run_time = 2
        )
        self.wait(2)

        self.play(
            title[1].set_color,GREEN,
            equation[0].set_color,GREEN
        )

        self.play(
            ShowCreation(box_LHS1),
            ShowCreation(box_LHS2)
        )

        self.wait(2)

        self.play(
            title[3].set_color,RED,
            equation[2].set_color,RED
        )

        self.play(
            ShowCreation(box_RHS1),
            ShowCreation(box_RHS2)
        )
        self.wait(2)

        self.play(Write(method))
        self.wait(2)
        self.play(
            FadeOut(VGroup(*self.mobjects))
        )
        self.wait()

    def calculate_LHS_RHS(self):
        equation0 = TexMobject('(1+2+3+....+n)^2', '=', '1^3 +2^3 + 3^3 +....+n^3')
        equation0.set_color(BLUE)
        equation0.to_edge(UP)

        self.add(equation0)

        comment1 = TextMobject("\\text{Let's consider this equation for} n = 5").shift(UP)
        equation = TexMobject('(1+2+3+4+5)^2', '=', '1^3 +2^3 + 3^3 + 4^3+ 5^3').shift(DOWN)
        equation.set_color(BLUE)
        self.add(comment1,equation0)
        self.play(Write(equation))
        self.wait(3)
        self.play(
            equation0.shift, 5*UP,
            comment1.shift,5*UP,
            equation.to_edge,UP
        )

        big_sq = Square(side_length=4.5).shift(4*LEFT)
        bottom_brace = Brace(big_sq,DOWN)
        bottom_text = bottom_brace.get_text('15')
        side_brace = Brace(big_sq,RIGHT)
        side_text = side_brace.get_text('15')

        self.play(
            ShowCreation(big_sq),
            GrowFromCenter(bottom_brace),
            GrowFromCenter(bottom_text),
            GrowFromCenter(side_brace),
            GrowFromCenter(side_text)
        )

        comment2 = TextMobject("Consider a 15 x 15 square").shift(2*UP+3.5*RIGHT)
        self.play(Write(comment2))
        self.wait(3)

        comment3 = TextMobject("Area of the square = 15 x 15").shift(UP+3.5*RIGHT)
        self.play(Write(comment3))
        self.wait(3)

        comment_list = ["Let's divide this square into", 
                        "15x15 small squares"]

        comment4 = VGroup(*[TextMobject(item) for item in comment_list]).arrange(DOWN)
        comment4.shift(DOWN+3.5*RIGHT)
        self.play(Write(comment4))
        self.wait(3)

        n = 15
        sqs_list = []
        for i in range(n):
            row = []
            for j in range(n):
                mob = Square(side_length=0.3)
                row.append(mob)
            sqs_horizontal = VGroup(*row)
            sqs_horizontal.arrange(RIGHT,buff=0)
            sqs_list.append(sqs_horizontal)

        sqs = VGroup(*sqs_list)

        sqs.arrange(DOWN,buff=0)
        sqs.shift(4*LEFT)

        self.play(
            ShowCreation(sqs)
        )
        self.wait()
        self.remove(big_sq)

        self.remove(comment2,comment3,comment4)

        comment_list = ["Side of the square is 15", 
                        "Let's see if we can",
                         "write the area as LHS"]

        comment5 = VGroup(*[TextMobject(item) for item in comment_list]).arrange(DOWN)
        comment5.shift(UP+3.5*RIGHT)
        self.play(Write(comment5))
        self.wait(2)

        self.remove(bottom_brace,bottom_text,side_brace,side_text)

        s1 = VGroup(sqs[0][0])
        s1copy = s1.copy()
        s1copy.set_fill(color=YELLOW,opacity=1)

        self.play(
            s1.set_fill,YELLOW,1,
        )
        self.play(
            s1copy.shift,4.75*DOWN
        )

        s2_list = []
        for i in range(1,3):
            for j in range(1,3):
                s2_list.append(sqs[i][j])
        
        s2 = VGroup(*s2_list)
        s2copy = VGroup(*[sqs[2][j].copy() for j in range(1,3)])
        s2copy.set_fill(color=GREEN,opacity=1)

        self.play(
            s2.set_fill,GREEN,1,
        )
        self.play(
            s2copy.next_to,s1copy,RIGHT,{"buff":0}
        )

        s3_list = []
        for i in range(3,6):
            for j in range(3,6):
                s3_list.append(sqs[i][j])
        
        s3 = VGroup(*s3_list)
        s3copy = VGroup(*[sqs[5][j].copy() for j in range(3,6)])
        s3copy.set_fill(color=LIGHT_BROWN,opacity=1)

        self.play(
            s3.set_fill,LIGHT_BROWN,1,
        )
        self.play(
            s3copy.next_to,s2copy,RIGHT,{"buff":0}
        )

        s4_list = []
        for i in range(6,10):
            for j in range(6,10):
                s4_list.append(sqs[i][j])
        
        s4 = VGroup(*s4_list)
        s4copy = VGroup(*[sqs[9][j].copy() for j in range(6,10)])
        s4copy.set_fill(color=DARK_BLUE,opacity=1)

        self.play(
            s4.set_fill,DARK_BLUE,1,
        )
        self.play(
            s4copy.next_to,s3copy,RIGHT,{"buff":0}
        )

        s5_list = []
        for i in range(10,15):
            for j in range(10,15):
                s5_list.append(sqs[i][j])
        
        s5 = VGroup(*s5_list)
        s5copy = VGroup(*[sqs[14][j].copy() for j in range(10,15)])
        s5copy.set_fill(color=MAROON,opacity=1)

        self.play(
            s5.set_fill,MAROON,1,
        )
        self.play(
            s5copy.next_to,s4copy,RIGHT,{"buff":0}
        )

        # Right side single squares
        s1copyr = s1.copy()
        s1copyr.set_fill(color=YELLOW,opacity=1)
        s2copyr = VGroup(*[sqs[j][2].copy() for j in range(1,3)])
        s2copyr.set_fill(color=GREEN,opacity=1)
        s3copyr = VGroup(*[sqs[j][5].copy() for j in range(3,6)])
        s3copyr.set_fill(color=LIGHT_BROWN,opacity=1)
        s4copyr = VGroup(*[sqs[j][9].copy() for j in range(6,10)])
        s4copyr.set_fill(color=DARK_BLUE,opacity=1)
        s5copyr = VGroup(*[sqs[j][14].copy() for j in range(10,15)])
        s5copyr.set_fill(color=MAROON,opacity=1)

        self.play(
            s1copyr.shift,5*RIGHT,
        )
        self.play(
            s2copyr.next_to,s1copyr,DOWN,{"buff":0},
        )
        self.play(
            s3copyr.next_to,s2copyr,DOWN,{"buff":0},
        )
        self.play(
            s4copyr.next_to,s3copyr,DOWN,{"buff":0},
        )
        self.play(
            s5copyr.next_to,s4copyr,DOWN,{"buff":0}
        )

        self.wait()

        bottom_bar = VGroup(s1copy,s2copy,s3copy,s4copy,s5copy)
        side_bar = VGroup(s1copyr,s2copyr,s3copyr,s4copyr,s5copyr)

        bottom_brace = Brace(bottom_bar,DOWN)
        bottom_text = bottom_brace.get_text('15')
        side_brace = Brace(side_bar,RIGHT)
        side_text = side_brace.get_text('15')

        self.play(
            GrowFromCenter(bottom_brace),
            GrowFromCenter(bottom_text)          
        )

        self.play(
            GrowFromCenter(side_brace),
            GrowFromCenter(side_text)
        )
        self.wait()

        bb1 = Brace(s1copy,DOWN).set_color(YELLOW)
        bt1 = bb1.get_text('1').set_color(YELLOW)
        bb2 = Brace(s2copy,DOWN).set_color(GREEN)
        bt2 = bb2.get_text('2').set_color(GREEN)
        bb3 = Brace(s3copy,DOWN).set_color(LIGHT_BROWN)
        bt3 = bb3.get_text('3').set_color(LIGHT_BROWN)
        bb4 = Brace(s4copy,DOWN).set_color(DARK_BLUE)
        bt4 = bb4.get_text('4').set_color(DARK_BLUE)
        bb5 = Brace(s5copy,DOWN).set_color(MAROON)
        bt5 = bb5.get_text('5').set_color(MAROON)

        sb1 = Brace(s1copyr,RIGHT).set_color(YELLOW)
        st1 = sb1.get_text('1').set_color(YELLOW)
        sb2 = Brace(s2copyr,RIGHT).set_color(GREEN)
        st2 = sb2.get_text('2').set_color(GREEN)
        sb3 = Brace(s3copyr,RIGHT).set_color(LIGHT_BROWN)
        st3 = sb3.get_text('3').set_color(LIGHT_BROWN)
        sb4 = Brace(s4copyr,RIGHT).set_color(DARK_BLUE)
        st4 = sb4.get_text('4').set_color(DARK_BLUE)
        sb5 = Brace(s5copyr,RIGHT).set_color(MAROON)
        st5 = sb5.get_text('5').set_color(MAROON)

        self.remove(bottom_brace,bottom_text)
        self.play(
            GrowFromCenter(bb1),
            GrowFromCenter(bt1)
        )
        self.play(
            GrowFromCenter(bb2),
            GrowFromCenter(bt2)
        )
        self.play(
            GrowFromCenter(bb3),
            GrowFromCenter(bt3)
        )
        self.play(
            GrowFromCenter(bb4),
            GrowFromCenter(bt4)
        )
        self.play(
            GrowFromCenter(bb5),
            GrowFromCenter(bt5)
        )
        self.wait()

        self.remove(side_brace,side_text)
        self.play(
            GrowFromCenter(sb1),
            GrowFromCenter(st1)
        )
        self.play(
            GrowFromCenter(sb2),
            GrowFromCenter(st2)
        )
        self.play(
            GrowFromCenter(sb3),
            GrowFromCenter(st3)
        )
        self.play(
            GrowFromCenter(sb4),
            GrowFromCenter(st4)
        )
        self.play(
            GrowFromCenter(sb5),
            GrowFromCenter(st5)
        )
        self.wait()

        comment_list = ["\\text {Area of the square}", 
                        "= 15 \\times 15",
                         "= 15^2",
                         "= (1 + 2 + 3 + 4 + 5)^2"]

        comment6 = VGroup(*[TexMobject(item) for item in comment_list]).arrange(DOWN)
        comment6.shift(3.5*RIGHT)
        self.remove(comment5)
        self.play(
            Write(comment6[0:2])
        )
        self.wait()
        self.play(
            Write(comment6[2])
        )
        self.wait(2)
        text = TextMobject('15 = 1 + 2 + 3 + 4 + 5').next_to(comment6[2],DOWN)
        self.play(
            Write(text)
        )
        self.wait()
        self.play(
            text.shift,10*RIGHT
        )
        self.play(
            Write(comment6[3])
        )
        self.wait()


        box1 = SurroundingRectangle(equation[0])
        box1.set_color(RED)

        box2 = SurroundingRectangle(comment6[-1])
        box2.set_color(RED)

        self.play(
            ShowCreation(box1),
            ShowCreation(box2)
        )

        comment_list = ["Area of the square is", 
                        "equal to the LHS"]

        comment7 = VGroup(*[TextMobject(item) for item in comment_list]).arrange(DOWN)
        comment7.shift(3*DOWN+3.5*RIGHT)
        self.play(Write(comment7))
        self.wait(3)

        # RHS
        mobs_to_remove = VGroup(comment7,box2,box1,comment6)
        mobs_to_fade1 = VGroup(sb1,sb2,sb3,sb4,sb5,st1,st2,st3,st4,st5)
        mobs_to_fade2 = VGroup(bb1,bb2,bb3,bb4,bb5,bt1,bt2,bt3,bt4,bt5)
        self.play(
            mobs_to_remove.shift,20*RIGHT,
            FadeOut(mobs_to_fade1),
            FadeOut(mobs_to_fade2),
            runt_time = 3
        )

        mobs_to_fade3 = VGroup(s1copy,s2copy,s3copy,s4copy,s5copy)
        mobs_to_fade4 = VGroup(s1copyr,s2copyr,s3copyr,s4copyr,s5copyr)
        self.play(
            FadeOut(mobs_to_fade3),
            FadeOut(mobs_to_fade4),
            runt_time = 3
        )

        comment_list = ["Now let's find the area", 
                        "in terms of the RHS"]

        comment8 = VGroup(*[TextMobject(item) for item in comment_list]).arrange(DOWN)
        comment8.shift(3.5*RIGHT)
        self.play(Write(comment8))
        self.wait(3)

        self.play(comment8.shift,10*RIGHT)

        green_list = []
        for i in range(1,3):
            green_list.append(sqs[i][0])
        greens1 = VGroup(*green_list)

        green_list = []
        for i in range(1,3):
            green_list.append(sqs[0][i])
        greens2 = VGroup(*green_list)

        self.play(
            greens1.set_fill,GREEN,1,
            greens2.set_fill,GREEN,1,
        )

        brown_list = []
        for i in range(3,6):
            for j in range(3):
                brown_list.append(sqs[i][j])
        browns1 = VGroup(*brown_list)

        brown_list = []
        for i in range(3):
            for j in range(3,6):
                brown_list.append(sqs[i][j])
        browns2 = VGroup(*brown_list)

        self.play(
            browns1.set_fill,LIGHT_BROWN,1,
            browns2.set_fill,LIGHT_BROWN,1,
        )
        self.wait()

        blue_list = []
        for i in range(6,10):
            for j in range(2):
                blue_list.append(sqs[i][j])
        blues1 = VGroup(*blue_list)

        blue_list = []
        for i in range(6,10):
            for j in range(2,6):
                blue_list.append(sqs[i][j])
        blues2 = VGroup(*blue_list)

        blue_list = []
        for i in range(2,6):
            for j in range(6,10):
                blue_list.append(sqs[i][j])
        blues3 = VGroup(*blue_list)

        blue_list = []
        for i in range(2):
            for j in range(6,10):
                blue_list.append(sqs[i][j])
        blues4 = VGroup(*blue_list)

        self.play(
            blues1.set_fill,DARK_BLUE,1,
            blues2.set_fill,DARK_BLUE,1,
            blues3.set_fill,DARK_BLUE,1,
            blues4.set_fill,DARK_BLUE,1,
        )
        self.wait()

        maroon_list = []
        for i in range(10,15):
            for j in range(5):
                maroon_list.append(sqs[i][j])
        maroons1 = VGroup(*maroon_list)

        maroon_list = []
        for i in range(10,15):
            for j in range(5,10):
                maroon_list.append(sqs[i][j])
        maroons2 = VGroup(*maroon_list)

        maroon_list = []
        for i in range(5,10):
            for j in range(10,15):
                maroon_list.append(sqs[i][j])
        maroons3 = VGroup(*maroon_list)

        maroon_list = []
        for i in range(5):
            for j in range(10,15):
                maroon_list.append(sqs[i][j])
        maroons4 = VGroup(*maroon_list)

        self.play(
            maroons1.set_fill,MAROON,1,
            maroons2.set_fill,MAROON,1,
            maroons3.set_fill,MAROON,1,
            maroons4.set_fill,MAROON,1,
        )
        self.wait()

        rect_yellow = SurroundingRectangle(s1,buff=0).set_color(BLACK)
        self.add(rect_yellow)
        self.wait()

        rect_greens0 = SurroundingRectangle(s2,buff=0).set_color(BLACK)
        rect_greens1 = SurroundingRectangle(greens1,buff=0).set_color(BLACK)
        rect_greens2 = SurroundingRectangle(greens2,buff=0).set_color(BLACK)
        self.add(rect_greens0,rect_greens1,rect_greens2)
        self.wait()

        rect_browns0 = SurroundingRectangle(s3,buff=0).set_color(BLACK)
        rect_browns1 = SurroundingRectangle(browns1,buff=0).set_color(BLACK)
        rect_browns2 = SurroundingRectangle(browns2,buff=0).set_color(BLACK)
        self.add(rect_browns0,rect_browns1,rect_browns2)
        self.wait()

        rect_blues0 = SurroundingRectangle(s4,buff=0).set_color(BLACK)
        rect_blues1 = SurroundingRectangle(blues1,buff=0).set_color(BLACK)
        rect_blues2 = SurroundingRectangle(blues2,buff=0).set_color(BLACK)
        rect_blues3 = SurroundingRectangle(blues3,buff=0).set_color(BLACK)
        rect_blues4 = SurroundingRectangle(blues4,buff=0).set_color(BLACK)
        self.add(rect_blues0,rect_blues1,rect_blues2,rect_blues3,rect_blues4)
        self.wait()

        rect_maroons0 = SurroundingRectangle(s5,buff=0).set_color(BLACK)
        rect_maroons1 = SurroundingRectangle(maroons1,buff=0).set_color(BLACK)
        rect_maroons2 = SurroundingRectangle(maroons2,buff=0).set_color(BLACK)
        rect_maroons3 = SurroundingRectangle(maroons3,buff=0).set_color(BLACK)
        rect_maroons4 = SurroundingRectangle(maroons4,buff=0).set_color(BLACK)
        self.add(rect_maroons0,rect_maroons1,rect_maroons2,rect_maroons3,rect_maroons4)
        self.wait()

        s1f = s1.copy()
        s2f = s2.copy()
        s3f = s3.copy()
        s4f = s4.copy()
        s5f = s5.copy()
        greens1f = greens1.copy()
        greens2f = greens2.copy()
        browns1f = browns1.copy()
        browns2f = browns2.copy()
        blues1f = blues1.copy()
        blues2f = blues2.copy()
        blues3f = blues3.copy()
        blues4f = blues4.copy()
        maroons1f = maroons1.copy()
        maroons2f = maroons2.copy()
        maroons3f = maroons3.copy()
        maroons4f = maroons4.copy()

        self.play(
            s1f.move_to,np.array((0,2.5,0)),
            run_time = 2
        )

        self.play(
            s2f.move_to,np.array((0,1.75,0)),
            greens1f.move_to,np.array((1,1.75,0)),
            greens2f.move_to,np.array((2,1.75,0)),
            run_time = 3
        )

        self.play(
            s3f.move_to,np.array((0,0.4,0)),
            browns1f.move_to,np.array((1.5,0.4,0)),
            browns2f.move_to,np.array((3.0,0.4,0)),
            run_time = 3
        )

        self.play(
            s4f.move_to,np.array((1.5,-1,0)),
            blues1f.move_to,np.array((4.5,-1,0)),
            blues2f.move_to,np.array((0,-1,0)),
            blues3f.move_to,np.array((3,-1,0)),
            blues4f.move_to,np.array((6,-1,0)),
            run_time = 5
        )

        self.play(
            s5f.move_to,np.array((-0.7,-2.7,0)),
            maroons1f.move_to,np.array((1.05,-2.7,0)),
            maroons2f.move_to,np.array((2.8,-2.7,0)),
            maroons3f.move_to,np.array((4.55,-2.7,0)),
            maroons4f.move_to,np.array((6.3,-2.7,0)),
            run_time = 5
        )

        self.play(
            greens2f.rotate,PI/2,
            greens2f.next_to,greens1f,RIGHT,{"buff":0},
        )
        self.play(
            blues4f.rotate,PI/2,
            blues4f.next_to,blues1f,RIGHT,{"buff":0},
        )
        self.wait()

        into1 = TexMobject("\\times 1").next_to(s1f,RIGHT)
        into1.set_color(YELLOW)
        self.play(
            Write(into1)
        )

        into2 = TexMobject("\\times 2").next_to(s2f,RIGHT)
        into2.set_color(GREEN)
        self.play(
            Transform(VGroup(s2f,greens1f,greens2f),s2f),
            Write(into2)
        )

        into3 = TexMobject("\\times 3").next_to(s3f,RIGHT)
        into3.set_color(LIGHT_BROWN)
        self.play(
            Transform(VGroup(s3f,browns1f,browns2f),s3f),
            Write(into3)
        )

        into4 = TexMobject("\\times 4").next_to(blues2f,RIGHT)
        into4.set_color(DARK_BLUE)
        self.play(
            Transform(VGroup(s4f,blues1f,blues2f,blues3f,blues4f),blues2f),
            Write(into4)
        )

        s5ff = s5f.copy().move_to(np.array((0,-2.7,0)))
        into5 = TexMobject("\\times 5").next_to(s5ff,RIGHT)
        into5.set_color(MAROON)
        
        self.play(
            Transform(VGroup(s5f,maroons1f,maroons2f,maroons3f,maroons4f),s5ff),
            Write(into5)
        )

        self.wait()

        sc1 = TexMobject("= 1^2 \\times 1 = 1^3").next_to(into1)
        sc2 = TexMobject("= 2^2 \\times 2 = 2^3").next_to(into2)
        sc3 = TexMobject("= 3^2 \\times 3 = 3^3").next_to(into3)
        sc4 = TexMobject("= 4^2 \\times 4 = 4^3").next_to(into4)
        sc5 = TexMobject("= 5^2 \\times 5 = 5^3").next_to(into5)

        sc1.set_color(YELLOW)
        sc2.set_color(GREEN)
        sc3.set_color(LIGHT_BROWN)
        sc4.set_color(DARK_BLUE)
        sc5.set_color(MAROON)

        self.play(
            Write(sc1),
        )
        self.play(
            Write(sc2),
        )
        self.play(
            Write(sc3),
        )
        self.play(
            Write(sc4),
        )
        self.play(
            Write(sc5),
        )

        self.wait(3)

        c1 = TexMobject("1^3")
        c2 = TexMobject("2^3")
        c3 = TexMobject("3^3")
        c4 = TexMobject("4^3")
        c5 = TexMobject("5^3")
        plus = TexMobject("+")

        RHS = VGroup(c1,plus,c2,plus.copy(),c3,plus.copy(),c4,plus.copy(),c5)
        RHS.arrange(DOWN)
        RHS.to_edge(RIGHT)

        box3 = SurroundingRectangle(RHS).set_color(RED)
        box4 = SurroundingRectangle(equation[2]).set_color(RED)

        self.play(
            Write(RHS)
        )
        self.wait()

        self.play(
            ShowCreation(box3),
            ShowCreation(box4)
        )

        self.wait()
        
        big_sq = Square(side_length=4.5).shift(4*LEFT)
        bottom_brace = Brace(big_sq,DOWN)
        bottom_text = bottom_brace.get_text('15')
        side_brace = Brace(big_sq,RIGHT)
        side_text = side_brace.get_text('15')

        self.play(
            ShowCreation(big_sq),
            GrowFromCenter(bottom_brace),
            GrowFromCenter(bottom_text),
            GrowFromCenter(side_brace),
            GrowFromCenter(side_text)
        )

        LHSarea = TextMobject("Area = LHS").move_to(np.array((-5.5,-3.6,0)))
        RHSarea = TextMobject("Area = RHS").move_to(np.array((5.5,-3.6,0)))

        self.play(
            Write(LHSarea)
        )

        self.play(
            Write(RHSarea)
        )
        self.wait(2)

        self.play(
            VGroup(*self.mobjects).shift, 20*UP
        )

        thank = TextMobject("Thank You !!!").scale(3)
        thank.set_color(DARK_BLUE)

        self.play(Write(thank))
        self.wait()


