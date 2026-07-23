---
type: smite-god
name: Mordred
pantheon: Arthurian
role: Solo Jungle
specializations:
- Slayer
- Tank
- Global
damage_type: physical
release_date: August 27, 2024
base_stats:
  health:
    base: 661.0
    per_level: 94.0
  mana:
    base: 296.0
    per_level: 42.0
  physical_prot:
    base: 20.52
    per_level: 3.24
  magical_prot:
    base: 31.4
    per_level: 1.5
  attack_speed:
    base: 1.0
    per_level: 1.4
  move_speed:
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Mordred Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 4 hit chain. Attacks in order of Mourning, Clarent, Clarent, Mourning with
    a 1, 0.75, 0.75, 1x swing time
  - 'Mourning Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Clarent Damage Scaling: 60% Strength + 100% Intelligence + 60% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: 'Mordred Notes: Deal Physical Damage to an enemy in front of you Mourning
    Damage Scaling : 100% Strength + 20% Intelligence + 100% Attack Damage Clarent
    Damage Scaling : 60% Strength + 100% Intelligence + 60% Attack Damage Range :
    1.92 meters Cone Angle : 120 degrees Expand Ability Video'
- slot: Passive
  name: Wrath of the Forsaken
  details:
  - Your Ultimate Ability Heart Slash can only be used after reaching 40 Wrath
  - Your Ultimate Ability Pursue the Weak can only be used after reaching 80 Wrath
  - Hitting enemy gods with abilities provides 2 Wrath and 1 for Attacks
  - Hitting enemy minions provides 1 Wrath
  - Passively gain 1 Wrath every 4 seconds
  - Wrath can only be gained once per ability per enemy hit
  description: 'Notes: ly gain 1 Wrath every 4 seconds Hit enemies to gain Wrath.
    Additionally, you have Shoulder Charge Expand Ability Video'
- slot: Passive
  name: Shoulder Charge
  cooldown:
  - 10.0
  details:
  - This deals Physical Damage to enemies hit
  - This ability can only be used within 2 seconds of using an ability or Attack
  - Cooldown is reset on hitting an enemy god with an ability
  - 'Damage: 12'
  - 'Damage Scaling: 3 Per Level'
  - 'Range: 4 meters'
  - 'Radius: 1.5 meters'
  - 'Cooldown: 10 seconds'
  description: 'INTERACT TO DASH Notes: After using an ability or attacking, your
    Interact Key becomes a Dash forward Damage : 12 Damage Scaling : 3 Per Level Range
    : 4 meters Radius : 1.5 meters Cooldown : 10 seconds Expand Ability Video'
- slot: 1st Ability
  name: Cruel Strikes
  cooldown:
  - 14.0
  - 13.0
  - 12.0
  - 11.0
  - 10.0
  cost:
  - 45.0
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  details:
  - First Slash, dealing Physical Damage to enemies in front of you
  - Then Slam, dealing Physical Damage to enemies in a line and either dealing Bonus
    Damage or Healing, based on your Attack Chain
  - Slam attack deals Bonus Damage on hit if Mourning is next in the Attack Chain
  - Slam attack Heals you on hit if Clarent if next in the Attack Chain
  - Reduced Healing on hitting enemy minions
  - 'Slash Damage: 75 | 100 | 125 | 150 | 175'
  - 'Slash Damage Scaling: 45% Strength'
  - 'Slam Damage: 85 | 120 | 155 | 190 | 225'
  - 'Slam Damage Scaling: 65% Strength'
  - 'Bonus Damage: 45% Protections'
  - 'Heal: 45% Protections'
  - 'Minion Heal: 8 | 11 | 14 | 17 | 20'
  - 'Slash Radius: 4 meters'
  - 'Slash Angle: 90 degrees'
  - 'Slam Range: 4 meters'
  - 'Slam Radius: 0.75 meters'
  - 'Cooldown: 14 | 13 | 12 | 11 | 10 seconds'
  - 'Cost: 45 | 50 | 55 | 60 | 65 mana'
  description: 'CONE SLASH, LINE SLAM Notes: Then Slam, dealing Physical Damage to
    enemies in a line and either dealing Bonus Damage or Healing , based on your Attack
    Chain Strike twice with your swords Slash Damage : 75 | 100 | 125 | 150 | 175
    Slash Damage Scaling : 45% Strength Slam Damage : 85 | 120 | 155 | 190 | 225 Slam
    Damage Scaling : 65% Strength Bonus Damage : 45% Protections Heal : 45% Protections
    Minion Heal : 8 | 11 | 14 | 17 | 20 Slash Radius : 4 meters Slash Angle : 90 degrees
    Slam Range : 4 meters Slam Radius : 0.75 meters Cooldown : 14 | 13 | 12 | 11 |
    10 seconds Cost : 45 | 50 | 55 | 60 | 65 mana Expand Ability Video'
