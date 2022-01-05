namespace SpriteKind {
    export const Erba = SpriteKind.create()
    export const Spina = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    game.over(true)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.vy == 0) {
        mySprite.vy = -120
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Spina, function (sprite4, otherSprite2) {
    info.changeLifeBy(-2)
    otherSprite2.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Erba, function (sprite2, otherSprite) {
    info.changeLifeBy(1)
    info.changeScoreBy(1)
    otherSprite.destroy()
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite3, location2) {
    game.over(false)
})
let Spine: Sprite = null
let Erba2: Sprite = null
let mySprite: Sprite = null
scene.setBackgroundColor(9)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.ay = 200
scene.cameraFollowSprite(mySprite)
controller.moveSprite(mySprite, 100, 0)
tiles.setTilemap(tilemap`level1`)
scene.setBackgroundImage(img`
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
    `)
for (let value of tiles.getTilesByType(assets.tile`myTile2`)) {
    tiles.setTileAt(value, assets.tile`transparency16`)
    tiles.placeOnTile(Erba2, value)
    Erba2 = sprites.create(img`
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
        `, SpriteKind.Erba)
    animation.runImageAnimation(
    Erba2,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
}
info.setLife(3)
for (let value2 of tiles.getTilesByType(assets.tile`myTile3`)) {
    Spine = sprites.create(img`
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
        `, SpriteKind.Spina)
    tiles.placeOnTile(Spine, value2)
    tiles.setTileAt(value2, assets.tile`transparency16`)
    animation.runImageAnimation(
    Spine,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    500,
    true
    )
}
game.onUpdate(function () {
    mySprite.setImage(img`
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
        `)
    if (mySprite.vy < 0) {
        mySprite.setImage(img`
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
            `)
    } else if (mySprite.vy > 0) {
        mySprite.setImage(img`
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
            `)
    } else if (mySprite.x % 2 == 0) {
        mySprite.setImage(img`
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
            `)
    } else {
    	
    }
    if (mySprite.vx < 0) {
        mySprite.image.flipX()
    }
})
forever(function () {
    music.playMelody("E B C5 A B G A F ", 103)
})
