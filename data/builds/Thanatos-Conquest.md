---
type: smite-build
god: Thanatos
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reaping
  aspect_pick_rate: 0.18
  aspect_win_rate: 0.55
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.66
    win_rate: 0.54
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.34
  - name: Hydra's Lament
    pick_rate: 0.38
    win_rate: 0.53
    alternates:
    - name: The Reaper
      pick_rate: 0.2
      win_rate: 0.57
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.51
  - name: The Reaper
    pick_rate: 0.26
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.17
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.61
  - name: Titan's Bane
    pick_rate: 0.29
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.65
    - name: The Reaper
      pick_rate: 0.08
      win_rate: 0.48
  - name: Heartseeker
    pick_rate: 0.19
    win_rate: 0.59
    alternates:
    - name: Titan's Bane
      pick_rate: 0.22
      win_rate: 0.56
    - name: Blinking Abyss
      pick_rate: 0.07
      win_rate: 0.53
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.61
    - name: Lucerne Hammer
      pick_rate: 0.07
      win_rate: 0.39
  source_url: https://smitebrain.com/gods/thanatos/
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
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Tekko-Kagi, Pendulum Blade, Runeforged Hammer, Avenging
    Blade, Shield Splitter, Tyrfing, Eye of the Storm, Lernaean Bow, Transcendence,
    Arondight, Golden Blade, Damaru, Barbed Carver, Oath-Sworn Spear, Rage, Bloodforge,
    Wyrmskin Hide, Musashi''s Dual Swords, Devourer''s Gauntlet, Genji''s Guard, Spectral
    Armor, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.55
      win: 0.54
      pick: 0.66
      fit: 1.0
    Hydra's Lament:
      total: 0.52
      efficiency: 0.45
      win: 0.53
      pick: 0.38
      fit: 0.71
    The Reaper:
      total: 0.54
      efficiency: 0.44
      win: 0.53
      pick: 0.26
      fit: 0.91
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.52
      efficiency: 0.28
      win: 0.59
      pick: 0.19
      fit: 1.0
    Titan's Bane:
      total: 0.53
      efficiency: 0.37
      win: 0.55
      pick: 0.29
      fit: 0.91
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
  - Heartseeker
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
    god: The Crusher, Pendulum Blade, Runeforged Hammer, Tekko-Kagi, Genji''s Guard,
    Avenging Blade, Arondight, Shield Splitter, Chandra''s Grace, Tyrfing, Breastplate
    of Valor, Eye of the Storm, Lernaean Bow, Shield of the Phoenix, Transcendence,
    Spectral Armor, Golden Blade, Kinetic Cuirass, Screeching Gargoyle, Damaru, Eye
    of Providence, Barbed Carver, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.55
      win: 0.54
      pick: 0.66
      fit: 0.78
    Hydra's Lament:
      total: 0.5
      efficiency: 0.45
      win: 0.53
      pick: 0.38
      fit: 0.54
    The Reaper:
      total: 0.49
      efficiency: 0.44
      win: 0.53
      pick: 0.26
      fit: 0.56
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.47
      efficiency: 0.28
      win: 0.59
      pick: 0.19
      fit: 0.66
    Titan's Bane:
      total: 0.47
      efficiency: 0.37
      win: 0.55
      pick: 0.29
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Hydra's Lament
  - The Reaper
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
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
    this god: Amanita Charm, The Crusher, Shield Splitter, Kinetic Cuirass, Shield
    of the Phoenix, Eye of Providence, Spirit Robe, Runeforged Hammer, Phoenix Feather,
    Eye of the Storm, Chandra''s Grace, Spectral Armor, Bloodforge, Genji''s Guard,
    Avenging Blade, Erosion, Tyrfing, Devourer''s Gauntlet, Glorious Pridwen, Tekko-Kagi,
    Shroud of Vengeance, Mantle Of Discord, Breastplate of Valor, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.55
      win: 0.54
      pick: 0.66
      fit: 0.44
    Shield Splitter:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.47
      efficiency: 0.45
      win: 0.53
      pick: 0.38
      fit: 0.37
    The Reaper:
      total: 0.51
      efficiency: 0.44
      win: 0.53
      pick: 0.26
      fit: 0.7
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.48
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Heartseeker
  - Tekko-Kagi
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Tekko-Kagi, Avenging Blade, Pendulum Blade, Oath-Sworn
    Spear, Runeforged Hammer, Shield Splitter, Tyrfing, Eye of the Storm, Lernaean
    Bow, Transcendence, Screeching Gargoyle, Riptalon, Golden Blade, Damaru, Arondight,
    Barbed Carver, Rage, Avatar''s Parashu, Spectral Armor, Genji''s Guard, Kinetic
    Cuirass, Void Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.55
      win: 0.54
      pick: 0.66
      fit: 1.0
    The Reaper:
      total: 0.55
      efficiency: 0.44
      win: 0.53
      pick: 0.26
      fit: 0.94
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.35
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.52
      efficiency: 0.28
      win: 0.59
      pick: 0.19
      fit: 1.0
    Titan's Bane:
      total: 0.53
      efficiency: 0.37
      win: 0.55
      pick: 0.29
      fit: 0.94
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
      win: 0.54
      pick: 0.66
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
