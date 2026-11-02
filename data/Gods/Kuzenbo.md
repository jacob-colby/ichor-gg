---
type: smite-god
name: Kuzenbo
pantheon: Japanese
role: Support
specializations:
- Crowd Control
- Lockdown
damage_type: magical
release_date: October 20, 2026
base_stats:
  health:
    base: 705.3
    per_level: 101.52
  health_regen:
    base: 1.84
    per_level: 0.22
  mana:
    base: 299.0
    per_level: 45.37
  mana_regen:
    base: 1.45
    per_level: 0.12
  physical_prot:
    base: 20.5
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.4
  attack_power:
    base: 36.0
    per_level: 2.42
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Kuzenbo Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
  damage_type: magical
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Water Bowl
  details:
  - Hard Crowd Control removes half your stacks, once every 1.5 seconds
  - Gives 15% Mitigations at max stacks
  - 'Damage Mitigation: 1.5% per 2% of Max HP Taken'
  - 'Max Stacks: 10'
  - 'Buff Duration: 30 seconds'
  detail_kinds:
  - null
  - null
  - buff
  - buff
  - buff
  description: Each time you take a portion of your max HP as damage (pre-mitigation),
    gain a stack of as your head fills with water, granting Damage Mitigation . Stacks
    last a duration and refresh when you gain another
- slot: 1st Ability
  name: NeNe Kappa
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Transfers 20% of your Health and Protections to the NeNe Kappa
  - Can bounce off walls up to 2 times
  - Can have multiple NeNe Kappas at once
  - NeNe Kappas attack once per second
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 55% Intelligence'
  - 'Damage: 35 | 45 | 55 | 65 | 75'
  - 'Range: 11.2 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - null
  - null
  - null
  - null
  - magical
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Transfers 20% of your Health and Protections to the Can have multiple
    s at once s attack once per second This ability passes through and damages non-god
    enemies, but bounces off walls, and stops on enemy gods Throw a that deals Magical
    Damage and can ricochet off walls. After hitting an enemy god or reaching maximum
    range, it bursts from its shell, Slowing them and attacking
- slot: 2nd Ability
  name: Shell Spikes
  cooldown:
  - 14.0
  - 13.5
  - 13.0
  - 12.5
  - 12.0
  cost:
  - 50.0
  details:
  - While active your NeNe Kappa also reflects a portion of damage taken
  - Can be activated while under the effect of Crowd Control
  - Reflected damage uses the base damage of the incoming attack, before Protections
    and Mitigations
  - This ability does not damage towers or phoenixes and cannot proc item effects
  - 'Damage Reflected: 15 | 20 | 25 | 30 | 35% of Damage Taken'
  - 'Cooldown Reduction: 0.6 | 0.7 | 0.8 | 0.9 | 1 second'
  - 'Buff Duration: 3 seconds'
  - 'Cooldown: 14 | 13.5 | 13 | 12.5 | 12 seconds'
  - 'Cost: 50 mana'
  detail_kinds:
  - null
  - null
  - null
  - null
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  description: Extend the spikes on your back, reflecting a portion of damage taken
    as Magical Damage to enemies who attack you. While active, each time you take
    damage, reduce the Cooldown of NeNe Kappa and Sumo Slam
- slot: 3rd Ability
  name: Sumo Slam
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Pushed targets can be hit up to 3 times
  - Only the first wall collision deals damage
  - You can turn freely with an increased turn radius
  - Dashes for a maximum of 1.5 seconds
  - 'Damage: 60 | 95 | 130 | 165 | 200'
  - 'Damage Scaling: 40% Intelligence'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  detail_kinds:
  - null
  - null
  - null
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  damage_type: magical
  description: Dash forward, becoming Slow Immune , dealing Magical Damage to enemy
    minions and Silencing and Pushing the first enemy god you hit. Each subsequent
    enemy you hit deals damage to both that enemy and the god you are pushing. Colliding
    with a wall also deals damage to the pushed god
- slot: Ultimate
  name: Watery Grave
  cooldown:
  - 75.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Damage ticks every 0.6s
  - Each hit after the first on an enemy deals 40% reduced damage
  - 'First Hit Damage: 80 | 130 | 180 | 230 | 280'
  - 'First Hit Damage Scaling: 40% Intelligence'
  - 'Subsequent Hits Damage: 40 | 65 | 90 | 115 | 140'
  - 'Subsequent Hits Damage Scaling: 20% Intelligence'
  - 'Movement Speed: 30%'
  - 'Damage Mitigation: 20%'
  - 'Radius: 3.6 meters'
  - 'Cooldown: 75 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  detail_kinds:
  - null
  - null
  - magical
  - magical
  - magical
  - magical
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  description: Pull into your shell and spin, summoning fierce currents that deal
    Magical Damage and Knock Back enemies. Gain Movement Speed , Damage Mitigation
    , CC Immunity , and move freely in all directions
aspects:
- name: Aspect of Spirits
  kit_changes: Coming Soon
source_url: https://wiki.smite2.com/w/Kuzenbo
last_verified: '2026-11-02'
---
<!-- WIKI:START -->
- Kuzenbo Basic Attack
- Water Bowl
- NeNe Kappa
- Shell Spikes
- Sumo Slam
- Watery Grave
<!-- WIKI:END -->
