---
type: smite-god
name: Ravana
pantheon: Hindu
role: Jungle
specializations:
- Brawler
- Burst Damage
damage_type: physical
release_date: August 25, 2026
base_stats:
  health:
    base: 626.52
    per_level: 101.52
  health_regen:
    base: 1.82
    per_level: 0.2
  mana:
    base: 296.0
    per_level: 42.0
  mana_regen:
    base: 1.46
    per_level: 0.13
  physical_prot:
    base: 21.4
    per_level: 3.0
  magical_prot:
    base: 27.5
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.4
  attack_power:
    base: 47.76
    per_level: 2.4
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ravana Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 0.75, 0.5, 1.25x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  detail_kinds:
  - null
  - null
  - physical
  - mechanic
  - mechanic
  damage_type: physical
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Chain of Blows
  details:
  - All stacks are lost when you fully lose your Shield
  - 'Shield Health: 6% of your Max Health'
  - 'Movement Speed: 3%'
  - 'Strength: 5'
  - 'Max Stacks: 3'
  detail_kinds:
  - shield
  - shield
  - buff
  - buff
  - buff
  description: Successful Attacks and abilities against enemies add to your Combo.
    Each time Combo reaches 8, you gain a Shield as well as Movement Speed and Strength
- slot: 1st Ability
  name: Prana Onslaught
  cooldown:
  - 9.0
  cost:
  - 30.0
  - 38.0
  - 45.0
  - 53.0
  - 60.0
  details:
  - 'Damage: 90 | 145 | 200 | 255 | 310'
  - 'Damage Scaling: 95% Strength'
  - 'Slow: 25%'
  - 'Slow Duration: 2.5 seconds'
  - 'Range: 3.2 meters'
  - 'Cone Angle: 120 degrees'
  - 'Cooldown: 9 seconds'
  - 'Cost: 30 | 38 | 45 | 53 | 60 mana'
  detail_kinds:
  - physical
  - physical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Cone Punch, Slow Throw a powerful punch, projecting your prana to deal
    Physical Damage and Slow enemies in front of you
- slot: 2nd Ability
  name: Overhead Kick
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
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 70 | 105 | 140 | 175 | 210'
  - 'Damage Scaling: 70% Strength'
  - 'Movement Speed: 50%'
  - 'Buff Duration: 0.85 seconds'
  - 'Range: 5.6 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - null
  - physical
  - physical
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Kick high, sending a shockwave forward that deals Physical Damage to
    all enemies in a line. Gain Movement Speed and become CC Immune and Damage Immune
    for the duration
- slot: 3rd Ability
  name: 10-Hand Shadow Fist
  cooldown:
  - 14.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - This ability passes through and damages all enemies, but stops on walls
  - 'Damage: 70 | 105 | 140 | 175 | 210'
  - 'Damage Scaling: 70% Strength'
  - 'Root Duration: 1 second'
  - 'Heal: 6 | 17 | 28 | 39 | 50'
  - 'Range: 7.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  detail_kinds:
  - null
  - physical
  - physical
  - debuff
  - heal
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Fire your fists forward, dealing Physical Damage as they pass through
    enemies. The first enemy god hit is Rooted . Heal from the first enemy god and
    the first 3 minions hit
- slot: Ultimate
  name: Mystic Rush
  cooldown:
  - 90.0
  cost:
  - 30.0
  - 38.0
  - 45.0
  - 53.0
  - 60.0
  details:
  - 'Damage: 200 | 275 | 350 | 425 | 500'
  - 'Damage Scaling: 110% Strength'
  - 'Increased Damage Taken: 10%'
  - 'Debuff Duration: 5 seconds'
  - 'Damage Mitigation: 10 | 15 | 20 | 25 | 30%'
  - 'Buff Duration: 5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 30 | 38 | 45 | 53 | 60 mana'
  detail_kinds:
  - physical
  - physical
  - debuff
  - debuff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Leap, Amp and Mitigate Become CC Immune and Leap to a target location,
    dealing Physical Damage to enemies in the area. Enemy gods hit take increased
    Damage from all sources. After landing, you gain Damage Mitigation for a duration
aspects:
- name: Aspect of the Rakshasa King
  kit_changes: Combo now stacks up to 999. Mystic Rush is replaced by an activator
    that lets you fire an enhanced version of your regular abilities. Using an enhanced
    ability consumes all Combo, grants a Shield equal to a percentage of your max
    Health, and if you have 50 or more Combo, a buff based on how much Combo was consumed.
source_url: https://wiki.smite2.com/w/Ravana
last_verified: '2026-08-29'
---
<!-- WIKI:START -->
- Ravana Basic Attack
- Chain of Blows
- Prana Onslaught
- Overhead Kick
- 10-Hand Shadow Fist
- Mystic Rush
<!-- WIKI:END -->
