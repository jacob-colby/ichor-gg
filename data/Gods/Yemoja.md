---
type: smite-god
name: Yemoja
pantheon: Yoruba
role: Support
specializations:
- Tank
- Healing
- Shielding
damage_type: magical
release_date: October 3, 2024
base_stats:
  health:
    base: 633.1
    per_level: 108.1
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 1.0
    per_level: 1.29
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 41.04
    per_level: 2.4
  health_regen:
    base: 1.82
    per_level: 0.2
abilities:
- slot: Basic Attack
  name: Yemoja Basic Attack
  details:
  - Projectile stops on first target hit, and does not pass through walls
  - Yemoja Attacks can hit allies with an increased radius, applying Omi Healing
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Ally Radius: 0.8 meters'
  description: Fire a projectile that deals Magical Damage to the first enemy hit
  damage_type: magical
  detail_kinds:
  - null
  - null
  - magical
  - mechanic
  - mechanic
  - mechanic
- slot: Passive
  name: Omi
  details:
  - Start with 7 Omi, earning an additional 1 at levels 5, 10, and 15
  - Cooldown Reduction increases Omi regeneration
  - 'Heal Per Tick: 1'
  - 'Heal Scaling Per Tick: 0.1 Per Level'
  - 'Heal Duration: 4 seconds'
  description: Start with 7 , earning an additional 1 at levels 5, 10, and 15 Cooldown
    Reduction increases regeneration Yemoja uses to cast spells instead of Mana, and
    her non-ultimate abilities have no cooldown. Yemoja's water based attacks and
    abilities can hit allies, providing them a Heal every 0.5 seconds. Yemoja's Attack
    healing only affects gods and does not proc item effects.
  detail_kinds:
  - null
  - null
  - heal
  - heal
  - heal
