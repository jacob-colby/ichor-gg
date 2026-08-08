---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.67
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.21
    win_rate: 0.62
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.55
    - name: Yogi's Necklace
      pick_rate: 0.1
      win_rate: 0.55
  - name: Breastplate of Valor
    pick_rate: 0.27
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.58
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.54
  - name: Genji's Guard
    pick_rate: 0.3
    win_rate: 0.59
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.18
      win_rate: 0.59
    - name: Heartwood Charm
      pick_rate: 0.05
      win_rate: 0.55
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.68
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.59
    - name: Heartwood Charm
      pick_rate: 0.06
      win_rate: 0.65
  - name: Dwarven Plate
    pick_rate: 0.05
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.69
    - name: Engraved Guard
      pick_rate: 0.04
      win_rate: 0.41
  - name: Legionnaire Armor
    pick_rate: 0.05
    win_rate: 0.42
    alternates:
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.9
    - name: Adroit Ring
      pick_rate: 0.04
      win_rate: 0.6
  community_starters:
  - name: Sands of Time
    pick_rate: 0.28
    win_rate: 0.56
  - name: Pendulum of The Ages
    pick_rate: 0.14
    win_rate: 0.63
  - name: Bluestone Brooch
    pick_rate: 0.1
    win_rate: 0.68
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-08-08'
  god_win_rate: 0.581140350877193
  god_matches_won: 265
  god_matches_played: 456
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-08'
  god_matches_analyzed: 14443
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Dwarven Plate — physical protection
    swap_item: Dwarven Plate
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Eye of Providence,
    Jotunn''s Revenge, Hydra''s Lament, The Crusher, Runeforged Hammer, Freya''s Tears,
    Oni Hunter''s Garb, Yogi''s Necklace, Shield of the Phoenix, Shield Splitter,
    Pharaoh''s Curse, Eye of the Storm, Golden Blade, Erosion, Spectral Armor, Lernaean
    Bow, Draconic Scale, Avenging Blade, Shogun''s Ofuda, Leviathan''s Hide, Damaru,
    Midgardian Mail, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.3
      fit: 0.32
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.32
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.62
      pick: 0.21
      fit: 0.5
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Berserker''s Shield, Kinetic Cuirass,
    Eye of Providence, Jotunn''s Revenge, Runeforged Hammer, Yogi''s Necklace, Chandra''s
    Grace, Oni Hunter''s Garb, Hydra''s Lament, The Crusher, Freya''s Tears, The Reaper,
    Pharaoh''s Curse, Golden Blade, Eye of the Storm, Shield Splitter, Riptalon, Phoenix
    Feather, Spectral Armor, Erosion, Lernaean Bow, Avenging Blade, Draconic Scale,
    Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.3
      fit: 0.3
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.3
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.79
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.62
      pick: 0.21
      fit: 0.5
    Amanita Charm:
      total: 0.58
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - The Crusher
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Berserker''s Shield, Amanita Charm,
    Kinetic Cuirass, Avenging Blade, Eye of Providence, Yogi''s Necklace, Screeching
    Gargoyle, Stone of Binding, Hydra''s Lament, Oni Hunter''s Garb, Runeforged Hammer,
    Freya''s Tears, Void Shield, The Reaper, Shield of the Phoenix, Void Stone, Pharaoh''s
    Curse, Shield Splitter, Riptalon, Golden Blade, Spectral Armor, Lernaean Bow,
    Silverbranch Bow, Eye of the Storm.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.59
      pick: 0.3
      fit: 0.24
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.32
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.24
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.21
      fit: 0.38
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Shifter's Shield
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Golden Blade, Yogi''s
    Necklace, Eye of Providence, Pharaoh''s Curse, Jotunn''s Revenge, Oni Hunter''s
    Garb, The Crusher, Riptalon, Hydra''s Lament, Runeforged Hammer, Freya''s Tears,
    Lernaean Bow, Shield of the Phoenix, Shogun''s Ofuda, Tyrfing, Silverbranch Bow,
    Spectral Armor, Shield Splitter, Erosion, Eye of the Storm, Dominance, Draconic
    Scale, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.59
      pick: 0.3
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.22
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.21
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
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Jotunn''s Revenge,
    Freya''s Tears, Amanita Charm, Hydra''s Lament, Kinetic Cuirass, Shield of the
    Phoenix, Eye of Providence, Yogi''s Necklace, Oni Hunter''s Garb, The Crusher,
    Runeforged Hammer, Screeching Gargoyle, Pharaoh''s Curse, Chandra''s Grace, Spectral
    Armor, Gladiator''s Shield, Erosion, Shield Splitter, Golden Blade, Draconic Scale,
    Prophetic Cloak, Arondight, Eye of the Storm, Shogun''s Ofuda, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.72
      win: 0.59
      pick: 0.3
      fit: 0.44
    Berserker's Shield:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.27
      fit: 0.44
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.21
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
    Eye of Providence, Jotunn''s Revenge, Hydra''s Lament, The Crusher, Runeforged
    Hammer, Freya''s Tears, Oni Hunter''s Garb, Shield of the Phoenix, Shield Splitter,
    Pharaoh''s Curse, Eye of the Storm, Golden Blade, Erosion, Spectral Armor, Lernaean
    Bow, Draconic Scale, Avenging Blade, Yogi''s Necklace, Shogun''s Ofuda, Leviathan''s
    Hide, Damaru, Midgardian Mail, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.58
      efficiency: 0.72
      win: 0.59
      pick: 0.3
      fit: 0.32
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
---
