---
type: smite-build
god: Pele
mode: Conquest
builds:
- source: community
  aspect: Aspect of Obsidian
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.55
  slot_order:
  - name: The Reaper
    pick_rate: 0.25
    win_rate: 0.57
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.22
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.59
  - name: The Crusher
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: The Reaper
      pick_rate: 0.17
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.53
  - name: Transcendence
    pick_rate: 0.13
    win_rate: 0.6
    alternates:
    - name: The Reaper
      pick_rate: 0.12
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.62
  - name: Heartseeker
    pick_rate: 0.19
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.16
      win_rate: 0.46
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.58
  - name: Titan's Bane
    pick_rate: 0.18
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.65
    - name: Shifter's Shield
      pick_rate: 0.06
      win_rate: 0.45
  - name: Blinking Abyss
    pick_rate: 0.06
    win_rate: 0.48
    alternates:
    - name: Titan's Bane
      pick_rate: 0.09
      win_rate: 0.69
    - name: Heartseeker
      pick_rate: 0.06
      win_rate: 0.61
  source_url: https://smitebrain.com/gods/pele/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Hydra''s Lament, Transcendence, Pendulum
    Blade, Runeforged Hammer, Tekko-Kagi, Avenging Blade, Arondight, Shield Splitter,
    Tyrfing, Eye of the Storm, Lernaean Bow, Golden Blade, Damaru, Barbed Carver,
    Oath-Sworn Spear, Genji''s Guard, Rage, Chandra''s Grace, Bloodforge, Breastplate
    of Valor, Wyrmskin Hide, Musashi''s Dual Swords, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 1.0
    Hydra's Lament:
      total: 0.5
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.77
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.57
      pick: 0.25
      fit: 0.78
    The Crusher:
      total: 0.59
      efficiency: 0.49
      win: 0.63
      pick: 0.15
      fit: 0.88
    Heartseeker:
      total: 0.51
      efficiency: 0.28
      win: 0.59
      pick: 0.19
      fit: 0.88
    Titan's Bane:
      total: 0.52
      efficiency: 0.37
      win: 0.6
      pick: 0.18
      fit: 0.78
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: The Crusher, Jotunn''s Revenge, Hydra''s Lament, Transcendence, Pendulum
    Blade, Runeforged Hammer, Tekko-Kagi, Genji''s Guard, Avenging Blade, Arondight,
    Shield Splitter, Chandra''s Grace, Tyrfing, Breastplate of Valor, Eye of the Storm,
    Lernaean Bow, Shield of the Phoenix, Spectral Armor, Golden Blade, Kinetic Cuirass,
    Screeching Gargoyle, Damaru, Eye of Providence, Barbed Carver, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.78
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.51
      efficiency: 0.44
      win: 0.57
      pick: 0.25
      fit: 0.56
    The Crusher:
      total: 0.56
      efficiency: 0.49
      win: 0.63
      pick: 0.15
      fit: 0.66
    Heartseeker:
      total: 0.47
      efficiency: 0.28
      win: 0.59
      pick: 0.19
      fit: 0.66
    Titan's Bane:
      total: 0.49
      efficiency: 0.37
      win: 0.6
      pick: 0.18
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - The Reaper
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Titan's Bane
  - Shield Splitter
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Jotunn''s Revenge, Amanita Charm, Shield Splitter, Shield
    of the Phoenix, Hydra''s Lament, Kinetic Cuirass, Eye of Providence, Chandra''s
    Grace, Spirit Robe, Runeforged Hammer, Genji''s Guard, Phoenix Feather, Eye of
    the Storm, Spectral Armor, Bloodforge, Avenging Blade, Glorious Pridwen, Breastplate
    of Valor, Erosion, Tyrfing, Devourer''s Gauntlet, Tekko-Kagi, Shroud of Vengeance,
    Mantle Of Discord, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shield Splitter:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.57
      pick: 0.25
      fit: 0.67
    The Crusher:
      total: 0.53
      efficiency: 0.49
      win: 0.63
      pick: 0.15
      fit: 0.47
    Titan's Bane:
      total: 0.46
      efficiency: 0.37
      win: 0.6
      pick: 0.18
      fit: 0.37
    Amanita Charm:
      total: 0.47
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Pendulum Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Pendulum Blade, Tekko-Kagi, Avenging
    Blade, Hydra''s Lament, Transcendence, Oath-Sworn Spear, Runeforged Hammer, Screeching
    Gargoyle, Shield Splitter, Tyrfing, Arondight, Eye of the Storm, Lernaean Bow,
    Genji''s Guard, Golden Blade, Damaru, Riptalon, Barbed Carver, Chandra''s Grace,
    Spectral Armor, Rage, Breastplate of Valor, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.57
      pick: 0.25
      fit: 0.85
    Pendulum Blade:
      total: 0.48
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 1.0
    The Crusher:
      total: 0.6
      efficiency: 0.49
      win: 0.63
      pick: 0.15
      fit: 0.95
    Heartseeker:
      total: 0.52
      efficiency: 0.28
      win: 0.59
      pick: 0.19
      fit: 0.95
    Titan's Bane:
      total: 0.54
      efficiency: 0.37
      win: 0.6
      pick: 0.18
      fit: 0.85
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
