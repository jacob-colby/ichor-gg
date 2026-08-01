---
type: smite-god
name: Aladdin
pantheon: Tales of Arabia
role: Jungle
specializations:
- Slayer
- Burst Damage
- Mobility
damage_type: magical
release_date: January 13, 2025
base_stats:
  health:
    base: 619.0
    per_level: 94.0
  mana:
    base: 279.04
    per_level: 45.36
  physical_prot:
    base: 19.0
    per_level: 3.0
  magical_prot:
    base: 31.4
    per_level: 1.5
  attack_speed:
    base: 0.98
    per_level: 1.51
  move_speed:
    base: 380.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Aladdin Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - Has a 5 hit chain. Attacks in order of 1, 1, 0.33, 0.33, 0.5x damage and swing
    time. Final 3 hits cleave
  - 'Damage Scaling: 100% Strength + 30% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Three Wishes
  details:
  - 'Wish: Wealth. +250 Gold. +10% Gold Gains. god Kills/Assists grant +33 Gold for
    3 minutes'
  - 'Wish: Immortality. While dead, wish to be instantly revived. Gain 75% Movement
    Speed for 10 seconds when leaving the fountain'
  - 'Wish: Power. Reset ability and item cooldowns. Gain a charge of Genie''s Strength'
  description: ONE-TIME POWER UPS Make 3 wishes at any time. Gain a charge of Genie's
    Strength every 10 seconds (-1 second per enemy slain, -5 seconds for gods)
- slot: 1st Ability
  name: Kufic Invocation
  cooldown:
  - 13.0
  cost:
  - 85.0
  details:
  - When fully charged the symbol travels further and hits a larger area
  - Use a charge of Genie's Strength to send symbols back to Aladdin, dealing Magical
    Damage when small or Magical Damage when large
  - Must have a charge of Genie's Strength when cast to be able to refire. You have
    5 seconds to refire
  - Subsequent hits deal 20% of the initial damage
  - When sent back, the Kufic symbol(s) will fly to where Aladdin was when he refired
  - This ability passes through and damages all enemies, and passes through walls
  - 'Sending Small Damage: 35 | 65 | 95 | 125 | 155'
  - 'Sending Small Scaling: 33% Intelligence + 30% Strength'
  - 'Sending Large Damage: 60 | 115 | 170 | 225 | 280'
  - 'Sending Large Scaling: 60% Intelligence + 55% Strength'
  - 'Returning Small Damage: 20 | 40 | 60 | 80 | 100'
  - 'Returning Small Scaling: 20% Intelligence + 30% Strength'
  - 'Returning Large Damage: 35 | 70 | 105 | 140 | 175'
  - 'Returning Large Scaling: 40% Intelligence + 48% Strength'
  - 'Range: 8.8/11.2 meters'
  - 'Radius: 0.8/1.6 meters'
  - 'Max Starting Angle: 90 degrees'
  - 'Cooldown: 13 seconds'
  - 'Cost: 85 mana'
  description: Aladdin fires 5 Kufic symbols that deal Magical Damage to enemies in
    a cone. Charge to narrow down the cone. When fully charged the symbols merge dealing
    Magical Damage
- slot: 2nd Ability
  name: Sultan's Grace
  cooldown:
  - 16.0
  - 15.5
  - 15.0
  - 14.5
  - 14.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Deals 0.25% increased damage to enemies for each % Health below 50%
  - Use a charge of Genie's Strength to summon the Genie to unleash a flurry of 5
    punches that deal Magical Damage to enemies in front of Aladdin
  - Must have a charge of Genie's Strength when cast to be able to refire. You have
    5 seconds to refire
  - You can cancel this ability at any time
  - 'Dash Damage: 70 | 115 | 160 | 205 | 250'
  - 'Dash Scaling:: 55% Intelligence + 55% Strength'
  - 'Dash Missing HP Bonus Scaling:: 0.13% Intelligence'
  - 'Punch Damage:: 20 | 30 | 40 | 50 | 60'
  - 'Punch Scaling:: 15% Intelligence + 27% Strength'
  - 'Range: 6.4 meters'
  - 'Radius: 1.92 meters'
  - 'Cooldown: 16 | 15.5 | 15 | 14.5 | 14 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Dash forward dealing Magical Damage to enemies you pass through
