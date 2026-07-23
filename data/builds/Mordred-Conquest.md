---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.55
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.56
    win_rate: 0.59
    alternates:
    - name: Barbed Carver
      pick_rate: 0.15
      win_rate: 0.61
    - name: Mystical Mail
      pick_rate: 0.03
      win_rate: 0.74
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.58
    - name: Shield of the Phoenix
      pick_rate: 0.12
      win_rate: 0.63
  - name: Dwarven Plate
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.59
    - name: Shield of the Phoenix
      pick_rate: 0.12
      win_rate: 0.52
  - name: Gladiator's Shield
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.18
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.6
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.55
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.17
      win_rate: 0.67
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.57
  - name: Medal of Defense
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.61
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.68
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Gladiator's Shield
  - Shifter's Shield
  flex_slots:
  - Eye of Providence
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Jotunn''s Revenge, Gladiator''s Shield, Kinetic Cuirass, Eye of Providence,
    Shield Splitter, The Crusher, Amanita Charm, Runeforged Hammer, Eye of the Storm,
    Spectral Armor, Hydra''s Lament, Erosion, Avenging Blade, Shield of the Phoenix,
    The Reaper, Berserker''s Shield, Wyrmskin Hide, Breastplate of Valor, Golden Blade,
    Midgardian Mail, Chandra''s Grace, Shroud of Vengeance, Mantle Of Discord, Leviathan''s
    Hide, Pharaoh''s Curse, Phoenix Feather.'
  slot_scores:
    Eye of Providence:
      total: 0.47
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.54
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
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
    Gladiator's Shield:
      total: 0.48
      efficiency: 0.3
      win: 0.63
      pick: 0.09
      fit: 0.55
    Shifter's Shield:
      total: 0.48
      efficiency: 0.3
      win: 0.59
      pick: 0.56
      fit: 0.54
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
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
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Gladiator''s Shield, The Crusher, Kinetic Cuirass, Eye
    of Providence, Shield Splitter, Amanita Charm, Hydra''s Lament, Runeforged Hammer,
    Spectral Armor, The Reaper, Eye of the Storm, Shield of the Phoenix, Avenging
    Blade, Erosion, Breastplate of Valor, Chandra''s Grace, Berserker''s Shield, Titan''s
    Bane, Screeching Gargoyle, Midgardian Mail, Golden Blade, Pendulum Blade, Tekko-Kagi,
    Yogi''s Necklace, Tyrfing, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.46
      efficiency: 0.46
      win: 0.55
      pick: 0.17
      fit: 0.27
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.48
    Gladiator's Shield:
      total: 0.47
      efficiency: 0.3
      win: 0.63
      pick: 0.09
      fit: 0.48
    Shifter's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.59
      pick: 0.56
      fit: 0.38
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Gladiator's Shield
  - The Reaper
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, The Reaper, Shield of the Phoenix,
    Gladiator''s Shield, The Crusher, Kinetic Cuirass, Chandra''s Grace, Eye of Providence,
    Shield Splitter, Runeforged Hammer, Phoenix Feather, Spectral Armor, Hydra''s
    Lament, Eye of the Storm, Avenging Blade, Spirit Robe, Erosion, Berserker''s Shield,
    Bloodforge, Golden Blade, Breastplate of Valor, Wyrmskin Hide, Glorious Pridwen,
    Midgardian Mail, Tyrfing, Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.41
    Gladiator's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.63
      pick: 0.09
      fit: 0.47
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    Shifter's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.59
      pick: 0.56
      fit: 0.41
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
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
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Kinetic Cuirass,
    Eye of Providence, Shield Splitter, The Reaper, Amanita Charm, Runeforged Hammer,
    Screeching Gargoyle, Spectral Armor, Hydra''s Lament, Eye of the Storm, Void Stone,
    Stone of Binding, Void Shield, Erosion, Titan''s Bane, Oath-Sworn Spear, Shield
    of the Phoenix, Tekko-Kagi, Berserker''s Shield, Heartseeker, Pendulum Blade,
    Breastplate of Valor, Chandra''s Grace, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.69
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.54
    Gladiator's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.63
      pick: 0.09
      fit: 0.46
    Shifter's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.59
      pick: 0.56
      fit: 0.44
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
