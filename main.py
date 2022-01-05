@namespace
class SpriteKind:
    Erba = SpriteKind.create()
    Spina = SpriteKind.create()

def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_on_overlap(sprite2, otherSprite):
    info.change_life_by(1)
    info.change_score_by(1)
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Erba, on_on_overlap)

def on_overlap_tile2(sprite3, location2):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

def on_a_pressed():
    if mySprite.vy == 0:
        mySprite.vy = -120
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap2(sprite4, otherSprite2):
    info.change_life_by(-2)
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Spina, on_on_overlap2)

Spine: Sprite = None
Erba2: Sprite = None
mySprite: Sprite = None
scene.set_background_color(9)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . e . . . . 
            . . . . . . . . . . e e e e . . 
            . . . . . . . . . e e e f e . . 
            . . . . e e e e e e e e e e e . 
            . . . e e e e e e e d d d . . . 
            . . e e e d d d d d d . . . . . 
            . . e d d d . d . d . . . . . . 
            . e e . d . . e . e . . . . . . 
            e e . . e . . e . e . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
mySprite.ay = 200
scene.camera_follow_sprite(mySprite)
controller.move_sprite(mySprite, 100, 0)
tiles.set_tilemap(tilemap("""
    level1
"""))
scene.set_background_image(img("""
    ccccccccccccccccccccccceeeeeeeeeeeeeeeeeeecccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebbccccccccccccccccccccc
        ccccccccccccccccccccccceeeeeeeeeeeeeeeeeeecccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebbccccccccccccccccccccc
        ccccccccccccccccccccccceeeeeeeeeeeeeeeeeeecccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeebbccccccccccccccccccccc
        cccccccccccccccccccccccceeeeeeeeeeeeeeeeeecccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeebbccccccccccccccccccccc
        ccccccccccccccbbcccccccceeeeeeeeeeeeeeeeeecccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeebbccccccccccccccccccccc
        ccccccccccccccbbccccccccceeeeeeeeeeeeeeeeecccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeebccccccccccccccccccccc
        ccccccccccccccbbbcccccccceeeeeeeeeeeeeeeeecccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeebccccccccccccccccccccc
        ccccccccccccccbbbccccccccceeeeeeeeeeeeeeeeccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeebccccccccccccccccccccc
        ccccccccccccccbbbccccccccceeeeeeeeeeeeeeeeccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeebbcccccccccccccccccccc
        ccccccccccccccbbbccccccccceeeeeeeeeeeeeeeeccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeebbcccccccccccccccccccc
        ccccccccccccccbbbccccccccceeeeeeeeeeeeeeeeccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeebbcccccccccccccccccccc
        ccccccccccccccbbbcccccccccceeeeeeeeeeeeeeeccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeebbcccccccccccccccccccc
        ccccccccccccccbbbcccccccccceeeeeeeeeeeeeeeccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeebbcccccccccccccccccccc
        ccccccccccccccbbbcccccccccceeeeeeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeebbcccccccccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbccccccccccceeeeeeeeeeeeeeeeeeeeebbcccccccccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbccccccccccceeeeeeeeeeeeeeeeeeeeebbbccccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbccccccccccceeeeeeeeeeeeeeeeeeeeebbbccccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbccccccccccceeeeeeeeeeeeeeeeeeeeebbbccccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbccccccccccceeeeeeeeeeeeeeeeeeeeebbbccccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbccccccccccceeeeeeeeeeeeeeeeeeeeecbbbcccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbcccccccccccceeeeeeeeeeeeeeeeeeeecbbbcccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbcccccccccccceeeeeeeeeeeeeeeeeeeecbbbcccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccbcccccccccccceeeeeeeeeeeeeeeeeeeecbbbcccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccbcccccccccccceeeeeeeeeeeeeeeeeeeecbbbbccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccbbccccccccccceeeeeeeeeeeeeeeeeeeeccbbbccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeecccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccbbcccccccccceeeeeeeeeeeeeeeeeeeeeccbbbccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccbbcccccccccceeeeeeeeeeeeeeeeeeeeeccbbbccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccbbcccccccccceeeeeeeeeeeeeeeeeeeeeccbbbccccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccbbcccccccccceeeeeeeeeeeeeeeeeeeeeccbbbbcccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccbbbcccccccccceeeeeeeeeeeeeeeeeeeeeccbbbbcccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccbbbcccccccccceeeeeeeeeeeeeeeeeeeeeccbbbbbccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccbbbccccccccceeeeeeeeeeeeeeeeeeeeeecccbbbbccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccbbbccccccccceeeeeeeeeeeeeeeeeeeeeecccbbbbccccccccccccccc
        ccccccccccccccbbbbbccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccbbbccccccccceeeeeeeeeeeeeeeeeeeeeecccbbbbccccccccccccccc
        ccccccccccccccbbbbcccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccbbbcccccccceeeeeeeeeeeeeeeeeeeeeeecccbbbbccccccccccccccc
        ccccccccccccccbbbbcccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbbccccccccceeeeeeeeeeeeeeeeeeeeeeeccccbbbbcccccccccccccc
        ccccccccccccccbbbbcccccccccceeeeeeeeeeeeccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbbccccccccceeeeeeeeeeeeeeeeeeeeeeeccccbbbbcccccccccccccc
        ccccccccccccccbbbbcccccccccceeeeeeeeeeeeccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbbccccccccceeeeeeeeeeeeeeeeeeeeeeeccccbbbbcccccccccccccc
        ccccccccccccccbbbbcccccccccceeeeeeeeeeeeccccccccccccccccbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbbccccccccceeeeeeeeeeeeeeeeeeeeeeeccccbbbbcccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeecccccccccccccccccbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbcccccccccceeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeecccccccccccccccccbbbbbbeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbcccccccccceeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeecccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeeecccccbbbbccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeeecccccbbbbccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeeccccccbbbbccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbbeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeeccccccbbbbccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeecccccccbbbccccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeecccccccbbbbcccccccccccc
        ccccccccccccccbbbbccccccccceeeeeeeeeeeccccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbccccccccceeeeeeeeeeeeeeeeeeeeeeecccccccbbbbcccccccccccc
        ccccccccccccccbbbcccccccccceeeeeeeeeeeccccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeecccccccbbbbcccccccccccc
        ccccccccccccccbbbcccccccccceeeeeeeeeeeccccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeecccccccbbbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeccccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeecccccccbbbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeecccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeecccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeecccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccbcccccccccceeeeeeeeeeeecccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccbcccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccbcccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccccccccccccceeeeeeeeeeeeeccccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccccccccccccceeeeeeeeeeeeeecccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        cccccccccccccccccccccccccceeeeeeeeeeeeeeecccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccbcccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        cccccccccccccccccccccccccceeeeeeeeeeeeeeecccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        cccccccccccccccccccccccccceeeeeeeeeeeeeeeeccccccccccccccbbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        cccccccccccccccccccccccccceeeeeeeeeeeeeeeeccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccccccccccceeeeeeeeeeeeeeeeeccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccccccccccceeeeeeeeeeeeeeeeeccccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccccccccccceeeeeeeeeeeeeeeeecccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        ccccccccccccccccccccccccceeeeeeeeeeeeeeeeecccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbcccccccccccc
        cccccccccccccccccccccccccceeeeeeeeeeeeeeeecccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        cccccccccccccccccccccccccceeeeeeeeeeeeeeeccccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        ccccccccccccccccbcccccccccceeeeeeeeeeeeeeccccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        ccccccccccccccccbcccccccccceeeeeeeeeeeeeeccccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        ccccccccccccccccbcccccccccceeeeeeeeeeeeeeccccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        ccccccccccccccccbcccccccccceeeeeeeeeeeeeecccccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeccccccccbbbccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccbbbccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeecccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeecccccccbbcccccccccccc
        cccccccccccccccbbcccccccccceeeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccc
        cccccccccccccccbbccccccccccceeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccc
        cccccccccccccccbbbcccccccccceeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccc
        cccccccccccccccbbbcccccccccceeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccc
        cccccccccccccccbbbcccccccccceeeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbcccccccccccc
        cccccccccccccccbbbccccccccccceeeeeeeeeeeeccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbcccccccccccc
        cccccccccccccccbbbccccccccccceeeeeeeeeeeecccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbcccccccccccc
        cccccccccccccccbbbccccccccccceeeeeeeeeeeecccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbcccccccccccc
        cccccccccccccccbbbccccccccccceeeeeeeeeeeecccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbcccccccccccc
        cccccccccccccccbbbccccccccccceeeeeeeeeeeecccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbcccccccccccc
        cccccccccccccccbbbccccccccccceeeeeeeeeeeecccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeecccbbbcccccccccccc
        cccccccccccccccbbbcccccccccccceeeeeeeeeeecccccccccccccccbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeecccbbbcccccccccccc
        cccccccccccccccbbbcccccccccccceeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbcccccccccccc
        cccccccccccccccbbbcccccccccccceeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbcccccccccccc
        ccccccccccccccccbbcccccccccccceeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbcccccccccccc
        ccccccccccccccccbbcccccccccccceeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbcccccccccccc
        ccccccccccccccccbccccccccccccceeeeeeeeeeeccccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeccccbcccccccccccc
        ccccccccccccccccbccccccccccccceeeeeeeeeeeecccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeccccbcccccccccccc
        ccccccccccccccccbccccccccccccceeeeeeeeeeeecccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccc
        ccccccccccccccccbccccccccccccceeeeeeeeeeeecccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccc
        ccccccccccccccccbccccccccccccceeeeeeeeeeeecccccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccc
        ccccccccccccccccbccccccccccccceeeeeeeeeeeecccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbccccccccccc
        cccccccccccccccccccccccccccccceeeeeeeeeeeeeccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbccccccccccc
        cccccccccccccccccccccccccccccceeeeeeeeeeeeeccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbccccccccccc
        cccccccccccccccccccccccccccccceeeeeeeeeeeeeccccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbccccccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeecccccccccccbbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbcccccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeccccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeecccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbccccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeecccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeecccccbbbccccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeececccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbccccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeecccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbccccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeecccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbccccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeecccccccccbbeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbbcccccccc
        ccccccccccccccccccccccccccccceeeeeeeeeeeeeeeeecccccccccbeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeccccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeccccbbbbcccccccc
"""))
for value in tiles.get_tiles_by_type(assets.tile("""
    myTile2
""")):
    tiles.set_tile_at(value, assets.tile("""
        transparency16
    """))
    tiles.place_on_tile(Erba2, value)
    Erba2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . 7 b . 7 b . . . 7 7 . . . . . 
                    . 7 7 b . 7 b . 7 7 b 7 b . . . 
                    . . 7 b . 7 b 7 7 b . 7 b . . . 
                    . . 7 b . 7 b 7 b . . 7 b b . . 
                    . . 7 b 7 b b 7 7 b . . 7 b . . 
                    . . 7 b 7 b . . 7 b . 7 7 b . . 
                    . 7 7 b 7 b . . 7 b . 7 b . . . 
                    . 7 b . 7 b . . 7 b . 7 b . . . 
                    . 7 7 b 7 b . . 7 b . 7 b . . . 
                    . . 7 b 7 b . 7 b . 7 7 b . . . 
                    . . 7 b 7 b . 7 b . 7 b . . . . 
                    . . 7 b 7 7 7 7 b . 7 b . . . . 
                    . 7 7 b . 7 7 b . . 7 7 b . . .
        """),
        SpriteKind.Erba)
    animation.run_image_animation(Erba2,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . 7 . . . . . . . . 7 . . . . 
                        . . 7 . . . . . 7 7 . . 7 . . . 
                        . . 7 7 . 7 . . . 7 . . 7 . . . 
                        . . . 7 . 7 7 . . 7 . . 7 . . . 
                        . . . 7 . . 7 . 7 7 . 7 7 . . . 
                        . . 7 7 . . 7 . 7 . . . 7 . . . 
                        . . 7 . . . 7 . 7 . . . 7 . . . 
                        . . 7 . . 7 7 . 7 . . . 7 . . . 
                        . 7 7 . . 7 . . 7 7 . . 7 . . . 
                        . 7 7 . . 7 7 . . 7 . . 7 . . . 
                        . . 7 . . . 7 . . 7 . . 7 7 . . 
                        . . 7 . . 7 7 . . 7 7 . . 7 . . 
                        . . 7 . 7 7 . . . . 7 . . 7 7 . 
                        . . 7 . 7 . . . . 7 7 . 7 7 . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        7 . . . . . . . . . . . . . . . 
                        7 . . . . . 7 7 . . 7 . . . . . 
                        7 7 . 7 . . . 7 . . 7 . . . . . 
                        . 7 . 7 7 . . 7 . . 7 . . . . . 
                        . 7 . . 7 . 7 7 . . 7 . . . . . 
                        7 7 . . 7 . 7 . . 7 7 . . . . . 
                        . 7 . . . 7 . 7 . . 7 7 . . . . 
                        . 7 . . 7 7 . 7 . . . 7 . . . . 
                        7 7 . . 7 . . 7 7 . . 7 . . . . 
                        7 7 . . 7 7 . . 7 . . 7 . . . . 
                        . 7 . . . 7 . . 7 . . 7 7 . . . 
                        . 7 . . 7 7 . . . 7 7 . . 7 . . 
                        . . 7 . 7 7 . . . . 7 . . 7 7 . 
                        . . 7 . 7 . . . . 7 7 . 7 7 . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . 7 . . . . . . . . 7 . . . . 
                        . . 7 . . . . . 7 7 . . 7 . . . 
                        . . 7 7 . 7 . . . 7 . . 7 . . . 
                        . . . 7 . 7 7 . . 7 . . 7 . . . 
                        . . . 7 . . 7 . 7 7 . 7 7 . . . 
                        . . 7 7 . . 7 . 7 . . . 7 . . . 
                        . . 7 . . . 7 . 7 . . . 7 . . . 
                        . . 7 . . 7 7 . 7 . . . 7 . . . 
                        . 7 7 . . 7 . . 7 7 . . 7 . . . 
                        . 7 7 . . 7 7 . . 7 . . 7 . . . 
                        . . 7 . . . 7 . . 7 . . 7 7 . . 
                        . . 7 . . 7 7 . . 7 7 . . 7 . . 
                        . . 7 . 7 7 . . . . 7 . . 7 7 . 
                        . . 7 . 7 . . . . 7 7 . 7 7 . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . 7 . . . . . . . . 7 . . 
                        . . . . 7 . . . . . 7 7 . . 7 . 
                        . . . . 7 7 . 7 . . . 7 . . 7 . 
                        . . . . . 7 . 7 7 . . 7 . . 7 . 
                        . . . . . 7 . . 7 . 7 7 7 7 . . 
                        . . . 7 7 . . 7 . 7 . . . 7 . . 
                        . . . 7 . . . 7 . 7 . . . 7 . . 
                        . . . 7 . . 7 7 . 7 . . . 7 . . 
                        . . 7 7 . . 7 . . 7 7 . . 7 . . 
                        . . 7 7 . . 7 7 . . 7 . . 7 . . 
                        . . . 7 . . . 7 . . 7 . . 7 7 . 
                        . . . 7 . 7 7 . . . 7 7 . . 7 . 
                        . . 7 . 7 7 . . . . 7 . . 7 7 . 
                        . . 7 . 7 . . . . 7 7 . 7 7 . .
            """)],
        500,
        True)
