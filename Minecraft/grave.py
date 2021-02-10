def kom():
    agent.teleport_to_player()
player.on_chat("kom", kom)


def grav_trapp():
    for i in range(60):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
        agent.destroy(RIGHT)
        agent.destroy(LEFT)
        agent.destroy(FORWARD)
        agent.destroy(DOWN)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
        agent.destroy(FORWARD)        
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
player.on_chat("trapp", grav_trapp)

def grav_tunell():
    for i in range(100):
        agent.destroy(DOWN)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(FORWARD)
        agent.destroy(UP)
        agent.move(FORWARD, 1)
player.on_chat("tunell", grav_tunell)


def hugg_tre():
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    for i in range(10):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(UP)
        agent.move(UP, 1)
player.on_chat("hugg", hugg_tre)

def drep_mobs():
    b = 50
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(CREEPER)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(ZOMBIE)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(SPIDER)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(ENDERMAN)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(WITCH)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(DROWNED)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(SLIME)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(SKELETON)),
        player.position(),
        b))
    mobs.kill(mobs.near(mobs.entities_by_type(mobs.monster(PILLAGER)),
        player.position(),
        b))
player.on_chat("drep", drep_mobs)
    

def tnt():
    blocks.fill(TNT, pos(1, 0, 1), pos(5, 5, 5), FillOperation.REPLACE)
player.on_chat("tnt", tnt)

def bro():
    blocks.fill(STONE, pos(1, 0, 1), pos(4, 0, 100), FillOperation.REPLACE)
player.on_chat("bro", bro)

def broS():
    blocks.fill(STONE, pos(1, 0, 1), pos(4, 0, -100), FillOperation.REPLACE)
player.on_chat("bros", broS)

def broV():
    blocks.fill(STONE, pos(1, 0, 1), pos(100, 0, 4), FillOperation.REPLACE)
player.on_chat("brov", broV)

def broO():
    blocks.fill(STONE, pos(1, 0, 1), pos(-100, 0, 4), FillOperation.REPLACE)
player.on_chat("broø", broO)

def diamant():
    blocks.fill(DIAMOND_BLOCK, pos(1, 0, 1), pos(2, 1, 2), FillOperation.REPLACE)
player.on_chat("rustning", diamant)

def metall():
    blocks.fill(IRON_BLOCK, pos(1, 0, 1), pos(2, 1, 2), FillOperation.REPLACE)
player.on_chat("metall", metall)
