---
type: smite-build
god: Osiris
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Fragmented
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.61
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.52
    alternates:
    - name: Golden Blade
      pick_rate: 0.12
      win_rate: 0.57
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.38
  - name: Berserker's Shield
    pick_rate: 0.35
    win_rate: 0.52
    alternates:
    - name: Golden Blade
      pick_rate: 0.1
      win_rate: 0.42
    - name: Kinetic Cuirass
      pick_rate: 0.1
      win_rate: 0.5
  - name: Kinetic Cuirass
    pick_rate: 0.21
    win_rate: 0.48
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.21
      win_rate: 0.36
    - name: Shogun's Ofuda
      pick_rate: 0.13
      win_rate: 0.47
  - name: Dwarven Plate
    pick_rate: 0.18
    win_rate: 0.55
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.5
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.4
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.12
      win_rate: 0.58
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.57
  - name: Veve Charm
    pick_rate: 0.12
    win_rate: 0.57
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 1.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.4
  source_url: https://smitebrain.com/gods/osiris/
  last_verified: '2026-08-01'
  god_win_rate: 0.5083333333333333
  god_matches_won: 61
  god_matches_played: 120
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Runeforged Hammer
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, Runeforged Hammer, The Crusher, Jotunn''s
    Revenge, Lernaean Bow, Eye of Providence, Pharaoh''s Curse, Genji''s Guard, Oni
    Hunter''s Garb, Hydra''s Lament, Damaru, Eye of the Storm, Avenging Blade, Shield
    Splitter, Dominance, Yogi''s Necklace, Breastplate of Valor, Tyrfing, Spectral
    Armor, Shogun''s Ofuda, Shield of the Phoenix, Freya''s Tears, Erosion, Eros''
    Bow, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.12
      fit: 0.57
    Berserker's Shield:
      total: 0.57
      efficiency: 0.71
      win: 0.52
      pick: 0.35
      fit: 0.45
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    Shifter's Shield:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.53
      fit: 0.35
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Golden Blade, Shield of the Phoenix, Eye of Providence,
    Runeforged Hammer, The Crusher, Genji''s Guard, Oni Hunter''s Garb, Pharaoh''s
    Curse, Riptalon, The Reaper, Jotunn''s Revenge, Lernaean Bow, Chandra''s Grace,
    Hydra''s Lament, Eye of the Storm, Shield Splitter, Damaru, Phoenix Feather, Spectral
    Armor, Breastplate of Valor, Erosion, Avenging Blade, Yogi''s Necklace, Freya''s
    Tears, Shogun''s Ofuda.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.56
      win: 0.57
      pick: 0.12
      fit: 0.53
    Berserker's Shield:
      total: 0.57
      efficiency: 0.71
      win: 0.52
      pick: 0.35
      fit: 0.47
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.48
      pick: 0.21
      fit: 0.54
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.52
      efficiency: 0.56
      win: 0.52
      pick: 0.53
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Jotunn''s Revenge, Golden Blade, Avenging Blade, Amanita
    Charm, Runeforged Hammer, Genji''s Guard, Riptalon, Eye of Providence, Lernaean
    Bow, The Reaper, Oni Hunter''s Garb, Hydra''s Lament, Silverbranch Bow, Tekko-Kagi,
    Void Shield, Pharaoh''s Curse, Stone of Binding, Damaru, Screeching Gargoyle,
    Void Stone, Heartseeker, Yogi''s Necklace, Breastplate of Valor, Eye of the Storm,
    Spectral Armor, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.56
      win: 0.57
      pick: 0.12
      fit: 0.42
    Avenging Blade:
      total: 0.51
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.52
      pick: 0.35
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.5
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Riptalon
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, Riptalon, The Crusher, Genji''s Guard,
    Pharaoh''s Curse, Lernaean Bow, Runeforged Hammer, Eye of Providence, Tyrfing,
    Oni Hunter''s Garb, Jotunn''s Revenge, Silverbranch Bow, Hydra''s Lament, Yogi''s
    Necklace, Damaru, Breastplate of Valor, Shogun''s Ofuda, Dominance, Spectral Armor,
    Shield of the Phoenix, Avenging Blade, Eye of the Storm, Eros'' Bow, Freya''s
    Tears, Shield Splitter.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.12
      fit: 0.6
    Berserker's Shield:
      total: 0.56
      efficiency: 0.71
      win: 0.52
      pick: 0.35
      fit: 0.41
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.48
      pick: 0.21
      fit: 0.36
    Shifter's Shield:
      total: 0.5
      efficiency: 0.56
      win: 0.52
      pick: 0.53
      fit: 0.26
    Riptalon:
      total: 0.49
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.5
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  flex_slots:
  - Hydra's Lament
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Jotunn''s Revenge,
    Golden Blade, Hydra''s Lament, Breastplate of Valor, Shield of the Phoenix, Amanita
    Charm, Freya''s Tears, The Crusher, Eye of Providence, Runeforged Hammer, Oni
    Hunter''s Garb, Pharaoh''s Curse, Chandra''s Grace, Lernaean Bow, Yogi''s Necklace,
    Screeching Gargoyle, Damaru, Spectral Armor, Gladiator''s Shield, Arondight, Avenging
    Blade, Shogun''s Ofuda, Eye of the Storm, Shield Splitter, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.56
      win: 0.57
      pick: 0.12
      fit: 0.34
    Genji's Guard:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.55
      efficiency: 0.71
      win: 0.52
      pick: 0.35
      fit: 0.33
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.4
    Hydra's Lament:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Golden Blade
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Runeforged Hammer, The Crusher, Golden
    Blade, Jotunn''s Revenge, Lernaean Bow, Eye of Providence, Pharaoh''s Curse, Genji''s
    Guard, Oni Hunter''s Garb, Hydra''s Lament, Damaru, Eye of the Storm, Avenging
    Blade, Shield Splitter, Shogun''s Ofuda, Dominance, Yogi''s Necklace, Breastplate
    of Valor, Tyrfing, Spectral Armor, Shield of the Phoenix, Freya''s Tears, Erosion,
    Eros'' Bow, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.12
      fit: 0.57
    Berserker's Shield:
      total: 0.57
      efficiency: 0.71
      win: 0.52
      pick: 0.35
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.48
      pick: 0.21
      fit: 0.45
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.51
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.35
  starter: *id001
---