info.set_life(3)
for value2 in tiles.get_tiles_by_type(assets.tile("""
    myTile3
""")):
    Spine = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . c . . . . c . . . . c . . . 
                    . . c 2 . . 2 c . . . . c . . . 
                    . . c c . . . c c . . . c 2 . . 
                    . . . c . . . . c c . . c . . . 
                    . . . . c . . . . c . . c . . . 
                    . . . . c c . . 2 c . . c c . . 
                    . . . . 2 c . . . c . . . c . . 
                    . . . . . c . . . c . . . c . . 
                    . . . . c c . . . c . . 2 c . . 
                    . . . c c . . . . c . . . c . . 
                    . . . c . . . . . . c . . c 2 . 
                    . . 2 c . . . . . 2 c . . c . . 
                    . . . c . . . . . . c . . c . . 
                    . . . c . . . . . c c 2 . c . . 
                    . . . c . . . . c c . . . c c .
        """),
        SpriteKind.Spina)
    tiles.place_on_tile(Spine, value2)
    tiles.set_tile_at(value2, assets.tile("""
        transparency16
    """))
    animation.run_image_animation(Spine,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . c . . . . . . . . . 
                        . . . . . . c c c . . . c . . . 
                        . . . c 2 . . . c . . 2 c . . . 
                        . . . c . . . 2 c . . . c . . . 
                        . . . c c . . . c . . . c . . . 
                        . . . . c . . . c . . c c . . . 
                        . . 2 c c . . . c 2 . c . . . . 
                        . . . c . . . . c . c c . . . . 
                        . . . c . . . . c . c . . . . . 
                        . . . c 2 . . . c . c c 2 . . . 
                        . . . c c . . c c . . c . . . . 
                        . . . . c . 2 c . . . c c . . . 
                        . . . . c . . c c . . 2 c . . . 
                        . . c c . . . . c . . c c . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . c . . . . . . . . . . 
                        . . . . . c c c . . . . . c . . 
                        . . c 2 . . . c . . . . 2 c . . 
                        . . c . . . 2 c . . . . . c . . 
                        . . c c . . . c . . . . . c . . 
                        . . . c . . . c . . . . c c . . 
                        . 2 c c . . . c . . 2 . c . . . 
                        . . c . . . . c . . . c c . . . 
                        . . c . . . . c . . . c . . . . 
                        . . c 2 . . . c . . c c 2 . . . 
                        . . c c . . . c c . . c . . . . 
                        . . . c . . 2 c . . . c c . . . 
                        . . . c . . . c c . . 2 c . . . 
                        . . c c . . . . c . . c c . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . c . . . . . . . . . . 
                        . . . . . c c c . . . . . c . . 
                        . . c 2 . . . c . . . . 2 c . . 
                        . . c . . . 2 c . . . . . c . . 
                        . . c c . . . c . . . . . c . . 
                        . . . c . . . c . . . . c c . . 
                        . 2 c c . . . c . . 2 . c . . . 
                        . . c . . . . c . . . c c . . . 
                        . . c . . . . c . . . c . . . . 
                        . . c 2 . . . c . . c c 2 . . . 
                        . . c c . . . c c . . c . . . . 
                        . . . c . . 2 c . . . c c . . . 
                        . . . c . . . c c . . 2 c . . . 
                        . . c c . . . . c . . c c . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . c . . . . . . . . . 
                        . . . . . . c c c . . . c . . . 
                        . . . c 2 . . . c . . 2 c . . . 
                        . . . c . . . 2 c . . . c . . . 
                        . . . c c . . . c . . . c . . . 
                        . . . . c . . . c . . c c . . . 
                        . . 2 c c . . . c 2 . c . . . . 
                        . . . c . . . . c . c c . . . . 
                        . . . c . . . . c . c . . . . . 
                        . . . c 2 . . . c . c c 2 . . . 
                        . . . c c . . c c . . c . . . . 
                        . . . . c . 2 c . . . c c . . . 
                        . . . . c . . c c . . 2 c . . . 
                        . . c c . . . . c . . c c . . .
            """)],
        500,
        True)

