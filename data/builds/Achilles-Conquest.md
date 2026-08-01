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
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Eye of the Storm
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Eye of Providence
  - Eye of the Storm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, Runeforged Hammer, Kinetic Cuirass,
    Eye of Providence, Eye of the Storm, Shield Splitter, Avenging Blade, The Reaper,
    Amanita Charm, Spectral Armor, Hydra''s Lament, Golden Blade, Erosion, Wyrmskin
    Hide, Tekko-Kagi, Shield of the Phoenix, Berserker''s Shield, Heartseeker, Tyrfing,
    Midgardian Mail, Chandra''s Grace, Lernaean Bow, Yogi''s Necklace, Pendulum Blade,
    Pharaoh''s Curse, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.46
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Eye of the Storm:
      total: 0.46
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.59
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
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Jotunn''s Revenge, The Crusher, Kinetic Cuirass,
    Shield of the Phoenix, Eye of Providence, Shield Splitter, Runeforged Hammer,
    Chandra''s Grace, Phoenix Feather, Spectral Armor, Eye of the Storm, Avenging
    Blade, Hydra''s Lament, Erosion, Spirit Robe, Golden Blade, Bloodforge, Wyrmskin
    Hide, Berserker''s Shield, Midgardian Mail, Tekko-Kagi, Tyrfing, Pharaoh''s Curse,
    Leviathan''s Hide, Yogi''s Necklace.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.49
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.74
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
  - Runeforged Hammer
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, The Reaper, Runeforged
    Hammer, Kinetic Cuirass, Eye of Providence, Tekko-Kagi, Shield Splitter, Eye of
    the Storm, Spectral Armor, Amanita Charm, Hydra''s Lament, Heartseeker, Oath-Sworn
    Spear, Void Stone, Pendulum Blade, Void Shield, Screeching Gargoyle, Golden Blade,
    Titan''s Bane, Erosion, Stone of Binding, Shield of the Phoenix, Wyrmskin Hide,
    Chandra''s Grace, Tyrfing, Berserker''s Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.78
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.65
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.71
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
      total: 0.23
      efficiency: 0.55
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
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.66
    Damaru:
      total: 0.23
      efficiency: 0.37
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
