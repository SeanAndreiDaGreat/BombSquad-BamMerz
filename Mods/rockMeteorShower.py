""" INFORMATION """
" INFORMATION CAN BE FOUND ON (www.github,com/SeanAndreiDaGreat/BombSquadEr-s-Mod) "
" Check out my channel (www.youtube.com/c/SeanAndreiDaGreat) Subscribing to me helps a lot "
" (Rock Meteor Shower Gamemode) "
""" CODING TIME """

import bs
import random

def bsGetAPIVersion():
    # see bombsquadgame.com/apichanges
    return 4

def bsGetGames():
    return [RockMeteorShower]

def bsGetLevels():
    return [ bs.Level('Rock Meteor Shower', displayName='${GAME}', gameType=RockMeteorShower,
                      settings={}, previewTexName='rampagePreview'),
             bs.Level('Epic Rock Meteor Shower', displayName='${GAME}', gameType=RockMeteorShower,
                      settings={'Epic Mode':True}, previewTexName='rampagePreview') ]

class RockMeteorShower(bs.TeamGameActivity):

    @classmethod
    def getName(cls):
        return 'Rock Meteor Shower'

    @classmethod
    def getScoreInfo(cls):
        return { 'scoreName':'Survived',
                 'scoreType':'milliseconds',
                 'scoreVersion':'B' }
    
    @classmethod
    def getDescription(cls, sessionType):
        return 'Rock is Hard, so Dodge it.'

    # we're currently hard-coded for one map..
    @classmethod
    def getSupportedMaps(cls, sessionType):
        return ['Rampage']

    @classmethod
    def getSettings(cls, sessionType):
        return [("Epic Mode", {'default':False})]
    
    # we support teams, free-for-all, and co-op sessions
    @classmethod
    def supportsSessionType(cls, sessionType):
        return True if (issubclass(sessionType,bs.TeamsSession)
                        or issubclass(sessionType,bs.FreeForAllSession)
                        or issubclass(sessionType,bs.CoopSession)) else False

    def __init__(self,settings):
        bs.TeamGameActivity.__init__(self, settings)

        if self.settings['Epic Mode']: self._isSlowMotion = True

        # print messages when players die (since its meaningful in this game)
        self.announcePlayerDeaths = True

        self._lastPlayerDeathTime = None
        
    def getInstanceScoreBoardDescription(self):
        return 'Survive from the 6 Rock Waves.'
        
    # called when our game is transitioning in but not ready to start..
    # ..we can go ahead and set our music and whatnot
    def onTransitionIn(self):
        bs.TeamGameActivity.onTransitionIn(self, music='Epic' if self.settings['Epic Mode'] else 'Survival')
      
    # called when our game actually starts
    def onBegin(self):

        bs.TeamGameActivity.onBegin(self)

        # drop a wave every few seconds.. and every so often drop the time between waves
        # ..lets have things increase faster if we have fewer players
        self._meteorTime = 1000
        t = 4000 if len(self.players) > 2 else 4000
        if self.settings['Epic Mode']: self._meteorTime = 1000
        if self.settings['Epic Mode']: t = 4000
        bs.gameTimer(t,self._decrementMeteorTime,repeat=True)
        bs.gameTimer(t,self._setMeteorTimer)
        
        t = 5000 if len(self.players) > 2 else 5000
        bs.gameTimer(t,self._rmsWave)
        t = 25000 if len(self.players) > 2 else 25000
        bs.gameTimer(t,self._rmsEnd)
        
        self._meteorTime2 = 1500
        t = 24500 if len(self.players) > 2 else 24500
        if self.settings['Epic Mode']: self._meteorTime2 = 1000
        if self.settings['Epic Mode']: t = 24000
        bs.gameTimer(t,self._decrementMeteorTime2,repeat=True)
        bs.gameTimer(t,self._setMeteorTimer2)
        
        t = 45000 if len(self.players) > 2 else 45000
        bs.gameTimer(t,self._rmsEnd2)
        
        self._meteorTime3 = 2000
        t = 43000 if len(self.players) > 2 else 43000
        if self.settings['Epic Mode']: self._meteorTime3 = 1500
        if self.settings['Epic Mode']: t = 43500
        bs.gameTimer(t,self._decrementMeteorTime3,repeat=True)
        bs.gameTimer(t,self._setMeteorTimer3)
        
        t = 60000 if len(self.players) > 2 else 60000
        bs.gameTimer(t,self._rmsEnd3)
        
        self._meteorTime4 = 0700
        t = 59300 if len(self.players) > 2 else 59300
        if self.settings['Epic Mode']: self._meteorTime4 = 0700
        if self.settings['Epic Mode']: t = 59300
        bs.gameTimer(t,self._decrementMeteorTime4,repeat=True)
        bs.gameTimer(t,self._setMeteorTimer4)
        
        t = 85000 if len(self.players) > 2 else 85000
        bs.gameTimer(t,self._rmsEnd4)
        
        self._meteorTime5 = 1000
        t = 84000 if len(self.players) > 2 else 84000
        if self.settings['Epic Mode']: self._meteorTime5 = 1000
        if self.settings['Epic Mode']: t = 83000
        bs.gameTimer(t,self._decrementMeteorTime5,repeat=True)
        bs.gameTimer(t,self._setMeteorTimer5)
        
        t = 100000 if len(self.players) > 2 else 100000
        bs.gameTimer(t,self._rmsEnd5)
        
        self._meteorTime6 = 0400
        t = 99600 if len(self.players) > 2 else 99600
        if self.settings['Epic Mode']: self._meteorTime6 = 0400
        if self.settings['Epic Mode']: t = 99600
        bs.gameTimer(t,self._decrementMeteorTime6,repeat=True)
        bs.gameTimer(t,self._setMeteorTimer6)
        
        t = 115000 if len(self.players) > 2 else 115000
        bs.gameTimer(t,self._rmsEnd6)
        
        self._meteorMedicTime = 0500
        t = 34500 if len(self.players) > 2 else 34500
        if self.settings['Epic Mode']: self._meteorMedicTime = 0250
        if self.settings['Epic Mode']: t = 34750
        bs.gameTimer(t,self._decrementMeteorMedicTime,repeat=True)
        bs.gameTimer(t,self._setMeteorMedicTimer)
        
        t = 35000 if len(self.players) > 2 else 35000
        bs.gameTimer(t,self._rmsMedic)
        t = 36500 if len(self.players) > 2 else 36500
        bs.gameTimer(t,self._rmsEndMedic)
        
        self._meteorMedicTime2 = 0500
        t = 49500 if len(self.players) > 2 else 49500
        if self.settings['Epic Mode']: self._meteorMedicTime2 = 0250
        if self.settings['Epic Mode']: t = 49750
        bs.gameTimer(t,self._decrementMeteorMedicTime2,repeat=True)
        bs.gameTimer(t,self._setMeteorMedicTimer2)
        
        t = 50000 if len(self.players) > 2 else 50000
        bs.gameTimer(t,self._rmsMedic2)
        t = 51500 if len(self.players) > 2 else 51500
        bs.gameTimer(t,self._rmsEndMedic2)
        
        self._meteorMedicTime3 = 0500
        t = 64500 if len(self.players) > 2 else 64500
        if self.settings['Epic Mode']: self._meteorMedicTime3 = 0250
        if self.settings['Epic Mode']: t = 64750
        bs.gameTimer(t,self._decrementMeteorMedicTime3,repeat=True)
        bs.gameTimer(t,self._setMeteorMedicTimer3)
        
        t = 65000 if len(self.players) > 2 else 65000
        bs.gameTimer(t,self._rmsMedic3)
        t = 66500 if len(self.players) > 2 else 66500
        bs.gameTimer(t,self._rmsEndMedic3)
        
        self._meteorMedicTime4 = 0500
        t = 79500 if len(self.players) > 2 else 79500
        if self.settings['Epic Mode']: self._meteorMedicTime4 = 0250
        if self.settings['Epic Mode']: t = 79750
        bs.gameTimer(t,self._decrementMeteorMedicTime4,repeat=True)
        bs.gameTimer(t,self._setMeteorMedicTimer4)
        
        t = 80000 if len(self.players) > 2 else 80000
        bs.gameTimer(t,self._rmsMedic4)
        t = 81500 if len(self.players) > 2 else 81500
        bs.gameTimer(t,self._rmsEndMedic4)
        
        self._meteorMedicTime5 = 0500
        t = 94500 if len(self.players) > 2 else 94500
        if self.settings['Epic Mode']: self._meteorMedicTime5 = 0250
        if self.settings['Epic Mode']: t = 94750
        bs.gameTimer(t,self._decrementMeteorMedicTime5,repeat=True)
        bs.gameTimer(t,self._setMeteorMedicTimer5)
        
        t = 95000 if len(self.players) > 2 else 95000
        bs.gameTimer(t,self._rmsMedic5)
        t = 96500 if len(self.players) > 2 else 96500
        bs.gameTimer(t,self._rmsEndMedic5)

        self._meteorMedicTime6 = 0500
        t = 115000 if len(self.players) > 2 else 115000
        if self.settings['Epic Mode']: self._meteorMedicTime6 = 0250
        if self.settings['Epic Mode']: t = 117500
        bs.gameTimer(t,self._decrementMeteorMedicTime6,repeat=True)
        bs.gameTimer(t,self._setMeteorMedicTimer6)
        
        t = 110000 if len(self.players) > 2 else 110000
        bs.gameTimer(t,self._rmsMedic6)
        t = 115000 if len(self.players) > 2 else 115000
        bs.gameTimer(t,self._rmsEndMedic6)
        
        t = 120000 if len(self.players) > 2 else 120000
        bs.gameTimer(t,self._rmsEndGame)

        self._timer = bs.OnScreenTimer()
        self._timer.start()

        # check for immediate end (if we've only got 1 player, etc)
        bs.gameTimer(5000, self._checkEndGame)

    def onPlayerJoin(self, player):
        # don't allow joining after we start
        # (would enable leave/rejoin tomfoolery)
        if self.hasBegun():
            bs.screenMessage(bs.Lstr(resource='playerDelayedJoinText',subs=[('${PLAYER}',player.getName(full=True))]),color=(0,1,0))
            # for score purposes, mark them as having died right as the game started
            player.gameData['deathTime'] = self._timer.getStartTime()
            return
        self.spawnPlayer(player)

    def onPlayerLeave(self, player):
         # augment default behavior...
        bs.TeamGameActivity.onPlayerLeave(self, player)
        # a departing player may trigger game-over
        self._checkEndGame()

    
    # overriding the default character spawning..
    def spawnPlayer(self, player):
                    
        spaz = self.spawnPlayerSpaz(player)

        # lets reconnect this player's controls to this
        # spaz but *without* the ability to attack or pick stuff up
        spaz.connectControlsToPlayer(enablePunch=False,
                                     enableBomb=False,
                                     enablePickUp=False)
                                     
        spaz.equipSpeed()

        # also lets have them make some noise when they die..
        spaz.playBigDeathSound = True        
        
    # various high-level game events come through this method
    def handleMessage(self,m):

        if isinstance(m,bs.PlayerSpazDeathMessage):

            bs.TeamGameActivity.handleMessage(self,m) # (augment standard behavior)

            deathTime = bs.getGameTime()
            
            # record the player's moment of death
            m.spaz.getPlayer().gameData['deathTime'] = deathTime
            
            # in co-op mode, end the game the instant everyone dies (more accurate looking)
            # in teams/ffa, allow a one-second fudge-factor so we can get more draws
            if isinstance(self.getSession(),bs.CoopSession):
                # teams will still show up if we check now.. check in the next cycle
                bs.pushCall(self._checkEndGame)
                self._lastPlayerDeathTime = deathTime # also record this for a final setting of the clock..
            else:
                bs.gameTimer(1000, self._checkEndGame)

        else:
            # default handler:
            bs.TeamGameActivity.handleMessage(self,m)

    def _checkEndGame(self):
        livingTeamCount = 0
        for team in self.teams:
            for player in team.players:
                if player.isAlive():
                    livingTeamCount += 1
                    break

        # in co-op, we go till everyone is dead.. otherwise we go until one team remains
        if isinstance(self.getSession(),bs.CoopSession):
            if livingTeamCount <= 0: self.endGame()
        else:
            if livingTeamCount <= 1: self.endGame()
        
    def _setMeteorTimer(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorTime),self._dropBombCluster)
        
    def _setMeteorTimer2(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorTime2),self._dropBombCluster2)
        
    def _setMeteorTimer3(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorTime3),self._dropBombCluster3)
        
    def _setMeteorTimer4(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorTime4),self._dropBombCluster4)
        
    def _setMeteorTimer5(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorTime5),self._dropBombCluster5)
        
    def _setMeteorTimer6(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorTime6),self._dropBombCluster6)
    
    def _setMeteorMedicTimer(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorMedicTime),self._dropMedicBombCluster)
        
    def _setMeteorMedicTimer2(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorMedicTime2),self._dropMedicBombCluster2)
        
    def _setMeteorMedicTimer3(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorMedicTime3),self._dropMedicBombCluster3)
        
    def _setMeteorMedicTimer4(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorMedicTime4),self._dropMedicBombCluster4)
        
    def _setMeteorMedicTimer5(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorMedicTime5),self._dropMedicBombCluster5)
        
    def _setMeteorMedicTimer6(self):
        bs.gameTimer(int((1.0+0.2*random.random())*self._meteorMedicTime6),self._dropMedicBombCluster6)
        
    def _dropBombCluster(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropBomb,pos,vel))
            delay += 100
        self._setMeteorTimer()
        
    def _dropBombCluster2(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropBomb2,pos,vel))
            delay += 100
        self._setMeteorTimer2()
        
    def _dropBombCluster3(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropBomb3,pos,vel))
            delay += 100
        self._setMeteorTimer3()
        
    def _dropBombCluster4(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropBomb4,pos,vel))
            delay += 100
        self._setMeteorTimer4()
        
    def _dropBombCluster5(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropBomb5,pos,vel))
            delay += 100
        self._setMeteorTimer5()
        
    def _dropBombCluster6(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropBomb6,pos,vel))
            delay += 100
        self._setMeteorTimer6()
        
    def _dropMedicBombCluster(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropMedicBomb,pos,vel))
            delay += 100
        self._setMeteorMedicTimer()
        
    def _dropMedicBombCluster2(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropMedicBomb2,pos,vel))
            delay += 100
        self._setMeteorMedicTimer2()
        
    def _dropMedicBombCluster3(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropMedicBomb3,pos,vel))
            delay += 100
        self._setMeteorMedicTimer3()
        
    def _dropMedicBombCluster4(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropMedicBomb4,pos,vel))
            delay += 100
        self._setMeteorMedicTimer4()
        
    def _dropMedicBombCluster5(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropMedicBomb5,pos,vel))
            delay += 100
        self._setMeteorMedicTimer5()
        
    def _dropMedicBombCluster6(self):

        # random note: code like this is a handy way to plot out extents and debug things
        if False:
            bs.newNode('locator',attrs={'position':(8,6,-5.5)})
            bs.newNode('locator',attrs={'position':(8,6,-2.3)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-5.5)})
            bs.newNode('locator',attrs={'position':(-7.3,6,-2.3)})

        # drop several bombs in series..
        delay = 0
        for i in range(random.randrange(1,3)):
            # drop them somewhere within our bounds with velocity pointing toward the opposite side
            pos = (-7.3+15.3*random.random(),11,-5.5+2.1*random.random())
            vel = ((-5.0+random.random()*30.0) * (-1.0 if pos[0] > 0 else 1.0), -4.0,0)
            bs.gameTimer(delay,bs.Call(self._dropMedicBomb6,pos,vel))
            delay += 100
        self._setMeteorMedicTimer6()

    def _dropBomb(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='basketball').autoRetain()
        b = bs.Bomb(position=position,velocity=velocity,bombType='impact').autoRetain()
        
    def _dropBomb2(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='knocker').autoRetain()
        b = bs.Bomb(position=position,velocity=velocity,bombType='impact').autoRetain()
       
    def _dropBomb3(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='ranger').autoRetain()
        b = bs.Bomb(position=position,velocity=velocity,bombType='impact').autoRetain()
        
    def _dropBomb4(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='combat').autoRetain()
        
    def _dropBomb5(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='dynamite').autoRetain()
        
    def _dropBomb6(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity).autoRetain()
        b = bs.Bomb(position=position,velocity=velocity).autoRetain()
        
    def _dropMedicBomb(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='healing').autoRetain()
        
    def _dropMedicBomb2(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='healing').autoRetain()
        
    def _dropMedicBomb3(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='healing').autoRetain()
        
    def _dropMedicBomb4(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='healing').autoRetain()
        
    def _dropMedicBomb5(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='healing').autoRetain()
        
    def _dropMedicBomb6(self,position,velocity):
        b = bs.Bomb(position=position,velocity=velocity,bombType='healing').autoRetain()

    def _decrementMeteorTime(self):
        self._meteorTime = max(10,int(self._meteorTime*0.9))
        
    def _decrementMeteorTime2(self):
        self._meteorTime2 = max(10,int(self._meteorTime2*0.9))
        
    def _decrementMeteorTime3(self):
        self._meteorTime3 = max(10,int(self._meteorTime3*0.9))
        
    def _decrementMeteorTime4(self):
        self._meteorTime4 = max(10,int(self._meteorTime4*0.9))
        
    def _decrementMeteorTime5(self):
        self._meteorTime5 = max(10,int(self._meteorTime5*0.9))
        
    def _decrementMeteorTime6(self):
        self._meteorTime6 = max(10,int(self._meteorTime6*0.9))
     
    def _decrementMeteorMedicTime(self):
        self._meteorMedicTime = max(10,int(self._meteorMedicTime*0.9))
        
    def _decrementMeteorMedicTime2(self):
        self._meteorMedicTime2 = max(10,int(self._meteorMedicTime2*0.9))
        
    def _decrementMeteorMedicTime3(self):
        self._meteorMedicTime3 = max(10,int(self._meteorMedicTime3*0.9))
        
    def _decrementMeteorMedicTime4(self):
        self._meteorMedicTime4 = max(10,int(self._meteorMedicTime4*0.9))
        
    def _decrementMeteorMedicTime5(self):
        self._meteorMedicTime5 = max(10,int(self._meteorMedicTime5*0.9))
        
    def _decrementMeteorMedicTime6(self):
        self._meteorMedicTime6 = max(10,int(self._meteorMedicTime6*0.9))
        
    def _rmsWave(self):
        self.showZoomMessage("Dodge Ball",scale=1.0,duration=3000)
        self.showZoomMessage("Lets Play Basketball.",color=(0.0,0.5,1.0),scale=0.4,duration=3300)
       
    def _rmsEnd(self):
        self.showZoomMessage("Knock it Off",scale=1.0,duration=3000)
        self.showZoomMessage("Knock Knock! Whos There?.",color=(0.0,0.5,1.0),scale=0.4,duration=3300)
        self._meteorTime = 9999999999
        
    def _rmsEnd2(self):
        self.showZoomMessage("Its Getting Closer",scale=1.0,duration=3000)
        self.showZoomMessage("O H H H  N O.",color=(0.0,0.5,1.0),scale=0.4,duration=3300)
        self._meteorTime2 = 9999999999
        
    def _rmsEnd3(self):
        self.showZoomMessage("Fighting Above my Head",scale=1.0,duration=3000)
        self.showZoomMessage("This is not an Aerial Fight.",color=(0.0,0.5,1.0),scale=0.4,duration=3300)
        self._meteorTime3 = 9999999999
        
    def _rmsEnd4(self):
        self.showZoomMessage("No Dynamite Fishing Please?",scale=1.0,duration=3000)
        self.showZoomMessage("Excuse me Im not a Fish.",color=(0.0,0.5,1.0),scale=0.4,duration=3300)
        self._meteorTime4 = 9999999999
        
    def _rmsEnd5(self):
        self.showZoomMessage("Bombs are Rapidly Falling in me",scale=1.0,duration=3000)
        self.showZoomMessage("Cloudy with a Chance of Explosion.",color=(0.0,0.5,1.0),scale=0.4,duration=3300)
        self._meteorTime5 = 9999999999
        
    def _rmsEnd6(self):
        self.showZoomMessage("You have Survived from the Rocks",color=(0.4,0.5,0.6),scale=3.0,duration=5000)
        self._meteorTime6 = 9999999999
        
    def _rmsMedic(self):
        self.showZoomMessage("M E D I C",color=(0.9,0.4,7.0),scale=2.0,duration=3000)
     
    def _rmsMedic2(self):
        self.showZoomMessage("M E D I C",color=(0.9,0.4,7.0),scale=2.0,duration=3000)
        
    def _rmsMedic3(self):
        self.showZoomMessage("M E D I C",color=(0.9,0.4,7.0),scale=2.0,duration=3000)
        
    def _rmsMedic4(self):
        self.showZoomMessage("M E D I C",color=(0.9,0.4,7.0),scale=2.0,duration=3000)
        
    def _rmsMedic5(self):
        self.showZoomMessage("M E D I C",color=(0.9,0.4,7.0),scale=2.0,duration=3000)
        
    def _rmsMedic6(self):
        self.showZoomMessage("M E D I C",color=(0.9,0.4,7.0),scale=2.0,duration=3000)
        
    def _rmsEndMedic(self):
        self._meteorMedicTime = 9999999999
        
    def _rmsEndMedic2(self):
        self._meteorMedicTime2 = 9999999999
        
    def _rmsEndMedic3(self):
        self._meteorMedicTime3 = 9999999999
        
    def _rmsEndMedic4(self):
        self._meteorMedicTime4 = 9999999999
        
    def _rmsEndMedic5(self):
        self._meteorMedicTime5 = 9999999999
        
    def _rmsEndMedic6(self):
        self._meteorMedicTime6 = 9999999999
        
    def _rmsEndGame(self):
        self.endGame()

    def endGame(self):

        curTime = bs.getGameTime()

        # mark 'death-time' as now for any still-living players
        # and award players points for how long they lasted.
        # (these per-player scores are only meaningful in team-games)
        for team in self.teams:
            for player in team.players:

                # throw an extra fudge factor +1 in so teams that
                # didn't die come out ahead of teams that did
                if 'deathTime' not in player.gameData: player.gameData['deathTime'] = curTime+1
                    
                # award a per-player score depending on how many seconds they lasted
                # (per-player scores only affect teams mode; everywhere else just looks at the per-team score)
                score = (player.gameData['deathTime']-self._timer.getStartTime())/1000
                if 'deathTime' not in player.gameData: score += 50 # a bit extra for survivors
                self.scoreSet.playerScored(player,score,screenMessage=False)

        # stop updating our time text, and set the final time to match
        # exactly when our last guy died.
        self._timer.stop(endTime=self._lastPlayerDeathTime)
        
        # ok now calc game results: set a score for each team and then tell the game to end
        results = bs.TeamGameResults()

        # remember that 'free-for-all' mode is simply a special form of 'teams' mode
        # where each player gets their own team, so we can just always deal in teams
        # and have all cases covered
        for team in self.teams:

            # set the team score to the max time survived by any player on that team
            longestLife = 0
            for player in team.players:
                longestLife = max(longestLife,(player.gameData['deathTime'] - self._timer.getStartTime()))
            results.setTeamScore(team,longestLife)

        self.end(results=results)
            
""" END OF CODE """
