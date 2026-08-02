---
type: smite-god
name: Merlin
pantheon: Arthurian
role: Mid
specializations:
- Nuker
- Burst Damage
damage_type: magical
release_date: March 24, 2025
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  mana:
    base: 337.46
    per_level: 45.36
  physical_prot:
    base: 17.48
    per_level: 2.76
  magical_prot:
    base: 27.38
    per_level: 1.38
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 40.85
    per_level: 2.21
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.56
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Merlin Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Overload
  details:
  - The damage from this ability can trigger Ability Item effects
  - 'Damage: 20'
  - 'Damage Scaling: 20% Intelligence'
  - 'Max Stacks: 3'
  - 'Buff Duration: 5 seconds'
  description: Using an ability provides 1 stack of . Firing a Attack consumes 1 stack
    of and deals Magical Damage to enemies hit
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
aspects:
- name: Aspect of Pandemonium
  kit_changes: Elemental Mastery has a reduced cooldown and each time it is used,
    a random Stance is selected with 2 random primary abilities, Flicker will always
    persist. Using Elemental Mastery provides an Intelligence buff for a short duration.
source_url: https://wiki.smite2.com/w/Merlin
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Merlin Basic Attack
- Overload
<!-- WIKI:END -->