- slot: 1st Ability
  name: Bouncing Bubble
  cost:
  - 2.0
  details:
  - Small bubbles deal reduced Magical Damage
  - Enemies hit by both large bubbles take 50% damage on the second hit
  - Allies hit gain Omi Healing
  - This ability changes to Moonstrike when used
  - 'Damage: 56 | 98 | 140 | 182 | 224'
  - 'Damage Scaling: 30% Intelligence'
  - 'Small Bubble Damage: 28 | 49 | 70 | 91 | 112'
  - 'Small Bubble Damage Scaling: 15% Intelligence'
  - 'Slow: 30%'
  - 'Slow Duration: 1.4 seconds'
  - 'Range: 5.6 meters'
  - 'Radius: 2.24 meters'
  - 'Small Bubble Radius: 1 meter'
  - 'Cost: 2 Omi'
  description: Toss a bubble that bounces twice, dealing Magical Damage and Slowing
    enemies before exploding into smaller bubbles
  damage_type: magical
  detail_kinds:
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
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 1st Ability (Alt)
  name: Moonstrike
  cost:
  - 2.0
  details:
  - Allies in the final strike have their Omi Healing replaced with a buff providing
    increased Attack Speed and Attack Damage
  - Enemy structures hit by the final strike are Stunned for 2 seconds
  - This ability changes to Bouncing Bubble when used
  - 'Damage: 30 | 60 | 90 | 120 | 150'
  - 'Damage Scaling: 20% Intelligence'
  - 'Final Damage: 65 | 105 | 145 | 185 | 225'
  - 'Final Damage Scaling: 40% Intelligence'
  - 'Stun Duration: 1 second'
  - 'Attack Speed: 30%'
  - 'Attack Damage: 20 | 25 | 30 | 35 | 40'
  - 'Buff Duration: 4 seconds'
  - 'Range: 10.4 meters'
  - 'Radius: 2.4 meters'
  - 'Final Radius: 1.6 meters'
  - 'Cost: 2 Omi'
  description: The Moon strikes multiple times at a location dealing Magical Damage
    before a final strike dealing increased Magical Damage and Stunning enemies hit
  damage_type: magical
  detail_kinds:
  - buff
  - stun
  - null
  - magical
  - magical
  - magical
  - magical
  - stun
  - buff
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Mending Waters
  cost:
  - 3.0
  details:
  - This ability also does bonus damage to enemy Health Shields
  - Allies hit gain Omi Healing
  - This ability passes through and damages all enemies, but stops on ally gods and
    walls
  - 'Damage: 65 | 95 | 125 | 155 | 185'
  - 'Damage Scaling: 50% Intelligence'
  - 'Bonus Damage to Shields: 2 | 2 | 2 | 2 | 3x'
  - 'Heal: 15 | 25 | 35 | 45 | 55'
  - 'Shield Health: 40 | 65 | 90 | 115 | 140'
  - 'Shield Health Scaling: 4% Max Health'
  - 'Range: 9.6 meters'
  - 'Radius: 1.12 meters'
  - 'Cost: 3 Omi'
  description: Fire a water wave, dealing Magical Damage to enemies. This wave stops
    and bounces between allied gods, Healing them and providing them a Health Shield
  damage_type: magical
  detail_kinds:
  - shield
  - null
  - null
  - magical
  - magical
  - magical
  - heal
  - shield
  - shield
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Riptide
  cost:
  - 3.0
  details:
  - Allies travel further and gain Movement Speed and Protections
  - Enemies are Slowed
  - Placing the ring at the maximum distance reverses it's direction
  - Allies that use the ring gain Omi Healing
  - 'Movement Speed: 10 | 12.5 | 15 | 17.5 | 20%'
  - 'Protections: 20 | 25 | 30 | 35 | 40'
  - 'Buff Duration: 3 seconds'
  - 'Slow: 10%'
  - 'Slow Duration: 2 seconds'
  - 'Range: 9.6 meters'
  - 'Radius: 2.24 meters'
  - 'Cost: 3 Omi'
  description: Create a water ring that Knocks Back anyone entering it
  detail_kinds:
  - buff
  - slow
  - null
  - null
  - buff
  - buff
  - buff
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: River's Rebuke
  cooldown:
  - 120.0
  details:
  - Allies impacted by the crashing waves gain Omi Healing and Moonstrike's buff
  - The waves begin crashing from the casting location after 4 seconds, traveling
    to the max range over 1 second
  - You gain a buff of increased Omi regeneration on using this ability
  - You gain half of your missing Omi immediately, but the duration of the regeneration
    buff is decreased based on the amount restored
  - 'Damage: 250 | 320 | 390 | 460 | 530'
  - 'Damage Scaling: 70% Intelligence'
  - 'Tremble Duration: 2 seconds'
  - 'Slow: 60%'
  - 'Slow Duration: 2 seconds'
  - 'Omi Regeneration: +0.5 Omi per second'
  - 'Omi Regeneration Duration: 10 seconds'
  - 'Range: 15 meters'
  - 'Radius: 4.5 meters'
  - 'Cooldown: 120 seconds'
  description: Conjure 2 large walls of water that block enemy movement and projectiles.
    After a delay they crash down dealing Magical Damage , Trembling , and applying
    a decaying Slow to enemies hit
  damage_type: magical
  detail_kinds:
  - null
  - null
  - null
  - null
  - magical
  - magical
  - debuff
  - slow
  - slow
  - buff
  - buff
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Downpour
  kit_changes: Mending Waters no longer affects allies but stops and bounces on enemy
    gods, dealing damage, shield damage and providing Yemoja stacking Intelligence
    per hit. Additionally Moonstrike no longer stuns gods but has increased Intelligence
    scaling.
source_url: https://wiki.smite2.com/w/Yemoja
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Yemoja Basic Attack
- Omi
- Bouncing Bubble
- Moonstrike
- Mending Waters
- Riptide
- River's Rebuke
<!-- WIKI:END -->