- slot: 3rd Ability
  name: Agile Run
  cooldown:
  - 18.0
  cost:
  - 50.0
  - 55.0
  - 60.0
  - 65.0
  - 70.0
  details:
  - Use a charge of Genie's Strength to call the Genie to slam down at the landing
    location. Enemies take Magical Damage and are Knocked Up
  - Cooldown is reduced if you land on an enemy god
  - The Angle Aladdin runs along the wall is determined by the angle Aladdin approaches
    the wall
  - Aladdin can toggle using a charge of Genie's Strength until a landing location
    is selected
  - Aladdin runs for 8.8 meters or until he reaches 5 meters in height. The wall run
    will always take 1.25 seconds
  - Aladdin can wall run along all walls, structures, and player made deployables
    that he would normally collide with
  - 'Landing Damage: 60 | 115 | 170 | 225 | 280'
  - 'Landing Scaling: 70% Intelligence + 50% Strength'
  - 'Genie Damage: 35 | 50 | 5 | 80 | 95'
  - 'Genie Scaling: 20% Intelligence + 40% Strength'
  - 'Genie Knockback Duration: 0.5 seconds'
  - 'Cooldown Reduction: -2 | -2.5 | -3 | -3.5 | -4 seconds'
  - 'Dash Range: 7.2 meters'
  - 'Leap Range: 8.8 meters'
  - 'Leap Radius: 3.2 meters'
  - 'Cooldown: 18 seconds'
  - 'Cost: 50 | 55 | 60 | 65 | 70 mana'
  description: Dash forward. Dashing into a wall causes you to run along it before
    Leaping to a location, dealing Magical Damage to enemies in the landing area
- slot: Ultimate
  name: Into The Lamp
  cooldown:
  - 90.0
  cost:
  - 70.0
  - 80.0
  - 90.0
  - 0.0
  - 110.0
  details:
  - Aladdin and the target have their health restored to a minimum amount. Aladdin's
    non-ultimate cooldowns are reset. The target's non-ultimate cooldowns are halved
  - The Lamp is left behind, allowing any god to enter the lamp and join the ongoing
    challenge
  - Damage dealt by the initial hit cannot trigger item effects
  - The fight lasts for 16 seconds, after which everyone is kicked out of the lamp.
    An escape lamp appears at 8 seconds into a fight
  - The escape can open early when either the main Aladdin and fight target (hereby
    referred to as combatants) die, or if only 1 team remains in the lamp
  - Entering the lamp or leaving the lamp requires interacting with the lamp. This
    interaction takes 0.5 seconds and is interrupted by taking damage
  - Non-combatants deal 33% reduced damage to and take 33% reduced damage from combatants
  - If while a fight is active a different Aladdin brings a target into the lamp,
    they become the new combatants. The previous combatants are now treated as non-combatants
    and the arena resets its fight timer and closes the escape if it was active
  - gods outside the lamp cannot target gods inside the lamp. gods inside the lamp
    cannot target gods outside the lamp
  - Being kicked out of the lamp interrupts any currently firing ability
  - gods will be returned to the original locations and camera rotations when leaving
    the lamp
  - Recalling and Into the Lamp are blocked from being used while inside the lamp
  - This ability passes through non-god enemies, but stops on walls and enemy gods
  - 'Damage: 150 | 250 | 350 | 450 | 550'
  - 'Damage Scaling: 70% Intelligence + 55% Strength'
  - 'Max Health Shield: 35%'
  - 'Self CDR: 50 | 55 | 60 | 65 | 70'
  - 'Enemy CDR: 50'
  - 'Protections: 10 | 15 | 20 | 25 | 30'
  - 'Lamp Interact Size: 4.5 meters'
  - 'Range: 13.6 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 70 | 80 | 90 | 00 | 110 mana'
  description: Throw the Lamp forward, dealing Magical Damage and stopping on first
    enemy god hit. If successful, Aladdin and the enemy god are pulled into the lamp
    to challenge each other
aspects: []
source_url: https://wiki.smite2.com/w/Aladdin
last_verified: '2026-08-01'
---
<!-- WIKI:START -->
- Aladdin Basic Attack
- Three Wishes
- Kufic Invocation
- Sultan's Grace
- Agile Run
- Into The Lamp
<!-- WIKI:END -->
