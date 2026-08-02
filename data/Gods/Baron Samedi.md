---
type: smite-god
name: Baron Samedi
pantheon: Voodoo
role: Mid Support
specializations:
- Nuker
- Healing
- Lockdown
damage_type: magical
release_date: October 3, 2024
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
    base: 375.0
    per_level: 0.0
  attack_power:
    base: 40.85
    per_level: 2.21
  health_regen:
    base: 1.7
    per_level: 0.2
  mana_regen:
    base: 1.57
    per_level: 0.14
abilities:
- slot: Basic Attack
  name: Baron Samedi Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - 'Hysteria Applied Per Hit: 5'
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - debuff
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Hysteria
  details:
  - Gods can have a max of 70 Hysteria
  - Gods at Max Hysteria deal Reduced Damage to Baron Samedi
  - Baron's Brew can be thrown at enemies to deal Magical Damage and apply Hysteria
  - Hysteria drains at a rate of 2 per second. This drain stops on the target for
    5 seconds when baron Samedi applies Hysteria to them
  - 'Damage: 40 + 13 Per Level'
  - 'Damage Reduction: 20%'
  - 'Hysteria Applied Per Hit: 30'
  description: 'Gods can have a max of 70 Gods at Max deal Reduced Damage to Baron
    Samedi Baron''s Brew can be thrown at enemies to deal Magical Damage and apply
    drains at a rate of 2 per second. This drain stops on the target for 5 seconds
    when baron Samedi applies to them Damage applies , granting your abilities bonus
    effects when enough is applied. Your team can also purchase Baron''s Brew from
    the Item Store Applied Per Hit: 30'
  damage_type: magical
  detail_kinds:
  - null
  - debuff
  - magical
  - null
  - magical
  - debuff
  - debuff
