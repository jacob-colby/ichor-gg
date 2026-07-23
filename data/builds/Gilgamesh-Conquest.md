---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.31
    win_rate: 0.58
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.18
      win_rate: 0.54
    - name: Golden Blade
      pick_rate: 0.13
      win_rate: 0.67
  - name: Berserker's Shield
    pick_rate: 0.15
    win_rate: 0.49
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.53
    - name: Golden Blade
      pick_rate: 0.09
      win_rate: 0.57
  - name: Shogun's Ofuda
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.63
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.55
  - name: Dwarven Plate
    pick_rate: 0.11
    win_rate: 0.53
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.12
      win_rate: 0.62
    - name: Berserker's Shield
      pick_rate: 0.11
      win_rate: 0.63
  - name: Kinetic Cuirass
    pick_rate: 0.05
    win_rate: 0.7
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.13
      win_rate: 0.74
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.63
  - name: Hunter's Bow
    pick_rate: 0.05
    win_rate: 0.36
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.63
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.43
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Golden Blade
  - Berserker's Shield
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Jotunn''s Revenge, The Crusher, Runeforged Hammer,
    Golden Blade, Berserker''s Shield, Eye of Providence, Shield Splitter, Avenging
    Blade, Hydra''s Lament, Spectral Armor, Eye of the Storm, Tyrfing, Amanita Charm,
    The Reaper, Tekko-Kagi, Lernaean Bow, Pharaoh''s Curse, Shogun''s Ofuda, Damaru,
    Erosion, Shield of the Phoenix, Genji''s Guard, Titan''s Bane, Rage, Eros'' Bow,
    Wyrmskin Hide, Chandra''s Grace.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.51
    Berserker's Shield:
      total: 0.44
      efficiency: 0.43
      win: 0.49
      pick: 0.15
      fit: 0.4
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.44
      win: 0.7
      pick: 0.05
      fit: 0.42
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
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
    this god: Kinetic Cuirass, Amanita Charm, The Reaper, Jotunn''s Revenge, The Crusher,
    Shield of the Phoenix, Chandra''s Grace, Eye of Providence, Runeforged Hammer,
    Shield Splitter, Phoenix Feather, Berserker''s Shield, Spectral Armor, Hydra''s
    Lament, Avenging Blade, Eye of the Storm, Golden Blade, Tyrfing, Spirit Robe,
    Erosion, Lernaean Bow, Pharaoh''s Curse, Bloodforge, Genji''s Guard, Tekko-Kagi,
    Riptalon, Damaru, Devourer''s Gauntlet.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.44
      win: 0.7
      pick: 0.05
      fit: 0.43
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - The Reaper
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Kinetic Cuirass, Jotunn''s Revenge, The Crusher, Avenging Blade,
    The Reaper, Runeforged Hammer, Tekko-Kagi, Eye of Providence, Berserker''s Shield,
    Hydra''s Lament, Shield Splitter, Spectral Armor, Golden Blade, Oath-Sworn Spear,
    Titan''s Bane, Tyrfing, Amanita Charm, Eye of the Storm, Void Stone, Screeching
    Gargoyle, Void Shield, Lernaean Bow, Stone of Binding, Pharaoh''s Curse, Heartseeker,
    Genji''s Guard, Erosion, Damaru.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.44
      win: 0.7
      pick: 0.05
      fit: 0.36
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Reaper:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.55
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
  - Demon Blade
  - Jotunn's Revenge
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
      total: 0.23
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.23
    Tyrfing:
      total: 0.24
      efficiency: 0.39
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
      total: 0.23
      efficiency: 0.22
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
