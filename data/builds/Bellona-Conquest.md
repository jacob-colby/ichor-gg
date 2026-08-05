---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.22
  aspect_win_rate: 0.49
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.4
    win_rate: 0.48
    alternates:
    - name: Golden Blade
      pick_rate: 0.17
      win_rate: 0.48
    - name: Berserker's Shield
      pick_rate: 0.16
      win_rate: 0.58
  - name: Berserker's Shield
    pick_rate: 0.31
    win_rate: 0.46
    alternates:
    - name: Golden Blade
      pick_rate: 0.16
      win_rate: 0.52
    - name: Shogun's Ofuda
      pick_rate: 0.14
      win_rate: 0.23
  - name: Kinetic Cuirass
    pick_rate: 0.17
    win_rate: 0.59
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.19
      win_rate: 0.48
    - name: Shogun's Ofuda
      pick_rate: 0.17
      win_rate: 0.5
  - name: Dwarven Plate
    pick_rate: 0.16
    win_rate: 0.54
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.15
      win_rate: 0.35
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.31
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: Dwarven Plate
      pick_rate: 0.08
      win_rate: 0.64
    - name: Engraved Guard
      pick_rate: 0.08
      win_rate: 0.36
  - name: Hunter's Bow
    pick_rate: 0.08
    win_rate: 0.17
    alternates:
    - name: Medal of Defense
      pick_rate: 0.06
      win_rate: 0.4
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-08-01'
  god_win_rate: 0.46875
  god_matches_won: 75
  god_matches_played: 160
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
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Eye of Providence, Genji''s Guard, Jotunn''s Revenge,
    Shield Splitter, Runeforged Hammer, Oni Hunter''s Garb, Freya''s Tears, Hide of
    the Nemean Lion, The Crusher, Hydra''s Lament, Breastplate of Valor, Eye of the
    Storm, Shield of the Phoenix, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s
    Curse, Avenging Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Lernaean Bow.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.46
      pick: 0.31
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.17
      fit: 0.7
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.48
      pick: 0.4
      fit: 0.6
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Eye of Providence, Runeforged
    Hammer, Genji''s Guard, Jotunn''s Revenge, Oni Hunter''s Garb, The Crusher, Hydra''s
    Lament, Chandra''s Grace, Eye of the Storm, Shield Splitter, The Reaper, Freya''s
    Tears, Breastplate of Valor, Erosion, Phoenix Feather, Spectral Armor, Avenging
    Blade, Draconic Scale, Pharaoh''s Curse, Yogi''s Necklace, Leviathan''s Hide,
    Midgardian Mail, Riptalon.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.58
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.46
      pick: 0.31
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.17
      fit: 0.68
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.82
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.59
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Amanita Charm, Genji''s Guard, Avenging
    Blade, Eye of Providence, Stone of Binding, Oni Hunter''s Garb, Runeforged Hammer,
    Screeching Gargoyle, Hydra''s Lament, Breastplate of Valor, Freya''s Tears, Void
    Shield, Shield Splitter, The Reaper, Void Stone, Shield of the Phoenix, Eye of
    the Storm, Spectral Armor, Heartseeker, Erosion, Yogi''s Necklace, Pharaoh''s
    Curse, Draconic Scale, Riptalon.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.51
      efficiency: 0.71
      win: 0.46
      pick: 0.31
      fit: 0.28
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.17
      fit: 0.53
    The Crusher:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Amanita Charm
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Genji''s Guard, Eye of Providence, Pharaoh''s Curse,
    Oni Hunter''s Garb, The Crusher, Jotunn''s Revenge, Riptalon, Breastplate of Valor,
    Runeforged Hammer, Freya''s Tears, Lernaean Bow, Hydra''s Lament, Tyrfing, Shield
    of the Phoenix, Silverbranch Bow, Spectral Armor, Shield Splitter, Yogi''s Necklace,
    Erosion, Eye of the Storm, Draconic Scale, Dominance, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.48
      pick: 0.17
      fit: 0.56
    Genji's Guard:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.46
      pick: 0.31
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.59
      pick: 0.17
      fit: 0.48
    Amanita Charm:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.38
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Hydra''s Lament,
    Eye of Providence, Oni Hunter''s Garb, The Crusher, Runeforged Hammer, Screeching
    Gargoyle, Chandra''s Grace, Gladiator''s Shield, Spectral Armor, Erosion, Shield
    Splitter, Yogi''s Necklace, Pharaoh''s Curse, Prophetic Cloak, Draconic Scale,
    Eye of the Storm, Arondight, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.59
      pick: 0.17
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Eye of Providence, Genji''s Guard, Jotunn''s
    Revenge, Shield Splitter, Runeforged Hammer, Oni Hunter''s Garb, Freya''s Tears,
    The Crusher, Hydra''s Lament, Breastplate of Valor, Eye of the Storm, Shield of
    the Phoenix, Erosion, Draconic Scale, Spectral Armor, Pharaoh''s Curse, Avenging
    Blade, Yogi''s Necklace, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Lernaean Bow, Hide of the Nemean Lion.'
  slot_scores:
    Eye of Providence:
      total: 0.53
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.33
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.46
      pick: 0.31
      fit: 0.38
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.6
      win: 0.59
      pick: 0.17
      fit: 0.7
    Amanita Charm:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.6
  starter: *id001
---
