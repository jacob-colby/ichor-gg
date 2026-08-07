---
type: smite-build
god: Horus
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Falcon
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.11
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.36
    win_rate: 0.61
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.18
      win_rate: 0.63
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.21
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.18
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.57
  - name: Breastplate of Valor
    pick_rate: 0.11
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.24
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.68
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.59
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.59
  - name: Dwarven Plate
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.61
    - name: Spirit Robe
      pick_rate: 0.05
      win_rate: 0.62
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.36
    - name: Legionnaire Armor
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Warrior's Axe
    pick_rate: 0.26
    win_rate: 0.57
  - name: Selflessness
    pick_rate: 0.19
    win_rate: 0.6
  - name: Sundering Axe
    pick_rate: 0.13
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/horus/
  last_verified: '2026-08-07'
  god_win_rate: 0.5940409683426443
  god_matches_won: 638
  god_matches_played: 1074
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-07'
  god_matches_analyzed: 13100
  starter:
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s Shield,
    Breastplate of Valor, Freya''s Tears, Oni Hunter''s Garb, Shield of the Phoenix,
    Erosion, Jotunn''s Revenge, Draconic Scale, Spectral Armor, Shield Splitter, Hydra''s
    Lament, Pharaoh''s Curse, The Crusher, Eye of the Storm, Leviathan''s Hide, Yogi''s
    Necklace, Midgardian Mail, Gladiator''s Shield, Hide of the Nemean Lion, Mantle
    Of Discord, Stone of Binding, Shogun''s Ofuda, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.21
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.76
    Runeforged Hammer:
      total: 0.56
      efficiency: 0.6
      win: 0.63
      pick: 0.18
      fit: 0.39
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.61
      pick: 0.36
      fit: 0.66
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: &id001
    base: Death's Toll
    upgrade: Death's Embrace
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Runeforged Hammer
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Eye of Providence, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Freya''s Tears, Erosion, Jotunn''s Revenge, Phoenix Feather, Spectral Armor,
    Draconic Scale, Pharaoh''s Curse, Hydra''s Lament, Eye of the Storm, Yogi''s Necklace,
    The Crusher, Leviathan''s Hide, Shield Splitter, Glorious Pridwen, Midgardian
    Mail, Gladiator''s Shield, Hide of the Nemean Lion, The Reaper.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.21
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.94
    Runeforged Hammer:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.18
      fit: 0.45
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.61
      pick: 0.36
      fit: 0.66
    Amanita Charm:
      total: 0.6
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.96
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Runeforged Hammer
  - Shifter's Shield
  - The Crusher
  - Amanita Charm
  flex_slots:
  - The Crusher
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, The Crusher, Amanita Charm, Kinetic Cuirass,
    Berserker''s Shield, Breastplate of Valor, Eye of Providence, Stone of Binding,
    Screeching Gargoyle, Oni Hunter''s Garb, Freya''s Tears, Avenging Blade, Void
    Shield, Shield of the Phoenix, Void Stone, Hydra''s Lament, Spectral Armor, Erosion,
    The Reaper, Yogi''s Necklace, Riptalon, Pharaoh''s Curse, Draconic Scale, Shield
    Splitter, Silverbranch Bow, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.21
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.54
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.18
      fit: 0.3
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.36
      fit: 0.46
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Runeforged Hammer
  - Shifter's Shield
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
    this god: Berserker''s Shield, Amanita Charm, Breastplate of Valor, Kinetic Cuirass,
    Golden Blade, Eye of Providence, Pharaoh''s Curse, Jotunn''s Revenge, Oni Hunter''s
    Garb, The Crusher, Riptalon, Hydra''s Lament, Freya''s Tears, Lernaean Bow, Shield
    of the Phoenix, Shogun''s Ofuda, Tyrfing, Silverbranch Bow, Yogi''s Necklace,
    Spectral Armor, Shield Splitter, Erosion, Eye of the Storm, Dominance, Draconic
    Scale, Leviathan''s Hide.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.21
      fit: 0.22
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.18
      fit: 0.32
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.36
      fit: 0.35
    Pharaoh's Curse:
      total: 0.49
      efficiency: 0.58
      win: 0.5
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Freya''s Tears,
    Jotunn''s Revenge, Amanita Charm, Shield of the Phoenix, Hydra''s Lament, Kinetic
    Cuirass, Berserker''s Shield, Eye of Providence, Oni Hunter''s Garb, The Crusher,
    Screeching Gargoyle, Chandra''s Grace, Gladiator''s Shield, Spectral Armor, Erosion,
    Shield Splitter, Yogi''s Necklace, Pharaoh''s Curse, Prophetic Cloak, Draconic
    Scale, Arondight, Eye of the Storm, Leviathan''s Hide, Midgardian Mail, Hide of
    the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.21
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.11
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.47
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.6
      win: 0.63
      pick: 0.18
      fit: 0.33
    Freya's Tears:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.36
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Berserker''s
    Shield, Freya''s Tears, Oni Hunter''s Garb, Shield of the Phoenix, Breastplate
    of Valor, Erosion, Jotunn''s Revenge, Draconic Scale, Spectral Armor, Shield Splitter,
    Hydra''s Lament, Pharaoh''s Curse, The Crusher, Eye of the Storm, Leviathan''s
    Hide, Yogi''s Necklace, Midgardian Mail, Gladiator''s Shield, Hide of the Nemean
    Lion, Mantle Of Discord, Stone of Binding, Shogun''s Ofuda, Screeching Gargoyle.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.21
      fit: 0.42
    Berserker's Shield:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.6
      win: 0.5
      pick: 0.0
      fit: 0.76
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
---
