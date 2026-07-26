---
type: smite-god
name: Xbalanque
pantheon: Maya
role: Carry
specializations:
- Constant Damage
- Global
- Mobile
damage_type: physical
release_date: September 23, 2025
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 312.96
    per_level: 38.64
  physical_prot:
    base: 18.76
    per_level: 2.76
  magical_prot:
    base: 25.3
    per_level: 1.38
  attack_speed:
    base: 1.0
    per_level: 1.61
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Xbalanque Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Physical Damage to the first enemy hit
- slot: Passive
  name: Dead of Night
  details:
  - 'Total god damage required per stack: 1,000 | 3,000 | 6,000 | 10,000 | 15,000
    | 21,000'
  - At max stacks, provides either 44 Strength + 30 Intelligence, or 20 Strength +
    66 Intelligence, depending on which stat is higher
  - 'Strength: 3 Per Stack'
  - 'Intelligence: 5 Per Stack'
  - 'Strength: 7 Per Empowered Stack'
  - 'Intelligence: 10 Per Empowered Stack'
  - 'Damage for Initial Stack: 1,000'
  - 'Damage Increase for Subsequent Stacks: 1,000'
  description: Deal damage to enemy gods to gain stacks. Each stack provides Strength
    or Intelligence , whichever is higher. At 3 and 6 stacks you gain an additional
    buff of Strength and Intelligence
- slot: 1st Ability
  name: Branching Bola
  cooldown:
  - 0.5
  cost:
  - 8.0
  - 11.0
  - 14.0
  - 17.0
  - 20.0
  details:
  - While this ability is active, each Attack consumes Mana
  - Splitting projectiles home on enemy gods in range
  - Hitting an enemy affected by Poison Darts causes the split projectiles to afflict
    enemies with a diminished debuff
  - Split attacks proc item hit effects for 40% damage and 20% healing
  - 'Increased Damage: 10 | 20 | 30 | 40 | 50'
  - 'Split Projectile Damage: 30 | 32.5 | 35 | 37.5 | 40%'
  - 'Split Projectile Range: 3.5 meters'
  - 'Cooldown: 0.5 seconds'
  - 'Cost: 8 | 11 | 14 | 17 | 20 mana Per Shot'
  description: While active, your Attacks deal additional damage . When the bola hits
    a target, it splits and deals reduced damage
- slot: 2nd Ability
  name: Poison Darts
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Poisoned enemies repeatedly take Physical Damage and are Slowed
  - Poison ticks every 0.5 seconds for 3 seconds
  - Enemies can only be hit by 7 darts, with each after the first doing reduced damage
  - Each dart stops on first target hit, and does not pass through walls
  - 'Damage: 20 | 30 | 40 | 50 | 60'
  - 'Damage Scaling: 25% Strength + 35% Intelligence'
  - 'Damage Per Tick: 10 | 15 | 20 | 25 | 30'
  - 'Damage Scaling Per Tick: 7.5% Strength + 15% Intelligence'
  - 'Subsequent Dart Damage: 30%'
  - 'Reduced Poison Damage: 50% from Split Projectiles'
  - 'Slow: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Reduced Poison Slow: 50% from Split Projectiles'
  - 'Slow Duration: 3s'
  - 'Range: 8.8 meters'
  - 'Cone Angle: 110 degrees'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Fire 15 dart projectiles in a cone, dealing Physical Damage and poisoning
    enemies hit
- slot: 3rd Ability
  name: Rising Jaguar
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - While in the air, you fire darts at all nearby enemies, dealing Physical Damage
  - Enemies affected by Poison Darts take additional damage
  - Enemies around you when the Dash starts will still be hit
  - Darts from this ability can pass through walls
  - 'Damage: 65 | 115 | 165 | 215 | 265'
  - 'Damage Scaling: 50% Strength + 35% Intelligence'
  - 'Bonus Damage: 30 | 35 | 40 | 45 | 50%'
  - 'Initial Dash Range: 4 meters'
  - 'Dart Radius: 4.8 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Dash in the direction you are currently traveling before rising in
    the air, becoming CC Immune
- slot: Ultimate
  name: Darkest of Nights
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - This ability hits every enemy god on the map
  - If an enemy god leaves the area, they are affected by a decaying Slow
  - 'Attack Range: 15.2 meters'
  - 'Attack Projectile Speed: +25%'
  - 'Attack Speed: 28 | 31 | 34 | 37 | 40%'
  - 'Movement Speed: 28 | 31 | 34 | 37 | 40%'
  - 'Buff Duration: 3 seconds'
  - 'Debuff Duration: 3 seconds'
  - 'Initial Slow Amount: 60%'
  - 'Slow Duration: 2 seconds'
  - 'Darkness Radius: 7.5 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: Shroud enemy gods in darkness, creating an area they cannot see out
    of. During this time you have increased Attack range , Attack projectile speed
    , Attack Speed , and Movement Speed
aspects:
- name: Aspect of the Nightstalker
  kit_changes: Branching Bola is no longer a toggle but provides 3 fires of ability-based
    projectiles. Poison Darts requires less hits to deal full damage. Darkest of Nights
    loses existing buffs but resets Poison darts and provides increased ability damage.
source_url: https://wiki.smite2.com/w/Xbalanque
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Xbalanque Basic Attack
- Dead of Night
- Branching Bola
- Poison Darts
- Rising Jaguar
- Darkest of Nights
<!-- WIKI:END -->
