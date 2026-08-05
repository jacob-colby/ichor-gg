---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.4
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.56
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.22
      win_rate: 0.59
    - name: Avenging Blade
      pick_rate: 0.12
      win_rate: 0.42
  - name: Daybreak Gavel
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.46
    - name: Gladiator's Shield
      pick_rate: 0.12
      win_rate: 0.65
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.47
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.58
  - name: Dwarven Plate
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.7
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.41
  - name: Glorious Pridwen
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.7
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.5
  - name: Medal of Defense
    pick_rate: 0.05
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.64
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.71
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-08-01'
  god_win_rate: 0.5236220472440944
  god_matches_won: 133
  god_matches_played: 254
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Amanita Charm, Runeforged Hammer, Berserker''s
    Shield, Kinetic Cuirass, Eye of Providence, Oni Hunter''s Garb, Hydra''s Lament,
    Eye of the Storm, Shield Splitter, Golden Blade, The Reaper, Spectral Armor, Shield
    of the Phoenix, Yogi''s Necklace, Breastplate of Valor, Lernaean Bow, Erosion,
    Pharaoh''s Curse, Damaru, Freya''s Tears, Heartseeker, Draconic Scale, Leviathan''s
    Hide, Wyrmskin Hide, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.54
      pick: 0.16
      fit: 0.17
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.32
      fit: 0.46
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, The Crusher, Eye of Providence, Jotunn''s Revenge, The Reaper, Runeforged
    Hammer, Oni Hunter''s Garb, Eye of the Storm, Shield Splitter, Hydra''s Lament,
    Chandra''s Grace, Erosion, Riptalon, Phoenix Feather, Spectral Armor, Freya''s
    Tears, Golden Blade, Breastplate of Valor, Draconic Scale, Pharaoh''s Curse, Yogi''s
    Necklace, Leviathan''s Hide, Midgardian Mail, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.54
      pick: 0.16
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.56
      pick: 0.32
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Runeforged Hammer, The Reaper, Kinetic Cuirass, Eye of Providence, Heartseeker,
    Oni Hunter''s Garb, Avenging Blade, Hydra''s Lament, Void Shield, Stone of Binding,
    Eye of the Storm, Riptalon, Titan''s Bane, Tekko-Kagi, Void Stone, Screeching
    Gargoyle, Golden Blade, Yogi''s Necklace, Shield Splitter, Breastplate of Valor,
    Silverbranch Bow, Spectral Armor, Pendulum Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.54
      pick: 0.16
      fit: 0.13
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.56
      pick: 0.32
      fit: 0.35
    The Crusher:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Riptalon, The Crusher, Amanita Charm,
    Jotunn''s Revenge, Kinetic Cuirass, Pharaoh''s Curse, Silverbranch Bow, Lernaean
    Bow, Runeforged Hammer, Oni Hunter''s Garb, Eye of Providence, Tyrfing, Hydra''s
    Lament, Shogun''s Ofuda, Breastplate of Valor, Yogi''s Necklace, Toxic Blade,
    Dominance, Spectral Armor, The Reaper, Shield of the Phoenix, Freya''s Tears,
    Tekko-Kagi, Eros'' Bow, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.54
      pick: 0.16
      fit: 0.1
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.56
      pick: 0.32
      fit: 0.27
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Gladiator's Shield
  - Hydra's Lament
  flex_slots:
  - Breastplate of Valor
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Gladiator''s Shield, Jotunn''s Revenge,
    Hydra''s Lament, Breastplate of Valor, Shield of the Phoenix, Freya''s Tears,
    Berserker''s Shield, Amanita Charm, The Crusher, Kinetic Cuirass, Eye of Providence,
    Oni Hunter''s Garb, Runeforged Hammer, Chandra''s Grace, Screeching Gargoyle,
    Yogi''s Necklace, Arondight, Spectral Armor, Pharaoh''s Curse, Pendulum Blade,
    Eye of the Storm, Golden Blade, Erosion, Shield Splitter, Leviathan''s Hide, Prophetic
    Cloak, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.54
      pick: 0.16
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.57
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.41
      win: 0.65
      pick: 0.12
      fit: 0.67
    Hydra's Lament:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Jotunn''s Revenge, Amanita Charm, Runeforged
    Hammer, Berserker''s Shield, Kinetic Cuirass, Eye of Providence, Oni Hunter''s
    Garb, Hydra''s Lament, Eye of the Storm, Avenging Blade, Shield Splitter, Golden
    Blade, The Reaper, Spectral Armor, Shield of the Phoenix, Yogi''s Necklace, Breastplate
    of Valor, Lernaean Bow, Erosion, Pharaoh''s Curse, Damaru, Freya''s Tears, Heartseeker,
    Draconic Scale, Leviathan''s Hide, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.59
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
---
