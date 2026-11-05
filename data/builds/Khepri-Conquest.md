---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.76
  aspect_win_rate: 0.55
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.42
    win_rate: 0.55
    alternates:
    - name: The Cosmic Horror
      pick_rate: 0.11
      win_rate: 0.55
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.6
  - name: Stampede
    pick_rate: 0.2
    win_rate: 0.45
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.66
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.46
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.67
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.59
  - name: Omen Drum
    pick_rate: 0.11
    win_rate: 0.52
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.74
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.67
    - name: Evil Eye
      pick_rate: 0.04
      win_rate: 0.67
  - name: Veve Charm
    pick_rate: 0.08
    win_rate: 0.73
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.67
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.28
    win_rate: 0.56
  - name: Heroism
    pick_rate: 0.23
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-11-04'
  god_win_rate: 0.5563636363636364
  god_matches_won: 153
  god_matches_played: 275
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic Scale, Shield
    of the Phoenix, Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Erosion,
    Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of Darkness, Stone
    of Binding, Midgardian Mail, Screeching Gargoyle, Spear of Desolation, Magi''s
    Cloak, Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Hide of the Nemean
    Lion, Lotus Sickle, Gladiator''s Shield, Prophetic Cloak, Ancile, Blood-Bound
    Book, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.36
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.58
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.66
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Rod
    of Tahuti, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather, Draconic Scale,
    Yogi''s Necklace, Ethereal Staff, Chandra''s Grace, Breastplate of Valor, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Shifter''s Shield, Midgardian Mail, Bancroft''s
    Talon, Regrowth Striders, Glorious Pridwen, Rod of Asclepius, Spear of Desolation,
    Leviathan''s Hide, Soul Locket, Hide of the Nemean Lion, Gladiator''s Shield,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.33
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.86
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.52
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.66
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.67
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.91
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Kinetic
    Cuirass, Screeching Gargoyle, Spear of Desolation, Stone of Binding, Void Stone,
    Void Shield, Breastplate of Valor, Obsidian Shard, Shield of the Phoenix, Draconic
    Scale, Spear of the Magus, Oni Hunter''s Garb, Erosion, Dreamer''s Idol, Eye of
    Providence, Shifter''s Shield, Midgardian Mail, Lotus Sickle, Helm of Radiance,
    Doom Orb, Helm of Darkness, Blood-Bound Book, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.58
      efficiency: 0.53
      win: 0.66
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.26
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.42
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.66
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Eros' Bow
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Eros' Bow
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s
    Garb, Draconic Scale, Spear of Desolation, Erosion, Lotus Sickle, Eye of Providence,
    Bragi''s Harp, Screeching Gargoyle, Blood-Bound Book, Helm of Radiance, Midgardian
    Mail, Shifter''s Shield, Eros'' Bow, Stone of Binding, Leviathan''s Hide, Magi''s
    Cloak, Mantle Of Discord, Helm of Darkness, Hide of the Nemean Lion, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.21
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.54
      efficiency: 0.57
      win: 0.66
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.53
      efficiency: 0.47
      win: 0.66
      pick: 0.0
      fit: 0.44
    Eros' Bow:
      total: 0.52
      efficiency: 0.5
      win: 0.66
      pick: 0.0
      fit: 0.34
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix, Spear of Desolation,
    Lotus Sickle, Screeching Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Gladiator''s
    Shield, Draconic Scale, Oni Hunter''s Garb, Prophetic Cloak, Erosion, Eye of Providence,
    Helm of Radiance, Blood-Bound Book, Shifter''s Shield, Gem of Focus, Heartwood
    Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace, Stone of Binding,
    Leviathan''s Hide, Regrowth Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.45
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.6
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.66
      pick: 0.0
      fit: 0.42
    Soul Gem:
      total: 0.59
      efficiency: 0.58
      win: 0.66
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
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
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, Tyrfing, The Reaper, Golden Blade, Breastplate of Valor, Runeforged
    Hammer, Spear of Desolation, Hydra''s Lament, Shield of the Phoenix, The Crusher,
    Oni Hunter''s Garb, Draconic Scale, Heartseeker, Erosion, Death Metal, Eye of
    Providence, Tekko-Kagi, Lotus Sickle, Titan''s Bane, Screeching Gargoyle, Shifter''s
    Shield, Toxic Blade, Midgardian Mail, Helm of Radiance, Blood-Bound Book, Bragi''s
    Harp, Obsidian Shard, Stone of Binding, Arondight, Avenging Blade, Nimble Ring,
    Leviathan''s Hide, Helm of Darkness.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.66
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.35
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Kinetic Cuirass, Spear of Desolation, Shield
    Splitter, Berserker''s Shield, Breastplate of Valor, The Reaper, Lotus Sickle,
    Shield of the Phoenix, Helm of Radiance, Blood-Bound Book, Runeforged Hammer,
    Obsidian Shard, Death Metal, Hydra''s Lament, Oni Hunter''s Garb, Draconic Scale,
    Helm of Darkness, Spear of the Magus, Ancient Signet, The Crusher, Erosion, Tyrfing,
    Eye of Providence, Polynomicon, Chronos'' Pendant, Heartseeker, Dreamer''s Idol,
    Screeching Gargoyle, Shifter''s Shield, Midgardian Mail, Stone of Binding, Jade
    Scepter, Titan''s Bane, Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.66
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.36
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.66
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic
    Scale, Shield of the Phoenix, Gluttonous Grimoire, Breastplate of Valor, Soul
    Gem, Erosion, Eye of Providence, Shifter''s Shield, Oni Hunter''s Garb, Helm of
    Darkness, Stone of Binding, Midgardian Mail, Screeching Gargoyle, Spear of Desolation,
    Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Hide of
    the Nemean Lion, Lotus Sickle, Gladiator''s Shield, Prophetic Cloak, Ancile, Blood-Bound
    Book, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.66
      pick: 0.2
      fit: 0.36
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.66
      pick: 0.0
      fit: 0.36
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.66
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.19
      fit: 0.58
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.66
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.66
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
