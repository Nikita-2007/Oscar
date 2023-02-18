screen corid:
    fixed:
        xsize 1920 ysize 1080
        add "images/bg/corridor.png" align (.5,.5)
    fixed:
        xsize 1920 ysize 1080

        fixed:
            xpos 0 ypos 0
            xsize 1920 ysize 1080
            add "images/dialog/school.png" align(.5,.5)
        fixed:
            xpos 0 ypos 0
            xsize 1920 ysize 1080
            add "images/avatar/door.png" align(.5,.5)

        button:
            xpos 0 ypos 0
            xsize 1920 ysize 1080
            idle_background "images/card/fist.png"
            hover_background "images/card/fisth.png"
            focus_mask True
            action Jump('start')
            hovered Play("sound", "audio/butthover.mp3")

        button:
            xpos 0 ypos 0
            xsize 1920 ysize 1080
            idle_background "images/card/foot.png"
            hover_background "images/card/footh.png"
            focus_mask True
            action Jump('start')
            hovered Play("sound", "audio/butthover.mp3")
label cor:
    show screen corid
    with fade
    with dissolve
    e "{cps=30}{color=#396770}Дверь к классном руководителю \nзаперта.{/color}{/cps}"
