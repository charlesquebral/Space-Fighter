    def hit_bonus(self):
        hit_group=pygame.sprite.spritecollide(self,bonusGroup,True)
        
        for bonus in hit_group:
            r=random.randint(0,3)
            #for testing a specific bonus only r=2
            if (bonus.type=="health"):
                self.add_health(50)
            elif bonus.type=="bullet":
                self.bonus_time=pygame.time.get_ticks()
                self.bullet_num=2
            elif bonus.type=="laser":
                self.bonus_time=pygame.time.get_ticks()
                #indicates constantly shooting laser instead of bullet
                self.bullet_num=999
            elif bonus.type=="timewarp"
                enemy.speed_y=2
            #regenerate a random bonus after player get a bonus
            if (r==0):
                bonus=Bonus(heartIMG,"health")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
            elif(r==1):
                bonus=Bonus(bonus_double_bulletIMG,"bullet")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
            elif(r==2):
                bonus=Bonus(bonus_laserIMG,"laser")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
            elif(r==3) :
                bonus=Bonus(bonus_timeWarpIMG,"timeWarp")
                spriteGroup.add(bonus)
                bonusGroup.add(bonus)
    
