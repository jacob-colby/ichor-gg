---
type: smite-build
god: Thor
mode: Conquest
builds:
- source: community
  aspect: Aspect of Thunderstruck
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.56
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.52
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.55
    - name: Runeforged Hammer
      pick_rate: 0.08
      win_rate: 0.53
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.61
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.16
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.13
      win_rate: 0.52
  - name: Hydra's Lament
    pick_rate: 0.13
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.6
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.44
  - name: Titan's Bane
    pick_rate: 0.19
    win_rate: 0.52
    alternates:
    - name: Heartseeker
      pick_rate: 0.17
      win_rate: 0.57
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.11
    win_rate: 0.54
    alternates:
    - name: Titan's Bane
      pick_rate: 0.17
      win_rate: 0.59
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.56
  - name: Lucerne Hammer
    pick_rate: 0.07
    win_rate: 0.51
    alternates:
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.62
    - name: Titan's Bane
      pick_rate: 0.05
      win_rate: 0.54
  source_url: https://smitebrain.com/gods/thor/
  last_verified: '2026-07-25'
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
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Runeforged Hammer, Hydra''s Lament, Kinetic Cuirass, Shield
    Splitter, Eye of the Storm, Eye of Providence, Avenging Blade, The Reaper, Amanita
    Charm, Spectral Armor, Heartseeker, Golden Blade, Erosion, Wyrmskin Hide, Berserker''s
    Shield, Tekko-Kagi, Shield of the Phoenix, Tyrfing, Genji''s Guard, Lernaean Bow,
    Chandra''s Grace, Midgardian Mail, Transcendence, Yogi''s Necklace, Pharaoh''s
    Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.54
      win: 0.55
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
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    Hydra's Lament:
      total: 0.47
      efficiency: 0.45
      win: 0.53
      pick: 0.13
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
  - Kinetic Cuirass
  - Hydra's Lament
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - The Reaper
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Hydra''s Lament, Runeforged Hammer, The Reaper, Kinetic Cuirass,
    Eye of Providence, Spectral Armor, Shield Splitter, Avenging Blade, Genji''s Guard,
    Amanita Charm, Eye of the Storm, Heartseeker, Shield of the Phoenix, Chandra''s
    Grace, Breastplate of Valor, Pendulum Blade, Tekko-Kagi, Berserker''s Shield,
    Golden Blade, Erosion, Gladiator''s Shield, Arondight, Tyrfing, Yogi''s Necklace,
    Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.54
      win: 0.55
      pick: 0.52
      fit: 0.56
    Kinetic Cuirass:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.37
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.53
      pick: 0.13
      fit: 0.42
    Runeforged Hammer:
      total: 0.44
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.37
    The Reaper:
      total: 0.44
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.4
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
  starter: *id001
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
    this god: Amanita Charm, The Reaper, The Crusher, Kinetic Cuirass, Shield of the
    Phoenix, Eye of Providence, Hydra''s Lament, Shield Splitter, Runeforged Hammer,
    Chandra''s Grace, Phoenix Feather, Spectral Armor, Eye of the Storm, Avenging
    Blade, Erosion, Spirit Robe, Berserker''s Shield, Bloodforge, Genji''s Guard,
    Golden Blade, Wyrmskin Hide, Midgardian Mail, Tyrfing, Pharaoh''s Curse, Devourer''s
    Gauntlet, Breastplate of Valor.'
  slot_scores:
    Eye of Providence:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.54
      win: 0.55
      pick: 0.52
      fit: 0.39
    Kinetic Cuirass:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Reaper:
      total: 0.47
      efficiency: 0.43
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
      efficiency: 0.44
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
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, The Reaper, Hydra''s Lament, Runeforged
    Hammer, Heartseeker, Kinetic Cuirass, Eye of Providence, Shield Splitter, Tekko-Kagi,
    Eye of the Storm, Spectral Armor, Amanita Charm, Oath-Sworn Spear, Void Stone,
    Screeching Gargoyle, Void Shield, Pendulum Blade, Golden Blade, Erosion, Stone
    of Binding, Berserker''s Shield, Genji''s Guard, Shield of the Phoenix, Wyrmskin
    Hide, Tyrfing.'
  slot_scores:
    Avenging Blade:
      total: 0.48
      efficiency: 0.41
      win: 0.5
      pick: 0.0
      fit: 0.77
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.54
      win: 0.55
      pick: 0.52
      fit: 0.66
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.53
      pick: 0.13
      fit: 0.36
    The Reaper:
      total: 0.47
      efficiency: 0.43
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
      total: 0.46
      efficiency: 0.36
      win: 0.52
      pick: 0.19
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
      win: 0.55
      pick: 0.52
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
