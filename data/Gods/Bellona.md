---
type: smite-god
name: Bellona
pantheon: Roman
role: Solo
specializations:
- Brawler
- Tank
- Lockdown
damage_type: physical
release_date: May 2, 2024
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 272.32
    per_level: 38.64
  physical_prot:
    base: 20.73
    per_level: 3.45
  magical_prot:
    base: 29.58
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 1.4
  move_speed:
    base: 370.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Bellona Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - You have 4 different weapons to attack with, depending on the most recent ability
    used
  - Bellona remains in her current Basic Attacks until she goes 7 seconds without
    dealing or taking damage
  - Greatsword has a 3 hit chain. Attacks in order of 1, 1, 1.5x damage and swing
    time, with no special effects
  - Sword and Shield has a 3 hit chain, Attacks in order of 0.5, 1, 1.5x damage and
    swing time and provides 1 Block Stack every enemy god hit. Max 3 stacks
  - Hammer has a 3 hit chain. Attacks in order of 1.5, 1, 1.5x damage and 1.5, 1,
    1.25x swing time. Hits all enemies in range of each attack
  - Scourge has a 3 hit chain. Attacks in order of 1, 0.5, 1x damage and swing time
    and Heals you on every successful hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Scourge Heal Per Hit: 5 | 6 | 7 | 8 | 9'
  - 'Scourge Heal Scaling Per Hit: 7% Physical Protection'
  - 'Range: 1.92 meters'
  - 'Scourge Range: 2.56 meters'
  - 'Cone Angle: 120 degrees'
  description: Bellona remains in her current s until she goes 7 seconds without dealing
    or taking damage Deal Physical Damage to an enemy in front of you
- slot: Passive
  name: Master Of War
  details:
  - If using Sword and Shield, you also get Physical and Magical Protection stacks
  - If using Scourge, you also get Attack Speed stacks
  - If using Hammer, you also get Strength stacks
  - All Basic Attacks still gain the Movement Speed per stack
  - 'Movement Speed: 1.5 Per Stack'
  - 'Physical Protection: 4 Per Stack'
  - 'Magical Protection: 4 Per Stack'
  - 'Strength: 3% Per Stack'
  - 'Attack Speed: 5% Per Stack'
  - 'Buff Duration: 7 seconds'
  - Max Buff Stacks 5
  description: When you hit or are hit by Basic Attacks, you gain stacks of Movement
    Speed
- slot: 1st Ability
  name: Shield Bash
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Gain 1 Block Stack for each enemy god hit
  - Change to Sword and Shield Basic Attacks
  - Every third successful Basic Attack against a god grants a Block Stack, reflecting
    damage
  - Block absorbs all damage from one god's Basic Attack per stack
  - Blocks also reflect back a portion of the blocked damage to enemies around Bellona
  - 'Damage: 75 | 115 | 155 | 195 | 235'
  - 'Damage Scaling: 50% Strength + 30% Physical and Magical Protection'
  - 'Reflect Damage: 25% of the damage blocked'
  - 'Reflect Damage Scaling: 7% Physical and Magical Protection'
  - 'Slow: 20%'
  - 'Slow Duration: 1.5 seconds'
  - 'Dash Range: 2.8 meters'
  - 'Bash Range: 4 meters'
  - 'Bash Cone Angle: 120 degrees'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Every third successful Basic Attack against a god grants a Block Stack
    , reflecting damage Dash forward with your shield to deal Physical Damage and
    Slow enemies in front of you
- slot: 2nd Ability
  name: Bludgeon
  cooldown:
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  - 10.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Change to Hammer Basic Attacks
  - Your Basic Attacks now hit nearby enemies
  - Final Slam damage increases by 35% for each enemy god hit by the Spin Attack
  - 'Spin Damage: 55 | 90 | 125 | 165 | 200'
  - 'Spin Damage Scaling: 25% Strength'
  - 'Slam Damage: 70 | 130 | 190 | 250 | 310'
  - 'Slam Damage Scaling: 70% Strength'
  - 'Spin Radius: 4 meters'
  - 'Slam Range: 4.8 meters'
  - 'Slam Radius: 1.92 meters'
  - 'Cooldown: 14 | 13 | 12 | 11 | 10 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Spin your hammer to deal Physical Damage to enemies around you, then
    slam to deal Physical Damage to enemies in a line
- slot: 3rd Ability
  name: Scourge
  cooldown:
  - 16.0
  - 15.0
  - 14.0
  - 13.0
  - 12.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Change to Scourge Basic Attacks
  - Your Basic Attacks Heal you
  - 'Damage: 80 | 120 | 160 | 200 | 240'
  - 'Damage Scaling: 50% Strength'
  - 'Heal: 6 | 7 | 8 | 9 | 10'
  - 'Heal Scaling: 6% Physical Protection'
  - 'Disarmed Duration: 1.25 | 1.4 | 1.55 | 1.7 | 1.85 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 1.6 meters'
  - 'Cooldown: 16 | 15 | 14 | 13 | 12 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: Change to Basic Attacks Lash out with your to deal Physical Damage
    and Disarm enemies
- slot: Ultimate
  name: Eagle's Rally
  cooldown:
  - 90.0
  cost:
  - 100.0
  details:
  - The flag empowers you and allied gods in the area, granting Strength, Intelligence,
    and Physical and Magical Protection
  - You are CC Immune while Leaping
  - 'Damage: 300 | 370 | 440 | 510 | 580'
  - 'Damage Scaling: 60% Strength'
  - 'Stun Duration: 0.75 seconds'
  - 'Strength: 8 | 16 | 24 | 32 | 40 + 7.5% Protections'
  - 'Intelligence: 22 | 30 | 38 | 46 | 54 + 7.5% Protections'
  - 'Protection: 15 | 20 | 25 | 30 | 35 + 7.5% Physical and Magical Protections'
  - 'Range: 8.8 meters'
  - 'Radius: 2.4 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 100 mana'
  description: The flag empowers you and allied gods in the area, granting Strength
    , Intelligence , and Physical and Magical Protection Leap forward and plant your
    flag to deal Physical Damage and Stun enemies
aspects:
- name: Aspect of Vindication
  kit_changes: Bludgeon no longer deals bonus Final Slam Damage but whenever Bellona
    gains Block Stacks with Sword and Shield or gains Health from Scourge, nearby
    allied gods also gain those benefits.
source_url: https://wiki.smite2.com/w/Bellona
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Bellona Basic Attack
- Master Of War
- Shield Bash
- Bludgeon
- Scourge
- Eagle's Rally
<!-- WIKI:END -->
