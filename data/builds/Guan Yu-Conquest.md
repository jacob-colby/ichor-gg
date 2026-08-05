---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.73
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.65
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.65
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.53
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.7
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.28
    win_rate: 0.62
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.22
      win_rate: 0.58
    - name: Prophetic Cloak
      pick_rate: 0.05
      win_rate: 0.86
  - name: Dwarven Plate
    pick_rate: 0.08
    win_rate: 0.73
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.52
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.89
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.88
    alternates:
    - name: Amanita Charm
      pick_rate: 0.06
      win_rate: 1.0
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.83
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Legionnaire Armor
      pick_rate: 0.07
      win_rate: 0.4
    - name: Adroit Ring
      pick_rate: 0.05
      win_rate: 0.25
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-08-01'
  god_win_rate: 0.5761589403973509
  god_matches_won: 87
  god_matches_played: 151
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Yogi's Necklace
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Yogi''s Necklace, Berserker''s Shield, Kinetic Cuirass,
    Eye of Providence, Jotunn''s Revenge, Runeforged Hammer, Hydra''s Lament, The
    Crusher, Freya''s Tears, Oni Hunter''s Garb, Shield Splitter, Shield of the Phoenix,
    Pharaoh''s Curse, Eye of the Storm, Golden Blade, Erosion, Spectral Armor, Lernaean
    Bow, Draconic Scale, Avenging Blade, Shogun''s Ofuda, Leviathan''s Hide, Midgardian
    Mail, Damaru, Hide of the Nemean Lion.'
  slot_scores:
    Yogi's Necklace:
      total: 0.55
      efficiency: 0.65
      win: 0.65
      pick: 0.11
      fit: 0.16
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.28
      fit: 0.32
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.7
      pick: 0.25
      fit: 0.32
    Prophetic Cloak:
      total: 0.62
      efficiency: 0.44
      win: 0.86
      pick: 0.05
      fit: 0.49
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.23
      fit: 0.5
    Amanita Charm:
      total: 0.76
      efficiency: 0.67
      win: 1.0
      pick: 0.06
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Yogi's Necklace
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Yogi''s Necklace, Shield of the Phoenix, Berserker''s
    Shield, Kinetic Cuirass, Eye of Providence, Jotunn''s Revenge, Runeforged Hammer,
    Chandra''s Grace, Oni Hunter''s Garb, Hydra''s Lament, The Crusher, Freya''s Tears,
    The Reaper, Golden Blade, Pharaoh''s Curse, Eye of the Storm, Shield Splitter,
    Phoenix Feather, Erosion, Riptalon, Spectral Armor, Avenging Blade, Lernaean Bow,
    Draconic Scale, Shogun''s Ofuda.'
  slot_scores:
    Yogi's Necklace:
      total: 0.55
      efficiency: 0.65
      win: 0.65
      pick: 0.11
      fit: 0.19
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.28
      fit: 0.3
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.7
      pick: 0.25
      fit: 0.3
    Prophetic Cloak:
      total: 0.61
      efficiency: 0.44
      win: 0.86
      pick: 0.05
      fit: 0.45
    Shifter's Shield:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.23
      fit: 0.5
    Amanita Charm:
      total: 0.81
      efficiency: 0.67
      win: 1.0
      pick: 0.06
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Yogi's Necklace
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, The Crusher, Berserker''s Shield,
    Avenging Blade, Kinetic Cuirass, Eye of Providence, Screeching Gargoyle, Stone
    of Binding, Hydra''s Lament, Runeforged Hammer, Oni Hunter''s Garb, Void Shield,
    Freya''s Tears, The Reaper, Void Stone, Shield of the Phoenix, Shield Splitter,
    Pharaoh''s Curse, Riptalon, Golden Blade, Eye of the Storm, Spectral Armor, Lernaean
    Bow, Heartseeker, Silverbranch Bow.'
  slot_scores:
    Yogi's Necklace:
      total: 0.54
      efficiency: 0.65
      win: 0.65
      pick: 0.11
      fit: 0.12
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.28
      fit: 0.24
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.7
      pick: 0.25
      fit: 0.24
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.44
      win: 0.86
      pick: 0.05
      fit: 0.37
    Shifter's Shield:
      total: 0.56
      efficiency: 0.56
      win: 0.65
      pick: 0.23
      fit: 0.38
    Amanita Charm:
      total: 0.74
      efficiency: 0.67
      win: 1.0
      pick: 0.06
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Prophetic Cloak
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Yogi''s Necklace, Berserker''s Shield, Kinetic Cuirass,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Jotunn''s Revenge, The Crusher,
    Oni Hunter''s Garb, Riptalon, Hydra''s Lament, Runeforged Hammer, Lernaean Bow,
    Freya''s Tears, Tyrfing, Shield of the Phoenix, Shogun''s Ofuda, Silverbranch
    Bow, Shield Splitter, Spectral Armor, Erosion, Eye of the Storm, Dominance, Draconic
    Scale, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.7
      pick: 0.25
      fit: 0.22
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.44
      win: 0.86
      pick: 0.05
      fit: 0.34
    Amanita Charm:
      total: 0.74
      efficiency: 0.67
      win: 1.0
      pick: 0.06
      fit: 0.35
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Prophetic Cloak
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Yogi's Necklace
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Prophetic Cloak, Yogi''s
    Necklace, Berserker''s Shield, Jotunn''s Revenge, Freya''s Tears, Hydra''s Lament,
    Kinetic Cuirass, Shield of the Phoenix, Eye of Providence, Oni Hunter''s Garb,
    The Crusher, Runeforged Hammer, Screeching Gargoyle, Pharaoh''s Curse, Chandra''s
    Grace, Gladiator''s Shield, Spectral Armor, Erosion, Shield Splitter, Golden Blade,
    Draconic Scale, Eye of the Storm, Arondight, Lernaean Bow, Shogun''s Ofuda.'
  slot_scores:
    Yogi's Necklace:
      total: 0.54
      efficiency: 0.65
      win: 0.65
      pick: 0.11
      fit: 0.12
    Genji's Guard:
      total: 0.61
      efficiency: 0.72
      win: 0.62
      pick: 0.28
      fit: 0.44
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.7
      pick: 0.25
      fit: 0.44
    Prophetic Cloak:
      total: 0.63
      efficiency: 0.44
      win: 0.86
      pick: 0.05
      fit: 0.58
    Shifter's Shield:
      total: 0.56
      efficiency: 0.56
      win: 0.65
      pick: 0.23
      fit: 0.4
    Amanita Charm:
      total: 0.75
      efficiency: 0.67
      win: 1.0
      pick: 0.06
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Eye of Providence, Jotunn''s Revenge, Runeforged Hammer, Hydra''s Lament, The
    Crusher, Freya''s Tears, Oni Hunter''s Garb, Shield Splitter, Shield of the Phoenix,
    Pharaoh''s Curse, Eye of the Storm, Golden Blade, Erosion, Spectral Armor, Lernaean
    Bow, Draconic Scale, Avenging Blade, Shogun''s Ofuda, Yogi''s Necklace, Leviathan''s
    Hide, Midgardian Mail, Damaru, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.28
      fit: 0.32
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.76
      efficiency: 0.67
      win: 1.0
      pick: 0.06
      fit: 0.5
  starter: *id001
---
