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
    pick_rate: 0.21
    win_rate: 0.51
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.43
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.48
  - name: Prophetic Cloak
    pick_rate: 0.19
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.52
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.39
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.55
    - name: Mystical Mail
      pick_rate: 0.08
      win_rate: 0.64
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.63
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.1
  - name: Hide of the Nemean Lion
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.75
    - name: Contagion
      pick_rate: 0.07
      win_rate: 0.36
  - name: Medal of Defense
    pick_rate: 0.1
    win_rate: 0.56
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.33
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.21
    win_rate: 0.32
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.5
  - name: Sundering Axe
    pick_rate: 0.13
    win_rate: 0.83
  source_url: https://smitebrain.com/gods/kuzenbo/
  last_verified: '2026-11-06'
  god_win_rate: 0.521978021978022
  god_matches_won: 95
  god_matches_played: 182
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
  - Genji's Guard
  - Prophetic Cloak
  - Kinetic Cuirass
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Gluttonous Grimoire, Shield of the Phoenix,
    Draconic Scale, Soul Gem, Breastplate of Valor, Erosion, Eye of Providence, Oni
    Hunter''s Garb, Midgardian Mail, Helm of Darkness, Stone of Binding, Spear of
    Desolation, Screeching Gargoyle, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord,
    Helm of Radiance, Gladiator''s Shield, Blood-Bound Book, Ancile, Void Stone, Shifter''s
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.34
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.45
      win: 0.63
      pick: 0.26
      fit: 0.55
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.72
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.28
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.22
      fit: 0.4
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Kinetic Cuirass
  - Freya's Tears
  - Hide of the Nemean Lion
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
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Rod of Tahuti, Gluttonous
    Grimoire, Blood-Bound Book, Phoenix Feather, Draconic Scale, Yogi''s Necklace,
    Ethereal Staff, Erosion, Oni Hunter''s Garb, Eye of Providence, Chandra''s Grace,
    Breastplate of Valor, Midgardian Mail, Bancroft''s Talon, Regrowth Striders, Glorious
    Pridwen, Leviathan''s Hide, Spear of Desolation, Gladiator''s Shield, Screeching
    Gargoyle, Helm of Darkness, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.32
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.72
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.53
      pick: 0.28
      fit: 0.51
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.22
      fit: 0.43
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Spear of Desolation
  - Rod of Tahuti
  flex_slots:
  - Hide of the Nemean Lion
  - Spear of Desolation
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
    for this god: Rod of Tahuti, Gluttonous Grimoire, Amanita Charm, Soul Gem, Spear
    of Desolation, Screeching Gargoyle, Stone of Binding, Void Stone, Void Shield,
    Obsidian Shard, Breastplate of Valor, Shield of the Phoenix, Spear of the Magus,
    Draconic Scale, Oni Hunter''s Garb, Dreamer''s Idol, Erosion, Eye of Providence,
    Doom Orb, Midgardian Mail, Helm of Radiance, Blood-Bound Book, Leviathan''s Hide,
    The World Stone, Helm of Darkness, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.24
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.54
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.22
      fit: 0.29
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.71
    Spear of Desolation:
      total: 0.54
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.82
      win: 0.56
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Breastplate
    of Valor, Nimble Ring, Shield of the Phoenix, Oni Hunter''s Garb, Draconic Scale,
    Spear of Desolation, Bragi''s Harp, Erosion, Blood-Bound Book, Eye of Providence,
    Screeching Gargoyle, Helm of Radiance, Midgardian Mail, Stone of Binding, Leviathan''s
    Hide, Ancient Signet, Bracer of The Abyss, Death Metal, Helm of Darkness, Magi''s
    Cloak, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.19
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.45
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.56
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.5
      efficiency: 0.57
      win: 0.56
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.47
      win: 0.56
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Prophetic Cloak
  - Kinetic Cuirass
  - Freya's Tears
  - Soul Gem
  flex_slots:
  - Prophetic Cloak
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Breastplate of Valor, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Gluttonous Grimoire, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s
    Garb, Draconic Scale, Erosion, Blood-Bound Book, Eye of Providence, Helm of Radiance,
    Gem of Focus, Heartwood Charm, Chandra''s Grace, Midgardian Mail, Helm of Darkness,
    Regrowth Striders, Stone of Binding, Ancient Signet, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.45
    Prophetic Cloak:
      total: 0.54
      efficiency: 0.45
      win: 0.63
      pick: 0.26
      fit: 0.58
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.5
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.28
      fit: 0.58
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.56
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Shield Splitter, Gluttonous Grimoire, Soul Gem, The
    Reaper, Tyrfing, Runeforged Hammer, Breastplate of Valor, Spear of Desolation,
    Golden Blade, Hydra''s Lament, Shield of the Phoenix, The Crusher, Oni Hunter''s
    Garb, Heartseeker, Draconic Scale, Tekko-Kagi, Death Metal, Titan''s Bane, Erosion,
    Eye of Providence, Bragi''s Harp, Blood-Bound Book, Obsidian Shard, Midgardian
    Mail, Screeching Gargoyle, Helm of Radiance, Avenging Blade, Nimble Ring, Arondight,
    Stone of Binding, Leviathan''s Hide, Lernaean Bow, Dominance, Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.56
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.2
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.22
      fit: 0.24
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
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
    Grimoire, Soul Gem, Jotunn''s Revenge, Spear of Desolation, Berserker''s Shield,
    Shield Splitter, The Reaper, Breastplate of Valor, Blood-Bound Book, Runeforged
    Hammer, Obsidian Shard, Death Metal, Helm of Radiance, Shield of the Phoenix,
    Hydra''s Lament, Oni Hunter''s Garb, Spear of the Magus, Draconic Scale, Helm
    of Darkness, Ancient Signet, The Crusher, Heartseeker, Polynomicon, Dreamer''s
    Idol, Erosion, Chronos'' Pendant, Eye of Providence, Jade Scepter, Midgardian
    Mail, Screeching Gargoyle, Tyrfing, Titan''s Bane, Triton''s Conch, Stone of Binding,
    Leviathan''s Hide, Shifter''s Shield.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.56
      pick: 0.0
      fit: 0.39
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.2
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.22
      fit: 0.24
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.56
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Hide of the Nemean Lion
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Gluttonous Grimoire, Shield
    of the Phoenix, Draconic Scale, Soul Gem, Breastplate of Valor, Erosion, Eye of
    Providence, Oni Hunter''s Garb, Shifter''s Shield, Midgardian Mail, Helm of Darkness,
    Stone of Binding, Spear of Desolation, Screeching Gargoyle, Leviathan''s Hide,
    Magi''s Cloak, Mantle Of Discord, Helm of Radiance, Gladiator''s Shield, Blood-Bound
    Book, Ancile, Void Stone.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.56
      pick: 0.0
      fit: 0.34
    Genji's Guard:
      total: 0.59
      efficiency: 0.71
      win: 0.63
      pick: 0.17
      fit: 0.34
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.6
      pick: 0.15
      fit: 0.72
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.53
      pick: 0.28
      fit: 0.55
    Draconic Scale:
      total: 0.53
      efficiency: 0.53
      win: 0.56
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.56
      pick: 0.0
      fit: 0.62
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
