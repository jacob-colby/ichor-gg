---
type: smite-god
name: Sobek
pantheon: Egyptian
role: Support
specializations:
- Tank
- Lockdown
- Execute
damage_type: magical
release_date: October 29, 2024
base_stats:
  health:
    base: 626.52
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
    base: 375.0
    per_level: 0.0
abilities:
- slot: Basic Attack
  name: Sobek Basic Attack
  details:
  - If multiple enemies are in the area, the enemy closest to the center of the area
    will be hit
  - 'Damage Scaling: 100% Strength + 20% Intelligence + 100% Attack Damage'
  - 'Range: 1.92 meters'
  - 'Cone Angle: 120 degrees'
  description: Deal Magical Damage to an enemy in front of you
- slot: Passive
  name: Blessing of the Nile
  details:
  - An ability can only provide 1 stack per cast
  - 'Protections: 5'
  - 'Protections Scaling: 0.5 Per Level'
  - 'Cooldown Rate: 2'
  - 'Cooldown Rate Scaling: 0.2 Per Level'
  - 'Buff Duration: 10 seconds'
  - 'Max Buff Stacks: 3'
  description: When Sobek deals damage he gains a stack of Protections and Cooldown
    Rate
- slot: 1st Ability
  name: Charge Prey
  cooldown:
  - 16.0
  cost:
  - 70.0
  - 75.0
  - 80.0
  - 85.0
  - 90.0
  details:
  - Damaged enemies are Stunned before being Thrown
  - You are Displacement Immune while Dashing and CC Immune while Throwing
  - Sobek has a 0 second postfire on a missed charge or a 0.3 second postfire when
    he attempts to Throw. This 0.3 second postfire occurs both after a Throw and if
    the enemy frees themselves with CC Immunity
  - This ability stops on first target hit, and does not pass through walls
  - 'Damage: 70 | 110 | 150 | 190 | 230'
  - 'Damage Scaling: 50% Intelligence'
  - 'Stun Duration: 0.47 seconds'
  - 'Range: 8.8 meters'
  - 'Radius: 0.48 meters'
  - 'Cooldown: 16 seconds'
  - 'Cost: 70 | 75 | 80 | 85 | 90 mana'
  description: Dash forward. The first enemy hit takes Magical Damage and stops the
    dash. Sobek Throws the enemy behind him
- slot: 2nd Ability
  name: Tail Whip
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Damaged enemies are also Knocked Back away from Sobek
  - The spin begins to displace 0.4 seconds after being cast, and remains displacing
    for 0.6 seconds afterwards
  - 'Damage: 80 | 125 | 170 | 215 | 260'
  - 'Damage Scaling: 40% Intelligence'
  - 'Radius: 3.2 meters'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Spin your tail, dealing Magical Damage in an area around Sobek
- slot: 3rd Ability
  name: Sickening Strike
  cooldown:
  - 13.0
  cost:
  - 60.0
  - 65.0
  - 70.0
  - 75.0
  - 80.0
  details:
  - Reduces enemy Healing
  - Diseased enemies take bonus Magical Damage over time, have Reduced Healing, and
    can spread the Disease for 2.5 seconds
  - The Disease will spread to enemies within 3.2 meters of someone currently Diseased
  - Each enemy hit by the cone Heals you, up to 4 times
  - Each enemy god hit by the cone reduces this ability's cooldown by 1 second, up
    to 4 seconds
  - The Damage over Time does not trigger item effects
  - 'Damage: 70 | 105 | 140 | 175 | 215'
  - 'Damage Scaling: 30% Intelligence'
  - 'God Disease Damage: 4 | 4.5 | 5 | 5.5 | 6% Max Health over 2.5 seconds'
  - 'Minion Disease Damage: 30 | 45 | 60 | 75 | 90 over 2.5 seconds'
  - 'Heal: 18 | 23 | 28 | 33 | 38'
  - 'Healing Reduction: -25%'
  - 'Healing Reduction Duration: 5 seconds'
  - 'Range: 5.6 meters'
  - 'Cone Angle: 110 degrees'
  - 'Cooldown: 13 seconds'
  - 'Cost: 60 | 65 | 70 | 75 | 80 mana'
  description: Diseased enemies take bonus Magical Damage over time , have Reduced
    Healing , and can spread the Disease for 2.5 seconds Each enemy god hit by the
    cone reduces this ability's cooldown by 1 second , up to 4 seconds Strike in front
    of you. This strike deals Magical Damage in a cone and applies Disease
- slot: Ultimate
  name: Lurking in the Waters
  cooldown:
  - 90.0
  cost:
  - 80.0
  - 90.0
  - 100.0
  - 110.0
  - 120.0
  details:
  - You may cancel this ability early, dealing reduced damage
  - Executes enemies below 10-25% HP, scaling with time submerged. Executed or killed
    enemies Heal you and grants permanent bonus Health
  - Lurking in the Waters deals 25% of its potential damage if emerging instantly
  - Sobek can pass through enemies and spawned walls while submerged
  - 'Damage: 300 | 420 | 540 | 660 | 780'
  - 'Damage Scaling: 80% Intelligence'
  - 'Protections: 20%'
  - 'Mana Regen: 10% Per Second'
  - 'Heal: 25% Max Health'
  - 'Bonus Health: 25'
  - 'Radius: 4.8 meters'
  - 'Cooldown: 90 seconds'
  - 'Cost: 80 | 90 | 100 | 110 | 120 mana'
  description: deals 25% of its potential damage if emerging instantly Submerge, Slowing
    enemies nearby and granting you CC Immunity , Protections , and Mana Regen . After
    4 seconds, emerge dealing Magical Damage to enemies in range
aspects:
- name: Aspect of Prey
  kit_changes: Charge Prey now passes through all targets, knocks them forward, and
    has bonus scaling. Sickening Strike deals increased damage against Jungle Monsters
    and the cooldown reduction now triggers off Jungle Monsters.
source_url: https://wiki.smite2.com/w/Sobek
last_verified: '2026-07-25'
---
<!-- WIKI:START -->
- Sobek Basic Attack
- Blessing of the Nile
- Charge Prey
- Tail Whip
- Sickening Strike
- Lurking in the Waters
<!-- WIKI:END -->
