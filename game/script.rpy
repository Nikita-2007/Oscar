define e = Character(None)

screen street:
    fixed:
        xsize 1920 ysize 1080
        add "images/bg/street1.png" align (.5,.5)
screen sms1:
    fixed:
        xsize 1920 ysize 1080
        add 'images/dialog/sms1/1.png' align (.5,.5)
screen sms2:
    fixed:
        xsize 1920 ysize 1080
        add 'images/dialog/sms1/2.png' align (.5,.5)
screen sms3:
    fixed:
        xsize 1920 ysize 1080
        add 'images/dialog/sms1/3.png' align (.5,.5)
screen sms4:
    fixed:
        xsize 1920 ysize 1080
        add 'images/dialog/sms1/4.png' align (.5,.5)

label start:
    play sound "audio/walk.mp3"
    with fade
    show screen street
    with dissolve
    play sound "audio/sms.mp3"
    show screen sms1
    with dissolve
    e ' '
    show screen sms2
    e ' '
    show screen sms3
    e ' '
    show screen sms4
    e ' '
    jump cor
