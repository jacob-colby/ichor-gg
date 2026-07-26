---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.18
  aspect_win_rate: 0.49
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.3
    win_rate: 0.58
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.24
      win_rate: 0.56
    - name: Golden Blade
      pick_rate: 0.11
      win_rate: 0.49
  - name: Shifter's Shield
    pick_rate: 0.17
    win_rate: 0.58
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.17
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.13
      win_rate: 0.55
  - name: The Reaper
    pick_rate: 0.09
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.49
    - name: Hydra's Lament
      pick_rate: 0.09
      win_rate: 0.68
  - name: Titan's Bane
    pick_rate: 0.18
    win_rate: 0.6
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.59
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.09
    win_rate: 0.74
    alternates:
    - name: Titan's Bane
      pick_rate: 0.15
      win_rate: 0.48
    - name: Dwarven Plate
      pick_rate: 0.06
      win_rate: 0.56
  - name: Blinking Abyss
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.76
    - name: Lucerne Hammer
      pick_rate: 0.06
      win_rate: 0.71
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-07-25'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Heartseeker, The Crusher, The Reaper, Tekko-Kagi, Tyrfing, Lernaean
    Bow, Hydra''s Lament, Golden Blade, Runeforged Hammer, Damaru, Avenging Blade,
    Rage, Shield Splitter, Berserker''s Shield, Demon Blade, Eye of the Storm, Transcendence,
    Musashi''s Dual Swords, Pendulum Blade, Spectral Armor, Pharaoh''s Curse, Eros''
    Bow, Kinetic Cuirass, Genji''s Guard, Arondight, Barbed Carver.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.54
      win: 0.58
      pick: 0.3
      fit: 0.52
    The Reaper:
      total: 0.47
      efficiency: 0.43
      win: 0.53
      pick: 0.09
      fit: 0.47
    Tekko-Kagi:
      total: 0.46
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.74
    The Crusher:
      total: 0.48
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.57
    Heartseeker:
      total: 0.52
      efficiency: 0.27
      win: 0.74
      pick: 0.09
      fit: 0.57
    Titan's Bane:
      total: 0.48
      efficiency: 0.36
      win: 0.6
      pick: 0.18
      fit: 0.47
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
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
  - Titan's Bane
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
    this god: The Reaper, Amanita Charm, The Crusher, Shield Splitter, Shield of the
    Phoenix, Kinetic Cuirass, Eye of Providence, Chandra''s Grace, Hydra''s Lament,
    Runeforged Hammer, Phoenix Feather, Tyrfing, Berserker''s Shield, Spectral Armor,
    Spirit Robe, Lernaean Bow, Tekko-Kagi, Genji''s Guard, Golden Blade, Eye of the
    Storm, Avenging Blade, Bloodforge, Riptalon, Pharaoh''s Curse, Damaru, Erosion,
    Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.54
      win: 0.58
      pick: 0.3
      fit: 0.31
    The Reaper:
      total: 0.48
      efficiency: 0.43
      win: 0.53
      pick: 0.09
      fit: 0.58
    The Crusher:
      total: 0.45
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.38
    Heartseeker:
      total: 0.49
      efficiency: 0.27
      win: 0.74
      pick: 0.09
      fit: 0.38
    Titan's Bane:
      total: 0.45
      efficiency: 0.36
      win: 0.6
      pick: 0.18
      fit: 0.28
    Amanita Charm:
      total: 0.46
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.55
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Heartseeker, The Crusher, The Reaper, Tekko-Kagi, Avenging Blade,
    Hydra''s Lament, Tyrfing, Runeforged Hammer, Lernaean Bow, Oath-Sworn Spear, Golden
    Blade, Pendulum Blade, Damaru, Shield Splitter, Riptalon, Screeching Gargoyle,
    Berserker''s Shield, Rage, Spectral Armor, Eye of the Storm, Kinetic Cuirass,
    Genji''s Guard, Transcendence, Eye of Providence, Void Stone, Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.54
      win: 0.58
      pick: 0.3
      fit: 0.64
    The Reaper:
      total: 0.48
      efficiency: 0.43
      win: 0.53
      pick: 0.09
      fit: 0.6
    Tekko-Kagi:
      total: 0.46
      efficiency: 0.34
      win: 0.5
      pick: 0.0
      fit: 0.8
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Heartseeker:
      total: 0.54
      efficiency: 0.27
      win: 0.74
      pick: 0.09
      fit: 0.7
    Titan's Bane:
      total: 0.5
      efficiency: 0.36
      win: 0.6
      pick: 0.18
      fit: 0.6
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
      win: 0.58
      pick: 0.3
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
