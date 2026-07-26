---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.42
    win_rate: 0.52
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.11
      win_rate: 0.37
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.66
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.44
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.55
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.51
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.56
  - name: Gladiator's Shield
    pick_rate: 0.08
    win_rate: 0.61
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.16
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.45
  - name: Titan's Bane
    pick_rate: 0.06
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.11
      win_rate: 0.46
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.52
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.36
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.65
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.52
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-07-25'
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
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, Runeforged Hammer, Kinetic Cuirass,
    Eye of Providence, Eye of the Storm, Shield Splitter, Avenging Blade, Titan''s
    Bane, The Reaper, Amanita Charm, Spectral Armor, Hydra''s Lament, Golden Blade,
    Erosion, Wyrmskin Hide, Berserker''s Shield, Shield of the Phoenix, Tekko-Kagi,
    Tyrfing, Chandra''s Grace, Midgardian Mail, Lernaean Bow, Yogi''s Necklace, Heartseeker,
    Pharaoh''s Curse, Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.46
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.54
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
      total: 0.48
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
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
    Blade, Titan''s Bane, Hydra''s Lament, Erosion, Spirit Robe, Berserker''s Shield,
    Golden Blade, Bloodforge, Wyrmskin Hide, Midgardian Mail, Tyrfing, Pharaoh''s
    Curse, Leviathan''s Hide, Yogi''s Necklace, Genji''s Guard.'
  slot_scores:
    Eye of Providence:
      total: 0.46
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.54
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
      total: 0.47
      efficiency: 0.43
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
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Runeforged Hammer
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Titan''s Bane, The
    Reaper, Runeforged Hammer, Kinetic Cuirass, Eye of Providence, Shield Splitter,
    Eye of the Storm, Tekko-Kagi, Spectral Armor, Hydra''s Lament, Amanita Charm,
    Oath-Sworn Spear, Void Stone, Heartseeker, Void Shield, Screeching Gargoyle, Pendulum
    Blade, Golden Blade, Erosion, Berserker''s Shield, Stone of Binding, Shield of
    the Phoenix, Wyrmskin Hide, Tyrfing, Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.78
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.54
      win: 0.5
      pick: 0.0
      fit: 0.65
    Runeforged Hammer:
      total: 0.45
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Reaper:
      total: 0.47
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.71
    Titan's Bane:
      total: 0.47
      efficiency: 0.36
      win: 0.56
      pick: 0.06
      fit: 0.61
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
      total: 0.22
      efficiency: 0.54
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
      total: 0.22
      efficiency: 0.21
      win: 0.5
      pick: 0.0
      fit: 1.0
  fun: true
  starter: *id001
---
