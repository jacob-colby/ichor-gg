---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.61
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.52
    alternates:
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.57
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.38
  - name: Berserker's Shield
    pick_rate: 0.35
    win_rate: 0.52
    alternates:
    - name: Golden Blade
      pick_rate: 0.1
      win_rate: 0.42
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.21
    win_rate: 0.48
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.21
      win_rate: 0.36
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.47
  - name: Dwarven Plate
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.5
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.4
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.58
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.57
  - name: Veve Charm
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 1.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.4
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-01'
  god_win_rate: 0.5083333333333333
  god_matches_won: 61
  god_matches_played: 120
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
  - Golden Blade
  - Eye of Providence
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  flex_slots:
  - Golden Blade
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Jotunn''s Revenge, Golden Blade, Eye of Providence,
    Shield Splitter, Avenging Blade, Hydra''s Lament, Eye of the Storm, Spectral Armor,
    Amanita Charm, The Crusher, Lernaean Bow, Tyrfing, Pharaoh''s Curse, Damaru, Erosion,
    Eros'' Bow, Shield of the Phoenix, Shogun''s Ofuda, Chandra''s Grace, Wyrmskin
    Hide, Genji''s Guard, Yogi''s Necklace, Rage, Midgardian Mail, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.35
    Berserker's Shield:
      total: 0.46
      efficiency: 0.41
      win: 0.52
      pick: 0.35
      fit: 0.45
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.48
      pick: 0.21
      fit: 0.45
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Eye of Providence, Chandra''s
    Grace, Runeforged Hammer, Jotunn''s Revenge, Shield Splitter, Phoenix Feather,
    Spectral Armor, Golden Blade, Eye of the Storm, Avenging Blade, Hydra''s Lament,
    Pharaoh''s Curse, The Crusher, Erosion, The Reaper, Lernaean Bow, Tyrfing, Spirit
    Robe, Damaru, Riptalon, Shogun''s Ofuda, Bloodforge, Genji''s Guard, Eros'' Bow.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.46
      efficiency: 0.41
      win: 0.52
      pick: 0.35
      fit: 0.47
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.48
      pick: 0.21
      fit: 0.54
    Shield of the Phoenix:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.63
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Avenging Blade, The Crusher, Runeforged Hammer,
    Eye of Providence, Hydra''s Lament, Heartseeker, Spectral Armor, Golden Blade,
    Titan''s Bane, Shield Splitter, Amanita Charm, Oath-Sworn Spear, Eye of the Storm,
    Screeching Gargoyle, Void Stone, Pendulum Blade, Lernaean Bow, Tyrfing, Void Shield,
    The Reaper, Damaru, Pharaoh''s Curse, Stone of Binding, Riptalon, Tekko-Kagi.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.44
      efficiency: 0.41
      win: 0.52
      pick: 0.35
      fit: 0.33
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.43
      efficiency: 0.44
      win: 0.48
      pick: 0.21
      fit: 0.36
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
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
  - Golden Blade
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  flex_slots:
  - Eye of Providence
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Runeforged Hammer, Jotunn''s Revenge, Golden Blade, Eye
    of Providence, Shield Splitter, Avenging Blade, Hydra''s Lament, Eye of the Storm,
    Spectral Armor, Amanita Charm, The Crusher, Lernaean Bow, Tyrfing, Pharaoh''s
    Curse, Damaru, Erosion, Eros'' Bow, Shield of the Phoenix, Shogun''s Ofuda, Chandra''s
    Grace, Wyrmskin Hide, Genji''s Guard, Yogi''s Necklace, Rage, Midgardian Mail,
    Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.3
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.48
      pick: 0.21
      fit: 0.45
    Shield Splitter:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.41
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
---
