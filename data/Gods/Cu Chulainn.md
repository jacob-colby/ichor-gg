---
type: smite-god
name: Cu Chulainn
pantheon: Celtic
role: Solo
specializations:
- Constant Damage
- Pressure
damage_type: physical
release_date: July 28, 2026
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  health_regen:
    base: 1.93
    per_level: 0.2
  physical_prot:
    base: 19.24
    per_level: 3.24
  magical_prot:
    base: 29.58
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 0.0
  attack_power:
    base: 38.69
    per_level: 2.4
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Cu Chulainn Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Human Form: Has a 3 hit chain. Attacks in order of 0.7, 0.7, 1x damage and swing
    time'
  - 'Berserk Form: Has a 3 hit chain. Attacks in order of 1.05, 1.05, 1.5x damage
    and swing time'
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 2.56 meters'
  - 'Cone Angle: 120 degrees'
  detail_kinds:
  - null
  - null
  - null
  - physical
  - mechanic
  - mechanic
  damage_type: physical
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Berserk
  details:
  - Gain Rage by hitting Abilities, per Attack, and when you or a nearby ally takes
    damage
  - Attacks and Abilities must deal at least 1 damage to generate Rage
  - Rage resets to 25 when you enter Berserk or respawn
  - The transformation is canceled if you lose the required Rage during the transformation
    phase
  - 'Strength: 2 Per Level'
  - 'Shield Health: 30'
  - 'Shield Health Scaling: 25 Per Level'
  - 'Health Conversion: 20% of Mana'
  - 'Berserk Threshold: 85 Rage'
  - 'Transformation Duration: 2 seconds'
  - 'Berserk Duration: 20 seconds'
  detail_kinds:
  - null
  - null
  - null
  - null
  - buff
  - shield
  - shield
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: 'Rage resets to 25 when you enter or respawn Your Mana, Mana Regen,
    and Mana Heals convert into your Health Pool instead of Mana. Abilities cost Rage,
    which only regenerates up to 25. After building high Rage, you go for a duration,
    gaining Strength and a Health Shield . While , your Abilities transform and cost
    no Rage Threshold: 85 Rage Duration: 20 seconds'
- slot: 1st Ability
  name: Barbed Spear
  cooldown:
  - 16.0
  - 15.0
  - 14.0
  - 13.0
  - 12.0
  cost:
  - 9.0
  details:
  - Reduces enemy Healing
  - This ability Stuns lane minions and jungle monsters, but not gods or jungle bosses
  - Hitting a minion restores Rage, more for a god, up to a cap
  - This ability passes through and damages all enemies, but stops on walls
  - 'Damage: 90 | 150 | 210 | 270 | 330'
  - 'Damage Scaling: 65% Strength'
  - 'Stun Duration: 2 seconds'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Minion Rage Gain: 7'
  - 'God Rage Gain: 10'
  - 'Max Rage Gain: 24'
  - 'Range: 7.2 meters'
  - 'Cooldown: 16 | 15 | 14 | 13 | 12 seconds'
  - 'Cost: 9 Rage'
  detail_kinds:
  - debuff
  - stun
  - null
  - null
  - physical
  - physical
  - stun
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Thrust your spear forward, dealing Physical Damage to enemies in front
    of you and Stunning weaker minions. Barbs reduce their Healing received for a
    duration
  stance: Human
- slot: 2nd Ability
  name: Vent Anger
  cooldown:
  - 6.0
  cost:
  - 16.0
  details:
  - This ability can be used without being ranked
  - This ability drains your Rage and returns none
  - This ability damages all enemies in the area, but stops on walls
  - 'Damage: 7 | 10 | 17 | 24 | 31 | 38'
  - 'Damage Scaling: 5% Strength'
  - 'Movement Speed: 5 | 5 | 6 | 7 | 8 | 9%'
  - 'Radius: 3.6 meters'
  - 'Cooldown: 6 seconds'
  - 'Cost: 16 Rage'
  detail_kinds:
  - null
  - null
  - null
  - physical
  - physical
  - buff
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Vent superheated steam for a duration, gaining Movement Speed and dealing
    Physical Damage to nearby enemies repeatedly
  stance: Human
- slot: 3rd Ability
  name: Salmon's Leap
  cooldown:
  - 15.0
  cost:
  - 9.0
  details:
  - Hitting a minion restores Rage, more for a god, up to a cap
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 80 | 135 | 190 | 245 | 300'
  - 'Damage Scaling: 60% Strength'
  - 'Minion Rage Gain: 5'
  - 'God Rage Gain: 8'
  - 'Max Rage Gain: 18'
  - 'Leap Range: 5.6 meters'
  - 'Slam Range: 3.2 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 9 Rage'
  detail_kinds:
  - null
  - null
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Leap to a target location and slam down, dealing Physical Damage to
    enemies around and in front of you.
  stance: Human
