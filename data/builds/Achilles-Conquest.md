---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.49
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.5
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.12
      win_rate: 0.3
    - name: Jotunn's Revenge
      pick_rate: 0.11
      win_rate: 0.65
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.53
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.49
  - name: Dwarven Plate
    pick_rate: 0.11
    win_rate: 0.48
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.45
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.55
  - name: Gladiator's Shield
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.15
      win_rate: 0.43
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.45
  - name: Titan's Bane
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.1
      win_rate: 0.4
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.48
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.35
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.63
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.5
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - Runeforged Hammer
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Gladiator's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, The Crusher, Runeforged Hammer, Titan''s Bane, Kinetic
    Cuirass, Shield Splitter, Eye of the Storm, Eye of Providence, Avenging Blade,
    The Reaper, Amanita Charm, Hydra''s Lament, Spectral Armor, Golden Blade, Wyrmskin
    Hide, Erosion, Berserker''s Shield, Shield of the Phoenix, Tekko-Kagi, Tyrfing,
    Chandra''s Grace, Heartseeker, Midgardian Mail, Lernaean Bow, Yogi''s Necklace,
    Transcendence, Leviathan''s Hide, Genji''s Guard.'
  slot_scores:
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
    Gladiator's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.63
      pick: 0.06
      fit: 0.48
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
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.58
      pick: 0.06
      fit: 0.49
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gladiator's Shield
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Gladiator's Shield
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
    this god: Amanita Charm, The Reaper, Jotunn''s Revenge, The Crusher, Kinetic Cuirass,
    Shield of the Phoenix, Eye of Providence, Shield Splitter, Runeforged Hammer,
    Chandra''s Grace, Phoenix Feather, Titan''s Bane, Eye of the Storm, Spectral Armor,
    Avenging Blade, Hydra''s Lament, Spirit Robe, Erosion, Berserker''s Shield, Bloodforge,
    Golden Blade, Wyrmskin Hide, Tyrfing, Midgardian Mail, Devourer''s Gauntlet, Genji''s
    Guard, Yogi''s Necklace, Leviathan''s Hide.'
  slot_scores:
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
    Gladiator's Shield:
      total: 0.46
      efficiency: 0.3
      win: 0.63
      pick: 0.06
      fit: 0.42
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
      efficiency: 0.45
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
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Avenging Blade, Titan''s Bane, The
    Reaper, Runeforged Hammer, Kinetic Cuirass, Eye of Providence, Shield Splitter,
    Eye of the Storm, Tekko-Kagi, Hydra''s Lament, Spectral Armor, Amanita Charm,
    Oath-Sworn Spear, Heartseeker, Void Stone, Void Shield, Screeching Gargoyle, Pendulum
    Blade, Golden Blade, Stone of Binding, Erosion, Berserker''s Shield, Shield of
    the Phoenix, Wyrmskin Hide, Tyrfing, Genji''s Guard.'
  slot_scores:
    Avenging Blade:
      total: 0.49
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.78
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.55
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
    Titan's Bane:
      total: 0.48
      efficiency: 0.37
      win: 0.58
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
