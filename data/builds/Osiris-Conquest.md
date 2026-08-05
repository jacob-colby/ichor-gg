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
  - Lernaean Bow
  - Berserker's Shield
  - Kinetic Cuirass
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Runeforged Hammer, Golden Blade, Lernaean Bow, The Crusher, Hydra''s
    Lament, Pharaoh''s Curse, Amanita Charm, Avenging Blade, Jotunn''s Revenge, Damaru,
    Oni Hunter''s Garb, Eye of Providence, Genji''s Guard, Eye of the Storm, Spectral
    Armor, Shogun''s Ofuda, Yogi''s Necklace, Shield Splitter, Eros'' Bow, Shield
    of the Phoenix, Tyrfing, Breastplate of Valor, Mantle Of Discord, Leviathan''s
    Hide, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.52
      pick: 0.35
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.48
      pick: 0.21
      fit: 0.45
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Runeforged Hammer, Shield of the Phoenix, Golden Blade,
    Lernaean Bow, Pharaoh''s Curse, The Crusher, Eye of Providence, Oni Hunter''s
    Garb, Hydra''s Lament, Avenging Blade, Riptalon, The Reaper, Chandra''s Grace,
    Jotunn''s Revenge, Genji''s Guard, Damaru, Spectral Armor, Eye of the Storm, Shield
    Splitter, Shogun''s Ofuda, Phoenix Feather, Yogi''s Necklace, Bloodforge, Mantle
    Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.52
      pick: 0.35
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.48
      pick: 0.21
      fit: 0.54
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.63
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.53
      efficiency: 0.58
      win: 0.52
      pick: 0.53
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.74
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Lernaean Bow
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, Jotunn''s Revenge, Runeforged Hammer,
    Lernaean Bow, Hydra''s Lament, Golden Blade, Amanita Charm, Riptalon, The Reaper,
    Oni Hunter''s Garb, Pharaoh''s Curse, Genji''s Guard, Damaru, Heartseeker, Tekko-Kagi,
    Eye of Providence, Yogi''s Necklace, Avatar''s Parashu, Spectral Armor, Void Shield,
    Eye of the Storm, Shogun''s Ofuda, Shield Splitter, Breastplate of Valor, Void
    Stone.'
  slot_scores:
    Lernaean Bow:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
    Avenging Blade:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.52
      pick: 0.35
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.48
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.38
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Runeforged Hammer
  - Riptalon
  - Pharaoh's Curse
  flex_slots:
  - Pharaoh's Curse
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Runeforged Hammer, Lernaean Bow, Pharaoh''s Curse, Riptalon,
    The Crusher, Hydra''s Lament, Amanita Charm, Oni Hunter''s Garb, Genji''s Guard,
    Jotunn''s Revenge, Avenging Blade, Tyrfing, Eye of Providence, Damaru, Shogun''s
    Ofuda, Spectral Armor, Yogi''s Necklace, Eros'' Bow, Breastplate of Valor, Eye
    of the Storm, Shield of the Phoenix, Shield Splitter, Mantle Of Discord, The Reaper.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Lernaean Bow:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.57
      efficiency: 0.74
      win: 0.52
      pick: 0.35
      fit: 0.41
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.33
    Riptalon:
      total: 0.51
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.48
    Pharaoh's Curse:
      total: 0.51
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Runeforged Hammer
  flex_slots:
  - Runeforged Hammer
  - Breastplate of Valor
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Genji''s Guard, Jotunn''s
    Revenge, Runeforged Hammer, Breastplate of Valor, Shield of the Phoenix, The Crusher,
    Amanita Charm, Lernaean Bow, Oni Hunter''s Garb, Pharaoh''s Curse, Freya''s Tears,
    Chandra''s Grace, Golden Blade, Eye of Providence, Avenging Blade, Arondight,
    Yogi''s Necklace, Spectral Armor, Damaru, Shogun''s Ofuda, Eros'' Bow, Gladiator''s
    Shield, Eye of the Storm, Mantle Of Discord, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.36
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.52
      pick: 0.35
      fit: 0.33
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.4
    Hydra's Lament:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.47
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Hydra's Lament
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - The Crusher
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Runeforged Hammer, Golden Blade, Lernaean Bow, The Crusher,
    Hydra''s Lament, Pharaoh''s Curse, Amanita Charm, Avenging Blade, Jotunn''s Revenge,
    Damaru, Oni Hunter''s Garb, Eye of Providence, Genji''s Guard, Eye of the Storm,
    Spectral Armor, Shogun''s Ofuda, Yogi''s Necklace, Shield Splitter, Eros'' Bow,
    Shield of the Phoenix, Tyrfing, Breastplate of Valor, Mantle Of Discord, Leviathan''s
    Hide, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.57
    Lernaean Bow:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.52
      pick: 0.35
      fit: 0.45
    Hydra's Lament:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.35
    Runeforged Hammer:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.47
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
---
