---
type: smite-god
name: Ix Chel
pantheon: Maya
role: Mid Support
specializations:
- Area Control
- Crowd Control
- Healing
damage_type: magical
release_date: August 11, 2026
base_stats:
  health:
    base: 569.48
    per_level: 86.48
  health_regen:
    base: 1.82
    per_level: 0.2
  mana:
    base: 319.68
    per_level: 45.36
  mana_regen:
    base: 1.56
    per_level: 0.12
  physical_prot:
    base: 17.72
    per_level: 3.0
  magical_prot:
    base: 29.81
    per_level: 1.72
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 33.12
    per_level: 2.21
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Ix Chel Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire a projectile that deals Magical Damage to the first enemy hit
- slot: Passive
  name: Rainbow Weaver
  details:
  - The empowered Attack is spent even if it misses
  - The empowered Attack triggers item effects and it benefits from 33% Lifesteal
  - The empowered Attack has 10% increased projectile speed and can hit enemy structures
    from beyond their attack radius
  - 'Bonus Damage: 40% Intelligence'
  - 'Range: 11.2 meters'
  - 'Radius: 1.28 meters'
  detail_kinds:
  - null
  - null
  - null
  - magical
  - mechanic
  - mechanic
  description: Gain a stack whenever your Abilities hit an enemy god or grant a beneficial
    effect to an allied god. At 6 stacks, your next Attack has no movement penalty
    , is larger , travels farther , and deals bonus Damage
- slot: 1st Ability
  name: Gleaming Blast
  cooldown:
  - 6.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - After Gleaming Blast hits an enemy, Threads of Light can be cast immediately
  - This ability does 40% bonus damage to Minions and Jungle Monsters
  - This ability passes through and damages non-god enemies, and passes through walls,
    but stops on enemy gods
  - 'Damage: 80 | 100 | 120 | 140 | 160'
  - 'Damage Scaling: 60% Intelligence'
  - 'Range: 11.2 meters'
  - 'Cooldown: 6 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  detail_kinds:
  - null
  - null
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: After hits an enemy, Threads of Light can be cast immediately Fire
    a blast of gleaming blast light that deals Magical Damage , stopping on the first
    enemy god hit and transforming this ability into Threads of Light
- slot: 1st Ability (Alt)
  name: Threads of Light
  cooldown:
  - 6.0
  cost:
  - 40.0
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  details:
  - 'Damage: 60 | 105 | 150 | 195 | 240'
  - 'Damage Scaling: 80% Intelligence'
  - 'Tip Damage: +25%'
  - 'Blind Duration: 1 second'
  - 'Range: 10 meters'
  - 'Cone Angle: 19.6 degrees'
  - 'Cooldown: 6 seconds'
  - 'Cost: 40 | 45 | 50 | 55 | 60 mana'
  detail_kinds:
  - magical
  - magical
  - magical
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Damage Area and Blind Illuminate strands in a cone to deal Magical
    Damage . Enemies facing the strands as they illuminate are Blinded . Enemies hit
    by the tip of the cone take additional damage
- slot: 2nd Ability
  name: Lunar Invocation
  cooldown:
  - 14.0
  cost:
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  - 95.0
  details:
  - 'Damage: 80 | 145 | 195 | 245 | 295'
  - 'Damage Scaling: 60% Intelligence'
  - 'Heal: 50 | 85 | 120 | 155 | 180'
  - 'Heal Scaling: 10% Intelligence'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 65 | 70 | 75 | 80 | 95 mana'
  detail_kinds:
  - magical
  - magical
  - heal
  - heal
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Area Damage, Knockup, and Heal Invoke lunar energy at an area. After
    a brief delay, it explodes, dealing Magical Damage and Knocking Up enemies while
    Healing allies
- slot: 3rd Ability
  name: Rainbow Crash
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - You can benefit from the Movement Speed of both the initial cast and an orb
  - Orbs bounce off walls a maximum of 2 times. Each allied god can pick up only 1
    orb per cast
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 85% Intelligence'
  - 'Movement Speed: 20%'
  - 'Root Duration: 1.25 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - buff
  - null
  - magical
  - magical
  - buff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Fire an arcing rainbow and gain Movement Speed . When it lands, deal
    Magical Damage and Root enemies. The rainbow splits into orbs that you and allied
    gods can pick up to gain Movement Speed
- slot: Ultimate
  name: Great End
  cooldown:
  - 110.0
  cost:
  - 90.0
  details:
  - Simultaneously hitting an enemy god and allied god extends the channel
  - Repeated hits deal increasing damage; this bonus rapidly decays when hits stop
  - Firing the beam grants maximum Rainbow Weaver stacks
  - If you start the Ability with maximum Rainbow Weaver stacks, gain bonus Echo for
    the duration
  - 'Damage Per Tick: 26 | 38 | 40 | 52 | 64'
  - 'Damage Scaling Per Tick: 8% Intelligence'
  - 'Heal Per Tick: 2% of Missing Health'
  - 'Echo: 20'
  - 'Range: 11.2 meters'
  - 'Radius: 0.4 meters'
  - 'Cooldown: 110 seconds'
  - 'Cost: 90 mana'
  detail_kinds:
  - null
  - null
  - null
  - buff
  - magical
  - magical
  - heal
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Become CC Immune and channel a rainbow beam. Enemies repeatedly take
    Magical Damage and allied gods repeatedly Heal . Damaging an enemy god or Healing
    an allied god also Heals you
aspects:
- name: Aspect of the Mother's Light
  kit_changes: Gleaming Blast and the Great End no longer deal damage. Gleaming Blast
    now shields ally gods and slows enemy gods. Lunar Invocation and the Great End
    have greatly increased healing
source_url: https://wiki.smite2.com/w/Ix_Chel
last_verified: '2026-08-19'
---
<!-- WIKI:START -->
- Ix Chel Basic Attack
- Rainbow Weaver
- Gleaming Blast
- Threads of Light
- Lunar Invocation
- Rainbow Crash
- Great End
<!-- WIKI:END -->
