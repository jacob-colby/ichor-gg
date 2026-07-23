---
type: smite-build
god: Odin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.27
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.25
      win_rate: 0.59
    - name: Runeforged Hammer
      pick_rate: 0.09
      win_rate: 0.64
  - name: Shifter's Shield
    pick_rate: 0.29
    win_rate: 0.6
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.19
      win_rate: 0.68
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.65
  - name: Genji's Guard
    pick_rate: 0.26
    win_rate: 0.64
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.2
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.53
  - name: Dwarven Plate
    pick_rate: 0.15
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.59
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.64
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.53
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.15
      win_rate: 0.81
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.64
  - name: Glorious Pridwen
    pick_rate: 0.04
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.31
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.88
  source_url: https://smitebrain.com/gods/odin/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Shield Splitter, The Crusher, Amanita
    Charm, Runeforged Hammer, Eye of the Storm, Spectral Armor, Hydra''s Lament, Erosion,
    Avenging Blade, Shield of the Phoenix, The Reaper, Berserker''s Shield, Wyrmskin
    Hide, Breastplate of Valor, Golden Blade, Midgardian Mail, Gladiator''s Shield,
    Chandra''s Grace, Shroud of Vengeance, Mantle Of Discord, Leviathan''s Hide, Pharaoh''s
    Curse, Phoenix Feather.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.51
      efficiency: 0.46
      win: 0.64
      pick: 0.26
      fit: 0.29
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.27
      fit: 0.46
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.64
    Shield Splitter:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shifter's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.6
      pick: 0.29
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Glorious Pridwen
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
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
    this god: Amanita Charm, Glorious Pridwen, The Reaper, Shield of the Phoenix,
    The Crusher, Kinetic Cuirass, Chandra''s Grace, Eye of Providence, Shield Splitter,
    Runeforged Hammer, Phoenix Feather, Hydra''s Lament, Spectral Armor, Eye of the
    Storm, Avenging Blade, Spirit Robe, Erosion, Berserker''s Shield, Bloodforge,
    Golden Blade, Breastplate of Valor, Wyrmskin Hide, Midgardian Mail, Tyrfing, Titan''s
    Bane, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.64
      pick: 0.26
      fit: 0.23
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
      win: 0.53
      pick: 0.27
      fit: 0.41
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.51
    Glorious Pridwen:
      total: 0.48
      efficiency: 0.23
      win: 0.67
      pick: 0.04
      fit: 0.67
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Eye of Providence
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, Kinetic Cuirass, Eye of Providence,
    Shield Splitter, The Reaper, Amanita Charm, Runeforged Hammer, Screeching Gargoyle,
    Spectral Armor, Hydra''s Lament, Eye of the Storm, Void Stone, Stone of Binding,
    Void Shield, Erosion, Titan''s Bane, Oath-Sworn Spear, Shield of the Phoenix,
    Tekko-Kagi, Berserker''s Shield, Heartseeker, Pendulum Blade, Breastplate of Valor,
    Chandra''s Grace, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.69
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Genji's Guard:
      total: 0.5
      efficiency: 0.46
      win: 0.64
      pick: 0.26
      fit: 0.24
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.27
      fit: 0.56
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.58
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
      win: 0.53
      pick: 0.27
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
