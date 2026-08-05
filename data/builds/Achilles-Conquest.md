---
type: smite-build
god: Achilles
mode: Conquest
builds:
- source: community
  aspect: Aspect of Prowess
  aspect_pick_rate: 0.06
  aspect_win_rate: 0.4
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.56
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.22
      win_rate: 0.59
    - name: Avenging Blade
      pick_rate: 0.12
      win_rate: 0.42
  - name: Daybreak Gavel
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.46
    - name: Gladiator's Shield
      pick_rate: 0.12
      win_rate: 0.65
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.47
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.58
  - name: Dwarven Plate
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.7
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.41
  - name: Glorious Pridwen
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.7
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.5
  - name: Medal of Defense
    pick_rate: 0.05
    win_rate: 0.56
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.07
      win_rate: 0.64
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.71
  source_url: https://smitebrain.com/gods/achilles/
  last_verified: '2026-08-01'
  god_win_rate: 0.5236220472440944
  god_matches_won: 133
  god_matches_played: 254
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
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Runeforged Hammer, Jotunn''s Revenge, Kinetic Cuirass,
    Berserker''s Shield, Avenging Blade, Amanita Charm, Hydra''s Lament, Oni Hunter''s
    Garb, Eye of the Storm, Eye of Providence, Golden Blade, Shield Splitter, Lernaean
    Bow, Spectral Armor, The Reaper, Heartseeker, Yogi''s Necklace, Pharaoh''s Curse,
    Damaru, Shield of the Phoenix, Wyrmskin Hide, Avatar''s Parashu, Erosion, Draconic
    Scale, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.74
      win: 0.54
      pick: 0.16
      fit: 0.17
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shifter's Shield:
      total: 0.54
      efficiency: 0.58
      win: 0.56
      pick: 0.32
      fit: 0.46
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Kinetic Cuirass,
    The Crusher, Berserker''s Shield, The Reaper, Jotunn''s Revenge, Eye of Providence,
    Oni Hunter''s Garb, Avenging Blade, Hydra''s Lament, Eye of the Storm, Chandra''s
    Grace, Shield Splitter, Spectral Armor, Golden Blade, Riptalon, Phoenix Feather,
    Pharaoh''s Curse, Erosion, Lernaean Bow, Draconic Scale, Yogi''s Necklace, Bloodforge,
    Mantle Of Discord.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.72
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.55
      efficiency: 0.58
      win: 0.56
      pick: 0.32
      fit: 0.55
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Reaper
  - The Crusher
  flex_slots:
  - Genji's Guard
  - The Reaper
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Avenging Blade, Runeforged Hammer,
    The Reaper, Berserker''s Shield, Hydra''s Lament, Kinetic Cuirass, Heartseeker,
    Amanita Charm, Avatar''s Parashu, Oni Hunter''s Garb, Eye of Providence, Golden
    Blade, Eye of the Storm, Lernaean Bow, Spectral Armor, Void Shield, Titan''s Bane,
    Riptalon, Tekko-Kagi, Yogi''s Necklace, Shield Splitter, Damaru, Pendulum Blade,
    Pharaoh''s Curse, Void Stone.'
  slot_scores:
    Avenging Blade:
      total: 0.56
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.78
    Genji's Guard:
      total: 0.53
      efficiency: 0.74
      win: 0.54
      pick: 0.16
      fit: 0.13
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.65
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Reaper:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.61
    The Crusher:
      total: 0.58
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Runeforged Hammer
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Golden Blade, Riptalon, The Crusher, Runeforged
    Hammer, Lernaean Bow, Pharaoh''s Curse, Jotunn''s Revenge, Kinetic Cuirass, Amanita
    Charm, Hydra''s Lament, Oni Hunter''s Garb, Tyrfing, Avenging Blade, Eye of Providence,
    Shogun''s Ofuda, Spectral Armor, Yogi''s Necklace, Eros'' Bow, The Reaper, Eye
    of the Storm, Breastplate of Valor, Shield of the Phoenix, Damaru, Tekko-Kagi,
    Shield Splitter, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.62
    Genji's Guard:
      total: 0.52
      efficiency: 0.74
      win: 0.54
      pick: 0.16
      fit: 0.1
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.43
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.34
    Riptalon:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Hydra's Lament
  - The Crusher
  flex_slots:
  - Breastplate of Valor
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Shield of the Phoenix, Breastplate of Valor, The Crusher, Runeforged Hammer, Berserker''s
    Shield, Kinetic Cuirass, Freya''s Tears, Amanita Charm, Chandra''s Grace, Oni
    Hunter''s Garb, Eye of Providence, Arondight, Avenging Blade, Spectral Armor,
    Yogi''s Necklace, Gladiator''s Shield, Pharaoh''s Curse, Lernaean Bow, Golden
    Blade, Screeching Gargoyle, Eye of the Storm, Pendulum Blade, Mantle Of Discord,
    Shield Splitter.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.74
      win: 0.54
      pick: 0.16
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.59
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.57
    Hydra's Lament:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Avenging Blade
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Runeforged Hammer, Jotunn''s Revenge, Kinetic
    Cuirass, Berserker''s Shield, Avenging Blade, Amanita Charm, Hydra''s Lament,
    Oni Hunter''s Garb, Eye of the Storm, Eye of Providence, Golden Blade, Shield
    Splitter, Lernaean Bow, Spectral Armor, The Reaper, Heartseeker, Yogi''s Necklace,
    Pharaoh''s Curse, Damaru, Shield of the Phoenix, Wyrmskin Hide, Avatar''s Parashu,
    Erosion, Draconic Scale, Breastplate of Valor.'
  slot_scores:
    Avenging Blade:
      total: 0.53
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.56
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
    The Crusher:
      total: 0.56
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.59
  starter: *id001
---
