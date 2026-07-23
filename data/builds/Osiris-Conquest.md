---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.39
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.57
    win_rate: 0.47
    alternates:
    - name: Golden Blade
      pick_rate: 0.15
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.06
      win_rate: 0.6
  - name: Berserker's Shield
    pick_rate: 0.3
    win_rate: 0.46
    alternates:
    - name: Golden Blade
      pick_rate: 0.15
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.36
  - name: Dwarven Plate
    pick_rate: 0.14
    win_rate: 0.39
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.2
      win_rate: 0.51
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.53
  - name: Shogun's Ofuda
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.21
      win_rate: 0.45
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.53
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.55
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.16
      win_rate: 0.53
    - name: Shogun's Ofuda
      pick_rate: 0.07
      win_rate: 0.6
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.55
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.65
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.18
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Golden Blade
  - Shogun's Ofuda
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
    this god: Jotunn''s Revenge, Runeforged Hammer, The Crusher, Kinetic Cuirass,
    Golden Blade, Shogun''s Ofuda, Eye of Providence, Shield Splitter, Avenging Blade,
    Eye of the Storm, Tyrfing, Hydra''s Lament, Spectral Armor, Amanita Charm, Lernaean
    Bow, Pharaoh''s Curse, The Reaper, Tekko-Kagi, Damaru, Erosion, Shield of the
    Phoenix, Wyrmskin Hide, Rage, Eros'' Bow, Genji''s Guard, Chandra''s Grace, Yogi''s
    Necklace.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.57
    Jotunn's Revenge:
      total: 0.46
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.3
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
      fit: 0.47
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.37
    Shogun's Ofuda:
      total: 0.44
      efficiency: 0.33
      win: 0.57
      pick: 0.09
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
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - The Crusher
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
    this god: Amanita Charm, The Reaper, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Eye of Providence, Chandra''s Grace, The Crusher, Runeforged
    Hammer, Shield Splitter, Phoenix Feather, Shogun''s Ofuda, Spectral Armor, Eye
    of the Storm, Avenging Blade, Hydra''s Lament, Golden Blade, Tyrfing, Spirit Robe,
    Erosion, Pharaoh''s Curse, Lernaean Bow, Bloodforge, Genji''s Guard, Damaru, Tekko-Kagi,
    Wyrmskin Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.23
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.46
    The Reaper:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.5
    The Crusher:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    Hammer, Tekko-Kagi, Kinetic Cuirass, Eye of Providence, Hydra''s Lament, Shield
    Splitter, Spectral Armor, Golden Blade, Oath-Sworn Spear, Titan''s Bane, Tyrfing,
    Amanita Charm, Eye of the Storm, Void Stone, Screeching Gargoyle, Void Shield,
    Lernaean Bow, Stone of Binding, Pharaoh''s Curse, Heartseeker, Genji''s Guard,
    Erosion, Damaru.'
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
    Tekko-Kagi:
      total: 0.44
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.6
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
