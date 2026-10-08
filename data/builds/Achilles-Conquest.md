---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.5
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.33
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.33
    - name: Avenging Blade
      pick_rate: 0.14
      win_rate: 0.33
  - name: Sanguine Lash
    pick_rate: 0.26
    win_rate: 0.64
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.33
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.33
  - name: Shifter's Shield
    pick_rate: 0.12
    win_rate: 0.0
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.12
      win_rate: 0.8
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.2
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.0
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.33
  - name: Hussar's Wings
    pick_rate: 0.09
    win_rate: 0.33
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.09
      win_rate: 0.67
    - name: Blinking Abyss
      pick_rate: 0.09
      win_rate: 0.33
  - name: Medal of Defense
    pick_rate: 0.14
    win_rate: 0.0
    alternates:
    - name: Xibalban Effigy
      pick_rate: 0.09
      win_rate: 0.0
    - name: Circle of Protection
      pick_rate: 0.09
      win_rate: 0.0
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.89
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.5
  - name: Sundering Axe
    pick_rate: 0.14
    win_rate: 0.17
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-10-08'
  god_win_rate: 0.37209302325581395
  god_matches_won: 16
  god_matches_played: 43
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-08'
  god_matches_analyzed: 1596
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Eye of the Storm
  - Runeforged Hammer
  - Sanguine Lash
  - Dwarven Plate
  flex_slots:
  - Runeforged Hammer
  - Eye of the Storm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Eye of the Storm,
    Shield Splitter, Avenging Blade, Heartseeker, Berserker''s Shield, Genji''s Guard,
    Hydra''s Lament, Breastplate of Valor, Titan''s Bane, The Crusher, Erosion, The
    Reaper, Eye of Providence, Draconic Scale, Shield of the Phoenix, Golden Blade,
    Daybreak Gavel, Midgardian Mail, Avatar''s Parashu, Stone of Binding, Hide of
    the Nemean Lion, Leviathan''s Hide, Void Shield, Pendulum Blade.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.56
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.26
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.54
    Eye of the Storm:
      total: 0.42
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.1
      fit: 0.59
    Sanguine Lash:
      total: 0.51
      efficiency: 0.36
      win: 0.64
      pick: 0.35
      fit: 0.52
    Dwarven Plate:
      total: 0.49
      efficiency: 0.4
      win: 0.67
      pick: 0.19
      fit: 0.26
  community_ordered:
  - Brawler’s Beat Stick
  - Runeforged Hammer
  - Sanguine Lash
  - Dwarven Plate
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Sanguine Lash
  - Dwarven Plate
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Amanita Charm, Genji''s Guard, Runeforged Hammer, Breastplate of Valor,
    Hydra''s Lament, Heartseeker, Shield Splitter, Avenging Blade, Eye of the Storm,
    Berserker''s Shield, Titan''s Bane, The Crusher, Shield of the Phoenix, Transcendence,
    Daybreak Gavel, The Reaper, Arondight, Screeching Gargoyle, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, Golden Blade.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.54
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.15
    Genji's Guard:
      total: 0.42
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.42
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.52
    Sanguine Lash:
      total: 0.49
      efficiency: 0.36
      win: 0.64
      pick: 0.35
      fit: 0.38
    Dwarven Plate:
      total: 0.47
      efficiency: 0.4
      win: 0.67
      pick: 0.19
      fit: 0.15
  community_ordered:
  - Brawler’s Beat Stick
  - Sanguine Lash
  - Dwarven Plate
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Jotunn's Revenge
  - Runeforged Hammer
  - Dwarven Plate
  - Sanguine Lash
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Runeforged
    Hammer, The Reaper, Shield Splitter, Eye of the Storm, Berserker''s Shield, Avenging
    Blade, Erosion, Genji''s Guard, Eye of Providence, Breastplate of Valor, Yogi''s
    Necklace, Draconic Scale, Phoenix Feather, Heartseeker, Hydra''s Lament, Stone
    of Binding, Midgardian Mail, Titan''s Bane, Chandra''s Grace, The Crusher, Daybreak
    Gavel, Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s Hide.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.34
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.43
      efficiency: 0.57
      win: 0.33
      pick: 0.1
      fit: 0.55
    Dwarven Plate:
      total: 0.5
      efficiency: 0.4
      win: 0.67
      pick: 0.19
      fit: 0.34
    Sanguine Lash:
      total: 0.51
      efficiency: 0.36
      win: 0.64
      pick: 0.35
      fit: 0.51
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Brawler’s Beat Stick
  - Runeforged Hammer
  - Dwarven Plate
  - Sanguine Lash
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Jotunn's Revenge
  - Dwarven Plate
  - Sanguine Lash
  - Heartseeker
  flex_slots:
  - Avenging Blade
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, Heartseeker, Amanita Charm, Runeforged
    Hammer, Titan''s Bane, The Crusher, Stone of Binding, The Reaper, Void Shield,
    Screeching Gargoyle, Void Stone, Shield Splitter, Eye of the Storm, Avatar''s
    Parashu, Genji''s Guard, Berserker''s Shield, Breastplate of Valor, Pendulum Blade,
    Hydra''s Lament, Tekko-Kagi, Erosion, Daybreak Gavel, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Toxic Blade.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.55
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.2
    Avenging Blade:
      total: 0.44
      efficiency: 0.49
      win: 0.33
      pick: 0.14
      fit: 0.78
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.65
    Dwarven Plate:
      total: 0.48
      efficiency: 0.4
      win: 0.67
      pick: 0.19
      fit: 0.2
    Sanguine Lash:
      total: 0.5
      efficiency: 0.36
      win: 0.64
      pick: 0.35
      fit: 0.42
    Heartseeker:
      total: 0.43
      efficiency: 0.47
      win: 0.33
      pick: 0.0
      fit: 0.81
  community_ordered:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Dwarven Plate
  - Sanguine Lash
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Riptalon
  - Sanguine Lash
  - Dwarven Plate
  flex_slots:
  - Golden Blade
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Jotunn''s Revenge, Golden Blade, Amanita Charm,
    Riptalon, Tyrfing, Silverbranch Bow, Toxic Blade, Runeforged Hammer, Lernaean
    Bow, Genji''s Guard, Breastplate of Valor, Pharaoh''s Curse, Tekko-Kagi, The Reaper,
    Shogun''s Ofuda, Shield Splitter, Avenging Blade, Heartseeker, Eye of the Storm,
    Hydra''s Lament, Daybreak Gavel, Dominance, Erosion, Shield of the Phoenix, Eye
    of Providence, Qin''s Blade.'
  slot_scores:
    Golden Blade:
      total: 0.42
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.62
    Brawler’s Beat Stick:
      total: 0.54
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.15
    Berserker's Shield:
      total: 0.45
      efficiency: 0.68
      win: 0.33
      pick: 0.0
      fit: 0.43
    Riptalon:
      total: 0.41
      efficiency: 0.51
      win: 0.33
      pick: 0.0
      fit: 0.58
    Sanguine Lash:
      total: 0.5
      efficiency: 0.4
      win: 0.64
      pick: 0.35
      fit: 0.37
    Dwarven Plate:
      total: 0.47
      efficiency: 0.4
      win: 0.67
      pick: 0.19
      fit: 0.15
  community_ordered:
  - Brawler’s Beat Stick
  - Sanguine Lash
  - Dwarven Plate
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Sanguine Lash
  - Dwarven Plate
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching
    Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight, Gladiator''s Shield,
    Eye of Erebus, Pendulum Blade, Shield Splitter, Prophetic Cloak, Chandra''s Grace,
    Avenging Blade, Heartseeker, Eye of the Storm, Daybreak Gavel, Erosion, Eye of
    Providence, Draconic Scale, Midgardian Mail, Stone of Binding, Titan''s Bane,
    The Crusher.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.54
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.17
    Genji's Guard:
      total: 0.44
      efficiency: 0.66
      win: 0.33
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.59
    Sanguine Lash:
      total: 0.48
      efficiency: 0.36
      win: 0.64
      pick: 0.35
      fit: 0.29
    Dwarven Plate:
      total: 0.48
      efficiency: 0.4
      win: 0.67
      pick: 0.19
      fit: 0.17
  community_ordered:
  - Brawler’s Beat Stick
  - Sanguine Lash
  - Dwarven Plate
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Eye of the Storm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Amanita Charm, Runeforged Hammer,
    Eye of the Storm, Shield Splitter, Heartseeker, Avenging Blade, Berserker''s Shield,
    Genji''s Guard, Hydra''s Lament, Breastplate of Valor, Titan''s Bane, The Crusher,
    Erosion, The Reaper, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Golden Blade, Daybreak Gavel, Midgardian Mail, Avatar''s Parashu, Stone of Binding,
    Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.33
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.29
      efficiency: 0.56
      win: 0.0
      pick: 0.17
      fit: 0.56
    Shield Splitter:
      total: 0.42
      efficiency: 0.55
      win: 0.33
      pick: 0.0
      fit: 0.54
    Eye of the Storm:
      total: 0.42
      efficiency: 0.52
      win: 0.33
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.57
      win: 0.33
      pick: 0.1
      fit: 0.59
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.33
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Kinetic Cuirass
  - Runeforged Hammer
  starter: *id001
---
