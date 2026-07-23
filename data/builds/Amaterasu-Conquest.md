---
type: smite-build
god: Amaterasu
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.67
    alternates:
    - name: Golden Blade
      pick_rate: 0.27
      win_rate: 0.55
    - name: Daybreak Gavel
      pick_rate: 0.08
      win_rate: 0.38
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.59
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.41
  - name: Shogun's Ofuda
    pick_rate: 0.12
    win_rate: 0.53
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.28
  - name: Dwarven Plate
    pick_rate: 0.19
    win_rate: 0.45
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.13
      win_rate: 0.65
    - name: Shogun's Ofuda
      pick_rate: 0.1
      win_rate: 0.69
  - name: Spirit Robe
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.13
      win_rate: 0.63
    - name: Contagion
      pick_rate: 0.05
      win_rate: 0.86
  - name: Contagion
    pick_rate: 0.07
    win_rate: 0.57
    alternates:
    - name: Engraved Guard
      pick_rate: 0.07
      win_rate: 0.57
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.8
  source_url: https://smitebrain.com/gods/amaterasu/
  last_verified: '2026-07-23'
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  flex_slots:
  - Shield Splitter
  - Berserker's Shield
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
    this god: Kinetic Cuirass, Eye of Providence, Jotunn''s Revenge, Shield Splitter,
    Amanita Charm, Eye of the Storm, Runeforged Hammer, Spectral Armor, The Crusher,
    Erosion, Hydra''s Lament, Shield of the Phoenix, Avenging Blade, Genji''s Guard,
    Wyrmskin Hide, Breastplate of Valor, Gladiator''s Shield, Chandra''s Grace, Golden
    Blade, Midgardian Mail, The Reaper, Shroud of Vengeance, Mantle Of Discord, Draconic
    Scale, Prophetic Cloak, Freya''s Tears.'
  slot_scores:
    Eye of Providence:
      total: 0.48
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.6
    Berserker's Shield:
      total: 0.47
      efficiency: 0.43
      win: 0.57
      pick: 0.22
      fit: 0.39
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shield Splitter:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shifter's Shield:
      total: 0.51
      efficiency: 0.3
      win: 0.67
      pick: 0.32
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Jotunn''s Revenge, Kinetic Cuirass,
    Chandra''s Grace, The Reaper, Eye of Providence, Shield Splitter, Runeforged Hammer,
    Phoenix Feather, The Crusher, Hydra''s Lament, Spectral Armor, Eye of the Storm,
    Avenging Blade, Erosion, Genji''s Guard, Bloodforge, Golden Blade, Breastplate
    of Valor, Wyrmskin Hide, Glorious Pridwen, Gladiator''s Shield, Midgardian Mail,
    Tyrfing, Leviathan''s Hide, Spirit Robe.'
  slot_scores:
    Berserker's Shield:
      total: 0.46
      efficiency: 0.43
      win: 0.57
      pick: 0.22
      fit: 0.3
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shield of the Phoenix:
      total: 0.47
      efficiency: 0.4
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shifter's Shield:
      total: 0.49
      efficiency: 0.3
      win: 0.67
      pick: 0.32
      fit: 0.46
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.76
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
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
    Eye of Providence, Shield Splitter, The Reaper, Amanita Charm, Screeching Gargoyle,
    Runeforged Hammer, Spectral Armor, Hydra''s Lament, Void Stone, Eye of the Storm,
    Stone of Binding, Void Shield, Erosion, Titan''s Bane, Genji''s Guard, Oath-Sworn
    Spear, Shield of the Phoenix, Tekko-Kagi, Pendulum Blade, Breastplate of Valor,
    Heartseeker, Chandra''s Grace, Golden Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.47
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.46
      efficiency: 0.43
      win: 0.57
      pick: 0.22
      fit: 0.28
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
    Shifter's Shield:
      total: 0.49
      efficiency: 0.3
      win: 0.67
      pick: 0.32
      fit: 0.44
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
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
