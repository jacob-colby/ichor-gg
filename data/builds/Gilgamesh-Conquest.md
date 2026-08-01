---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.36
  aspect_win_rate: 0.55
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.21
      win_rate: 0.58
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.55
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.42
  - name: Shogun's Ofuda
    pick_rate: 0.12
    win_rate: 0.62
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.14
      win_rate: 0.54
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.6
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.65
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.46
  - name: Kinetic Cuirass
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.83
    - name: Contagion
      pick_rate: 0.05
      win_rate: 1.0
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.71
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.4
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-08-01'
  god_win_rate: 0.547486033519553
  god_matches_won: 98
  god_matches_played: 179
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
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Runeforged Hammer
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
    this god: Jotunn''s Revenge, The Crusher, Shogun''s Ofuda, Runeforged Hammer,
    Eye of Providence, Golden Blade, Avenging Blade, Shield Splitter, The Reaper,
    Spectral Armor, Hydra''s Lament, Eye of the Storm, Amanita Charm, Tekko-Kagi,
    Tyrfing, Lernaean Bow, Pharaoh''s Curse, Erosion, Damaru, Eros'' Bow, Shield of
    the Phoenix, Chandra''s Grace, Yogi''s Necklace, Rage, Wyrmskin Hide, Genji''s
    Guard, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.44
      efficiency: 0.4
      win: 0.51
      pick: 0.22
      fit: 0.4
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.47
      efficiency: 0.32
      win: 0.71
      pick: 0.07
      fit: 0.23
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
    Shogun's Ofuda:
      total: 0.46
      efficiency: 0.33
      win: 0.62
      pick: 0.12
      fit: 0.4
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - The Reaper
  - The Crusher
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, The Reaper, Jotunn''s Revenge, The Crusher, Shield of
    the Phoenix, Eye of Providence, Chandra''s Grace, Runeforged Hammer, Shield Splitter,
    Phoenix Feather, Spectral Armor, Hydra''s Lament, Eye of the Storm, Avenging Blade,
    Golden Blade, Tyrfing, Spirit Robe, Tekko-Kagi, Erosion, Pharaoh''s Curse, Lernaean
    Bow, Bloodforge, Riptalon, Genji''s Guard, Midgardian Mail, Yogi''s Necklace,
    Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.29
    Hide of the Nemean Lion:
      total: 0.47
      efficiency: 0.32
      win: 0.71
      pick: 0.07
      fit: 0.22
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
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shogun's Ofuda:
      total: 0.45
      efficiency: 0.33
      win: 0.62
      pick: 0.12
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - The Reaper
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - The Reaper
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
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, The Reaper, Tekko-Kagi,
    Runeforged Hammer, Eye of Providence, Spectral Armor, Golden Blade, Hydra''s Lament,
    Shield Splitter, Amanita Charm, Oath-Sworn Spear, Eye of the Storm, Void Stone,
    Tyrfing, Screeching Gargoyle, Void Shield, Lernaean Bow, Heartseeker, Pharaoh''s
    Curse, Stone of Binding, Erosion, Pendulum Blade, Shield of the Phoenix, Damaru,
    Kinetic Cuirass.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.46
      efficiency: 0.32
      win: 0.71
      pick: 0.07
      fit: 0.19
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
    Shogun's Ofuda:
      total: 0.45
      efficiency: 0.33
      win: 0.62
      pick: 0.12
      fit: 0.33
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
