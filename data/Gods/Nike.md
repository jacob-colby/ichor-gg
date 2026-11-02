---
type: smite-god
name: Nike
pantheon: Greek
role: Solo
specializations:
- Tank
- Crowd Control
- Healing
damage_type: physical
release_date: October 6, 2026
base_stats:
  health:
    base: 668.5
    per_level: 101.52
  health_regen:
    base: 1.84
    per_level: 0.22
  mana:
    base: 296.0
    per_level: 42.0
  mana_regen:
    base: 1.45
    per_level: 0.12
  physical_prot:
    base: 20.7
    per_level: 3.45
  magical_prot:
    base: 29.6
    per_level: 1.5
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 39.0
    per_level: 2.37
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Nike Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 3 hit chain. Attacks in order of 1, 1, 1.5x damage and swing time. First
    2 hits cleave
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
  name: To Victory!
  details:
  - When an ally consumes a Laurel with an Attack; you Heal them
  - When you Attack an enemy, you consume a Laurel, Healing yourself, and dealing
    bonus Physical Damage
  - 'Damage: 10'
  - 'Damage Scaling: 20% Strength'
  - 'Heal: 10'
  - 'Heal Scaling: 10% Intelligence + 2 Per Level'
  - 'Max Stacks: 3'
  - 'Stack Duration: 10 seconds'
  detail_kinds:
  - heal
  - heal
  - physical
  - physical
  - heal
  - heal
  - mechanic
  - mechanic
  damage_type: physical
  description: Hitting an enemy with an ability grants a Laurel to you and allied
    gods within 10 meters
- slot: 1st Ability
  name: Rend
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This is a Channeled ability
  - A target hit 2 times loses Protections
  - A target hit 3 times is Disarmed
  - You are Displacement Immune while Channeling
  - 'Damage: 50 | 80 | 110 | 140 | 170'
  - 'Damage Scaling: 40% Strength'
  - 'Protections Reduced: 3 | 6 | 9 | 12 | 15'
  - 'Debuff Duration: 5 seconds'
  - 'Disarm Duration: 1 | 1.25 | 1.5 | 1.75 | 2 seconds'
  - 'Range: 8 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - null
  - debuff
  - stun
  - mechanic
  - physical
  - physical
  - debuff
  - debuff
  - stun
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Slam the ground 3 times, sending fissures forward. Each fissure deals
    Physical Damage
- slot: 2nd Ability
  name: Barrier Formation
  cooldown:
  - 15.0
  - 14.5
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This is a Channeled ability
  - While channeling, your turning is limited, and your Movement Speed is reduced
  - Every 5 Intelligence you build reduces the self movement slow by 1%, up to a max
    of 50% reduction at 250 Intelligence
  - You are Knockback Immune while channeling
  - 'Repel Damage: 10 | 15 | 20 | 25 | 30'
  - 'Repel Damage Scaling: 5% Strength'
  - 'Collapse Damage: 80 | 140 | 200 | 260 | 320'
  - 'Collapse Damage Scaling: 50% Strength'
  - 'Duration: 4 seconds'
  - 'Radius: 4 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - null
  - debuff
  - null
  - mechanic
  - physical
  - physical
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: While channeling, your turning is limited , and your Movement Speed
    is reduced Channel a barrier in front of you that blocks ranged Attacks. Enemies
    who touch the barrier are Knocked Back and take Physical Damage . Reactivate to
    collapse the barrier, dealing Physical Damage to enemies in front of it
- slot: 3rd Ability
  name: Valiant Leap
  cooldown:
  - 16.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 60% Strength'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 16 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  detail_kinds:
  - physical
  - physical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Leap, Area Knockup Leap to a target location, dealing Physical Damage
    and Knocking Up enemies where you land
- slot: Ultimate
  name: Sentinel of Zeus
  cooldown:
  - 90.0
  - 85.0
  - 80.0
  - 75.0
  - 70.0
  cost:
  - 90.0
  - 95.0
  - 100.0
  - 105.0
  - 110.0
  details:
  - While this buff is active, you do not consume Laurels, but Attacks against enemies
    still Heal you and deal the bonus Physical Damage
  - You are CC Immune at the start of this ability
  - 'Damage: 200 | 250 | 300 | 350 | 400'
  - 'Damage Scaling: 70% Strength'
  - 'Slow: 40%'
  - 'Slow Duration: 4 seconds'
  - 'Shield: 25 | 27.5 | 30 | 32.5 | 35% Max Health'
  - 'Shield Duration: 10 seconds'
  - 'CC Immunity Duration: 0.5 seconds'
  - 'Radius: 6.4 meters'
  - 'Cooldown: 90 | 85 | 80 | 75 | 70 seconds'
  - 'Cost: 90 | 95 | 100 | 105 | 110 mana'
  detail_kinds:
  - heal
  - mechanic
  - physical
  - physical
  - slow
  - slow
  - shield
  - shield
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Transform into an armored sentinel and send out a shockwave, dealing
    Physical Damage and Slowing nearby enemies. Gain a Shield
aspects:
- name: Aspect of Victorious Conquest
  kit_changes: '''Laurels are granted only to you. At 3 Laurels, your next ability
    deals bonus Physical Damage scaling with Strrength and consumes them. Barrier
    Formation no longer channels; it travels forward 9m, lingers 1s, and Knocks Up
    enemies who touch it. Valant Leap no longer Knocks Up. Sentinel of Zeus no longer
    grants a Shield; it grants full Laurels, and ability hits do not consume Laurels
    while the buff is active.'
source_url: https://wiki.smite2.com/w/Nike
last_verified: '2026-11-02'
---
<!-- WIKI:START -->
- Nike Basic Attack
- To Victory!
- Rend
- Barrier Formation
- Valiant Leap
- Sentinel of Zeus
<!-- WIKI:END -->
