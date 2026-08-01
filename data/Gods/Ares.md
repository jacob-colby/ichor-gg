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
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 20.73
    per_level: 3.45
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
  name: Ares Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of 1, 0.75, 1, 1.25x damage and swing time
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Blessed Armaments
  details:
  - Build Protections to increase Strength Aura
  - Build Cooldown Rate to increase Intelligence Aura
  - Both Auras increase with level
  - Allies gain 50% of the buff
  - 'Strength & Intelligence: 1 Per Level'
  - 'Strength: 8% of Protections from Items'
  - 'Intelligence: 80% of Cooldown Rate'
  description: Provide Strength and Intelligence in an Aura
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
  - Deals bonus damage based on the enemies' Maximum Health
  - You are Displacement Immune while Channeling
  - You can fire your Shackles ability while Channeling this ability, but no other
    attacks
  - You can cancel this ability at any time
  - 'Damage Per Tick: 20 | 25 | 30 | 35 | 40'
  - 'Damage Scaling Per Tick: 7% Intelligence'
  - 'Bonus Damage Scaling: 1 | 1 | 2 | 2 | 3% Enemy Max Health'
  - 'Minion Damage Per Tick: 20 | 25 | 30 | 35 | 40'
  - 'Minion Damage Scaling Per Tick: 7% Intelligence'
  - 'Bonus Minion Damage Scaling: 3.5% Minion Max Health'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 45 degrees'
  - 'Cooldown: 12 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
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
  - Deal Magical Damage when Chains attach
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
  description: Attach a chain to nearby gods, then Pull the gods towards you, and
    finally Stun enemies around you.
aspects:
- name: Aspect of Reverberation
  kit_changes: Call to Arms no longer grants Protections or affects allies. Instead,
    Ares empowers his Shield for his next Basic Attack stunning the target and spreading
    damage to nearby enemies.
source_url: https://wiki.smite2.com/w/Ares
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Ares Basic Attack
- Blessed Armaments
- Shackles
- Call to Arms
- Searing Flesh
- No Escape
<!-- WIKI:END -->
