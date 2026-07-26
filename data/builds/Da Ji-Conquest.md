---
type: smite-build
god: Da Ji
mode: Conquest
builds:
- source: community
  aspect: Aspect of Ferocity
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.48
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.59
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.19
      win_rate: 0.57
    - name: Barbed Carver
      pick_rate: 0.05
      win_rate: 0.57
  - name: Hydra's Lament
    pick_rate: 0.3
    win_rate: 0.56
    alternates:
    - name: Barbed Carver
      pick_rate: 0.16
      win_rate: 0.48
    - name: Transcendence
      pick_rate: 0.15
      win_rate: 0.56
  - name: Barbed Carver
    pick_rate: 0.16
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.18
      win_rate: 0.57
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.5
  - name: Titan's Bane
    pick_rate: 0.31
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.26
      win_rate: 0.53
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.62
  - name: Heartseeker
    pick_rate: 0.16
    win_rate: 0.64
    alternates:
    - name: Titan's Bane
      pick_rate: 0.2
      win_rate: 0.6
    - name: Blinking Abyss
      pick_rate: 0.05
      win_rate: 0.58
  - name: Lucerne Hammer
    pick_rate: 0.09
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.12
      win_rate: 0.54
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.74
  source_url: https://smitebrain.com/gods/da-ji/
  last_verified: '2026-07-25'
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
  - Titan's Bane
  - The Reaper
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
    this god: The Crusher, The Reaper, Pendulum Blade, Runeforged Hammer, Tekko-Kagi,
    Avenging Blade, Arondight, Shield Splitter, Tyrfing, Lernaean Bow, Eye of the
    Storm, Transcendence, Golden Blade, Damaru, Genji''s Guard, Oath-Sworn Spear,
    Rage, Chandra''s Grace, Breastplate of Valor, Bloodforge, Wyrmskin Hide, Spectral
    Armor, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.54
      win: 0.53
      pick: 0.59
      fit: 1.0
    Hydra's Lament:
      total: 0.54
      efficiency: 0.45
      win: 0.56
      pick: 0.3
      fit: 0.77
    The Reaper:
      total: 0.49
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.53
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.88
    Heartseeker:
      total: 0.52
      efficiency: 0.27
      win: 0.64
      pick: 0.16
      fit: 0.88
    Titan's Bane:
      total: 0.51
      efficiency: 0.36
      win: 0.55
      pick: 0.31
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
  - Titan's Bane
  - The Reaper
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
    god: The Crusher, The Reaper, Pendulum Blade, Runeforged Hammer, Tekko-Kagi, Genji''s
    Guard, Avenging Blade, Arondight, Shield Splitter, Chandra''s Grace, Breastplate
    of Valor, Tyrfing, Lernaean Bow, Eye of the Storm, Spectral Armor, Shield of the
    Phoenix, Transcendence, Golden Blade, Kinetic Cuirass, Damaru, Eye of Providence,
    Screeching Gargoyle, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.54
      win: 0.53
      pick: 0.59
      fit: 0.78
    Hydra's Lament:
      total: 0.5
      efficiency: 0.45
      win: 0.56
      pick: 0.3
      fit: 0.54
    The Reaper:
      total: 0.46
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.49
      efficiency: 0.27
      win: 0.64
      pick: 0.16
      fit: 0.66
    Titan's Bane:
      total: 0.47
      efficiency: 0.36
      win: 0.55
      pick: 0.31
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Heartseeker
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, The Crusher, Shield Splitter, Shield of the
    Phoenix, Kinetic Cuirass, Eye of Providence, Chandra''s Grace, Runeforged Hammer,
    Spirit Robe, Genji''s Guard, Phoenix Feather, Eye of the Storm, Spectral Armor,
    Avenging Blade, Bloodforge, Breastplate of Valor, Erosion, Glorious Pridwen, Tyrfing,
    Tekko-Kagi, Devourer''s Gauntlet, Lernaean Bow, Berserker''s Shield, Mantle Of
    Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.59
      fit: 0.48
    Hydra's Lament:
      total: 0.49
      efficiency: 0.45
      win: 0.56
      pick: 0.3
      fit: 0.42
    The Reaper:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.67
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.47
    Heartseeker:
      total: 0.46
      efficiency: 0.27
      win: 0.64
      pick: 0.16
      fit: 0.47
    Amanita Charm:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.62
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
  - The Reaper
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
    for this god: The Crusher, The Reaper, Tekko-Kagi, Avenging Blade, Pendulum Blade,
    Runeforged Hammer, Oath-Sworn Spear, Screeching Gargoyle, Shield Splitter, Tyrfing,
    Arondight, Lernaean Bow, Eye of the Storm, Genji''s Guard, Transcendence, Golden
    Blade, Damaru, Riptalon, Spectral Armor, Chandra''s Grace, Kinetic Cuirass, Breastplate
    of Valor, Rage.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.54
      win: 0.53
      pick: 0.59
      fit: 1.0
    Hydra's Lament:
      total: 0.5
      efficiency: 0.45
      win: 0.56
      pick: 0.3
      fit: 0.54
    The Reaper:
      total: 0.5
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.85
    The Crusher:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.95
    Heartseeker:
      total: 0.53
      efficiency: 0.27
      win: 0.64
      pick: 0.16
      fit: 0.95
    Titan's Bane:
      total: 0.52
      efficiency: 0.36
      win: 0.55
      pick: 0.31
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
      win: 0.53
      pick: 0.59
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
