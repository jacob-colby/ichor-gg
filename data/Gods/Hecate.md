---
type: smite-god
name: Hecate
pantheon: Greek
role: Mid
specializations:
- Nuker
- Lockdown
- Buffs
damage_type: magical
release_date: June 27, 2024
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
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Hecate Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Mythic Ritual
  details:
  - Interacting with an allied Structure creates a zone which regenerates Health and
    Mana
  - Interacting with an allied god who has recently killed a god will increase both
    your and that ally's Strength and Intelligence
  - Channel time is 2 seconds
  - Can move while Channeling. Channel will not be interrupted if the target or Hecate
    get out of range
  - Structure buff area has infinite duration. Only 1 Structure can be buffed at a
    time. If a new one is buffed the previous one will lose the effect
  - Must complete the ritual on an allied god within 30 seconds of that god getting
    a kill
  - 'Health Regen: 2 + 0.25 Per Level'
  - 'Mana Regen: 2 + 0.25 Per Level'
  - 'Strength: 5 + 2 Per Level'
  - 'Intelligence: 8 + 3.2 Per Level'
  - 'Buff Duration: 300 seconds'
  description: You may interact with things to empower them
- slot: 1st Ability
  name: Triplicate Form
  cooldown:
  - 9.0
  - 8.5
  - 8.0
  - 7.5
  - 7.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Power Form deals Magical Damage and marks enemies to take Bonus Magical Damage
    when damaged by another god
  - Hex Form deals Magical Damage and Mesmerizes enemies
  - Both projectiles linger at max range for 1 second and can still hit enemies. Each
    projectile can only hit an enemy 1 time
  - Only damage dealt by the Basic Attacks and abilities of gods trigger the bonus
    damage from the mark
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 80 | 125 | 170 | 215 | 260'
  - 'Damage Scaling: 75% Intelligence'
  - 'Bonus Damage: 10 | 13 | 16 | 19 | 22'
  - 'Bonus Damage Scaling: 2% Intelligence'
  - 'Mesmerize Duration: 1 second'
  - 'Mark Duration: 5 seconds'
  - 'Range: 11.2 meters'
  - 'Radius: 0.75 meters'
  - 'Cooldown: 9 | 8.5 | 8 | 7.5 | 7 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Split yourself and fire a projectile, alternating between Power Form
    and Hex Form
- slot: 2nd Ability
  name: Spell Eater
  cooldown:
  - 9.0
  cost:
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  - 90.0
  details:
  - Reactive to call down the Sigil and deal Magical Damage to enemies in the targeted
    area
  - Sigil has a max charge of 12
  - Damage is increased by 7.5% per charge
  - Max damage is 190% base damage and scaling
  - You can target this ability anywhere on the map, regardless of where the Sigil
    was created
  - Sigil always takes 0.75 seconds to land, regardless of the distance it travels
  - 'Damage: 80 | 130 | 180 | 230 | 280'
  - 'Damage Scaling: 50% Intelligence'
  - 'Range: 9 meters'
  - 'Charge Radius: 20 meters'
  - 'Attack Radius: 3.2 meters'
  - 'Cooldown: 9 seconds'
  - 'Cost: 50 | 60 | 70 | 80 | 90 mana'
  description: Create a Sigil that charges up when gods activate abilities in a large
    area
- slot: 3rd Ability
  name: Repel Magic
  cooldown:
  - 12.0
  cost:
  - 30.0
  - 35.0
  - 40.0
  - 45.0
  - 50.0
  details:
  - Deals Magical Damage near whomever is Shielded
  - Activating this increases your Movement Speed, and gives Spell Eater 3 charges
  - 'Damage: 75 | 120 | 165 | 210 | 255'
  - 'Damage Scaling: 70% Intelligence'
  - 'Magical Shield Health: 90 | 155 | 220 | 285 | 350'
  - 'Movement Speed: 15%'
  - 'Buff Duration: 6 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 30 | 35 | 40 | 45 | 50 mana'
  description: Activating this increases your Movement Speed , and gives Spell Eater
    3 charges Grant yourself or an allied god a Magical Shield , absorbing Magical
    Damage
- slot: Ultimate
  name: Open the Gates
  cooldown:
  - 90.0
  cost:
  - 90.0
  details:
  - Deals Magical Damage to enemies
  - You and allied gods can interact with the Portals to Teleport between them
  - One Portal is always opened right in front of you, the other is opened at a targeted
    area
  - Enemies that cleanse or immune the Stun will not be Teleported
  - The initial delay is 1.5 seconds, the interactable lifetime is 10 seconds
  - You and allied gods can interact with the portals once
  - 'Damage: 320 | 370 | 420 | 470 | 520'
  - 'Damage Scaling: 85% Intelligence'
  - 'Stun: 1 second'
  - 'Range: 14 meters'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 90 mana'
  description: Open two Portals between realms, Stunning , then Teleporting enemy
    gods to the opposite Portal
aspects:
- name: Aspect of Ruin
  kit_changes: Spell Eater can no longer be refired but instead reduces enemy ability
    damage in the area. Additionally, each time an enemy ability is cast a projectile
    lands and explodes at their location. Spell Eater's cooldown is increased.
source_url: https://wiki.smite2.com/w/Hecate
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Hecate Basic Attack
- Mythic Ritual
- Triplicate Form
- Spell Eater
- Repel Magic
- Open the Gates
<!-- WIKI:END -->
