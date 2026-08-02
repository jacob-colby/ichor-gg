---
type: smite-god
name: Poseidon
pantheon: Greek
role: Mid
specializations:
- Nuker
- Area Control
damage_type: magical
release_date: November 25, 2024
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 316.32
    per_level: 42.0
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.98
    per_level: 1.61
  move_speed:
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 44.4
    per_level: 2.4
  health_regen:
    base: 1.82
    per_level: 0.2
  mana_regen:
    base: 1.56
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Poseidon Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - Successfully hit Attacks generate Tide
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Changing Tides
  details:
  - Each successful Attack generates 10% Tide
  - Using abilities decreases Tide
  - 'Max Tide Bonus Movement Speed: 10%'
  - 'Max Tide Bonus Ability Damage: 15%'
  description: Successfully hit Attacks to gain Tide. You have increased Movement
    Speed and your abilities do additional damage based on the amount of Tide you
    have.
  detail_kinds:
  - null
  - null
  - buff
  - buff
- slot: 1st Ability
  name: Tidal Surge
  cooldown:
  - 10.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Subsequent wave hits deal 50% less damage
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 100 | 140 | 180 | 220 | 260'
  - 'Damage Scaling: 70% Intelligence'
  - 'Tide Cost: -15%'
  - 'Range: 12.8 meters'
  - 'Large Wave Radius: 0.56 meters'
  - 'Small Wave Radius: 0.28 meters'
  - 'Cooldown: 10 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80'
  description: Summon a wave, dealing Magical Damage and Knocking Back enemies. Activate
    while Trident is active to send out two additional waves
  damage_type: magical
  detail_kinds:
  - null
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Trident
  cooldown:
  - 15.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - The additional Attack shots apply ability damage and trigger ability on-hit effects
  - All Attack shots increase Tide on successful hit
  - This ability does not cost Tide
  - 'Damage: 20 | 30 | 40 | 50 | 60'
  - 'Damage Scaling: 25% Intelligence'
  - 'Attack Speed: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Movement Speed: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Attack Damage: 25'
  - 'Buff Duration: 6 seconds'
  - 'Cooldown: 15 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  description: Activate your , gaining increased Attack Speed , Movement Speed , and
    Attack Damage . While activated Tidal Surge and Attacks fire two additional shots
  damage_type: magical
  detail_kinds:
  - null
  - null
  - null
  - magical
  - magical
  - buff
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Whirlpool
  cooldown:
  - 15.0
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - This ability hits 6 times over 3 seconds
  - 'Damage: 15 | 25 | 35 | 45 | 55'
  - 'Damage Scaling: 20% Intelligence'
  - 'Tide Cost: -15%'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 15 | 14 | 13 | 12 | 11 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Summon a whirlpool, Crippling , Vortexing , and dealing Magical Damage
    repeatedly to enemies in an area
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Release the Kraken!
  cooldown:
  - 90.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - 'Outer Ring Damage: 175 | 210 | 245 | 280 | 315'
  - 'Outer Ring Damage Scaling: 50% Intelligence'
  - 'Inner Ring Damage: 350 | 420 | 490 | 560 | 630'
  - 'Inner Ring Damage Scaling: 110% Intelligence'
  - 'Slow: 30%'
  - 'Stun Duration: 1 | 1.2 | 1.4 | 1.6 | 1.8 seconds'
  - 'Tide Cost: -20%'
  - 'Range: 7.2 meters'
  - 'Inner Radius: 2.4 meters'
  - 'Outer Radius: 4.8 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: AREA DAMAGE KNOCKUP Summon the Kraken, dealing Magical Damage and Slowing
    enemies in its area. Enemies in the center area when it spawns take increased
    Magical Damage and are Stunned and Knocked Up
  detail_kinds:
  - magical
  - magical
  - magical
  - magical
  - slow
  - stun
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of the Trident
  kit_changes: Poseidon's Attacks always fire side waves. Trident no longer affects
    Tidal Surge but can be activated to focus the side waves, causing them to pierce
    enemies, and both abilities deal extra Basic Attack damage.
source_url: https://wiki.smite2.com/w/Poseidon
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Poseidon Basic Attack
- Changing Tides
- Tidal Surge
- Trident
- Whirlpool
- Release the Kraken!
<!-- WIKI:END -->
