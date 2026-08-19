---
type: smite-build
god: Guan Yu
mode: Conquest
builds:
- source: community
  aspect: Aspect of the General
  aspect_pick_rate: 0.66
  aspect_win_rate: 0.63
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.66
    alternates:
    - name: Heartwood Charm
      pick_rate: 0.18
      win_rate: 0.62
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.45
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.59
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.23
      win_rate: 0.65
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.63
  - name: Breastplate of Valor
    pick_rate: 0.24
    win_rate: 0.7
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.66
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.43
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.74
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.56
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.79
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.53
  - name: Draconic Scale
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.5
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.8
  community_starters:
  - name: Sands Of Time
    pick_rate: 0.28
    win_rate: 0.54
  - name: Pendulum of the Ages
    pick_rate: 0.18
    win_rate: 0.72
  - name: Hunter's Cowl
    pick_rate: 0.11
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/guan-yu/
  last_verified: '2026-08-19'
  god_win_rate: 0.5756097560975609
  god_matches_won: 236
  god_matches_played: 410
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield, Jotunn''s Revenge,
    The Crusher, Shield of the Phoenix, Oni Hunter''s Garb, Hydra''s Lament, Shield
    Splitter, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Golden
    Blade, Eye of Providence, Spectral Armor, Shogun''s Ofuda, Leviathan''s Hide,
    Midgardian Mail, Lernaean Bow, Avenging Blade, Screeching Gargoyle, Mantle Of
    Discord, Stone of Binding, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.59
      pick: 0.34
      fit: 0.32
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.7
      pick: 0.37
      fit: 0.32
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.79
      pick: 0.26
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Berserker''s
    Shield, Jotunn''s Revenge, Chandra''s Grace, The Crusher, Runeforged Hammer, Oni
    Hunter''s Garb, The Reaper, Hydra''s Lament, Golden Blade, Eye of the Storm, Pharaoh''s
    Curse, Phoenix Feather, Erosion, Shield Splitter, Spectral Armor, Eye of Providence,
    Riptalon, Shogun''s Ofuda, Leviathan''s Hide, Avenging Blade, Midgardian Mail,
    Glorious Pridwen.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.7
      pick: 0.37
      fit: 0.3
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.6
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.64
      efficiency: 0.59
      win: 0.79
      pick: 0.26
      fit: 0.45
    Amanita Charm:
      total: 0.62
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - The Crusher
  flex_slots:
  - Genji's Guard
  - Transcendence
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
    for this god: The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Berserker''s Shield,
    Amanita Charm, Avenging Blade, Screeching Gargoyle, Stone of Binding, Void Shield,
    Oni Hunter''s Garb, Shield of the Phoenix, Hydra''s Lament, Void Stone, The Reaper,
    Runeforged Hammer, Shield Splitter, Riptalon, Spectral Armor, Pharaoh''s Curse,
    Erosion, Golden Blade, Eye of the Storm, Silverbranch Bow, Eye of Providence,
    Tekko-Kagi.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.59
      pick: 0.34
      fit: 0.24
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.64
      win: 0.7
      pick: 0.37
      fit: 0.24
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.55
    Transcendence:
      total: 0.49
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.16
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.79
      pick: 0.26
      fit: 0.37
    The Crusher:
      total: 0.59
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.54
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Pharaoh's Curse
  flex_slots:
  - Golden Blade
  - Pharaoh's Curse
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Kinetic Cuirass, Amanita Charm, Golden Blade, The
    Crusher, Jotunn''s Revenge, Pharaoh''s Curse, Riptalon, Oni Hunter''s Garb, Shield
    of the Phoenix, Tyrfing, Shogun''s Ofuda, Hydra''s Lament, Runeforged Hammer,
    Silverbranch Bow, Lernaean Bow, Spectral Armor, Erosion, Shield Splitter, Eye
    of Providence, Eye of the Storm, Leviathan''s Hide, Toxic Blade, Midgardian Mail,
    Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.56
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.59
      pick: 0.34
      fit: 0.22
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.64
      win: 0.7
      pick: 0.37
      fit: 0.22
    Freya's Tears:
      total: 0.63
      efficiency: 0.59
      win: 0.79
      pick: 0.26
      fit: 0.34
    Pharaoh's Curse:
      total: 0.54
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Berserker''s Shield, Amanita Charm, Hydra''s Lament, The Crusher,
    Oni Hunter''s Garb, Screeching Gargoyle, Chandra''s Grace, Gladiator''s Shield,
    Pharaoh''s Curse, Spectral Armor, Erosion, Runeforged Hammer, Eye of Providence,
    Prophetic Cloak, Shield Splitter, Leviathan''s Hide, Eye of the Storm, Golden
    Blade, Shogun''s Ofuda, Midgardian Mail, Arondight, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.59
      pick: 0.34
      fit: 0.44
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.64
      win: 0.7
      pick: 0.37
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.5
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.66
      efficiency: 0.59
      win: 0.79
      pick: 0.26
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Jotunn''s Revenge, The Crusher, Shield of the Phoenix, Oni Hunter''s Garb, Hydra''s
    Lament, Shield Splitter, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s
    Curse, Golden Blade, Eye of Providence, Spectral Armor, Shogun''s Ofuda, Leviathan''s
    Hide, Midgardian Mail, Lernaean Bow, Avenging Blade, Screeching Gargoyle, Mantle
    Of Discord, Stone of Binding, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.59
      pick: 0.34
      fit: 0.32
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.79
      pick: 0.26
      fit: 0.49
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.5
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Amanita Charm, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Shield of the Phoenix, Oni Hunter''s Garb,
    Hydra''s Lament, Shield Splitter, Runeforged Hammer, Eye of the Storm, Erosion,
    Pharaoh''s Curse, Golden Blade, Eye of Providence, Spectral Armor, Shogun''s Ofuda,
    Leviathan''s Hide, Midgardian Mail, Lernaean Bow, Avenging Blade, Screeching Gargoyle,
    Mantle Of Discord, Stone of Binding, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.59
      pick: 0.34
      fit: 0.32
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.62
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.64
      win: 0.7
      pick: 0.37
      fit: 0.32
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.62
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.59
      win: 0.62
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.58
      efficiency: 0.63
      win: 0.62
      pick: 0.0
      fit: 0.5
  swaps:
  - added: Breastplate of Valor
    removed: Freya's Tears
    reason: community 70% win over 98 matches (vs 58% on this god), taking the model's
      weakest slot from Freya's Tears
  starter: *id001
---
