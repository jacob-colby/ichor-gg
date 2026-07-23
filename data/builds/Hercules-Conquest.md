---
type: smite-build
god: Hercules
mode: Conquest
builds:
- source: community
  aspect: Aspect of Preservation
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.43
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.41
    win_rate: 0.53
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.17
      win_rate: 0.54
    - name: Jotunn's Revenge
      pick_rate: 0.1
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.31
    win_rate: 0.56
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.26
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.26
      win_rate: 0.46
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.58
  - name: Dwarven Plate
    pick_rate: 0.24
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.53
  - name: Glorious Pridwen
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.55
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.67
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Shield Splitter,
    Jotunn''s Revenge, Spectral Armor, Erosion, Eye of the Storm, Runeforged Hammer,
    Shield of the Phoenix, The Crusher, Hydra''s Lament, Berserker''s Shield, Avenging
    Blade, Gladiator''s Shield, Draconic Scale, Midgardian Mail, Shroud of Vengeance,
    Wyrmskin Hide, Mantle Of Discord, Prophetic Cloak, Chandra''s Grace, Freya''s
    Tears, Leviathan''s Hide, Pharaoh''s Curse.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.56
      pick: 0.31
      fit: 0.36
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.42
      win: 0.56
      pick: 0.25
      fit: 0.36
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.77
    Shifter's Shield:
      total: 0.45
      efficiency: 0.3
      win: 0.53
      pick: 0.41
      fit: 0.67
    Amanita Charm:
      total: 0.43
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Glorious Pridwen — physical protection
    swap_item: Glorious Pridwen
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Eye of Providence,
    Chandra''s Grace, Jotunn''s Revenge, Glorious Pridwen, Phoenix Feather, The Reaper,
    Shield Splitter, Spectral Armor, Runeforged Hammer, The Crusher, Eye of the Storm,
    Erosion, Hydra''s Lament, Spirit Robe, Avenging Blade, Berserker''s Shield, Gladiator''s
    Shield, Midgardian Mail, Wyrmskin Hide, Leviathan''s Hide, Pharaoh''s Curse, Golden
    Blade, Bloodforge.'
  slot_scores:
    Genji's Guard:
      total: 0.45
      efficiency: 0.46
      win: 0.56
      pick: 0.31
      fit: 0.28
    Breastplate of Valor:
      total: 0.42
      efficiency: 0.42
      win: 0.56
      pick: 0.25
      fit: 0.28
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.74
    Shifter's Shield:
      total: 0.43
      efficiency: 0.3
      win: 0.53
      pick: 0.41
      fit: 0.5
    Amanita Charm:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - Avenging Blade
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
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, Amanita Charm, Shield Splitter, The Reaper, Screeching Gargoyle,
    Spectral Armor, Void Stone, Stone of Binding, Runeforged Hammer, Void Shield,
    Erosion, Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Titan''s Bane,
    Berserker''s Shield, Oath-Sworn Spear, Tekko-Kagi, Chandra''s Grace, Midgardian
    Mail, Pendulum Blade, Gladiator''s Shield.'
  slot_scores:
    Avenging Blade:
      total: 0.42
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.44
      efficiency: 0.46
      win: 0.56
      pick: 0.31
      fit: 0.26
    Breastplate of Valor:
      total: 0.42
      efficiency: 0.42
      win: 0.56
      pick: 0.25
      fit: 0.26
    Jotunn's Revenge:
      total: 0.45
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.53
    Shifter's Shield:
      total: 0.42
      efficiency: 0.3
      win: 0.53
      pick: 0.41
      fit: 0.47
    The Crusher:
      total: 0.43
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.54
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
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spectral Armor, Erosion, Kinetic Cuirass, Eye of Providence,
    Shield of the Phoenix, Pharaoh''s Curse, Jotunn''s Revenge, Chandra''s Grace,
    Void Stone, Shield Splitter, Stampede, Eye of the Storm, Runeforged Hammer, Void
    Shield, Phoenix Feather, Shogun''s Ofuda, Doublet of Binding, Mystical Mail, Avenging
    Blade, Berserker''s Shield, The Crusher, Eros'' Bow, The Reaper, Hydra''s Lament,
    Gladiator''s Shield, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.45
      efficiency: 0.46
      win: 0.56
      pick: 0.31
      fit: 0.32
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.78
    Shifter's Shield:
      total: 0.45
      efficiency: 0.3
      win: 0.53
      pick: 0.41
      fit: 0.68
    Spectral Armor:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.78
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.46
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.98
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Shield of the Phoenix
  - Shifter's Shield
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shield of the Phoenix
  - Shifter's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Spectral Armor, Erosion, Shield of the Phoenix, Kinetic
    Cuirass, Eye of Providence, Chandra''s Grace, Pharaoh''s Curse, Phoenix Feather,
    Jotunn''s Revenge, Runeforged Hammer, Void Stone, The Reaper, Stampede, Void Shield,
    Shogun''s Ofuda, Shield Splitter, Eye of the Storm, Avenging Blade, Doublet of
    Binding, The Crusher, Mystical Mail, Eros'' Bow, Berserker''s Shield, Hydra''s
    Lament, Spirit Robe, Umbral Link.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.46
      win: 0.56
      pick: 0.31
      fit: 0.26
    Shield of the Phoenix:
      total: 0.43
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.79
    Shifter's Shield:
      total: 0.43
      efficiency: 0.3
      win: 0.53
      pick: 0.41
      fit: 0.54
    Spectral Armor:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.44
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.84
  starter: *id001
  aspect: Aspect of Preservation
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Void Stone
  - Spectral Armor
  - Amanita Charm
  - Erosion
  flex_slots:
  - Void Stone
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Jotunn''s Revenge, Spectral Armor, Void Stone, Erosion,
    Void Shield, The Crusher, Avenging Blade, The Reaper, Kinetic Cuirass, Eye of
    Providence, Shield of the Phoenix, Pharaoh''s Curse, Chandra''s Grace, Runeforged
    Hammer, Stampede, Screeching Gargoyle, Shield Splitter, Phoenix Feather, Shogun''s
    Ofuda, Eye of the Storm, Doublet of Binding, Stone of Binding, Eros'' Bow, Mystical
    Mail, Hydra''s Lament, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.46
      win: 0.56
      pick: 0.31
      fit: 0.23
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
    Void Stone:
      total: 0.43
      efficiency: 0.3
      win: 0.5
      pick: 0.0
      fit: 1.0
    Spectral Armor:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.99
    Erosion:
      total: 0.43
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.79
  starter: *id001
  aspect: Aspect of Preservation
---