- slot: 2nd Ability
  name: Bloodrage
  cooldown:
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - While buffed, Attacks on enemies apply stacks, reducing their Protections and
    increasing your own as well as providing Bonus Attack Speed
  - Hitting an enemy god with the initial hit of this attack applies two stacks
  - Protections buff and debuff stack up to 4 times
  - Bonus Protections are refreshed on hit, but Bonus Attack Speed is lost when the
    Movement Speed Buff ends
  - 'Damage: 70 | 115 | 160 | 205 | 250'
  - 'Damage Scaling: 60% Strength + 40% Intelligence'
  - 'Attack Speed: 32 | 34 | 36 | 38 | 40%'
  - 'Bonus Attack Speed: 5% Per Stack'
  - 'Movement Speed: 12 | 14 | 16 | 18 | 20%'
  - 'Protections: 6 | 7 | 8 | 9 | 10 Per Stack'
  - 'Buff Duration: 4 | 4.5 | 5 | 5.5 | 6 seconds'
  - 'Protections Reduced: -4 | -5 | -6 | -7 | -8'
  - 'Debuff Duration: 4 | 4.5 | 5 | 5.5 | 6 seconds'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: 'AREA DAMAGE, SPEED BUFF Notes: Deal Physical Damage to enemies around
    you, then gain increased Attack Speed and Movement Speed Damage : 70 | 115 | 160
    | 205 | 250 Damage Scaling : 60% Strength + 40% Intelligence Attack Speed : 32
    | 34 | 36 | 38 | 40% Bonus Attack Speed : 5% Per Stack Movement Speed : 12 | 14
    | 16 | 18 | 20% Protections : 6 | 7 | 8 | 9 | 10 Per Stack Buff Duration : 4 |
    4.5 | 5 | 5.5 | 6 seconds Protections Reduced : -4 | -5 | -6 | -7 | -8 Debuff
    Duration : 4 | 4.5 | 5 | 5.5 | 6 seconds Radius : 3.2 meters Cooldown : 14 seconds
    Cost : 50 | 55 | 60 | 65 | 70 mana Expand Ability Video'
- slot: 3rd Ability
  name: Severing Slice
  cooldown:
  - 12.0
  cost:
  - 40.0
  - 50.0
  - 60.0
  - 70.0
  - 80.0
  details:
  - Direct hits with the center of the projectile cause targets to Bleed, taking Bonus
    Physical Damage as they move
  - Enemy gods are damaged for every 1.25 meters they move
  - Minions take damage over time instead of due to movement
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 55 | 85 | 115 | 145 | 175'
  - 'Damage Scaling: 70% Intelligence'
  - 'Bleed Damage: 25 | 30 | 35 | 40 | 45'
  - 'Bleed Damage Scaling: 12.5% Strength'
  - 'Minion Damage: 15 | 20 | 25 | 30 | 35'
  - 'Minion Damage Scaling: 5% Strength'
  - 'Slow: 30%'
  - 'Debuff Duration: 2.5 seconds'
  - 'Range: 9.6 meters'
  - 'Radius: 0.6 meters'
  - 'Inner Radius: 0.2 meters'
  - 'Cooldown: 12 seconds'
  - 'Cost: 40 | 50 | 60 | 70 | 80 mana'
  description: 'PROJECTILE BLEED, SLOW Notes: Direct hits with the center of the projectile
    cause targets to Bleed , taking Bonus Physical Damage as they move Fire a projectile
    that deals Physical Damage and Slows enemies Damage : 55 | 85 | 115 | 145 | 175
    Damage Scaling : 70% Intelligence Bleed Damage : 25 | 30 | 35 | 40 | 45 Bleed
    Damage Scaling : 12.5% Strength Minion Damage : 15 | 20 | 25 | 30 | 35 Minion
    Damage Scaling : 5% Strength Slow : 30% Debuff Duration : 2.5 seconds Range :
    9.6 meters Radius : 0.6 meters Inner Radius : 0.2 meters Cooldown : 12 seconds
    Cost : 40 | 50 | 60 | 70 | 80 mana Expand Ability Video'
