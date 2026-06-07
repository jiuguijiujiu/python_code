# 一代英雄机
class HeroFighter:
    def power(self):
        return 60

# 二代英雄机
class AdvHeroFighter(HeroFighter):
    def power(self):
        return 80

# 敌机
class EnemyFighter:
    def power(self):
        return 70

# 对战平台,且限定左边英雄机，右边敌机，限定加了也没有，一般不加
def object_play(hero:HeroFighter, enemy:EnemyFighter):
    if hero.power() >= enemy.power():
        print("英雄机赢了")
    else:
        print("英雄机输了")

if __name__ == '__main__':
    hero1 = HeroFighter()
    hero2 = AdvHeroFighter()
    enemy = EnemyFighter()

    # 第一场
    object_play(hero1, enemy)

    # 第二场
    object_play(hero2, enemy)