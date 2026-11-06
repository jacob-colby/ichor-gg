---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.5
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.48
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.29
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.78
  - name: Stampede
    pick_rate: 0.24
    win_rate: 0.5
    alternates:
    - name: Screeching Gargoyle
      pick_rate: 0.12
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.55
  - name: Shell of Rebuke
    pick_rate: 0.32
    win_rate: 0.48
    alternates:
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.24
    win_rate: 0.36
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.2
      win_rate: 0.61
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.2
  - name: Shield
    pick_rate: 0.06
    win_rate: 1.0
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.33
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.36
    win_rate: 0.57
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.28
  - name: Archmage's Gem
    pick_rate: 0.15
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-11-06'
  god_win_rate: 0.5392156862745098
  god_matches_won: 55
  god_matches_played: 102
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Draconic Scale
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Genji''s Guard, Amanita Charm, Kinetic Cuirass, Rod
    of Tahuti, Gluttonous Grimoire, Draconic Scale, Shield of the Phoenix, Soul Gem,
    Breastplate of Valor, Erosion, Eye of Providence, Oni Hunter''s Garb, Stone of
    Binding, Midgardian Mail, Helm of Darkness, Spear of Desolation, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Hide of the Nemean Lion,
    Blood-Bound Book, Nimble Ring, Ancile, Gladiator''s Shield, Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.31
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.67
    Draconic Scale:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.62
      efficiency: 0.5
      win: 0.78
      pick: 0.09
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Draconic Scale
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Amanita Charm, Genji''s Guard, Shield of the Phoenix,
    Soul Gem, Kinetic Cuirass, Rod of Tahuti, Blood-Bound Book, Gluttonous Grimoire,
    Phoenix Feather, Yogi''s Necklace, Ethereal Staff, Draconic Scale, Breastplate
    of Valor, Oni Hunter''s Garb, Chandra''s Grace, Erosion, Eye of Providence, Bancroft''s
    Talon, Midgardian Mail, Regrowth Striders, Spear of Desolation, Leviathan''s Hide,
    Glorious Pridwen, Hide of the Nemean Lion, Nimble Ring, Helm of Radiance.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.28
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.79
    Draconic Scale:
      total: 0.51
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.55
    Shifter's Shield:
      total: 0.61
      efficiency: 0.5
      win: 0.78
      pick: 0.09
      fit: 0.55
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Shifter''s Shield, Rod of Tahuti, Genji''s Guard, Amanita Charm,
    Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Stone of Binding, Spear of Desolation,
    Void Stone, Void Shield, Breastplate of Valor, Obsidian Shard, Shield of the Phoenix,
    Draconic Scale, Spear of the Magus, Oni Hunter''s Garb, Erosion, Dreamer''s Idol,
    Eye of Providence, Midgardian Mail, Blood-Bound Book, Helm of Radiance, Doom Orb,
    Leviathan''s Hide, Helm of Darkness, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.52
      efficiency: 0.49
      win: 0.54
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.23
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.43
    Shifter's Shield:
      total: 0.59
      efficiency: 0.5
      win: 0.78
      pick: 0.09
      fit: 0.42
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Genji's Guard
  - Nimble Ring
  - Bragi's Harp
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Shifter''s Shield, Genji''s Guard, Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Shield of the Phoenix,
    Nimble Ring, Oni Hunter''s Garb, Draconic Scale, Erosion, Spear of Desolation,
    Eye of Providence, Bragi''s Harp, Blood-Bound Book, Helm of Radiance, Midgardian
    Mail, Stone of Binding, Leviathan''s Hide, Magi''s Cloak, Helm of Darkness, Mantle
    Of Discord, Hide of the Nemean Lion, Ancient Signet, Death Metal.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.2
    Nimble Ring:
      total: 0.49
      efficiency: 0.57
      win: 0.54
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.47
      win: 0.54
      pick: 0.0
      fit: 0.44
    Shifter's Shield:
      total: 0.58
      efficiency: 0.5
      win: 0.78
      pick: 0.09
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Genji''s Guard,
    Rod of Tahuti, Amanita Charm, Soul Gem, Kinetic Cuirass, Breastplate of Valor,
    Shield of the Phoenix, Spear of Desolation, Gluttonous Grimoire, Chronos'' Pendant,
    Oni Hunter''s Garb, Draconic Scale, Gladiator''s Shield, Prophetic Cloak, Erosion,
    Blood-Bound Book, Helm of Radiance, Eye of Providence, Midgardian Mail, Nimble
    Ring, Gem of Focus, Heartwood Charm, Helm of Darkness, Stone of Binding, Chandra''s
    Grace, Ancient Signet.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.41
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.54
      pick: 0.0
      fit: 0.39
    Shifter's Shield:
      total: 0.59
      efficiency: 0.5
      win: 0.78
      pick: 0.09
      fit: 0.39
    Soul Gem:
      total: 0.53
      efficiency: 0.58
      win: 0.54
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti, Genji''s
    Guard, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass,
    Shield Splitter, Gluttonous Grimoire, Soul Gem, The Reaper, Tyrfing, Runeforged
    Hammer, Breastplate of Valor, Spear of Desolation, Hydra''s Lament, Golden Blade,
    Shield of the Phoenix, The Crusher, Oni Hunter''s Garb, Draconic Scale, Heartseeker,
    Erosion, Death Metal, Eye of Providence, Tekko-Kagi, Titan''s Bane, Blood-Bound
    Book, Midgardian Mail, Helm of Radiance, Bragi''s Harp, Obsidian Shard, Stone
    of Binding, Nimble Ring, Avenging Blade, Leviathan''s Hide, Arondight, Helm of
    Darkness, Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.21
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.59
      efficiency: 0.5
      win: 0.78
      pick: 0.09
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Shifter''s Shield, Rod of Tahuti,
    Genji''s Guard, Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Kinetic
    Cuirass, Soul Gem, Jotunn''s Revenge, Shield Splitter, Spear of Desolation, The
    Reaper, Breastplate of Valor, Blood-Bound Book, Helm of Radiance, Tyrfing, Runeforged
    Hammer, Shield of the Phoenix, Obsidian Shard, Death Metal, Oni Hunter''s Garb,
    Hydra''s Lament, Nimble Ring, Draconic Scale, Helm of Darkness, Ancient Signet,
    Spear of the Magus, Bragi''s Harp, Golden Blade, The Crusher, Erosion, Polynomicon,
    Eye of Providence, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Midgardian
    Mail, Stone of Binding, Jade Scepter.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.3
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.2
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.58
      efficiency: 0.5
      win: 0.78
      pick: 0.09
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s
    Guard, Gluttonous Grimoire, Draconic Scale, Shield of the Phoenix, Soul Gem, Breastplate
    of Valor, Erosion, Eye of Providence, Oni Hunter''s Garb, Shifter''s Shield, Stone
    of Binding, Midgardian Mail, Helm of Darkness, Spear of Desolation, Magi''s Cloak,
    Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Hide of the Nemean Lion,
    Blood-Bound Book, Nimble Ring, Ancile, Gladiator''s Shield, Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.63
      win: 0.54
      pick: 0.0
      fit: 0.31
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.13
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.36
      pick: 0.4
      fit: 0.51
    Draconic Scale:
      total: 0.52
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
