---
type: smite-god
name: Ganesha
pantheon: Hindu
role: Support
specializations:
- Tank
- Area Control
- Crowd Control
- Buffs
damage_type: magical
release_date: June 20, 2025
base_stats:
  health:
    base: 668.5
    per_level: 101.52
  mana:
    base: 337.0
    per_level: 45.37
  physical_prot:
    base: 20.5
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ganesha Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 5 hit chain. Attacks in order of 1.05, 0.8, 0.8, 1.5, 0.95x damage and swing
    time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Good Fortune
  details:
  - 'Bonus Gold: 50 Per Gifted God Kill'
  description: GIFT KILLS TO ALLIES Any time you deal a killing blow, the nearest
    allied god receives the credit and you receive the rewards for an assist instead
    plus a bonus amount of gold. In addition, your assist range and the time before
    you lose assist credit is increased
- slot: 1st Ability
  name: Turn of Fate
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  details:
  - Enemy gods are marked for 5 seconds. Any Hard Crowd Control effect consumes the
    mark to deal bonus Magical Damage
  - Bonus Damage buff stacks up to 5 times. Minions grant 1 stack and gods grant 2
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 90 | 150 | 210 | 270 | 330'
  - 'Damage Scaling: 55% Intelligence'
  - 'Mark Bonus Damage: 15'
  - 'Mark Bonus Damage Scaling: 5 Per Enemy Level'
  - 'Bonus Damage: 3% Per Stack'
  - 'Buff Duration: 4 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 1.2 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 65 | 70 | 75 | 80 | 85 mana'
  description: Send a curse forward dealing Magical Damage to enemies it passes through.
    For each enemy hit, all nearby allied gods gain Bonus Damage
- slot: 2nd Ability
  name: Ohm
  cooldown:
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  - 10.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - Ganesha gains an additional 50% of the Protections he provides
  - You are Displacement Immune while Channeling
  - You are Slowed while Channeling
  - You can cancel this ability at any time
  - 'Protections: 20 | 30 | 40 | 50 | 60'
  - 'Self Slow: 15%'
  - 'Radius: 5.6 meters'
  - 'Cone Angle: 45 degrees'
  - 'Cooldown: 14 | 13 | 12 | 11 | 10 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  description: Rise into the lotus position Silencing enemies in front of you and
    increasing Protections of nearby allied gods
- slot: 3rd Ability
  name: Remove Obstacles
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 70.0
  details:
  - While Dashing you pass through ultimate player made walls and destroy non-ultimate
    player made walls
  - You pass through but do not destroy ally walls
  - Damage dealt to enemy gods is split between 3 hits
  - You cannot cancel this ability while Dashing, but you can on contact with an enemy
    god
  - Canceling this ability early ends the Stun immediately and doesn't Knock Up
  - 'Damage: 90 | 135 | 180 | 225 | 270'
  - 'Damage Scaling: 45% Intelligence'
  - 'Stun Duration: 0.75 seconds'
  - 'Range: 7.5 meters'
  - 'Radius: 0.64 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 70 mana'
  description: You cannot cancel this ability while Dashing , but you can on contact
    with an enemy god Dash forward dealing Magical Damage to enemy minions you pass
    through and stopping on enemy gods, Stunning them before Knocking them up
- slot: Ultimate
  name: Dharmic Pillars
  cooldown:
  - 75.0
  cost:
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  details:
  - Enemies continue to take Magical Damage if they stay in the field
  - Minions take 40% reduced damage from this ability
  - 'Initial Damage: 144 | 208 | 272 | 336 | 400'
  - 'Initial Damage Scaling: 64% Intelligence'
  - 'Damage Per Tick: 90 | 130 | 170 | 210 | 250'
  - 'Damage Scaling Per Tick: 40% Intelligence'
  - 'Slow: 30%'
  - 'Protections Reduced: 10 | 20 | 30 | 40 | 50'
  - 'Debuff Duration: 3 seconds'
  - 'Range: 8.8 meters'
  - 'Cooldown: 75 seconds'
  - 'Cost: 65 | 70 | 75 | 80 | 85 mana'
  description: Summon 4 Great Pillars to imprison your enemies. Enemies that pass
    the field between each pillar take an initial hit of Magical Damage , are Slowed
    , and have their Protections Reduced
aspects:
- name: Aspect of the Triumphant
  kit_changes: Ohm no longer silences but deals damage to enemies in front of you
    and provides yourself and allies Movement Speed. Turn of Fate's mark now only
    procs the next time you hit the marked enemy with an ability. Additionally you
    no longer bestow kills to allies but each god kill provides permanent Cooldown
    Rate.
source_url: https://wiki.smite2.com/w/Ganesha
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Ganesha Basic Attack
- Good Fortune
- Turn of Fate
- Ohm
- Remove Obstacles
- Dharmic Pillars
<!-- WIKI:END -->