def on_on_update():
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . e . . . . 
                . . . . . . . . . . e e e e . . 
                . . . . . . . . . e e e f e . . 
                . . . . e e e e e e e e e e e . 
                . . . e e e e e e e d d d . . . 
                . . e e e d d d d d d . . . . . 
                . . e d d d . d . d . . . . . . 
                . e e . d . . e . e . . . . . . 
                e e . . e . . e . e . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    if mySprite.vy < 0:
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . e . . . . 
                        . . . . . . . . . . e e e e . . 
                        . . . . . . . . . . e e f e . . 
                        . . . . . . . . . e e e e e e . 
                        . . . . . . . e e e d d d . . . 
                        . . . . e e e e e e d . . . . . 
                        . . . e e e e d d d e . . . . . 
                        . . e e e d d d . d e . . . . . 
                        . . e d d d . e . . . . . . . . 
                        . e e . d . . e . . . . . . . . 
                        e e . . e . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    elif mySprite.vy > 0:
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        e e . . . . . . . . . . . . . . 
                        . e . . . . . . . . . . . . . . 
                        . e e e . . . . . . . . . . . . 
                        . . e e e e . . . . . . . . . . 
                        . . e e e e e e e . e . . . . . 
                        . . . d d e e e e e e e e . . . 
                        . . . . d e e d e e e f e . . . 
                        . . . . e d d d e d e e e e . . 
                        . . . . e . . e e d d d . . . . 
                        . . . . . . . e . e . . . . . . 
                        . . . . . . . . . e . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    elif mySprite.x % 2 == 0:
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . e . 3 . . 
                        . . . . . . . . . . e e e e . . 
                        . . . . . . . . . e e e f e . . 
                        . . . . e e e e e e e e e e e . 
                        . . . e e e e e e e d d d . . . 
                        . . e e e d d d d d d . . . . . 
                        . . e d d d d . d . . . . . . . 
                        . e e d . . e . e . . . . . . . 
                        e e . e . . e . e . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    else:
        pass
    if mySprite.vx < 0:
        mySprite.image.flip_x()
game.on_update(on_on_update)

def on_forever():
    music.play_melody("E B C5 A B G A F ", 103)
forever(on_forever)
