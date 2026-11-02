---
type: smite-god
name: Scylla
pantheon: Greek
role: Mid
specializations:
- Nuker
- Burst Damage
damage_type: magical
release_date: June 2, 2025
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 322.62
    per_level: 48.3
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 40.85
    per_level: 2.21
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.56
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Scylla Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Quick Learner
  details:
  - 'Intelligence: 20 Per Max Ability'
  - 'Mana Regen: 2 Per Max Ability'
  description: MAX RANK ABILITIES ARE STRONGER Your abilities gain an additional effect
    at max rank. In addition, gain Intelligence and Mana Regen for each max rank ability
  detail_kinds:
  - buff
  - buff
- slot: 1st Ability
  name: Sic 'Em
  cooldown:
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - At max rank, the two closest enemies to the first target will also be hit
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 85 | 130 | 175 | 220 | 265'
  - 'Damage Scaling: 75% Intelligence'
  - 'Root Duration: 1.75 seconds'
  - 'Cripple Duration: 1.75 seconds'
  - 'Range: 10.4 meters'
  - 'Radius: 0.48 meters'
  - 'Explosion Radius: 2.4 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Send two hounds forward, Rooting , Crippling , and dealing Magical
    Damage
  damage_type: magical
  detail_kinds:
  - buff
  - null
  - magical
  - magical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Crush
  cooldown:
  - 10.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - At max rank, enemies in the area also have their Magical Protections reduced and
    the field persists if detonated early
  - Reactivate to detonate the field early
  - This ability does 20% bonus damage to Minion and Jungle Monsters.
  - 'Damage: 100 | 155 | 210 | 265 | 320'
  - 'Damage Scaling: 90% Intelligence'
  - 'Slow: 30%'
  - 'Magical Protection Reduced: 10%'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: Creates a magical field that Slows enemies. After 5 seconds it detonates,
    dealing Magical Damage
  damage_type: magical
  detail_kinds:
  - debuff
  - null
  - null
  - magical
  - magical
  - slow
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Sentinel
  cooldown:
  - 15.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - At max rank, hitting an enemy god with the empowered Attack reduces your active
    ability cooldowns
  - Sentinel vision is granted through line of sight blockers
  - 'Damage: 40 | 45 | 50 | 55 | 60'
  - 'Damage Scaling: 50% Intelligence'
  - 'Buff Duration: 5 seconds'
  - 'Cooldown Reduction: -3 seconds'
  - 'Vision Radius: 6.4 | 8 | 9.6 | 11.2 | 12.8 meters'
  - 'Range: 11.2 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: vision is granted through line of sight blockers Summon a sentinel
    at the target area, granting vision of enemies for 5 seconds. Reactive the ability
    to Leap to the sentinel location and gain a buff that causes your next Attack
    to deal Magical Damage
  damage_type: magical
  detail_kinds:
  - buff
  - null
  - magical
  - magical
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: I'm a Monster
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - If you kill an enemy god with this attack, the duration resets and you may attack
    again
  - Whenever this ability deals damage to enemy gods you gain 1 stack, killing enemy
    gods provides 3. At max rank, each stack provides bonus damage to this ability
  - 'Damage: 400 | 500 | 600 | 700 | 800'
  - 'Damage Scaling: 120% Intelligence'
  - 'Bonus Damage: 5 Per Stack'
  - 'Bonus Damage Scaling: 2% Intelligence Per Stack'
  - 'Movement Speed: 35%'
  - 'Range: 9.6 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: Become CC Immune for the next 6 seconds, and gain Movement Speed .
    Reactivate to deal Magical Damage at the target area
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - magical
  - magical
  - magical
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of the Devourer
  kit_changes: Your non-ultimate abilities now provide Mana when damaging enemies
    instead of spending it. I'm a Monster can only be used when at full Mana, consuming
    all of it. It no longer provides Movement Speed, but now can be fired up to 3
    times and the damage scales from your Max Mana. I'm a Monster stacks now immediately
    provide max Mana and at max rank you gain bonus Mana. Sentinel's Empowered Attack
    also sclaes with Max Mana, but no longer Cooldown Reduces itself.
source_url: https://wiki.smite2.com/w/Scylla
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Scylla Basic Attack
- Quick Learner
- Sic 'Em
- Crush
- Sentinel
- I'm a Monster
<!-- WIKI:END -->
