---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.36
  aspect_win_rate: 0.55
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.31
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.21
      win_rate: 0.58
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.55
  - name: Berserker's Shield
    pick_rate: 0.22
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.2
      win_rate: 0.53
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.42
  - name: Shogun's Ofuda
    pick_rate: 0.12
    win_rate: 0.62
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.14
      win_rate: 0.54
    - name: Barbed Carver
      pick_rate: 0.09
      win_rate: 0.6
  - name: Dwarven Plate
    pick_rate: 0.12
    win_rate: 0.65
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.5
    - name: Berserker's Shield
      pick_rate: 0.08
      win_rate: 0.46
  - name: Kinetic Cuirass
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.83
    - name: Contagion
      pick_rate: 0.05
      win_rate: 1.0
  - name: Hide of the Nemean Lion
    pick_rate: 0.07
    win_rate: 0.71
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.4
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.6
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-08-01'
  god_win_rate: 0.547486033519553
  god_matches_won: 98
  god_matches_played: 179
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shogun''s Ofuda, The Crusher, Amanita Charm, Runeforged Hammer, Lernaean
    Bow, Eye of Providence, Oni Hunter''s Garb, Pharaoh''s Curse, Hydra''s Lament,
    Damaru, Yogi''s Necklace, Breastplate of Valor, Eye of the Storm, Avenging Blade,
    Shield Splitter, Dominance, Riptalon, Spectral Armor, Shield of the Phoenix, Tekko-Kagi,
    The Reaper, Tyrfing, Genji''s Guard, Freya''s Tears, Kinetic Cuirass.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.05
      fit: 0.24
    Golden Blade:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.16
      fit: 0.51
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.21
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.71
      pick: 0.07
      fit: 0.23
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.12
      fit: 0.4
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shogun''s Ofuda, Shield of the Phoenix, The Crusher,
    Riptalon, Eye of Providence, The Reaper, Runeforged Hammer, Oni Hunter''s Garb,
    Pharaoh''s Curse, Lernaean Bow, Chandra''s Grace, Hydra''s Lament, Damaru, Breastplate
    of Valor, Eye of the Storm, Shield Splitter, Yogi''s Necklace, Phoenix Feather,
    Spectral Armor, Freya''s Tears, Avenging Blade, Erosion, Genji''s Guard, Kinetic
    Cuirass.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.05
      fit: 0.25
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.21
      fit: 0.32
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.54
      win: 0.71
      pick: 0.07
      fit: 0.28
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.12
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - The Crusher
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Shogun''s Ofuda, Avenging Blade, Amanita Charm, Runeforged
    Hammer, Riptalon, Oni Hunter''s Garb, Eye of Providence, Lernaean Bow, Hydra''s
    Lament, The Reaper, Silverbranch Bow, Pharaoh''s Curse, Void Shield, Tekko-Kagi,
    Damaru, Stone of Binding, Screeching Gargoyle, Heartseeker, Breastplate of Valor,
    Yogi''s Necklace, Void Stone, Spectral Armor, Eye of the Storm, Genji''s Guard,
    Kinetic Cuirass.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.05
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.21
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.71
      pick: 0.07
      fit: 0.19
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shogun's Ofuda:
      total: 0.52
      efficiency: 0.53
      win: 0.62
      pick: 0.12
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Shogun's Ofuda
  flex_slots:
  - Golden Blade
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shogun''s Ofuda, The Crusher, Riptalon, Amanita Charm, Pharaoh''s Curse,
    Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Oni Hunter''s Garb, Eye of
    Providence, Tyrfing, Hydra''s Lament, Breastplate of Valor, Yogi''s Necklace,
    Damaru, Spectral Armor, Dominance, Genji''s Guard, Toxic Blade, Shield of the
    Phoenix, The Reaper, Freya''s Tears, Avenging Blade, Eye of the Storm, Kinetic
    Cuirass.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.05
      fit: 0.21
    Golden Blade:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.16
      fit: 0.56
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.38
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.21
      fit: 0.24
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.71
      pick: 0.07
      fit: 0.18
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.53
      win: 0.62
      pick: 0.12
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shogun''s Ofuda, Hydra''s Lament,
    Breastplate of Valor, The Crusher, Genji''s Guard, Amanita Charm, Shield of the
    Phoenix, Freya''s Tears, Oni Hunter''s Garb, Eye of Providence, Runeforged Hammer,
    Pharaoh''s Curse, Yogi''s Necklace, Chandra''s Grace, Lernaean Bow, Damaru, Screeching
    Gargoyle, Spectral Armor, Riptalon, Arondight, Gladiator''s Shield, Silverbranch
    Bow, Avenging Blade, Eye of the Storm, Kinetic Cuirass.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.43
      win: 1.0
      pick: 0.05
      fit: 0.21
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.3
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.58
      pick: 0.21
      fit: 0.45
    Hydra's Lament:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.71
      pick: 0.07
      fit: 0.17
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Amanita Charm, Runeforged Hammer, Kinetic
    Cuirass, Genji''s Guard, Lernaean Bow, Eye of Providence, Oni Hunter''s Garb,
    Pharaoh''s Curse, Hydra''s Lament, Damaru, Yogi''s Necklace, Breastplate of Valor,
    Eye of the Storm, Avenging Blade, Shogun''s Ofuda, Shield Splitter, Dominance,
    Riptalon, Spectral Armor, Shield of the Phoenix, Tekko-Kagi, The Reaper, Tyrfing,
    Freya''s Tears.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.51
      pick: 0.22
      fit: 0.4
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.21
      fit: 0.37
    Kinetic Cuirass:
      total: 0.42
      efficiency: 0.6
      win: 0.33
      pick: 0.06
      fit: 0.42
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.5
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.32
  starter: *id001
---
