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
      pick_rate: 0.18
      win_rate: 0.54
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.31
    win_rate: 0.56
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.25
      win_rate: 0.49
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.26
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.26
      win_rate: 0.47
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.56
  - name: Dwarven Plate
    pick_rate: 0.24
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.49
    - name: Breastplate of Valor
      pick_rate: 0.09
      win_rate: 0.56
  - name: Glorious Pridwen
    pick_rate: 0.06
    win_rate: 0.62
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.55
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.46
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.71
  source_url: https://smitebrain.com/gods/hercules/
  last_verified: '2026-07-22'
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
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Eye of Providence, Amanita Charm, Shield Splitter,
    Erosion, Jotunn''s Revenge, Spectral Armor, Eye of the Storm, Shield of the Phoenix,
    Runeforged Hammer, The Crusher, Hydra''s Lament, Avenging Blade, Berserker''s
    Shield, Gladiator''s Shield, Draconic Scale, Shroud of Vengeance, Midgardian Mail,
    Prophetic Cloak, Wyrmskin Hide, Mantle Of Discord, Magi''s Cloak, Phoenix Feather,
    Freya''s Tears, Leviathan''s Hide.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.67
    Genji's Guard:
      total: 0.45
      efficiency: 0.44
      win: 0.56
      pick: 0.31
      fit: 0.36
    Breastplate of Valor:
      total: 0.43
      efficiency: 0.41
      win: 0.55
      pick: 0.26
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
      efficiency: 0.44
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
  - Kinetic Cuirass
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Glorious Pridwen, Kinetic Cuirass,
    Eye of Providence, Chandra''s Grace, Jotunn''s Revenge, Phoenix Feather, Shield
    Splitter, The Reaper, Spectral Armor, Runeforged Hammer, Eye of the Storm, Erosion,
    Spirit Robe, The Crusher, Hydra''s Lament, Avenging Blade, Berserker''s Shield,
    Gladiator''s Shield, Midgardian Mail, Wyrmskin Hide, Bloodforge, Leviathan''s
    Hide, Ancile, Golden Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.44
      win: 0.56
      pick: 0.31
      fit: 0.28
    Breastplate of Valor:
      total: 0.41
      efficiency: 0.41
      win: 0.55
      pick: 0.26
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
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Avenging Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, Amanita Charm, Shield Splitter, Screeching Gargoyle, The Reaper,
    Spectral Armor, Void Stone, Stone of Binding, Void Shield, Erosion, Runeforged
    Hammer, Eye of the Storm, Hydra''s Lament, Shield of the Phoenix, Oath-Sworn Spear,
    Titan''s Bane, Berserker''s Shield, Tekko-Kagi, Pendulum Blade, Midgardian Mail,
    Gladiator''s Shield, Chandra''s Grace, Shroud of Vengeance.'
  slot_scores:
    Avenging Blade:
      total: 0.42
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.44
      efficiency: 0.44
      win: 0.56
      pick: 0.31
      fit: 0.26
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.53
    Kinetic Cuirass:
      total: 0.41
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.42
      efficiency: 0.3
      win: 0.53
      pick: 0.41
      fit: 0.47
    The Crusher:
      total: 0.42
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: fun-crit
  slot_order:
  - Tyrfing
  - Rage
  - Bragi's Harp
  - Death Metal
  - Damaru
  - Demon Blade
  flex_slots:
  - Rage
  - Bragi's Harp
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
    Tyrfing:
      total: 0.24
      efficiency: 0.39
      win: 0.5
      pick: 0.0
      fit: 0.67
    Rage:
      total: 0.23
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Bragi's Harp:
      total: 0.23
      efficiency: 0.36
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
      efficiency: 0.37
      win: 0.5
      pick: 0.0
      fit: 0.66
    Demon Blade:
      total: 0.23
      efficiency: 0.23
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
    Shield of the Phoenix, Pharaoh''s Curse, Void Stone, Shield Splitter, Stampede,
    Chandra''s Grace, Eye of the Storm, Void Shield, Phoenix Feather, Runeforged Hammer,
    Shogun''s Ofuda, Jotunn''s Revenge, Mystical Mail, Doublet of Binding, Avenging
    Blade, Berserker''s Shield, Eros'' Bow, Gladiator''s Shield, The Crusher, Hydra''s
    Lament, The Reaper, Midgardian Mail, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.45
      efficiency: 0.44
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
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.78
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
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
    Cuirass, Eye of Providence, Chandra''s Grace, Phoenix Feather, Pharaoh''s Curse,
    Void Stone, Jotunn''s Revenge, Stampede, Runeforged Hammer, Void Shield, Shield
    Splitter, The Reaper, Eye of the Storm, Shogun''s Ofuda, Avenging Blade, Mystical
    Mail, Doublet of Binding, Eros'' Bow, Spirit Robe, The Crusher, Hydra''s Lament,
    Berserker''s Shield, Umbral Link, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.44
      efficiency: 0.44
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
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
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
  - Genji's Guard
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
    for this god: Amanita Charm, Spectral Armor, Jotunn''s Revenge, Void Stone, Erosion,
    Void Shield, Avenging Blade, The Crusher, The Reaper, Kinetic Cuirass, Eye of
    Providence, Shield of the Phoenix, Pharaoh''s Curse, Chandra''s Grace, Stampede,
    Screeching Gargoyle, Shield Splitter, Runeforged Hammer, Phoenix Feather, Shogun''s
    Ofuda, Eye of the Storm, Stone of Binding, Mystical Mail, Doublet of Binding,
    Eros'' Bow, Hydra''s Lament, Oath-Sworn Spear, Berserker''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.43
      efficiency: 0.44
      win: 0.56
      pick: 0.31
      fit: 0.23
    Jotunn's Revenge:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.51
    Void Stone:
      total: 0.43
      efficiency: 0.31
      win: 0.5
      pick: 0.0
      fit: 1.0
    Spectral Armor:
      total: 0.44
      efficiency: 0.48
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
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