- slot: 1st Ability
  name: Vivid Gaze
  cooldown:
  - 11.0
  - 10.5
  - 10.0
  - 9.5
  - 9.0
  cost:
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  details:
  - Deals bonus Magical Damage to enemies hit by the overlap
  - Hitting a god above 30 Hysteria applies a Strength, Intelligence, and Attack Speed
    Reduction
  - Vivid Gaze will trigger its Hysteria effect if its own damage brings targets above
    the Hysteria threshold
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 70 | 125 | 180 | 235 | 290'
  - 'Damage Scaling: 70% Intelligence'
  - 'Overlap Damage: +25%'
  - 'Power Reduction: 20%'
  - 'Attack Speed Reduction: 20%'
  - '% Reduction Scaling: 5% Protections'
  - 'Debuff Duration: 3 | 3.5 | 4 | 4.5 | 5 seconds'
  - 'Hysteria Applied Per Hit: 15'
  - 'Range: 9.6 meters'
  - 'Radius: 1.28 meters'
  - 'Cooldown: 11 | 10.5 | 10 | 9.5 | 9 seconds'
  - 'Cost: 55 | 60 | 65 | 70 | 75 mana'
  description: will trigger its Hysteria effect if its own damage brings targets above
    the Hysteria threshold Summon skulls that deal Magical Damage in an X shape
  damage_type: magical
  detail_kinds:
  - magical
  - debuff
  - null
  - null
  - magical
  - magical
  - magical
  - debuff
  - debuff
  - debuff
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Consign Spirits
  cooldown:
  - 14.0
  cost:
  - 60.0
  details:
  - Hitting a god Heals nearby allies for Missing Health
  - Hitting a god above 30 Hysteria makes the Heal apply a Speed Buff and Slow Immunity
  - Allies within 8.8 meters of Baron Samedi or the center of Consign Spirits will
    receive the Heal
  - 'Damage: 85 | 140 | 195 | 250 | 305'
  - 'Damage Scaling: 80% Intelligence'
  - 'Heal: 25 | 35 | 45 | 55 | 65'
  - 'Heal: 3% Missing Health'
  - '% Missing Scaling: 5% Cooldown Rate'
  - 'Movement Speed: 25 | 27.5 | 30 | 32.5 | 35%'
  - 'Buff Duration: 3 | 3.25 | 3.5 | 3.75 | 4 seconds'
  - 'Hysteria Applied Per Hit: 20'
  - 'Range: 8.8 meters'
  - 'Radius: 2.88 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 mana'
  description: Allies within 8.8 meters of Baron Samedi or the center of will receive
    the Heal Call spirits that deal Magical Damage to enemies in an area
  damage_type: magical
  detail_kinds:
  - heal
  - heal
  - heal
  - magical
  - magical
  - heal
  - heal
  - heal
  - buff
  - buff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Wrap It Up
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Constricted gods take Magical Damage over 1.75 seconds
  - Minions take a tick of Magical Damage when the snake passes through them
  - Hitting a god above 30 Hysteria causes the snake to explode when it Roots, applying
    a Mesmerize to nearby enemies
  - Enemies must be at or above 30 Hysteria when Wrap It Up hits to trigger its Hysteria
    effect
  - The snake deals damage every 0.4375 seconds, for a total of 5 ticks
  - This ability passes through and damages non-god enemies, but stops on walls and
    enemy gods
  - 'Damage: 90 | 140 | 190 | 240 | 290'
  - 'Damage Scaling: 50% Intelligence'
  - 'Slow Duration: 1.75 seconds'
  - 'Root Duration: 0.75 seconds'
  - 'Mesmerize Duration: 1.5 seconds'
  - 'Hysteria Applied Per Tick: 5'
  - 'Hysteria Applied on Explosion: 25'
  - 'Range: 9.6 meters'
  - 'Radius: 0.8 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Hitting a god above 30 Hysteria causes the snake to explode when it
    Roots , applying a Mesmerize to nearby enemies Enemies must be at or above 30
    Hysteria when hits to trigger its Hysteria effect Throw a snake that constricts
    enemy gods, Slowing them to a Root
  damage_type: magical
  detail_kinds:
  - magical
  - magical
  - debuff
  - null
  - null
  - null
  - magical
  - magical
  - slow
  - debuff
  - debuff
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Life of the Party
  cooldown:
  - 110.0
  - 105.0
  - 100.0
  - 95.0
  - 90.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - The Vortex deals Magical Damage every 0.5 seconds
  - Gods above 30 Hysteria are Vortexed with more intensity
  - You gain Damage Reduction while Channeling
  - You can cancel this ability at any time
  - 'Vortex Damage: 15 | 20 | 25 | 30 | 35'
  - 'Vortex Damage Scaling: 7% Intelligence'
  - 'Slam Damage: 200 | 270 | 340 | 410 | 480'
  - 'Slam Damage Scaling: 70% Intelligence'
  - 'Slam Health Damage: 10%'
  - '% Health Scaling: 2.5% Physical + Magical Protection'
  - 'Stun Duration: 1.3 seconds'
  - 'Damage Reduction: 50%'
  - 'Hysteria Applied Per Tick: 2'
  - 'Hysteria Applied on Slam: 30'
  - 'Range: 9.6 meters'
  - 'Cone Angle: 60 degrees'
  - 'Cooldown: 110 | 105 | 100 | 95 | 90 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: Open a Coffin that Vortexes enemies towards Baron Samedi. Gods Vortexed
    into the Coffin take Magical Damage and are Stunned
  detail_kinds:
  - stun
  - stun
  - buff
  - null
  - magical
  - magical
  - magical
  - magical
  - magical
  - magical
  - stun
  - buff
  - debuff
  - debuff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Hysteria
  kit_changes: Hysteria applied over max deals damage. Max Hysteria no longer reduces
    damage. Consign Spirits only heals Baron. Vivid Gaze bonus now grants Hysteria
    over time, but no debuff. Wrap It Up explosion and DoT apply Bonus Hysteria, but
    the explosion no longer Mesmerizes. Your personal Brew can be thrown every 20s.
source_url: https://wiki.smite2.com/w/Baron_Samedi
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Baron Samedi Basic Attack
- Hysteria
- Vivid Gaze
- Consign Spirits
- Wrap It Up
- Life of the Party
<!-- WIKI:END -->
