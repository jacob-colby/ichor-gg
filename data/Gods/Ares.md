---
type: smite-god
name: Ares
pantheon: Greek
role: Support
specializations:
- Tank
- Lockdown
- Buffs
damage_type: magical
release_date: July 18, 2024
base_stats:
  health:
    base: 668.52
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
    base: 20.73
    per_level: 3.45
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 47.76
    per_level: 2.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ares Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 0.75, 1, 1.25x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  detail_kinds:
  - null
  - null
  - magical
  - mechanic
  - mechanic
  damage_type: magical
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Blessed Armaments
  details:
  - Allies gain 50% of the buff
  - 'Strength & Intelligence: 1 Per Level'
  - 'Strength: 8% of Protections from Items'
  - 'Intelligence: 80% of Cooldown Rate'
  detail_kinds:
  - null
  - buff
  - buff
  - buff
  description: Provide Strength and Intelligence in an aura
- slot: 1st Ability
  name: Shackles
  cooldown:
  - 15.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - You can refire after hitting an enemy god
  - Three Shackles may be out at one time
  - Gain a Movement Speed buff while an enemy god is Shackled
  - Movement Speed buff stacks for each uniquely Shackled god
  - Shackled gods take repeating Magical Damage
  - You have 2 seconds to fire another Shackle after successfully hitting an enemy
    god
  - You can fire this ability while channeling Searing Flesh
  - This ability passes through and damages non-god enemies, and passes through walls,
    but stops on enemy gods
  - 'Initial Damage: 40 | 65 | 90 | 115 | 140'
  - 'Initial Damage Scaling: 25% Strength'
  - 'Damage Per Tick: 20 | 40 | 60 | 80 | 100'
  - 'Damage Scaling Per Tick: 15% Intelligence'
  - 'Slow: 15%'
  - 'Slow Duration: 4 seconds'
  - 'Cripple Duration: 4 seconds'
  - 'Movement Speed: 15%'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  detail_kinds:
  - null
  - null
  - buff
  - buff
  - magical
  - null
  - null
  - null
  - magical
  - magical
  - magical
  - magical
  - slow
  - slow
  - debuff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Three may be out at one time Fire a Shackle projectile that deals Magical
    Damage , Cripples , and Slows
- slot: 2nd Ability
  name: Call to Arms
  cooldown:
  - 15.0
  - 14.5
  - 14.0
  - 13.5
  - 13.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - Damaging enemy gods increases the duration and the effects of this buff
  - The buff is extended by 4 seconds after hitting an enemy god 3 times
  - 'Protections: 20 | 25 | 30 | 35 | 40'
  - 'Attack Damage: 8 | 16 | 24 | 30 | 36'
  - 'Health Regen: 6 | 8 | 10 | 12 | 14'
  - 'Buff Duration: 6 seconds'
  - 'Radius: 5.6 meters'
  - 'Cooldown: 15 | 14.5 | 14 | 13.5 | 13 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  detail_kinds:
  - null
  - null
  - buff
  - buff
  - null
  - buff
  - mechanic
  - mechanic
  - mechanic
  description: You and nearby allied gods gain Protections and Attack Damage . Ares
    gains bonus Health Regen
- slot: 3rd Ability
  name: Searing Flesh
  cooldown:
  - 12.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - This is a Channeled ability
  - Reduces enemy Healing
  - You are Displacement Immune while Channeling
  - You can cancel this ability at any time
  - 'Damage Per Tick: 20 | 25 | 30 | 35 | 40'
  - 'Damage Scaling Per Tick: 7% Intelligence'
  - 'Bonus Damage Scaling: 1 | 1 | 2 | 2 | 3% Enemy Max Health'
  - 'Minion Damage Per Tick: 20 | 25 | 30 | 35 | 40'
  - 'Minion Damage Scaling Per Tick: 7% Intelligence'
  - 'Bonus Minion Damage Scaling: 3.5% Minion Max Health'
  - 'Healing Reduction: -40%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 45 degrees'
  - 'Cooldown: 12 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  detail_kinds:
  - null
  - debuff
  - mechanic
  - null
  - magical
  - magical
  - magical
  - magical
  - magical
  - magical
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Flames pour from your shield, dealing Magical Damage repeatedly to
    enemies in front of you Minion Minion
- slot: Ultimate
  name: No Escape
  cooldown:
  - 90.0
  cost:
  - 80.0
  - 85.0
  - 90.0
  - 95.0
  - 100.0
  details:
  - Deal Magical Damage when chains attach
  - Deal Magical Damage to nearby enemies while Stunning
  - You are CC Immune and gain Damage Mitigation while Channeling this ability
  - Channel lasts 2.5 seconds. Enemy gods are Displaced toward you after 2.17 seconds
    of Channeling
  - 'Initial Damage: 80 | 110 | 140 | 170 | 200'
  - 'Initial Damage Scaling: 20% Intelligence + 30% Strength'
  - 'Final Damage: 250 | 325 | 400 | 475 | 550'
  - 'Final Damage Scaling: 50% Intelligence + 55% Strength'
  - 'Stun Duration: 0.75 seconds'
  - 'Damage Mitigation: 40 | 45 | 50 | 55 | 60%'
  - 'Range: 5.6 meters'
  - 'Radius: 2.8 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 80 | 85 | 90 | 95 | 100 mana'
  detail_kinds:
  - magical
  - magical
  - mechanic
  - stun
  - magical
  - magical
  - magical
  - magical
  - stun
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Attach a chain to nearby gods, then Pull the gods towards you, and
    finally Stun enemies around you.
aspects:
- name: Aspect of Reverberation
  kit_changes: Blessed Armaments now only applies to self. Call to Arms no longer
    grants Protections, Regen, or affects allies. Instead, Ares empowers his Shield
    for his next Attack, gaining Movement Speed, stunning the target and spreading
    damage to nearby enemies. No Escape no longer pulls or stuns but deals increased
    damage and roots.
source_url: https://wiki.smite2.com/w/Ares
last_verified: '2026-11-02'
---
<!-- WIKI:START -->
- Ares Basic Attack
- Blessed Armaments
- Shackles
- Call to Arms
- Searing Flesh
- No Escape
<!-- WIKI:END -->
