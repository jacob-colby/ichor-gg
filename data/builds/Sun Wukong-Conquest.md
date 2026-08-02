---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.59
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.35
    win_rate: 0.55
    alternates:
    - name: Mystical Mail
      pick_rate: 0.14
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.1
      win_rate: 0.81
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.47
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.86
  - name: Soul Gem
    pick_rate: 0.08
    win_rate: 0.77
    alternates:
    - name: Genji's Guard
      pick_rate: 0.21
      win_rate: 0.56
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.58
  - name: Sundering Echo
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.12
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.5
  - name: Draconic Scale
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.6
    - name: Spirit Robe
      pick_rate: 0.06
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Oracle Staff
      pick_rate: 0.04
      win_rate: 1.0
    - name: Dwarven Plate
      pick_rate: 0.04
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-01'
  god_win_rate: 0.5892857142857143
  god_matches_won: 99
  god_matches_played: 168
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
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Runeforged Hammer
  flex_slots:
  - Eye of the Storm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Jotunn''s Revenge, Kinetic Cuirass, Eye of Providence,
    Eye of the Storm, Shield Splitter, Avenging Blade, Golden Blade, Amanita Charm,
    Hydra''s Lament, Spectral Armor, The Crusher, Berserker''s Shield, Erosion, Lernaean
    Bow, Tyrfing, Pharaoh''s Curse, Genji''s Guard, Wyrmskin Hide, Shield of the Phoenix,
    Chandra''s Grace, Midgardian Mail, Shogun''s Ofuda, Yogi''s Necklace, Damaru,
    Heartseeker, Eros'' Bow, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.55
    Eye of the Storm:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.63
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield Splitter
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Eye of Providence,
    Runeforged Hammer, Shield Splitter, Chandra''s Grace, Eye of the Storm, Phoenix
    Feather, Jotunn''s Revenge, Spectral Armor, Avenging Blade, Erosion, Golden Blade,
    Berserker''s Shield, Hydra''s Lament, The Crusher, Pharaoh''s Curse, Genji''s
    Guard, The Reaper, Spirit Robe, Wyrmskin Hide, Midgardian Mail, Lernaean Bow,
    Tyrfing, Bloodforge, Shogun''s Ofuda, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shield of the Phoenix:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.73
    Runeforged Hammer:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.51
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.87
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Heartseeker
  flex_slots:
  - Kinetic Cuirass
  - Heartseeker
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, The Crusher, Runeforged Hammer,
    Kinetic Cuirass, Heartseeker, Eye of Providence, Titan''s Bane, Hydra''s Lament,
    Shield Splitter, Spectral Armor, Pendulum Blade, Amanita Charm, Eye of the Storm,
    The Reaper, Golden Blade, Void Stone, Oath-Sworn Spear, Screeching Gargoyle, Void
    Shield, Berserker''s Shield, Lernaean Bow, Tyrfing, Tekko-Kagi, Stone of Binding,
    Erosion, Pharaoh''s Curse, Shield of the Phoenix.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.59
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Heartseeker:
      total: 0.44
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Demon Blade
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: For fun — deliberately fights this god's kit (Crit / attack-speed party
    build). Scored on gold-value + flavor fit only; not meta-checked.
  slot_scores:
    Golden Blade:
      total: 0.22
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.24
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Eye of the Storm
  - Runeforged Hammer
  flex_slots:
  - Eye of the Storm
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Runeforged Hammer, Jotunn''s Revenge, Kinetic Cuirass,
    Eye of Providence, Eye of the Storm, Shield Splitter, Avenging Blade, Golden Blade,
    Amanita Charm, Hydra''s Lament, Spectral Armor, The Crusher, Berserker''s Shield,
    Erosion, Lernaean Bow, Tyrfing, Pharaoh''s Curse, Wyrmskin Hide, Shield of the
    Phoenix, Chandra''s Grace, Midgardian Mail, Shogun''s Ofuda, Yogi''s Necklace,
    Genji''s Guard, Damaru, Heartseeker, Eros'' Bow, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.55
    Eye of the Storm:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.63
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
---
