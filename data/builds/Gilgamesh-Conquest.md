---
type: smite-build
god: Gilgamesh
mode: Conquest
builds:
- source: community
  aspect: Aspect of Shamash
  aspect_pick_rate: 0.41
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.31
    win_rate: 0.52
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.24
      win_rate: 0.56
    - name: Golden Blade
      pick_rate: 0.1
      win_rate: 0.56
  - name: Berserker's Shield
    pick_rate: 0.21
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.23
      win_rate: 0.58
    - name: Barbed Carver
      pick_rate: 0.07
      win_rate: 0.56
  - name: Shogun's Ofuda
    pick_rate: 0.1
    win_rate: 0.51
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.15
      win_rate: 0.54
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.6
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.51
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.57
  - name: Dwarven Plate
    pick_rate: 0.05
    win_rate: 0.62
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.58
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.56
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.64
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.58
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.62
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.48
  - name: Hunter's Cowl
    pick_rate: 0.16
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/gilgamesh/
  last_verified: '2026-08-11'
  god_win_rate: 0.5487804878048781
  god_matches_won: 450
  god_matches_played: 820
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Golden Blade, Amanita Charm, Genji''s Guard, Pharaoh''s
    Curse, Lernaean Bow, Runeforged Hammer, Kinetic Cuirass, Oni Hunter''s Garb, Damaru,
    Hydra''s Lament, Breastplate of Valor, Riptalon, Eye of the Storm, Spectral Armor,
    Shield of the Phoenix, Silverbranch Bow, Freya''s Tears, Shield Splitter, Tekko-Kagi,
    Avenging Blade, Dominance, The Reaper, Tyrfing, Erosion.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.54
      win: 0.56
      pick: 0.1
      fit: 0.51
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.12
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.29
      fit: 0.4
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.24
      fit: 0.37
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.32
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Riptalon, The Crusher, Genji''s
    Guard, The Reaper, Kinetic Cuirass, Golden Blade, Pharaoh''s Curse, Oni Hunter''s
    Garb, Runeforged Hammer, Chandra''s Grace, Breastplate of Valor, Lernaean Bow,
    Hydra''s Lament, Phoenix Feather, Damaru, Freya''s Tears, Spectral Armor, Eye
    of the Storm, Shield Splitter, Erosion, Eye of Providence, Draconic Scale, Leviathan''s
    Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.15
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.53
      pick: 0.29
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.66
      win: 0.56
      pick: 0.24
      fit: 0.32
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.6
    The Crusher:
      total: 0.53
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Riptalon
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Avenging Blade, Genji''s Guard, Riptalon, Amanita Charm,
    Golden Blade, Silverbranch Bow, Stone of Binding, Pharaoh''s Curse, Void Shield,
    Lernaean Bow, Runeforged Hammer, The Reaper, Oni Hunter''s Garb, Screeching Gargoyle,
    Tekko-Kagi, Breastplate of Valor, Hydra''s Lament, Kinetic Cuirass, Heartseeker,
    Damaru, Void Stone, Spectral Armor, Freya''s Tears, Shield of the Phoenix, Toxic
    Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.52
      efficiency: 0.48
      win: 0.56
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.1
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.29
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.56
      pick: 0.24
      fit: 0.48
    Riptalon:
      total: 0.51
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.43
    The Crusher:
      total: 0.56
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Riptalon
  - The Crusher
  flex_slots:
  - The Crusher
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Riptalon, The Crusher, Genji''s Guard, Amanita Charm,
    Pharaoh''s Curse, Silverbranch Bow, Lernaean Bow, Oni Hunter''s Garb, Breastplate
    of Valor, Kinetic Cuirass, Tyrfing, Runeforged Hammer, Hydra''s Lament, Damaru,
    Toxic Blade, Spectral Armor, Freya''s Tears, Shield of the Phoenix, Eros'' Bow,
    Yogi''s Necklace, The Reaper, Dominance, Tekko-Kagi, Eye of the Storm.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.54
      win: 0.56
      pick: 0.1
      fit: 0.56
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.09
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.29
      fit: 0.38
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.24
      fit: 0.24
    Riptalon:
      total: 0.53
      efficiency: 0.56
      win: 0.56
      pick: 0.0
      fit: 0.51
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.32
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Hydra's Lament
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Hydra''s Lament, Freya''s Tears, Shield of the Phoenix, The Crusher, Amanita Charm,
    Pharaoh''s Curse, Oni Hunter''s Garb, Kinetic Cuirass, Golden Blade, Chandra''s
    Grace, Screeching Gargoyle, Lernaean Bow, Runeforged Hammer, Riptalon, Damaru,
    Spectral Armor, Silverbranch Bow, Gladiator''s Shield, Yogi''s Necklace, Leviathan''s
    Hide, Arondight, Erosion, Eye of Providence.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.53
      pick: 0.29
      fit: 0.3
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.56
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.66
      win: 0.56
      pick: 0.24
      fit: 0.45
    Hydra's Lament:
      total: 0.52
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.56
      pick: 0.0
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Kinetic Cuirass, Amanita Charm, Genji''s
    Guard, Golden Blade, Pharaoh''s Curse, Lernaean Bow, Runeforged Hammer, Oni Hunter''s
    Garb, Damaru, Hydra''s Lament, Breastplate of Valor, Riptalon, Eye of the Storm,
    Spectral Armor, Shield of the Phoenix, Silverbranch Bow, Freya''s Tears, Shield
    Splitter, Tekko-Kagi, Avenging Blade, Dominance, The Reaper, Tyrfing, Erosion.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.56
      pick: 0.0
      fit: 0.12
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.53
      pick: 0.29
      fit: 0.4
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.66
      win: 0.56
      pick: 0.24
      fit: 0.37
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.51
      pick: 0.12
      fit: 0.42
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.52
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.32
  starter: *id001
---
