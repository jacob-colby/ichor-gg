---
type: smite-build
god: Tsukuyomi
mode: Conquest
builds:
- source: community
  aspect: Aspect of Mangetsu
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.38
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.37
    win_rate: 0.55
    alternates:
    - name: Transcendence
      pick_rate: 0.32
      win_rate: 0.56
    - name: Spear of Desolation
      pick_rate: 0.14
      win_rate: 0.52
  - name: Transcendence
    pick_rate: 0.19
    win_rate: 0.54
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.14
      win_rate: 0.66
    - name: Hydra's Lament
      pick_rate: 0.14
      win_rate: 0.62
  - name: Hydra's Lament
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.53
    - name: The Reaper
      pick_rate: 0.11
      win_rate: 0.55
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.65
    alternates:
    - name: Titan's Bane
      pick_rate: 0.21
      win_rate: 0.48
    - name: Rod of Tahuti
      pick_rate: 0.09
      win_rate: 0.55
  - name: Titan's Bane
    pick_rate: 0.21
    win_rate: 0.63
    alternates:
    - name: Heartseeker
      pick_rate: 0.15
      win_rate: 0.58
    - name: Lucerne Hammer
      pick_rate: 0.05
      win_rate: 0.48
  - name: Blinking Abyss
    pick_rate: 0.08
    win_rate: 0.68
    alternates:
    - name: Titan's Bane
      pick_rate: 0.08
      win_rate: 0.63
    - name: Lucerne Hammer
      pick_rate: 0.08
      win_rate: 0.53
  source_url: https://smitebrain.com/gods/tsukuyomi/
  last_verified: '2026-07-23'
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Tekko-Kagi
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Hydra's Lament
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
    this god: The Crusher, Tekko-Kagi, Tyrfing, The Reaper, Lernaean Bow, Golden Blade,
    Runeforged Hammer, Damaru, Avenging Blade, Rage, Shield Splitter, Berserker''s
    Shield, Demon Blade, Eye of the Storm, Pendulum Blade, Musashi''s Dual Swords,
    Spectral Armor, Pharaoh''s Curse, Arondight, Kinetic Cuirass, Barbed Carver, Eros''
    Bow, Genji''s Guard.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.37
      fit: 0.52
    Hydra's Lament:
      total: 0.48
      efficiency: 0.45
      win: 0.56
      pick: 0.17
      fit: 0.41
    Tekko-Kagi:
      total: 0.46
      efficiency: 0.35
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
      total: 0.49
      efficiency: 0.28
      win: 0.65
      pick: 0.22
      fit: 0.57
    Titan's Bane:
      total: 0.49
      efficiency: 0.37
      win: 0.63
      pick: 0.21
      fit: 0.47
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
  - The Crusher
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
    god: The Crusher, The Reaper, Tekko-Kagi, Tyrfing, Runeforged Hammer, Lernaean
    Bow, Genji''s Guard, Pendulum Blade, Golden Blade, Avenging Blade, Shield Splitter,
    Damaru, Chandra''s Grace, Berserker''s Shield, Arondight, Spectral Armor, Breastplate
    of Valor, Kinetic Cuirass, Rage, Eye of the Storm, Eye of Providence, Shield of
    the Phoenix, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.55
      win: 0.55
      pick: 0.37
      fit: 0.56
    Hydra's Lament:
      total: 0.48
      efficiency: 0.45
      win: 0.56
      pick: 0.17
      fit: 0.42
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
    Heartseeker:
      total: 0.48
      efficiency: 0.28
      win: 0.65
      pick: 0.22
      fit: 0.5
    Titan's Bane:
      total: 0.48
      efficiency: 0.37
      win: 0.63
      pick: 0.21
      fit: 0.4
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - The Reaper
  - Heartseeker
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
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
    Phoenix, Kinetic Cuirass, Eye of Providence, Chandra''s Grace, Tyrfing, Spirit
    Robe, Runeforged Hammer, Phoenix Feather, Berserker''s Shield, Spectral Armor,
    Lernaean Bow, Tekko-Kagi, Genji''s Guard, Bloodforge, Eye of the Storm, Golden
    Blade, Avenging Blade, Riptalon, Damaru, Pharaoh''s Curse, Erosion, Breastplate
    of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.55
      win: 0.55
      pick: 0.37
      fit: 0.31
    Hydra's Lament:
      total: 0.46
      efficiency: 0.45
      win: 0.56
      pick: 0.17
      fit: 0.28
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.58
    Heartseeker:
      total: 0.46
      efficiency: 0.28
      win: 0.65
      pick: 0.22
      fit: 0.38
    Titan's Bane:
      total: 0.46
      efficiency: 0.37
      win: 0.63
      pick: 0.21
      fit: 0.28
    Amanita Charm:
      total: 0.46
      efficiency: 0.45
      win: 0.5
      pick: 0.0
      fit: 0.55
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
  - The Reaper
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    for this god: The Crusher, The Reaper, Tekko-Kagi, Avenging Blade, Tyrfing, Oath-Sworn
    Spear, Runeforged Hammer, Lernaean Bow, Pendulum Blade, Golden Blade, Damaru,
    Screeching Gargoyle, Shield Splitter, Riptalon, Rage, Berserker''s Shield, Spectral
    Armor, Eye of the Storm, Kinetic Cuirass, Genji''s Guard, Void Stone, Eye of Providence,
    Pharaoh''s Curse.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.55
      win: 0.55
      pick: 0.37
      fit: 0.64
    Hydra's Lament:
      total: 0.47
      efficiency: 0.45
      win: 0.56
      pick: 0.17
      fit: 0.33
    The Reaper:
      total: 0.47
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.5
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.7
    Heartseeker:
      total: 0.51
      efficiency: 0.28
      win: 0.65
      pick: 0.22
      fit: 0.7
    Titan's Bane:
      total: 0.51
      efficiency: 0.37
      win: 0.63
      pick: 0.21
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
      win: 0.55
      pick: 0.37
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
