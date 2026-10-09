---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.57
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.29
    win_rate: 0.39
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.23
      win_rate: 0.33
    - name: Avenging Blade
      pick_rate: 0.13
      win_rate: 0.4
  - name: Sanguine Lash
    pick_rate: 0.2
    win_rate: 0.44
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.45
    - name: Dagger of Frenzy
      pick_rate: 0.09
      win_rate: 0.57
  - name: Shifter's Shield
    pick_rate: 0.12
    win_rate: 0.11
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.12
      win_rate: 0.67
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.25
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.45
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.0
  - name: Hussar's Wings
    pick_rate: 0.06
    win_rate: 0.25
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.6
    - name: Sanguine Lash
      pick_rate: 0.06
      win_rate: 0.75
  - name: Medal of Defense
    pick_rate: 0.1
    win_rate: 0.0
    alternates:
    - name: Xibalban Effigy
      pick_rate: 0.07
      win_rate: 0.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.33
  - name: Hunter's Cowl
    pick_rate: 0.18
    win_rate: 0.71
  - name: Sundering Axe
    pick_rate: 0.15
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-10-09'
  god_win_rate: 0.3875
  god_matches_won: 31
  god_matches_played: 80
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-09'
  god_matches_analyzed: 2961
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Breastplate of Valor, Amanita Charm, Runeforged Hammer,
    Eye of the Storm, Shield Splitter, Avenging Blade, Heartseeker, Berserker''s Shield,
    Genji''s Guard, Hydra''s Lament, Titan''s Bane, The Crusher, Erosion, The Reaper,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Golden Blade, Daybreak
    Gavel, Midgardian Mail, Avatar''s Parashu, Stone of Binding, Leviathan''s Hide,
    Void Shield, Pendulum Blade, Kinetic Cuirass.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.5
      efficiency: 0.42
      win: 0.67
      pick: 0.19
      fit: 0.26
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.17
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.39
      pick: 0.0
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.22
      fit: 0.33
    Runeforged Hammer:
      total: 0.46
      efficiency: 0.57
      win: 0.39
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.39
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Hide of the Nemean Lion
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
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Breastplate of Valor, Amanita Charm, Genji''s Guard, Hydra''s Lament,
    Runeforged Hammer, Heartseeker, Avenging Blade, Shield Splitter, Eye of the Storm,
    Berserker''s Shield, Titan''s Bane, The Crusher, Shield of the Phoenix, Transcendence,
    Daybreak Gavel, The Reaper, Arondight, Screeching Gargoyle, Erosion, Eye of Providence,
    Oni Hunter''s Garb, Stone of Binding, Draconic Scale, Pendulum Blade, Midgardian
    Mail, Golden Blade, Kinetic Cuirass.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.67
      pick: 0.19
      fit: 0.15
    Genji's Guard:
      total: 0.44
      efficiency: 0.66
      win: 0.39
      pick: 0.0
      fit: 0.25
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.25
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.39
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.22
      fit: 0.19
    Amanita Charm:
      total: 0.44
      efficiency: 0.65
      win: 0.39
      pick: 0.0
      fit: 0.27
  community_ordered:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Breastplate of Valor, Shield of the
    Phoenix, Runeforged Hammer, The Reaper, Shield Splitter, Eye of the Storm, Berserker''s
    Shield, Avenging Blade, Erosion, Genji''s Guard, Eye of Providence, Yogi''s Necklace,
    Draconic Scale, Phoenix Feather, Heartseeker, Hydra''s Lament, Stone of Binding,
    Midgardian Mail, Titan''s Bane, Chandra''s Grace, The Crusher, Daybreak Gavel,
    Magi''s Cloak, Leviathan''s Hide, Kinetic Cuirass.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.51
      efficiency: 0.42
      win: 0.67
      pick: 0.19
      fit: 0.34
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.21
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.72
      win: 0.39
      pick: 0.0
      fit: 0.45
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.53
      win: 0.39
      pick: 0.0
      fit: 0.72
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.39
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Hide of the Nemean Lion
  flex_slots:
  - Avenging Blade
  - Transcendence
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
    for this god: Jotunn''s Revenge, Breastplate of Valor, Avenging Blade, Heartseeker,
    Amanita Charm, Titan''s Bane, The Crusher, Runeforged Hammer, Stone of Binding,
    The Reaper, Void Shield, Screeching Gargoyle, Void Stone, Shield Splitter, Eye
    of the Storm, Avatar''s Parashu, Genji''s Guard, Berserker''s Shield, Pendulum
    Blade, Hydra''s Lament, Tekko-Kagi, Erosion, Daybreak Gavel, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Toxic Blade, Kinetic Cuirass.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.49
      efficiency: 0.42
      win: 0.67
      pick: 0.19
      fit: 0.2
    Avenging Blade:
      total: 0.48
      efficiency: 0.49
      win: 0.4
      pick: 0.13
      fit: 0.78
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.13
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.39
      pick: 0.0
      fit: 0.65
    Transcendence:
      total: 0.39
      efficiency: 0.53
      win: 0.39
      pick: 0.0
      fit: 0.22
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.22
      fit: 0.25
  community_ordered:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Breastplate of Valor
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Berserker's Shield
  - Breastplate of Valor
  - Dagger of Frenzy
  - Hide of the Nemean Lion
  flex_slots:
  - Golden Blade
  - Dagger of Frenzy
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Breastplate of Valor, Jotunn''s Revenge, Golden
    Blade, Amanita Charm, Riptalon, Tyrfing, Silverbranch Bow, Toxic Blade, Runeforged
    Hammer, Lernaean Bow, Genji''s Guard, Pharaoh''s Curse, Tekko-Kagi, The Reaper,
    Shogun''s Ofuda, Avenging Blade, Shield Splitter, Heartseeker, Eye of the Storm,
    Hydra''s Lament, Daybreak Gavel, Dominance, Erosion, Shield of the Phoenix, Eye
    of Providence, Qin''s Blade, Kinetic Cuirass.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.52
      win: 0.39
      pick: 0.0
      fit: 0.62
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.67
      pick: 0.19
      fit: 0.15
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.39
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.48
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.1
    Dagger of Frenzy:
      total: 0.45
      efficiency: 0.37
      win: 0.57
      pick: 0.12
      fit: 0.38
    Hide of the Nemean Lion:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.22
      fit: 0.2
  community_ordered:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Dagger of Frenzy
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Jotunn''s Revenge,
    Genji''s Guard, Amanita Charm, Hydra''s Lament, Shield of the Phoenix, Screeching
    Gargoyle, Runeforged Hammer, Berserker''s Shield, Arondight, Gladiator''s Shield,
    Eye of Erebus, Pendulum Blade, Avenging Blade, Shield Splitter, Prophetic Cloak,
    Chandra''s Grace, Heartseeker, Eye of the Storm, Daybreak Gavel, Erosion, Eye
    of Providence, Draconic Scale, Midgardian Mail, Stone of Binding, Titan''s Bane,
    The Crusher, Kinetic Cuirass.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.48
      efficiency: 0.42
      win: 0.67
      pick: 0.19
      fit: 0.17
    Genji's Guard:
      total: 0.47
      efficiency: 0.66
      win: 0.39
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.12
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.39
      pick: 0.0
      fit: 0.59
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.22
      fit: 0.22
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.39
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Brawler’s Beat Stick
  - Breastplate of Valor
  - Hide of the Nemean Lion
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
    Kinetic Cuirass, Eye of the Storm, Shield Splitter, Heartseeker, Avenging Blade,
    Berserker''s Shield, Genji''s Guard, Hydra''s Lament, Breastplate of Valor, Titan''s
    Bane, The Crusher, Erosion, The Reaper, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Golden Blade, Daybreak Gavel, Midgardian Mail, Avatar''s Parashu,
    Stone of Binding, Leviathan''s Hide, Void Shield, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.39
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.29
      efficiency: 0.56
      win: 0.0
      pick: 0.13
      fit: 0.56
    Shield Splitter:
      total: 0.45
      efficiency: 0.55
      win: 0.39
      pick: 0.0
      fit: 0.54
    Eye of the Storm:
      total: 0.45
      efficiency: 0.52
      win: 0.39
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.46
      efficiency: 0.57
      win: 0.39
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.39
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Kinetic Cuirass
  starter: *id001
---
