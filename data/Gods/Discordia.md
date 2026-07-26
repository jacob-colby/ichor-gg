---
type: smite-god
name: Discordia
pantheon: Roman
role: Mid
specializations:
- Nuker
- Burst Damage
damage_type: magical
release_date: January 13, 2026
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 334.1
    per_level: 42.0
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Discordia Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Contest of Gods
  details:
  - Healing ticks every 0.5 seconds
  - 'Intelligence: 5'
  - 'Intelligence Scaling: 1 Per Level'
  - 'Strength: 2.5'
  - 'Strength Scaling: 1 Per Level'
  - 'Intelligence Self Buff: 10 + 10%'
  - 'Lifesteal Self Buff: 15%'
  - 'Heal: 0.5% Max Health'
  - 'Self Buff Duration: 6 seconds'
  description: The god on your team with the highest damage dealt to enemy gods gains
    a Strength and Intelligence buff . Gaining a level, god kill, or god assist provides
    a random temporary self buff of Intelligence , Lifesteal , or Healing
- slot: 1st Ability
  name: Unruly Magic
  cooldown:
  - 12.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Enemies hit by the area damage will not take damage from the minor projectiles
  - The orb passes through and damages all enemies, and passes through walls
  - The minor projectiles pass through and damage all enemies, but bounce off walls
  - 'Damage: 85 | 135 | 185 | 235 | 285'
  - 'Damage Scaling: 75% Intelligence'
  - 'Area Damage: 100 | 150 | 200 | 250 | 300'
  - 'Area Damage Scaling: 60% Intelligence'
  - 'Projectile Damage: 20 | 30 | 40 | 50 | 60'
  - 'Projectile Damage Scaling: 10% Intelligence'
  - 'Range: 10 meters'
  - 'Radius: 1.12 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Fire out an orb of unruly magic dealing Magical Damage . After reaching
    the target location, the orb explodes in a small area dealing Magical Damage before
    breaking into bouncing minor projectiles that each deal Magical Damage
- slot: 2nd Ability
  name: Strife
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Enemies affected by Madness will move towards and attack their nearest ally, dealing
    Magical Damage
  - Enemies affected by Madness will attack between 0 and 2 times, depending on the
    distance to their nearest ally
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 60% Intelligence'
  - 'Bonus Damage: 10 | 20 | 30 | 40 | 50'
  - 'Bonus Damage Scaling: 10% Intelligence'
  - 'Root Duration: 1 second'
  - 'Madness Duration: 1 second'
  - 'Range: 9.4 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Create an area that deals Magical Damage . Hitting 1 enemy causes them
    to be Rooted , hitting multiple applies Madness instead
- slot: 3rd Ability
  name: Erratic Behavior
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Damaging enemy gods increases the field duration by 0.25 seconds, up to a max
    of an additional 3 seconds
  - Ability cooldown reduction ticks every 0.5 seconds and does not apply to this
    ability
  - 'Movement Speed: 20 | 25 | 30 | 35 | 40%'
  - 'Cooldown Reduction: -0.2 | -0.4 | -0.6 | -0.8 | -1 second'
  - 'Ultimate Cooldown Reduction: -0.4 seconds'
  - 'Range: 6.4 meters'
  - 'Field Radius: 2.4 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Leap and create a field in an area. While within the field, you gain
    Stealth , Movement Speed , and ability cooldown reduction
- slot: Ultimate
  name: Golden Apple of Discord
  cooldown:
  - 90.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Enemies afflicted by the Apple effect are Crippled and Trembled
  - Enemies caught in the explosion take both the initial Magical Damage and the delayed
    explosion Magical Damage, but do not explode in an area
  - This ability passes through and damages non-god enemies, and bounces off walls,
    but stops on enemy gods
  - 'Initial Damage: 125 | 150 | 175 | 200 | 225'
  - 'Initial Damage Scaling: 50% Intelligence'
  - 'Explosion Damage: 200 | 250 | 300 | 350 | 400'
  - 'Explosion Damage Scaling: 60% Intelligence'
  - 'Cripple Duration: 2 seconds'
  - 'Tremble Duration: 2 seconds'
  - 'Range: 35 meters'
  - 'Radius: 1.12 meters'
  - 'Explosion Radius: 5.6 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Enemies caught in the explosion take both the initial Magical Damage
    and the delayed explosion Magical Damage , but do not explode in an area Throw
    the which deals Magical Damage before exploding in an area dealing additional
    Magical Damage and spreading the effects of the Apple
aspects:
- name: Aspect of the Gilded Victor
  kit_changes: Contest of Gods only provides you extra Attack Damage from Intelligence.
    Unruly Magic does not explode but returns back, dealing damage and providing a
    stack causing your next attacks to explode. Erratic Behavior no longer creates
    a field of stealth but attack speed and attack damage. Golden Apple of Discord
    is faster and does not spread.
source_url: https://wiki.smite2.com/w/Discordia
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Discordia Basic Attack
- Contest of Gods
- Unruly Magic
- Strife
- Erratic Behavior
- Golden Apple of Discord
<!-- WIKI:END -->
