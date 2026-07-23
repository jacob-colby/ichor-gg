---
type: smite-build
god: Ratatoskr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Thickbark
  aspect_pick_rate: 0.42
  aspect_win_rate: 0.47
  slot_order:
  - name: Thistlethorn Acorn
    pick_rate: 0.33
    win_rate: 0.49
    alternates:
    - name: Ashwhorl Acorn
      pick_rate: 0.27
      win_rate: 0.49
    - name: Briskberry Acorn
      pick_rate: 0.18
      win_rate: 0.36
  - name: Briskberry Acorn
    pick_rate: 0.36
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.34
    - name: Ashwhorl Acorn
      pick_rate: 0.09
      win_rate: 0.41
  - name: Jotunn's Revenge
    pick_rate: 0.17
    win_rate: 0.37
    alternates:
    - name: Briskberry Acorn
      pick_rate: 0.13
      win_rate: 0.45
    - name: Thistlethorn Acorn
      pick_rate: 0.11
      win_rate: 0.49
  - name: Heartseeker
    pick_rate: 0.16
    win_rate: 0.55
    alternates:
    - name: Titan's Bane
      pick_rate: 0.1
      win_rate: 0.45
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.48
  - name: Titan's Bane
    pick_rate: 0.14
    win_rate: 0.48
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.63
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.42
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.67
  source_url: https://smitebrain.com/gods/ratatoskr/
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
  - Hydra's Lament
  - Titan's Bane
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
    this god: The Crusher, The Reaper, Hydra''s Lament, Titan''s Bane, Tekko-Kagi,
    Pendulum Blade, Runeforged Hammer, Avenging Blade, Shield Splitter, Tyrfing, Eye
    of the Storm, Lernaean Bow, Transcendence, Arondight, Golden Blade, Damaru, Barbed
    Carver, Oath-Sworn Spear, Rage, Bloodforge, Wyrmskin Hide, Musashi''s Dual Swords,
    Devourer''s Gauntlet, Genji''s Guard, Spectral Armor, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.37
      pick: 0.17
      fit: 1.0
    Hydra's Lament:
      total: 0.49
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.71
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.91
    The Crusher:
      total: 0.55
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 1.0
    Heartseeker:
      total: 0.5
      efficiency: 0.28
      win: 0.55
      pick: 0.16
      fit: 1.0
    Titan's Bane:
      total: 0.49
      efficiency: 0.37
      win: 0.48
      pick: 0.14
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
  - Pendulum Blade
  - The Crusher
  - Heartseeker
  flex_slots:
  - Heartseeker
  - Pendulum Blade
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
    god: The Crusher, Hydra''s Lament, The Reaper, Pendulum Blade, Titan''s Bane,
    Runeforged Hammer, Tekko-Kagi, Genji''s Guard, Avenging Blade, Arondight, Shield
    Splitter, Chandra''s Grace, Tyrfing, Breastplate of Valor, Eye of the Storm, Lernaean
    Bow, Shield of the Phoenix, Transcendence, Spectral Armor, Golden Blade, Kinetic
    Cuirass, Screeching Gargoyle, Damaru, Eye of Providence, Barbed Carver, Oath-Sworn
    Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.55
      win: 0.37
      pick: 0.17
      fit: 0.78
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.54
    The Reaper:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.56
    Pendulum Blade:
      total: 0.44
      efficiency: 0.29
      win: 0.5
      pick: 0.0
      fit: 0.78
    The Crusher:
      total: 0.49
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.66
    Heartseeker:
      total: 0.45
      efficiency: 0.28
      win: 0.55
      pick: 0.16
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Shield Splitter
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: The Reaper, Amanita Charm, The Crusher, Shield Splitter, Kinetic Cuirass,
    Shield of the Phoenix, Eye of Providence, Hydra''s Lament, Spirit Robe, Runeforged
    Hammer, Phoenix Feather, Eye of the Storm, Chandra''s Grace, Spectral Armor, Bloodforge,
    Genji''s Guard, Avenging Blade, Erosion, Titan''s Bane, Tyrfing, Devourer''s Gauntlet,
    Glorious Pridwen, Tekko-Kagi, Shroud of Vengeance, Mantle Of Discord, Breastplate
    of Valor, Lernaean Bow.'
  slot_scores:
    Eye of Providence:
      total: 0.44
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.34
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shield Splitter:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.57
    The Reaper:
      total: 0.48
      efficiency: 0.44
      win: 0.5
      pick: 0.0
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
  - Titan's Bane
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
    for this god: The Crusher, The Reaper, Titan''s Bane, Tekko-Kagi, Avenging Blade,
    Pendulum Blade, Hydra''s Lament, Oath-Sworn Spear, Runeforged Hammer, Shield Splitter,
    Tyrfing, Eye of the Storm, Lernaean Bow, Transcendence, Screeching Gargoyle, Riptalon,
    Golden Blade, Damaru, Arondight, Barbed Carver, Rage, Avatar''s Parashu, Spectral
    Armor, Genji''s Guard, Kinetic Cuirass, Void Stone.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.55
      win: 0.37
      pick: 0.17
      fit: 1.0
    The Reaper:
      total: 0.52
      efficiency: 0.44
      win: 0.5
      pick: 0.0
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
      total: 0.5
      efficiency: 0.28
      win: 0.55
      pick: 0.16
      fit: 1.0
    Titan's Bane:
      total: 0.49
      efficiency: 0.37
      win: 0.48
      pick: 0.14
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
      win: 0.37
      pick: 0.17
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
