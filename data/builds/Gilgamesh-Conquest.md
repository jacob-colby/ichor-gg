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
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Runeforged Hammer
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shogun''s Ofuda, The Crusher, Runeforged Hammer, Jotunn''s Revenge,
    Lernaean Bow, Golden Blade, Hydra''s Lament, Amanita Charm, Avenging Blade, Pharaoh''s
    Curse, Oni Hunter''s Garb, Damaru, Genji''s Guard, Eye of Providence, Eye of the
    Storm, Spectral Armor, Yogi''s Necklace, Shield Splitter, Riptalon, The Reaper,
    Eros'' Bow, Shield of the Phoenix, Tekko-Kagi, Breastplate of Valor, Tyrfing,
    Heartseeker, Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.51
      pick: 0.22
      fit: 0.4
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.57
      win: 0.71
      pick: 0.07
      fit: 0.23
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    Shogun's Ofuda:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.4
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Runeforged Hammer
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shogun''s Ofuda, Runeforged Hammer, Shield of the Phoenix,
    The Crusher, Riptalon, The Reaper, Jotunn''s Revenge, Golden Blade, Lernaean Bow,
    Oni Hunter''s Garb, Pharaoh''s Curse, Eye of Providence, Hydra''s Lament, Chandra''s
    Grace, Avenging Blade, Genji''s Guard, Damaru, Spectral Armor, Eye of the Storm,
    Shield Splitter, Yogi''s Necklace, Phoenix Feather, Bloodforge, Mantle Of Discord,
    Kinetic Cuirass.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.51
      pick: 0.22
      fit: 0.43
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.6
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.57
      win: 0.71
      pick: 0.07
      fit: 0.28
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.7
    Shogun's Ofuda:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - The Crusher
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, Jotunn''s Revenge, Shogun''s Ofuda,
    Runeforged Hammer, Lernaean Bow, Hydra''s Lament, Golden Blade, Amanita Charm,
    Riptalon, The Reaper, Oni Hunter''s Garb, Pharaoh''s Curse, Genji''s Guard, Damaru,
    Heartseeker, Tekko-Kagi, Eye of Providence, Yogi''s Necklace, Avatar''s Parashu,
    Spectral Armor, Void Shield, Eye of the Storm, Shield Splitter, Breastplate of
    Valor, Void Stone, Kinetic Cuirass.'
  slot_scores:
    Avenging Blade:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.68
    Berserker's Shield:
      total: 0.55
      efficiency: 0.74
      win: 0.51
      pick: 0.22
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.57
      win: 0.71
      pick: 0.07
      fit: 0.19
    The Crusher:
      total: 0.55
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shogun's Ofuda:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Hide of the Nemean Lion
  - Runeforged Hammer
  - The Crusher
  - Shogun's Ofuda
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
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shogun''s Ofuda, Golden Blade, The Crusher, Runeforged Hammer, Riptalon,
    Lernaean Bow, Pharaoh''s Curse, Jotunn''s Revenge, Hydra''s Lament, Amanita Charm,
    Oni Hunter''s Garb, Genji''s Guard, Avenging Blade, Eye of Providence, Tyrfing,
    Damaru, Yogi''s Necklace, Spectral Armor, Eros'' Bow, The Reaper, Breastplate
    of Valor, Eye of the Storm, Shield of the Phoenix, Mantle Of Discord, Shield Splitter,
    Tekko-Kagi, Kinetic Cuirass.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.51
      pick: 0.22
      fit: 0.38
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.57
      win: 0.71
      pick: 0.07
      fit: 0.18
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.32
    The Crusher:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.32
    Shogun's Ofuda:
      total: 0.54
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Hydra's Lament
  - Hide of the Nemean Lion
  - Shogun's Ofuda
  flex_slots:
  - Genji's Guard
  - Shogun's Ofuda
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Genji''s Guard, Shogun''s Ofuda, The Crusher, Runeforged Hammer, Breastplate of
    Valor, Shield of the Phoenix, Amanita Charm, Lernaean Bow, Oni Hunter''s Garb,
    Pharaoh''s Curse, Freya''s Tears, Chandra''s Grace, Golden Blade, Eye of Providence,
    Avenging Blade, Yogi''s Necklace, Spectral Armor, Damaru, Arondight, Riptalon,
    Eros'' Bow, Mantle Of Discord, Gladiator''s Shield, Eye of the Storm, Kinetic
    Cuirass.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.54
      efficiency: 0.74
      win: 0.51
      pick: 0.22
      fit: 0.3
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.44
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.57
      win: 0.71
      pick: 0.07
      fit: 0.17
    Shogun's Ofuda:
      total: 0.53
      efficiency: 0.57
      win: 0.62
      pick: 0.12
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Golden Blade
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Runeforged Hammer
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Golden Blade
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
    Underrated for this god: The Crusher, Runeforged Hammer, Jotunn''s Revenge, Lernaean
    Bow, Golden Blade, Hydra''s Lament, Kinetic Cuirass, Amanita Charm, Avenging Blade,
    Pharaoh''s Curse, Oni Hunter''s Garb, Damaru, Genji''s Guard, Eye of Providence,
    Eye of the Storm, Spectral Armor, Yogi''s Necklace, Shogun''s Ofuda, Shield Splitter,
    Riptalon, The Reaper, Eros'' Bow, Shield of the Phoenix, Tekko-Kagi, Breastplate
    of Valor, Tyrfing, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.51
    Lernaean Bow:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Berserker's Shield:
      total: 0.56
      efficiency: 0.74
      win: 0.51
      pick: 0.22
      fit: 0.4
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.37
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
---