- slot: Ultimate
  name: Spear of Mortal Pain
  cooldown:
  - 105.0
  - 100.0
  - 95.0
  - 90.0
  - 85.0
  cost:
  - 14.0
  details:
  - Hitting a minion restores Rage, more for a god, up to a cap
  - This ability damages all enemies in the area, but stops on walls
  - 'Damage: 175 | 245 | 315 | 385 | 455'
  - 'Damage Scaling: 65% Strength'
  - 'Minion Rage Gain: 12'
  - 'God Rage Gain: 32'
  - 'Max Rage Gain: 42'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 105 | 100 | 95 | 90 | 85 seconds'
  - 'Cost: 14 Rage'
  detail_kinds:
  - null
  - null
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Swing Gae Bulg in a circle around you, dealing Physical Damage and
    Knocking Up all nearby enemies. You are CC Immune while channeling
  stance: Human
- slot: 1st Ability
  name: Ground Slam
  cooldown:
  - 16.0
  - 15.0
  - 14.0
  - 13.0
  - 12.0
  details:
  - Reduces enemy Healing
  - This ability passes through and damages all enemies, but stops on walls
  - 'Damage: 90 | 150 | 210 | 270 | 330'
  - 'Damage Scaling: 65% Strength'
  - 'Root Duration: 1 | 1.1 | 1.2 | 1.3 | 1.4 seconds'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 7.2 meters'
  - 'Cooldown: 16 | 15 | 14 | 13 | 12 seconds'
  detail_kinds:
  - debuff
  - null
  - physical
  - physical
  - debuff
  - debuff
  - debuff
  - mechanic
  - mechanic
  damage_type: physical
  description: Slam your arms down, dealing Physical Damage and Rooting enemies in
    front of you
  stance: Berserk
- slot: 2nd Ability
  name: Vent Anger
  details:
  - This ability activates automatically and lasts for the duration of Berserk
  - This ability damages all enemies in the area, but stops on walls
  - 'Damage: 7 | 10 | 17 | 24 | 31 | 38'
  - 'Damage Scaling: 5% Strength'
  - 'Movement Speed: 5 | 5 | 6 | 7 | 8 | 9%'
  - 'Radius: 3.6 meters'
  detail_kinds:
  - null
  - null
  - physical
  - physical
  - buff
  - mechanic
  damage_type: physical
  description: Vent superheated steam, gaining Movement Speed and dealing Physical
    Damage to nearby enemies repeatedly
  stance: Berserk
- slot: 3rd Ability
  name: Furious Charge
  cooldown:
  - 15.0
  details:
  - You are Knockup Immune while Dashing
  - 'Damage: 80 | 135 | 190 | 245 | 300'
  - 'Damage Scaling: 60% Strength'
  - 'Stun Duration: 1 second'
  - 'Range: 5.6 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 15 seconds'
  detail_kinds:
  - mechanic
  - physical
  - physical
  - stun
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Dash forward, dealing Physical Damage , Stunning enemies, and Pushing
    them with you
  stance: Berserk
- slot: Ultimate
  name: War Cry
  cooldown:
  - 35.0
  details:
  - This ability damages all enemies in the area, but stops on walls
  - 'Damage: 175 | 245 | 315 | 385 | 455'
  - 'Damage Scaling: 65% Strength'
  - 'Tremble Duration: 1 second'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 35 seconds'
  detail_kinds:
  - null
  - physical
  - physical
  - debuff
  - mechanic
  - mechanic
  damage_type: physical
  description: Unleash a terrifying yell, dealing Physical Damage and Trembling all
    nearby enemies
  stance: Berserk
aspects:
- name: Aspect of the Warped
  kit_changes: Start the game as Berserk. Vent Anger now costs Rage when Berserk.
    After reaching 100 Rage, become Warped gaining massive power and losing Rage every
    0.5s. After reaching 0 Rage transform back to Human form with reduced Protections
    and Damage.
source_url: https://wiki.smite2.com/w/Cu_Chulainn
last_verified: '2026-08-19'
---
<!-- WIKI:START -->
- Cu Chulainn Basic Attack
- Berserk
- Barbed Spear
- Vent Anger
- Salmon's Leap
- Spear of Mortal Pain
- Ground Slam
- Vent Anger
- Furious Charge
- War Cry
<!-- WIKI:END -->
