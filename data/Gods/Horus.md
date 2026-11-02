---
type: smite-god
name: Horus
pantheon: Egyptian
role: Support Solo
specializations:
- Healing
- Mobility
damage_type: physical
release_date: June 2, 2026
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  health_regen:
    base: 1.82
    per_level: 0.2
  mana:
    base: 296.0
    per_level: 42.0
  mana_regen:
    base: 1.45
    per_level: 0.12
  physical_prot:
    base: 21.6
    per_level: 3.24
  magical_prot:
    base: 29.6
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.4
  attack_power:
    base: 48.0
    per_level: 2.37
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Horus Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  detail_kinds:
  - null
  - physical
  - mechanic
  - mechanic
  damage_type: physical
  description: Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Resolute
  details:
  - 'Protections: 2 Per Stack'
  - 'Crowd Control Reduction: 1.5% Per Stack'
  - 'Heal: 3 Per Stack'
  - 'Buff Duration: 3 seconds'
  - 'Max Buff Stacks: 10'
  detail_kinds:
  - buff
  - buff
  - heal
  - buff
  - buff
  description: Stack Protections, Heal Gain stacks when an enemy god damages you.
    Each stack grants Protections and Crowd Control Reduction for a short duration.
    When expires, Heal based on your stacks
- slot: 1st Ability
  name: Updraft
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - Your next Attack within 5 seconds fires a gust forward, dealing Physical Damage
    and Slowing enemies. Enemies already Knocked Up take bonus Physical Damage
  - The gust cannot Critically Strike and is spent even if it misses
  - The gust triggers item effects and benefits from reduced Lifesteal
  - The gust passes through and damages all enemies, and passes through walls
  - The gust does not benefit from the bonus damage of Hydra's Lament despite consuming
    the item proc
  - 'Updraft Damage: 50 | 95 | 140 | 185 | 230'
  - 'Updraft Damage Scaling: 75% Strength'
  - 'Gust Damage: 20 | 30 | 40 | 50 | 60 + 100% Basic Attack Damage'
  - 'Knocked Up Gust Bonus Damage: 150%'
  - 'Slow: 25%'
  - 'Slow Duration: 2.5 seconds'
  - 'Gust Range: 8.8 meters'
  - 'Updraft Radius: 2.08 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  detail_kinds:
  - physical
  - null
  - null
  - null
  - null
  - physical
  - physical
  - physical
  - physical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: 'Create an updraft around you, dealing Physical Damage and Knocking
    Up nearby enemies Damage: 50 | 95 | 140 | 185 | 230 Damage Scaling: 75% Strength
    Radius: 2.08 meters'
- slot: 2nd Ability
  name: Fracture
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - You are Slowed during the cleave
  - 'Dash Damage: 70 | 95 | 120 | 145 | 170'
  - 'Dash Damage Scaling: 30% Strength'
  - 'Cleave Damage: 45 | 80 | 115 | 150 | 185'
  - 'Cleave Damage Scaling: 40% Strength'
  - 'Stun Duration: 1.25 seconds'
  - 'Protections Reduction: 3 | 6 | 9 | 12 | 15'
  - 'Debuff Duration: 3 seconds'
  - 'Self Slow: 50%'
  - 'Dash Range: 6.4 meters'
  - 'Cleave Cone Angle: 100 degrees'
  - 'Cleave Cone Range: 3.84 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  detail_kinds:
  - slow
  - physical
  - physical
  - physical
  - physical
  - stun
  - debuff
  - debuff
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Dash forward, dealing Physical Damage . Hitting an enemy god stops
    the Dash and Stuns them, then you cleave enemies in front of you, dealing Physical
    Damage and reducing their Protections
- slot: 3rd Ability
  name: Protector's Surge
  cooldown:
  - 14.0
  cost:
  - 45.0
  details:
  - Grants bonus Healing based on stacks of Resolute; does not consume stacks
  - If the selected ally is longer on the ground or dies, Horus will land either underneath
    or directly at the targeted ally depending on their last location
  - 'Heal: 30 | 60 | 90 | 120 | 150'
  - 'Protections Buff: 6 | 10 | 14 | 18 | 22'
  - 'Buff Duration: 5 seconds'
  - 'Range: 9.6 meters'
  - 'Heal Radius: 3.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 45 mana'
  detail_kinds:
  - heal
  - null
  - heal
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Leap to a target ally and descend on their location. When you land,
    Heal the target ally and nearby allies and grant them Protections for a duration
- slot: Ultimate
  name: To The Skies!
  cooldown:
  - 105.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - You are immobile and CC Immune while channeling
  - Your mirror image moves at 135% of your Movement Speed
  - 1 second after landing, all allies near your start location are also Teleported
    and receive a Shield
  - 'Damage: 150 | 230 | 310 | 390 | 470'
  - 'Damage Scaling: 80% Strength'
  - 'Shield Health: 160 | 240 | 320 | 400 | 480'
  - 'Shield Duration: 4 seconds'
  - 'Channel Duration: 1 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 105 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  detail_kinds:
  - mechanic
  - null
  - null
  - physical
  - physical
  - shield
  - shield
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: physical
  description: Send a mirror image into the sky to choose a landing location. After
    selecting a location, channel briefly, then Teleport to that location. On landing,
    deal Physical Damage , Knock Back enemies, and grant yourself a Health Shield
aspects:
- name: Aspect of the Falcon
  kit_changes: Fracture no longer stuns but deals increased damage on the cleave.
    Protector's Surge has reduced range but now can target a location spawning a wind
    sprite or targeting a enemy dealing damage and granting a gust attack. To The
    Skies! no longer teleports allies but deals bonus damage in the center.
source_url: https://wiki.smite2.com/w/Horus
last_verified: '2026-11-02'
---
<!-- WIKI:START -->
- Horus Basic Attack
- Resolute
- Updraft
- Fracture
- Protector's Surge
- To The Skies!
<!-- WIKI:END -->