- slot: Ultimate
  name: Heart Slash
  cooldown:
  - 20.0
  cost:
  - 40.0
  details:
  - If you hit an enemy god, they are Rooted. You then Channel to siphon their lifeforce,
    gaining a Health Shield and Healing over time while dealing Physical Damage repeatedly
    to that enemy
  - Ability repeatedly deals damage every 0.3 seconds over 1.5 seconds
  - This ability passes through and damages all enemies, and passes through walls
  - 'Damage: 100 | 155 | 210 | 265 | 320'
  - 'Damage Scaling: 75% Strength'
  - 'Damage Per Tick: 30 | 40 | 50 | 60 | 70'
  - 'Damage Scaling Per Tick: 25% Intelligence'
  - 'Heal: 10 | 20 | 30 | 40 | 50'
  - 'Heal Scaling: 12.5% Intelligence'
  - 'Shield Health: 160 | 200 | 240 | 280 | 320'
  - 'Range: 6 meters'
  - 'Radius: 1 meter'
  - 'Cooldown: 20 seconds'
  - 'Cost: 40 Wrath'
  description: 'ROOT, DRAIN Notes: If you hit an enemy god, they are Rooted . You
    then Channel to siphon their lifeforce, gaining a Health Shield and Healing over
    time while dealing Physical Damage repeatedly to that enemy Deal Physical Damage
    to enemies in an area in front of you Damage : 100 | 155 | 210 | 265 | 320 Damage
    Scaling : 75% Strength Damage Per Tick : 30 | 40 | 50 | 60 | 70 Damage Scaling
    Per Tick : 25% Intelligence Heal : 10 | 20 | 30 | 40 | 50 Heal Scaling : 12.5%
    Intelligence Shield Health : 160 | 200 | 240 | 280 | 320 Range : 6 meters Radius
    : 1 meter Cooldown : 20 seconds Cost : 40 Wrath Expand Ability Video'
- slot: Ultimate
  name: Pursue the Weak
  cost:
  - 80.0
  details:
  - Nearby enemies take Physical Damage and are Stunned
  - After a short delay, you Knock Up yourself and Stunned enemies into the sky, repeatedly
    dealing Physical Damage
  - You Heal per enemy god hit with this attack
  - Charge lasts 4 seconds but will continue if within a wall, ending immediately
    when possible
  - You gain vision of all enemies around you while Dashing
  - If no enemy gods are able to be Knocked Up, the follow-up attack will not start
  - 'Damage: 170 | 220 | 270 | 320 | 370'
  - 'Damage Scaling: 80% Strength + 75% Intelligence'
  - 'Damage Per Tick: 85 | 105 | 125 | 145 | 165'
  - 'Damage Scaling Per Tick: 20% Strength + 15% Intelligence'
  - 'Heal: 30 | 35 | 40 | 45 | 50'
  - 'Heal Scaling: 25% Intelligence'
  - 'Stun Duration: 0.5 seconds'
  - 'Radius: 3.2 meters'
  - 'Cost: 80 Wrath'
  description: 'CHARGE THROUGH WALLS Notes: After a short delay, you Knock Up yourself
    and Stunned enemies into the sky , repeatedly dealing Physical Damage If no enemy
    gods are able to be Knocked Up , the follow-up attack will not start Become CC
    Immune and Dash forward, traveling through walls, stopping on the first enemy
    god hit Damage : 170 | 220 | 270 | 320 | 370 Damage Scaling : 80% Strength + 75%
    Intelligence Damage Per Tick : 85 | 105 | 125 | 145 | 165 Damage Scaling Per Tick
    : 20% Strength + 15% Intelligence Heal : 30 | 35 | 40 | 45 | 50 Heal Scaling :
    25% Intelligence Stun Duration : 0.5 seconds Radius : 3.2 meters Cost : 80 Wrath
    Expand Ability Video'
aspects:
- name: Aspect of Rage
  kit_changes: Attacks while Bloodrage is active no longer provide bonus Protections
    or Attack Speed but instead Mordred's non-ultimate and non-passive ability cooldowns
    are lowered. Additionally Shoulder Charge deals more damage if it has hit an enemy
    god recently.
source_url: https://wiki.smite2.com/w/Mordred
last_verified: '2026-07-23'
---
<!-- WIKI:START -->
- Mordred Basic Attack
- Wrath of the Forsaken
- Shoulder Charge
- Cruel Strikes
- Bloodrage
- Severing Slice
- Heart Slash
- Pursue the Weak
<!-- WIKI:END -->
