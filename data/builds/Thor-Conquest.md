---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.56
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.52
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.55
    - name: Runeforged Hammer
      pick_rate: 0.08
      win_rate: 0.53
  - name: Shifter's Shield
    pick_rate: 0.16
    win_rate: 0.62
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.15
      win_rate: 0.51
    - name: Barbed Carver
      pick_rate: 0.14
      win_rate: 0.53
  - name: Hydra's Lament
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.46
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.52
  - name: Titan's Bane
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Heartseeker
      pick_rate: 0.17
      win_rate: 0.57
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.12
    win_rate: 0.53
    alternates:
    - name: Titan's Bane
      pick_rate: 0.18
      win_rate: 0.59
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.57
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.49
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.67
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Hydra's Lament
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Shield Splitter
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Hydra''s Lament, Runeforged Hammer, Shield Splitter, Kinetic
    Cuirass, Eye of the Storm, Eye of Providence, Avenging Blade, The Reaper, Amanita
    Charm, Spectral Armor, Heartseeker, Golden Blade, Wyrmskin Hide, Erosion, Tekko-Kagi,
    Berserker''s Shield, Shield of the Phoenix, Tyrfing, Genji''s Guard, Lernaean
    Bow, Chandra''s Grace, Transcendence, Midgardian Mail, Pendulum Blade, Yogi''s
    Necklace.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.52
      fit: 0.55
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hydra's Lament:
      total: 0.47
      efficiency: 0.45
      win: 0.54
      pick: 0.14
      fit: 0.44
    Runeforged Hammer:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.61
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Hydra''s Lament, Runeforged Hammer, The Reaper, Kinetic Cuirass,
    Eye of Providence, Shield Splitter, Spectral Armor, Avenging Blade, Genji''s Guard,
    Amanita Charm, Eye of the Storm, Shield of the Phoenix, Heartseeker, Chandra''s
    Grace, Pendulum Blade, Breastplate of Valor, Tekko-Kagi, Berserker''s Shield,
    Erosion, Golden Blade, Gladiator''s Shield, Tyrfing, Arondight, Yogi''s Necklace,
    Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.55
      win: 0.56
      pick: 0.52
      fit: 0.56
    Hydra's Lament:
      total: 0.47
      efficiency: 0.45
      win: 0.54
      pick: 0.14
      fit: 0.42
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
    Titan's Bane:
      total: 0.44
      efficiency: 0.37
      win: 0.53
      pick: 0.21
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
  - Kinetic Cuirass
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
    this god: Amanita Charm, The Reaper, The Crusher, Hydra''s Lament, Kinetic Cuirass,
    Shield of the Phoenix, Shield Splitter, Eye of Providence, Runeforged Hammer,
    Chandra''s Grace, Phoenix Feather, Eye of the Storm, Spectral Armor, Avenging
    Blade, Spirit Robe, Erosion, Bloodforge, Berserker''s Shield, Genji''s Guard,
    Golden Blade, Wyrmskin Hide, Tyrfing, Devourer''s Gauntlet, Midgardian Mail, Breastplate
    of Valor, Tekko-Kagi.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.56
      pick: 0.52
      fit: 0.39
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.54
      pick: 0.14
      fit: 0.34
    The Reaper:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.46
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.73
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Titan's Bane
  flex_slots:
  - Titan's Bane
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, The Reaper, Hydra''s Lament, Runeforged
    Hammer, Heartseeker, Kinetic Cuirass, Shield Splitter, Eye of Providence, Tekko-Kagi,
    Eye of the Storm, Oath-Sworn Spear, Spectral Armor, Amanita Charm, Void Stone,
    Screeching Gargoyle, Pendulum Blade, Void Shield, Stone of Binding, Golden Blade,
    Erosion, Berserker''s Shield, Tyrfing, Wyrmskin Hide, Genji''s Guard, Shield of
    the Phoenix.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.55
      win: 0.56
      pick: 0.52
      fit: 0.66
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.54
      pick: 0.14
      fit: 0.36
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.72
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.53
      pick: 0.21
      fit: 0.62
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
      win: 0.56
      pick: 0.52
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
