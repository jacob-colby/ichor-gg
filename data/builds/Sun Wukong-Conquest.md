---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.51
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.5
    win_rate: 0.52
    alternates:
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.51
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.52
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.42
  - name: Gladiator's Shield
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.55
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.43
  - name: Dwarven Plate
    pick_rate: 0.17
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.49
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.49
  - name: Glorious Pridwen
    pick_rate: 0.05
    win_rate: 0.68
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.15
      win_rate: 0.48
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.53
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.69
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.64
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-07-25'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
  god_win_rate: 0.5101694915254237
  god_matches_won: 301
  god_matches_played: 590
  god_division: obsidian
  god_window_start: '2026-07-14'
  god_window_end: '2026-07-27'
  god_matches_analyzed: 17172
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - The Crusher
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Runeforged Hammer, Kinetic Cuirass, The Crusher,
    Eye of Providence, Eye of the Storm, Shield Splitter, Avenging Blade, Golden Blade,
    Amanita Charm, Spectral Armor, Berserker''s Shield, Hydra''s Lament, Tyrfing,
    Erosion, Wyrmskin Hide, Lernaean Bow, Pharaoh''s Curse, The Reaper, Shield of
    the Phoenix, Tekko-Kagi, Chandra''s Grace, Midgardian Mail, Shogun''s Ofuda, Yogi''s
    Necklace, Eros'' Bow, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Gladiator's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.63
      pick: 0.17
      fit: 0.49
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Glorious Pridwen
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, The Reaper, Jotunn''s
    Revenge, Eye of Providence, Shield Splitter, Runeforged Hammer, Chandra''s Grace,
    The Crusher, Phoenix Feather, Spectral Armor, Eye of the Storm, Avenging Blade,
    Berserker''s Shield, Hydra''s Lament, Erosion, Golden Blade, Spirit Robe, Pharaoh''s
    Curse, Tyrfing, Bloodforge, Lernaean Bow, Wyrmskin Hide, Midgardian Mail, Leviathan''s
    Hide, Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Gladiator's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.63
      pick: 0.17
      fit: 0.43
    Glorious Pridwen:
      total: 0.48
      efficiency: 0.21
      win: 0.68
      pick: 0.05
      fit: 0.63
    Amanita Charm:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.75
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Gladiator's Shield
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Gladiator's Shield
  - Runeforged Hammer
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, The Reaper, Runeforged
    Hammer, Kinetic Cuirass, Tekko-Kagi, Eye of Providence, Titan''s Bane, Spectral
    Armor, Shield Splitter, Eye of the Storm, Hydra''s Lament, Amanita Charm, Golden
    Blade, Oath-Sworn Spear, Void Stone, Berserker''s Shield, Void Shield, Screeching
    Gargoyle, Heartseeker, Tyrfing, Erosion, Lernaean Bow, Pendulum Blade, Stone of
    Binding, Pharaoh''s Curse.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.59
    Gladiator's Shield:
      total: 0.45
      efficiency: 0.3
      win: 0.63
      pick: 0.17
      fit: 0.37
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Reaper:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Tyrfing
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Jotunn's Revenge
  - Demon Blade
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
    Lernaean Bow:
      total: 0.23
      efficiency: 0.36
      win: 0.5
      pick: 0.0
      fit: 0.67
    Jotunn's Revenge:
      total: 0.22
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.23
    Tyrfing:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.67
    Death Metal:
      total: 0.25
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.38
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
---
