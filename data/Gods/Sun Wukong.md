---
type: smite-god
name: Sun Wukong
pantheon: Chinese
role: Solo
specializations:
- Brawler
- Pressure
damage_type: physical
release_date: July 15, 2025
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 323.0
    per_level: 48.26
  physical_prot:
    base: 19.2
    per_level: 3.24
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 0.96
    per_level: 1.29
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 48.0
    per_level: 2.21
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.57
    per_level: 0.13
abilities:
- slot: Basic Attack
  name: Sun Wukong Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 0.75, 1, 1.25x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
  damage_type: physical
  detail_kinds:
  - null
  - null
  - physical
  - mechanic
  - mechanic
- slot: Passive
  name: Undefeated Body
  cooldown:
  - 90.0
  details:
  - Clones use The Magic Cudgel and Master's Will when you do
  - Clones inherit 100% of your Health, Protections, Strength, and Intelligence but
    deal 50% damage and are instantly killed by Hard Crowd Control effects, except
    Knockbacks and Banishes
  - 'Strength & Intelligence: 10'
  - 'Strength & Intelligence Scaling: 1 Per Level'
  - 'Protections: 10'
  - 'Protections Scaling: 1.5 Per Level'
  - 'Buff Duration: 8 seconds'
  - 'Clone Lifetime: 10 seconds'
  - 'Cooldown: 90 seconds'
  description: When you drop below 60% Health, gain increased Strength , Intelligence
    , and Protections . If you go above this threshold, the buff persists for a short
    duration. When you drop below 30% Health, you spawn a clone. This effect has a
    cooldown
  detail_kinds:
  - null
  - null
  - buff
  - buff
  - buff
  - buff
  - buff
  - buff
  - mechanic
- slot: 1st Ability
  name: The Magic Cudgel
  cooldown:
  - 12.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - This ability has reduced Strength Scaling but increased Intelligence Scaling to
    enemies that are further away
  - Strength Scaling starts decreasing from 50% of the ability's range to a floor
    of 50% of the total Strength Scaling
  - Intelligence Scaling starts increasing from 50% of the ability's range starting
    with a floor of 50% of the total Intelligence Scaling
  - Intelligence increases the length of this ability up to 1.5x at 500 Intelligence
  - 'Damage: 115 | 155 | 195 | 235 | 275'
  - 'Close Range Damage Scaling: 60% Strength + 35% Intelligence'
  - 'Far Range Damage Scaling: 30% Strength + 70% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 0.96 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Slam down with your Cudgel, dealing Physical Damage
  damage_type: physical
  detail_kinds:
  - debuff
  - null
  - null
  - null
  - physical
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Master's Will
  cooldown:
  - 11.0
  cost:
  - 60.0
  details:
  - This ability has reduced Strength Scaling but increased Intelligence Scaling to
    enemies that are further away
  - Strength Scaling starts decreasing from 50% of the ability's range to a floor
    of 50% of the total Strength Scaling
  - Intelligence Scaling starts increasing from 50% of the ability's range starting
    with a floor of 50% of the total Intelligence Scaling
  - Intelligence increases the length of this ability up to 1.5x at 500 Intelligence
  - 'Damage: 90 | 150 | 210 | 270 | 330'
  - 'Close Range Damage Scaling: 65% Strength + 37.5% Intelligence'
  - 'Far Range Damage Scaling: 32.5% Strength + 75% Intelligence'
  - 'Slow: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Attack Speed Reduction: 20 | 22.5 | 25 | 27.5 | 30%'
  - 'Debuff Duration: 3 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 11 seconds'
  - 'Cost: 60 mana'
  description: Strike around you dealing Physical Damage . Enemies hit are Slowed
    and have reduced Attack Speed
  damage_type: physical
  detail_kinds:
  - debuff
  - null
  - null
  - null
  - physical
  - physical
  - physical
  - slow
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: 72 Transformations
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  details:
  - 'Ox: Knockback enemies in your path, dealing Physical Damage'
  - 'Tiger: Maul the first enemy you hit, dealing Physical Damage and Stunning them'
  - 'Eagle: Is the fastest of the three forms'
  - Choose which form to transform into based on where you are aiming when the ability
    is fired. Ox is the closest, Tiger in the middle, and Eagle the farthest
  - All 3 forms are Slow Immune and Root Immune while the Ox form is also Knockup
    Immune
  - 'Ox Damage: 70 | 105 | 140 | 175 | 210'
  - 'Ox Damage Scaling: 60% Strength'
  - 'Tiger Damage: 100 | 170 | 240 | 310 | 380'
  - 'Tiger Damage Scaling: 80% Strength'
  - 'Stun Duration: 1.4 seconds'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 65 | 70 | 75 | 80 | 85 mana'
  description: Transform into an Ox, Tiger, or Eagle, and Dash forward
  detail_kinds:
  - stun
  - physical
  - null
  - null
  - mechanic
  - physical
  - physical
  - physical
  - physical
  - stun
  - mechanic
  - mechanic
- slot: Ultimate
  name: Somersault Cloud
  cooldown:
  - 110.0
  - 105.0
  - 100.0
  - 95.0
  - 90.0
  cost:
  - 100.0
  details:
  - Refire to land early, dealing Physical Damage at the landing spot
  - You are CC Immune while using this ability
  - If all clones are killed while on your cloud, your Stealth effect ends early
  - 'Damage: 200 | 275 | 350 | 425 | 500'
  - 'Damage Scaling: 100% Strength'
  - 'Heal Per Tick: 2% Max Health + 5% Intelligence'
  - 'Range: 12 meters'
  - 'Radius: 4 meters'
  - 'Cooldown: 110 | 105 | 100 | 95 | 90 seconds'
  - 'Cost: 100 mana'
  description: Rise into a cloud leaving a clone to fight in your stead. While in
    the cloud you are Stealthed and Heal every 0.5 seconds
  damage_type: physical
  detail_kinds:
  - physical
  - mechanic
  - buff
  - physical
  - physical
  - heal
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Transformation
  kit_changes: 72 Transformations has a reduced Cooldown and locks your animal form
    until Somersault Cloud is used. Locking in Ox form causes Master’s Will to Knockup.
    Tiger form provides stacking Attack Speed on hits of The Magic Cudgel and Eagle
    form causes your other two non-ultimate abilities to have a reduced Cooldown.
source_url: https://wiki.smite2.com/w/Sun_Wukong
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Sun Wukong Basic Attack
- Undefeated Body
- The Magic Cudgel
- Master's Will
- 72 Transformations
- Somersault Cloud
<!-- WIKI:END -->
