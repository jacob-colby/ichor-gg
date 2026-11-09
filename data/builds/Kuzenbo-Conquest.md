---
type: smite-build
god: Kuzenbo
mode: Conquest
builds:
- source: community
  aspect: Aspect of Spirits
  aspect_pick_rate: 0.46
  aspect_win_rate: 0.49
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.24
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.45
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.5
  - name: Prophetic Cloak
    pick_rate: 0.15
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.48
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.59
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.51
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.52
    - name: Mystical Mail
      pick_rate: 0.06
      win_rate: 0.71
  - name: Genji's Guard
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.53
  - name: Hide of the Nemean Lion
    pick_rate: 0.1
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.73
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.6
  - name: Medal of Defense
    pick_rate: 0.11
    win_rate: 0.7
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.04
      win_rate: 0.5
    - name: Sage's Ring
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.32
  - name: Bluestone Brooch
    pick_rate: 0.18
    win_rate: 0.51
  - name: Selflessness
    pick_rate: 0.11
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/kuzenbo/
  last_verified: '2026-11-08'
  god_win_rate: 0.5014925373134328
  god_matches_won: 168
  god_matches_played: 335
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Prophetic Cloak — magical protection
    swap_item: Prophetic Cloak
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Draconic Scale, Gluttonous
    Grimoire, Shield of the Phoenix, Soul Gem, Breastplate of Valor, Erosion, Eye
    of Providence, Oni Hunter''s Garb, Midgardian Mail, Helm of Darkness, Stone of
    Binding, Spear of Desolation, Screeching Gargoyle, Leviathan''s Hide, Magi''s
    Cloak, Mantle Of Discord, Helm of Radiance, Gladiator''s Shield, Blood-Bound Book,
    Ancile, Void Stone, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.34
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.4
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.51
      pick: 0.3
      fit: 0.55
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Freya's Tears
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Hide of the Nemean Lion
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Mystical Mail — physical protection
    swap_item: Mystical Mail
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Rod
    of Tahuti, Draconic Scale, Gluttonous Grimoire, Blood-Bound Book, Phoenix Feather,
    Yogi''s Necklace, Ethereal Staff, Erosion, Oni Hunter''s Garb, Eye of Providence,
    Chandra''s Grace, Breastplate of Valor, Midgardian Mail, Bancroft''s Talon, Regrowth
    Striders, Glorious Pridwen, Leviathan''s Hide, Spear of Desolation, Gladiator''s
    Shield, Screeching Gargoyle, Helm of Darkness, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.32
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.85
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.54
      win: 0.63
      pick: 0.22
      fit: 0.43
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Genji's Guard
  - Hide of the Nemean Lion
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Spear of Desolation
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Soul Gem, Kinetic
    Cuirass, Spear of Desolation, Screeching Gargoyle, Stone of Binding, Draconic
    Scale, Void Stone, Void Shield, Obsidian Shard, Breastplate of Valor, Shield of
    the Phoenix, Spear of the Magus, Oni Hunter''s Garb, Dreamer''s Idol, Erosion,
    Eye of Providence, Doom Orb, Midgardian Mail, Helm of Radiance, Blood-Bound Book,
    Leviathan''s Hide, The World Stone, Helm of Darkness, Shifter''s Shield.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.64
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.24
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.71
    Spear of Desolation:
      total: 0.55
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.82
      win: 0.58
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Draconic Scale, Soul Gem, Breastplate of Valor, Nimble Ring, Shield of the Phoenix,
    Oni Hunter''s Garb, Spear of Desolation, Bragi''s Harp, Erosion, Blood-Bound Book,
    Eye of Providence, Screeching Gargoyle, Helm of Radiance, Midgardian Mail, Stone
    of Binding, Leviathan''s Hide, Ancient Signet, Bracer of The Abyss, Death Metal,
    Helm of Darkness, Magi''s Cloak, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.19
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.51
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.58
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Prophetic Cloak
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Breastplate of Valor, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Screeching Gargoyle, Gluttonous Grimoire, Draconic Scale, Chronos'' Pendant, Gladiator''s
    Shield, Oni Hunter''s Garb, Erosion, Blood-Bound Book, Eye of Providence, Helm
    of Radiance, Gem of Focus, Heartwood Charm, Chandra''s Grace, Midgardian Mail,
    Helm of Darkness, Regrowth Striders, Stone of Binding, Ancient Signet, Shifter''s
    Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.5
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.45
      win: 0.63
      pick: 0.2
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.51
      pick: 0.3
      fit: 0.58
    Soul Gem:
      total: 0.56
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, The Reaper, Tyrfing, Draconic Scale, Runeforged Hammer, Breastplate
    of Valor, Spear of Desolation, Golden Blade, Hydra''s Lament, Shield of the Phoenix,
    The Crusher, Oni Hunter''s Garb, Heartseeker, Tekko-Kagi, Death Metal, Titan''s
    Bane, Erosion, Eye of Providence, Bragi''s Harp, Blood-Bound Book, Obsidian Shard,
    Midgardian Mail, Screeching Gargoyle, Helm of Radiance, Avenging Blade, Nimble
    Ring, Arondight, Stone of Binding, Leviathan''s Hide, Lernaean Bow, Dominance,
    Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.72
      win: 0.58
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.47
    Shield Splitter:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Kinetic Cuirass, Spear of Desolation, Berserker''s
    Shield, Shield Splitter, Draconic Scale, The Reaper, Breastplate of Valor, Blood-Bound
    Book, Runeforged Hammer, Obsidian Shard, Death Metal, Helm of Radiance, Shield
    of the Phoenix, Hydra''s Lament, Oni Hunter''s Garb, Spear of the Magus, Helm
    of Darkness, Ancient Signet, The Crusher, Heartseeker, Polynomicon, Dreamer''s
    Idol, Erosion, Chronos'' Pendant, Eye of Providence, Jade Scepter, Midgardian
    Mail, Screeching Gargoyle, Tyrfing, Titan''s Bane, Triton''s Conch, Stone of Binding,
    Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.58
      pick: 0.0
      fit: 0.24
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.47
    Spear of Desolation:
      total: 0.53
      efficiency: 0.6
      win: 0.58
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Gluttonous
    Grimoire, Shield of the Phoenix, Draconic Scale, Soul Gem, Breastplate of Valor,
    Erosion, Eye of Providence, Oni Hunter''s Garb, Shifter''s Shield, Midgardian
    Mail, Helm of Darkness, Stone of Binding, Spear of Desolation, Screeching Gargoyle,
    Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Helm of Radiance, Gladiator''s
    Shield, Blood-Bound Book, Ancile, Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.58
      pick: 0.0
      fit: 0.34
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.57
      pick: 0.15
      fit: 0.34
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.0
      fit: 0.72
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.51
      pick: 0.3
      fit: 0.55
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.6
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-09-24'
  partial_windows:
    ob44: '2026-09-24'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of Spirits
    status: shown
    window: ob47
    window_rule: newest
    window_start: '2026-11-03'
    window_end: '2026-11-08'
    matches: 140
    wins: 67
    win_share: 0.48
    aggregate:
      aspect_matches: 162
      aspect_win_rate: 0.469
      no_aspect_matches: 191
      no_aspect_win_rate: 0.513
    roles:
    - role: Solo
      matches: 99
      share: 0.71
    - role: Support
      matches: 27
      share: 0.19
    - role: Jungle
      matches: 8
      share: 0.06
    - role: Mid
      matches: 5
      share: 0.04
    - role: Carry
      matches: 1
      share: 0.01
    base_role: Support
    base_role_share: 0.19
    role_shift:
      role: Solo
      share: 0.71
      says: 'most Aspect of Spirits players do not play Support: Solo 71%, Support
        19%'
    items:
    - name: Freya's Tears
      share: 0.59
    - name: Genji's Guard
      share: 0.41
    - name: Shifter's Shield
      share: 0.34
    - name: Mystical Mail
      share: 0.31
    - name: Prophetic Cloak
      share: 0.26
    - name: Ethereal Staff
      share: 0.21
    - name: Gladiator's Shield
      share: 0.19
    - name: Breastplate of Valor
      share: 0.16
    starters:
    - name: Bluestone Brooch
      share: 0.3
    - name: Bluestone Pendant
      share: 0.19
    - name: Sundering Axe
      share: 0.15
    relics:
    - name: sundering-arc
      share: 0.37
    - name: phantom-shell
      share: 0.23
    - name: purification-beads
      share: 0.17
    matches_by_window:
      ob47: 140
      ob46: 207
    unmapped_slugs:
    - aegis-of-acceleration
    - agility-relic
    - brawlers-ruin
    - phantom-shell
    - purification-beads
    - sundering-arc
---
