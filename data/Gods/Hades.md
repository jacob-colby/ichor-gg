---
type: smite-god
name: Hades
pantheon: Greek
role: Solo
specializations:
- Nuker
- Mobile
- Lockdown
damage_type: magical
release_date: May 30, 2024
base_stats:
  health:
    base: 619.0
    per_level: 94.0
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
    base: 19.24
    per_level: 3.24
  magical_prot:
    base: 27.73
    per_level: 1.73
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 44.21
    per_level: 2.21
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Hades Basic Attack
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
  name: Blight
  details:
  - Blighted enemies have reduced Strength and Intelligence
  - Your abilities have extra effects on Blighted enemies
  - 'Damage Reduction: 5%'
  - 'Enhanced Damage Reduction: 10%'
  - 'Debuff Duration: 8 seconds'
  detail_kinds:
  - debuff
  - null
  - debuff
  - debuff
  - debuff
  description: ed enemies have reduced Strength and Intelligence Your abilities have
    extra effects on ed enemies Your attacks and abilities apply
- slot: 1st Ability
  name: Death From Below
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Blighted enemies are Slowed
  - 'Damage: 70 | 115 | 160 | 205 | 250'
  - 'Damage Scaling: 85% Intelligence'
  - 'Slow: 20 | 25 | 30 | 35 | 40%'
  - 'Slow Duration: 2 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - slow
  - magical
  - magical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Leap through the underworld, then emerge and deal Magical Damage to
    enemies
- slot: 2nd Ability
  name: Shroud of Darkness
  cooldown:
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  - 10.0
  cost:
  - 60.0
  details:
  - Blighted enemies are also Feared
  - Enemies are feared away from Hades
  - Enemies who are Blighted have their Blight enhanced for 5s
  - 'Silence Duration: 0.75 | 0.85 | 0.95 | 1.05 | 1.15 seconds'
  - 'Silence Duration Scaling: 0.2 seconds Per 100 Item Protections, Stacking up to
    2 Times'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 110 degrees'
  - 'Cooldown: 14 | 13 | 12 | 11 | 10 seconds'
  - 'Cost: 60 mana'
  detail_kinds:
  - debuff
  - null
  - null
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  description: Silence enemies in front of you
- slot: 3rd Ability
  name: Devour Souls
  cooldown:
  - 10.0
  - 9.5
  - 9.0
  - 8.5
  - 8.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Blighted enemies Detonate when hit, dealing additional Magical Damage to them
    and enemies around them
  - Each Detonation also Heals you and nearby allies
  - Enemies take reduced damage if hit by multiple explosions
  - Blight explosions can chain, detonating Blighted enemies not in the original detonate
    area. These contribute towards your Heal
  - Hades Heals immediately. Allies within 10.4 meters have a homing projectile sent
    towards them that Heals on arrival
  - 'Damage: 70 | 105 | 140 | 175 | 210'
  - 'Damage Scaling: 75% Intelligence'
  - 'Detonation Damage: 10 | 25 | 40 | 55 | 70'
  - 'Detonation Damage Scaling: 45% Intelligence'
  - 'Heal: 10 | 19 | 28 | 37 | 46'
  - 'Heal Scaling: 2.5% Physical Protection + 2.5% Magical Protection + 8% Intelligence'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 10 | 9.5 | 9 | 8.5 | 8 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - magical
  - heal
  - null
  - heal
  - heal
  - magical
  - magical
  - magical
  - magical
  - heal
  - heal
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Devour the souls of your enemies, dealing Magical Damage to enemies
    around you
- slot: Ultimate
  name: Pillar of Agony
  cooldown:
  - 110.0
  cost:
  - 100.0
  details:
  - You are CC Immune, and gain increased Protections while Channeling
  - Hits 8 times over 4 seconds
  - Blighted enemies have their Protections reduced
  - You may use one other ability while Channeling
  - If you use Death From Below while Channeling, the remaining Channel time will
    be 1.5 seconds regardless of remaining time
  - This Vortex increases in intensity as the Channel time progresses
  - You are Rooted while Channeling
  - You can cancel this ability at any time
  - 'Damage Per Tick: 40 | 55 | 70 | 85 | 100'
  - 'Damage Scaling Per Tick: 25% Intelligence'
  - 'Protections: 20 | 35 | 50 | 65 | 80 + 10% Protections From Items'
  - 'Protections Reduced: 10 | 13 | 16 | 19 | 22 + 10%'
  - 'Debuff Duration: 4 seconds'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 110 seconds'
  - 'Cost: 100 mana'
  detail_kinds:
  - mechanic
  - null
  - debuff
  - null
  - null
  - stun
  - debuff
  - null
  - magical
  - magical
  - buff
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: You are CC Immune , and gain increased Protections while Channeling
    Channel a Vortex around you that drags foes to their death, and repeatedly deals
    Magical Damage
aspects: []
source_url: https://wiki.smite2.com/w/Hades
last_verified: '2026-11-02'
---
<!-- WIKI:START -->
- Hades Basic Attack
- Blight
- Death From Below
- Shroud of Darkness
- Devour Souls
- Pillar of Agony
<!-- WIKI:END -->
