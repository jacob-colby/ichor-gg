---
type: smite-god
name: Geb
pantheon: Egyptian
role: Support
specializations:
- Tank
- Area Control
- Shielding
damage_type: magical
release_date: January 7, 2025
base_stats:
  health:
    base: 705.27
    per_level: 101.52
  mana:
    base: 299.36
    per_level: 45.36
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 29.7
    per_level: 1.62
  attack_speed:
    base: 0.96
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
  attack_power:
    base: 44.4
    per_level: 2.4
  health_regen:
    base: 1.84
    per_level: 0.22
  mana_regen:
    base: 1.45
    per_level: 0.12
abilities:
- slot: Basic Attack
  name: Geb Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - mechanic
  - mechanic
- slot: Passive
  name: Hard as Rock
  details:
  - 'Attack Damage Reduction: -5%'
  - 'Critical Strike Damage Reduction: -65%'
  description: TAKE REDUCED DAMAGE Geb cannot take more than 20% of his max HP from
    a single attack. Additionally, Geb takes Reduced Damage from enemy god Attacks
    and Critical Strikes
  detail_kinds:
  - buff
  - buff
- slot: 1st Ability
  name: Roll Out
  cooldown:
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  - 10.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Enemies hit take Magical Damage and are Slowed
  - Your speed increases over 3 seconds before becoming CC Immune and causing enemy
    gods hit to be Knocked Back
  - After 3 seconds this ability can be refired to Leap forward, dealing Magical Damage
    and Knocking Up enemies hit
  - As your speed increases, the damage of this ability also increases from 75% to
    100%
  - Total Charge duration lasts 6 seconds
  - You can cancel this ability at any time
  - 'Damage: 100 | 175 | 250 | 325 | 400'
  - 'Damage Scaling: 50% Intelligence'
  - 'Slow: 30%'
  - 'Slow Duration: 2 seconds'
  - 'Radius: 0.8 meters'
  - 'Leap Range: 5.6 meters'
  - 'Leap Radius: 2.4 meters'
  - 'Cooldown: 14 | 13 | 12 | 11 | 10 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Charge forward, stopping on the first enemy god hit
  damage_type: magical
  detail_kinds:
  - magical
  - mechanic
  - null
  - null
  - null
  - null
  - magical
  - magical
  - slow
  - slow
  - mechanic
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 2nd Ability
  name: Shock Wave
  cooldown:
  - 14.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Damage decreases with distance, down to 80% at max range
  - 'Damage: 80 | 145 | 210 | 275 | 340'
  - 'Damage Scaling: 50% Intelligence'
  - 'Cone Angle: 90 degrees'
  - 'Cone Range: 8.8 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Create a shock wave in a cone, dealing Magical Damage and Knocking
    Up enemies hit
  damage_type: magical
  detail_kinds:
  - null
  - magical
  - magical
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: 3rd Ability
  name: Stone Shield
  cooldown:
  - 15.0
  cost:
  - 60.0
  details:
  - Allies also gain the Hard as Rock buff benefits while the Shield is active
  - The Shield also Cleanses CC when applied
  - 'Shield Health: 50 | 95 | 140 | 185 | 230'
  - 'Shield Health Scaling: 10 Per Level + 0.05% Max Health'
  - 'Shield Duration: 3 | 3.5 | 4 | 4.5 | 5 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 15 seconds'
  - 'Cost: 60 mana'
  description: Provide yourself or an allied god a Health Shield
  detail_kinds:
  - shield
  - shield
  - shield
  - shield
  - shield
  - mechanic
  - mechanic
  - mechanic
  - mechanic
- slot: Ultimate
  name: Cataclysm
  cooldown:
  - 90.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Targets take Additional Damage based on their current Health
  - You are CC Immune while using this ability
  - 'Damage: 160 | 260 | 360 | 460 | 560'
  - 'Damage Scaling: 15% of Enemy''s Current Health'
  - 'Stun: 1.4 | 1.5 | 1.6 | 1.7 | 1.8 seconds'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Pull apart the earth, dealing Magical Damage and Stunning enemy gods
    hit
  damage_type: magical
  detail_kinds:
  - magical
  - mechanic
  - magical
  - magical
  - stun
  - mechanic
  - mechanic
  - mechanic
aspects:
- name: Aspect of Calamity
  kit_changes: Geb's attacks are ranged, travel slowly, and pierce with damage falloff.
    Shockwave deals circular damage, Crits, triggers on-hits, and grants Attack Speed
    on god hit. Stone Shield is self-only and buffs attack damage. Cataclysm causes
    Knockback rather than a Stun. -7.5% Base Health, -5% Base Protections.
source_url: https://wiki.smite2.com/w/Geb
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Geb Basic Attack
- Hard as Rock
- Roll Out
- Shock Wave
- Stone Shield
- Cataclysm
<!-- WIKI:END -->
