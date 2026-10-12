---
type: smite-build
god: Bellona
mode: Conquest
builds:
- source: community
  aspect: Aspect of Vindication
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.62
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.87
    win_rate: 0.62
    alternates:
    - name: Daybreak Gavel
      pick_rate: 0.02
      win_rate: 0.63
    - name: Berserker's Shield
      pick_rate: 0.02
      win_rate: 0.38
  - name: Sanguine Lash
    pick_rate: 0.52
    win_rate: 0.67
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.23
      win_rate: 0.61
    - name: Vital Amplifier
      pick_rate: 0.06
      win_rate: 0.63
  - name: Berserker's Shield
    pick_rate: 0.23
    win_rate: 0.63
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.21
      win_rate: 0.55
    - name: Umbral Link
      pick_rate: 0.16
      win_rate: 0.61
  - name: Kinetic Cuirass
    pick_rate: 0.16
    win_rate: 0.68
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.65
    - name: Hussar's Wings
      pick_rate: 0.11
      win_rate: 0.56
  - name: Shogun's Ofuda
    pick_rate: 0.09
    win_rate: 0.77
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.09
      win_rate: 0.76
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Shogun's Ofuda
      pick_rate: 0.05
      win_rate: 0.58
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.44
    win_rate: 0.65
  - name: Leather Cowl
    pick_rate: 0.2
    win_rate: 0.54
  - name: Death's Embrace
    pick_rate: 0.16
    win_rate: 0.72
  source_url: https://smitebrain.com/gods/bellona/
  last_verified: '2026-10-12'
  god_win_rate: 0.6023809523809524
  god_matches_won: 253
  god_matches_played: 420
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-12'
  god_matches_analyzed: 6672
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament, Stone
    of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian Mail,
    Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide,
    Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.4
    Berserker's Shield:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.36
      fit: 0.38
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.68
      pick: 0.27
      fit: 0.7
    Shield Splitter:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.54
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Shield of the Phoenix, Runeforged
    Hammer, Shield Splitter, Shifter''s Shield, Eye of the Storm, Genji''s Guard,
    Breastplate of Valor, Erosion, The Reaper, Eye of Providence, Draconic Scale,
    Hydra''s Lament, Yogi''s Necklace, Avenging Blade, Phoenix Feather, Chandra''s
    Grace, Glorious Pridwen, Stone of Binding, Midgardian Mail, Daybreak Gavel, Hide
    of the Nemean Lion, Golden Blade, Magi''s Cloak, Leviathan''s Hide, Heartseeker.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.42
    Berserker's Shield:
      total: 0.57
      efficiency: 0.6
      win: 0.63
      pick: 0.36
      fit: 0.4
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.68
      pick: 0.27
      fit: 0.68
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.47
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.88
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Amanita Charm, Stone of Binding, Avenging Blade,
    Screeching Gargoyle, Heartseeker, Void Shield, Genji''s Guard, Shield Splitter,
    Breastplate of Valor, Void Stone, Shifter''s Shield, Runeforged Hammer, Titan''s
    Bane, The Crusher, Eye of the Storm, The Reaper, Erosion, Hydra''s Lament, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Pendulum
    Blade, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.71
    Avenging Blade:
      total: 0.56
      efficiency: 0.49
      win: 0.63
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.57
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.68
      pick: 0.27
      fit: 0.53
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  - Shogun's Ofuda
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Jotunn''s Revenge, Golden Blade, Genji''s Guard, Breastplate
    of Valor, Tyrfing, Shifter''s Shield, Shield Splitter, Pharaoh''s Curse, Runeforged
    Hammer, Riptalon, Lernaean Bow, Silverbranch Bow, Erosion, Eye of Providence,
    Stone of Binding, Toxic Blade, Eye of the Storm, Shield of the Phoenix, Hydra''s
    Lament, Draconic Scale, Magi''s Cloak, Daybreak Gavel, Screeching Gargoyle, The
    Reaper, Tekko-Kagi.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.56
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.63
      pick: 0.36
      fit: 0.45
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.21
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.68
      pick: 0.27
      fit: 0.48
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.38
    Shogun's Ofuda:
      total: 0.6
      efficiency: 0.5
      win: 0.77
      pick: 0.19
      fit: 0.45
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shogun's Ofuda
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
  - Breastplate of Valor
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shogun's Ofuda — magical protection
    swap_item: Shogun's Ofuda
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Genji''s Guard,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Shifter''s Shield, Shield Splitter, Prophetic Cloak, Erosion, Runeforged
    Hammer, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Arondight, Magi''s Cloak, Eye of Erebus, Mantle Of Discord,
    Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Hide of the
    Nemean Lion, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.68
      pick: 0.27
      fit: 0.55
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Jotunn''s Revenge, Shield Splitter, Shifter''s
    Shield, Genji''s Guard, Breastplate of Valor, Runeforged Hammer, Eye of the Storm,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament,
    Stone of Binding, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s
    Hide, Void Shield, Stampede, Ancile, Prophetic Cloak, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.67
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.68
      pick: 0.27
      fit: 0.7
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.54
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.6
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Sanguine Lash
  - Kinetic Cuirass
  - Freya's Tears
  - Shogun's Ofuda
  flex_slots:
  - Shogun's Ofuda
  - Sanguine Lash
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Jotunn''s Revenge,
    Shield Splitter, Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Runeforged
    Hammer, Eye of the Storm, Erosion, Eye of Providence, Draconic Scale, Shield of
    the Phoenix, Hydra''s Lament, Stone of Binding, Magi''s Cloak, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide of the Nemean Lion,
    Heartseeker, Leviathan''s Hide, Void Shield, Stampede, Ancile, Prophetic Cloak,
    Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.4
    Sanguine Lash:
      total: 0.55
      efficiency: 0.36
      win: 0.67
      pick: 0.71
      fit: 0.55
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.68
      pick: 0.27
      fit: 0.7
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.54
    Shogun's Ofuda:
      total: 0.57
      efficiency: 0.44
      win: 0.77
      pick: 0.19
      fit: 0.38
  community_ordered:
  - Sanguine Lash
  - Kinetic Cuirass
  - Freya's Tears
  - Shogun's Ofuda
  swaps:
  - added: Shogun's Ofuda
    removed: Shifter's Shield
    reason: community 77% win over 38 matches (vs 60% on this god), taking the model's
      weakest slot from Shifter's Shield
  - added: Sanguine Lash
    removed: Shield Splitter
    reason: community 67% win over 218 matches (vs 60% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
