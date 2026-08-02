---
type: smite-god
name: Tsukuyomi
pantheon: Japanese
role: Jungle
specializations:
- Slayer
- Mobile
- Constant Damage
damage_type: physical
release_date: September 9, 2025
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 316.32
    per_level: 42.0
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 25.42
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 380.0
    per_level: 0.0
  attack_power:
    base: 48.12
    per_level: 2.76
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.46
    per_level: 0.13
abilities:
- slot: Basic Attack
  name: Tsukuyomi Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Physical Damage to an enemy in front of you
  damage_type: physical
  detail_kinds:
  - null
  - physical
  - mechanic
  - mechanic
- slot: Passive
  name: Shingetsu & Mangetsu
  details:
  - Empowered Shingetsu cleaves for 50% damage and Restores Mana
  - Empowered Mangetsu deals bonus Physical Damage and Heals
  - 'Shingetsu Mana Restore: 3'
  - 'Shingetsu Mana Restore Scaling: 20% Strength'
  - 'Mangetsu Bonus Damage: 2'
  - 'Mangetsu Bonus Damage Scaling: 15% Strength + 30% Intelligence'
  - 'Mangetsu Heal: 5'
  - 'Mangetsu Heal Scaling: 1 Per Level'
  description: Damaging enemies empowers your twin tonfas, Shingetsu and Mangetsu
- slot: 1st Ability
  name: Dark Moon Shuriken
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - Retrieving the Shuriken from a god reduces this ability's cooldown
  - After casting, your next Shingetsu Attack becomes a ranged attack that steals
    Movement Speed
  - If a god dies while a Shuriken is in them, it will drop to the floor
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 70 | 120 | 170 | 220 | 270'
  - 'Damage Scaling: 80% Strength + 70% Intelligence'
  - 'Cooldown Reduction: 4 seconds'
  - 'Movement Speed Steal: 25%'
  - 'Buff Duration: 4 seconds'
  - 'Range: 10.4 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Throw a Shuriken that deals Physical Damage to enemies and sticks into
    the first god hit
  damage_type: physical
  detail_kinds:
  - buff
  - null
  - null
  - null
  - physical
  - physical
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Kusarigama
  cooldown:
  - 14.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - While Strength is higher than Intelligence, it is Shingetsu Infused. Otherwise,
    it is Mangetsu Infused
  - 'Shingetsu Infused: Gain Movement Speed and the final swing Stuns'
  - 'Mangetsu Infused: The final swing gains +20% Base Damage, +20% Intelligence Scaling,
    and +3.2 meters range'
  - Gain either a Shingetsu Infused Attack or a Mangetsu Infused Attack on hitting
    the final swing, depending on the infusion of the attack
  - You are Knockup Immune while swinging
  - 'Swing Damage: 30 | 55 | 80 | 105 | 130'
  - 'Swing Damage Scaling: 40% Strength + 25% Intelligence'
  - 'Shingetsu Final Damage: 50 | 95 | 140 | 185 | 230'
  - 'Shingetsu Final Damage Scaling: 90% Strength + 50% Intelligence'
  - 'Shingetsu Stun Duration: 0.8 | 0.9 | 1 | 1.1 | 1.2 seconds'
  - 'Shingetsu Movement Speed: 25%'
  - 'Mangetsu Final Damage: 60 | 114 | 168 | 222 | 276'
  - 'Mangetsu Final Damage Scaling: 90% Strength + 70% Intelligence'
  - 'Disarmed Duration: 1 second'
  - 'Final Swing Range: 4.8 meters'
  - 'Initial Swings Radius: 3.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: While Strength is higher than Intelligence, it is Shingetsu Infused
    . Otherwise, it is Mangetsu Infused Perform a 3-swing combo with a . The first
    2 swings deal Physical Damage and Disarm enemies. The final swing deals more Damage
  detail_kinds:
  - null
  - null
  - null
  - null
  - mechanic
  - physical
  - physical
  - null
  - null
  - null
  - null
  - null
  - null
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Silver Moon Caltrops
  cooldown:
  - 14.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - Enemies moving within the Caltrops take additional Damage and are Slowed again
  - After casting, your next Mangetsu Attack becomes a ranged attack that deals bonus
    Physical Damage
  - Checks for movement every 0.25 seconds for 6 seconds
  - 'Damage: 20 | 30 | 40 | 50 | 60'
  - 'Damage Scaling: 12.5% Strength + 15% Intelligence'
  - 'Slow: 20%'
  - 'Slow Duration: 1.5 seconds'
  - 'Mangetsu Bonus Damage: 5'
  - 'Mangetsu Bonus Damage Scaling: 30% Strength + 65% Intelligence'
  - 'Cooldown: 14 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  description: Scatter Caltrops in an area, dealing Physical Damage and Slowing enemies
  damage_type: physical
  detail_kinds:
  - physical
  - null
  - null
  - physical
  - physical
  - slow
  - slow
  - null
  - null
  - mechanic
  - mechanic
- slot: Ultimate
  name: Piercing Moonlight
  cooldown:
  - 100.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - After firing, Dash through all marked gods in order, up to a maximum of 12 times,
    dealing Physical Damage with each strike, applying Shingetsu and Mangetsu effects,
    as well as Attack Item Effects
  - Killing a god with this ability empowers both weapons and grants both ranged attacks
  - This ability passes through and damages all enemies, and passes through walls
  - 'Beam Damage: 30 | 50 | 70 | 90 | 110'
  - 'Beam Damage Scaling: 15% Strength + 40% Intelligence'
  - 'Dash Damage: 60 | 85 | 110 | 135 | 160'
  - 'Dash Damage Scaling: 55% Strength + 20% Intelligence'
  - 'Damage Mitigation: 20%'
  - 'Cooldown: 100 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Fire 4 piercing beams of moonlight, marking and dealing Physical Damage
    to enemy gods. You are CC Immune and have Damage Reduction while firing
  detail_kinds:
  - null
  - null
  - null
  - physical
  - physical
  - physical
  - physical
  - buff
  - mechanic
  - mechanic
aspects:
- name: Aspect of Mangetsu
  kit_changes: When gaining Shingetsu Ranged Attack, they become Mangetsu Ranged Attacks
    instead. Dark Moon Shuriken no longer sticks to gods. Piercing Moonlight hits
    each target only once for major damage in an AoE, before returning to his casting
    location.
source_url: https://wiki.smite2.com/w/Tsukuyomi
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Tsukuyomi Basic Attack
- Shingetsu & Mangetsu
- Dark Moon Shuriken
- Kusarigama
- Silver Moon Caltrops
- Piercing Moonlight
<!-- WIKI:END -->
