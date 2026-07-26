---
type: smite-build
god: Bastet
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Watchful Pride
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.51
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.65
    win_rate: 0.55
    alternates:
    - name: Transcendence
      pick_rate: 0.13
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.44
  - name: Transcendence
    pick_rate: 0.3
    win_rate: 0.58
    alternates:
    - name: Barbed Carver
      pick_rate: 0.18
      win_rate: 0.54
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.56
  - name: Barbed Carver
    pick_rate: 0.18
    win_rate: 0.54
    alternates:
    - name: Pendulum Blade
      pick_rate: 0.16
      win_rate: 0.57
    - name: The Crusher
      pick_rate: 0.11
      win_rate: 0.54
  - name: Heartseeker
    pick_rate: 0.31
    win_rate: 0.62
    alternates:
    - name: Titan's Bane
      pick_rate: 0.23
      win_rate: 0.48
    - name: The Crusher
      pick_rate: 0.06
      win_rate: 0.67
  - name: Titan's Bane
    pick_rate: 0.27
    win_rate: 0.66
    alternates:
    - name: Heartseeker
      pick_rate: 0.17
      win_rate: 0.52
    - name: Lucerne Hammer
      pick_rate: 0.08
      win_rate: 0.53
  - name: Lucerne Hammer
    pick_rate: 0.08
    win_rate: 0.55
    alternates:
    - name: Heartseeker
      pick_rate: 0.09
      win_rate: 0.65
    - name: Titan's Bane
      pick_rate: 0.07
      win_rate: 0.56
  source_url: https://smitebrain.com/gods/bastet/
  last_verified: '2026-07-25'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - The Reaper
  - Transcendence
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Tekko-Kagi, Runeforged Hammer,
    Pendulum Blade, Avenging Blade, Shield Splitter, Tyrfing, Lernaean Bow, Eye of
    the Storm, Golden Blade, Arondight, Damaru, Oath-Sworn Spear, Rage, Bloodforge,
    Wyrmskin Hide, Musashi''s Dual Swords, Devourer''s Gauntlet, Genji''s Guard, Spectral
    Armor, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.54
      win: 0.55
      pick: 0.65
      fit: 1.0
    Transcendence:
      total: 0.49
      efficiency: 0.39
      win: 0.58
      pick: 0.3
      fit: 0.52
    The Reaper:
      total: 0.51
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.27
      win: 0.62
      pick: 0.31
      fit: 1.0
    Titan's Bane:
      total: 0.57
      efficiency: 0.36
      win: 0.66
      pick: 0.27
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
  - Hydra's Lament
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
    god: The Crusher, Hydra''s Lament, The Reaper, Pendulum Blade, Runeforged Hammer,
    Tekko-Kagi, Genji''s Guard, Avenging Blade, Arondight, Shield Splitter, Chandra''s
    Grace, Breastplate of Valor, Tyrfing, Lernaean Bow, Eye of the Storm, Spectral
    Armor, Shield of the Phoenix, Golden Blade, Kinetic Cuirass, Damaru, Eye of Providence,
    Screeching Gargoyle, Oath-Sworn Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.54
      win: 0.55
      pick: 0.65
      fit: 0.78
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
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
      win: 0.62
      pick: 0.31
      fit: 0.66
    Titan's Bane:
      total: 0.52
      efficiency: 0.36
      win: 0.66
      pick: 0.27
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - The Reaper
  - The Crusher
  - Heartseeker
  - Titan's Bane
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, The Crusher, Shield Splitter, Kinetic Cuirass,
    Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Runeforged Hammer,
    Spirit Robe, Chandra''s Grace, Eye of the Storm, Phoenix Feather, Spectral Armor,
    Genji''s Guard, Avenging Blade, Bloodforge, Erosion, Tyrfing, Tekko-Kagi, Breastplate
    of Valor, Glorious Pridwen, Mantle Of Discord, Devourer''s Gauntlet, Lernaean
    Bow, Berserker''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.54
      win: 0.55
      pick: 0.65
      fit: 0.44
    The Reaper:
      total: 0.48
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.7
    The Crusher:
      total: 0.47
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.5
    Heartseeker:
      total: 0.46
      efficiency: 0.27
      win: 0.62
      pick: 0.31
      fit: 0.5
    Titan's Bane:
      total: 0.5
      efficiency: 0.36
      win: 0.66
      pick: 0.27
      fit: 0.4
    Amanita Charm:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.65
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
  - The Reaper
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
    for this god: The Crusher, The Reaper, Tekko-Kagi, Avenging Blade, Pendulum Blade,
    Hydra''s Lament, Runeforged Hammer, Oath-Sworn Spear, Shield Splitter, Tyrfing,
    Lernaean Bow, Eye of the Storm, Golden Blade, Screeching Gargoyle, Riptalon, Damaru,
    Arondight, Spectral Armor, Rage, Avatar''s Parashu, Genji''s Guard, Kinetic Cuirass,
    Eye of Providence.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.54
      win: 0.55
      pick: 0.65
      fit: 1.0
    The Reaper:
      total: 0.52
      efficiency: 0.43
      win: 0.5
      pick: 0.0
      fit: 0.94
    Tekko-Kagi:
      total: 0.49
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.94
    The Crusher:
      total: 0.54
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.54
      efficiency: 0.27
      win: 0.62
      pick: 0.31
      fit: 1.0
    Titan's Bane:
      total: 0.58
      efficiency: 0.36
      win: 0.66
      pick: 0.27
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
      pick: 0.65
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
