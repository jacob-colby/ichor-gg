---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.05
  aspect_win_rate: 0.43
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.5
    win_rate: 0.55
    alternates:
    - name: Stampede
      pick_rate: 0.2
      win_rate: 0.53
    - name: Yogi's Necklace
      pick_rate: 0.03
      win_rate: 0.45
  - name: Stampede
    pick_rate: 0.26
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.6
    - name: Screeching Gargoyle
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.25
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.49
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.19
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.48
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.52
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: Sage's Ring
      pick_rate: 0.09
      win_rate: 0.46
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.53
  community_starters:
  - name: Conduit Gem
    pick_rate: 0.29
    win_rate: 0.51
  - name: Bluestone Pendant
    pick_rate: 0.18
    win_rate: 0.52
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-11-04'
  god_win_rate: 0.5384615384615384
  god_matches_won: 308
  god_matches_played: 572
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
  - Freya's Tears
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Draconic Scale, Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Gluttonous
    Grimoire, Shield of the Phoenix, Soul Gem, Breastplate of Valor, Erosion, Eye
    of Providence, Oni Hunter''s Garb, Shifter''s Shield, Stone of Binding, Midgardian
    Mail, Helm of Darkness, Spear of Desolation, Magi''s Cloak, Mantle Of Discord,
    Leviathan''s Hide, Helm of Radiance, Hide of the Nemean Lion, Blood-Bound Book,
    Nimble Ring, Ancile, Gladiator''s Shield, Void Stone, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.31
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.49
      pick: 0.35
      fit: 0.51
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
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
  - Genji's Guard
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    this god: Amanita Charm, Draconic Scale, Shield of the Phoenix, Soul Gem, Kinetic
    Cuirass, Rod of Tahuti, Blood-Bound Book, Gluttonous Grimoire, Phoenix Feather,
    Ethereal Staff, Breastplate of Valor, Oni Hunter''s Garb, Chandra''s Grace, Erosion,
    Eye of Providence, Shifter''s Shield, Bancroft''s Talon, Midgardian Mail, Regrowth
    Striders, Spear of Desolation, Leviathan''s Hide, Glorious Pridwen, Hide of the
    Nemean Lion, Nimble Ring, Helm of Radiance, Yogi''s Necklace, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.28
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.65
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.79
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.49
      pick: 0.35
      fit: 0.45
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.55
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Draconic Scale, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Kinetic Cuirass, Stone of Binding, Spear of Desolation, Void Stone,
    Screeching Gargoyle, Void Shield, Breastplate of Valor, Obsidian Shard, Shield
    of the Phoenix, Spear of the Magus, Oni Hunter''s Garb, Erosion, Dreamer''s Idol,
    Eye of Providence, Shifter''s Shield, Midgardian Mail, Blood-Bound Book, Helm
    of Radiance, Doom Orb, Leviathan''s Hide, Helm of Darkness, Magi''s Cloak.'
  slot_scores:
    Stone of Binding:
      total: 0.53
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.7
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.23
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.52
    Spear of Desolation:
      total: 0.52
      efficiency: 0.6
      win: 0.55
      pick: 0.0
      fit: 0.43
    Draconic Scale:
      total: 0.56
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Shield of the Phoenix, Nimble Ring,
    Oni Hunter''s Garb, Erosion, Spear of Desolation, Eye of Providence, Bragi''s
    Harp, Blood-Bound Book, Helm of Radiance, Shifter''s Shield, Midgardian Mail,
    Stone of Binding, Leviathan''s Hide, Magi''s Cloak, Helm of Darkness, Mantle Of
    Discord, Hide of the Nemean Lion, Ancient Signet, Death Metal, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.2
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.49
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.44
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Amanita
    Charm, Soul Gem, Kinetic Cuirass, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Gluttonous Grimoire, Chronos'' Pendant, Screeching Gargoyle,
    Oni Hunter''s Garb, Gladiator''s Shield, Prophetic Cloak, Erosion, Blood-Bound
    Book, Helm of Radiance, Eye of Providence, Shifter''s Shield, Midgardian Mail,
    Nimble Ring, Gem of Focus, Heartwood Charm, Helm of Darkness, Stone of Binding,
    Chandra''s Grace, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.41
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.49
      pick: 0.35
      fit: 0.55
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.39
    Soul Gem:
      total: 0.54
      efficiency: 0.58
      win: 0.55
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    win/pick). Underrated for this god: Rod of Tahuti, Draconic Scale, Berserker''s
    Shield, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous
    Grimoire, Soul Gem, The Reaper, Tyrfing, Runeforged Hammer, Breastplate of Valor,
    Spear of Desolation, Hydra''s Lament, Golden Blade, Shield of the Phoenix, The
    Crusher, Oni Hunter''s Garb, Heartseeker, Erosion, Death Metal, Eye of Providence,
    Tekko-Kagi, Titan''s Bane, Shifter''s Shield, Blood-Bound Book, Midgardian Mail,
    Helm of Radiance, Bragi''s Harp, Obsidian Shard, Stone of Binding, Nimble Ring,
    Avenging Blade, Leviathan''s Hide, Arondight, Helm of Darkness, Magi''s Cloak,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.21
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.48
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Draconic Scale, Berserker''s
    Shield, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Soul Gem, Jotunn''s
    Revenge, Shield Splitter, Spear of Desolation, The Reaper, Breastplate of Valor,
    Blood-Bound Book, Helm of Radiance, Tyrfing, Runeforged Hammer, Shield of the
    Phoenix, Obsidian Shard, Death Metal, Oni Hunter''s Garb, Hydra''s Lament, Nimble
    Ring, Helm of Darkness, Ancient Signet, Spear of the Magus, Bragi''s Harp, Golden
    Blade, The Crusher, Erosion, Polynomicon, Eye of Providence, Heartseeker, Dreamer''s
    Idol, Chronos'' Pendant, Shifter''s Shield, Midgardian Mail, Stone of Binding,
    Jade Scepter, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.3
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Draconic Scale
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Gluttonous
    Grimoire, Draconic Scale, Shield of the Phoenix, Soul Gem, Breastplate of Valor,
    Erosion, Eye of Providence, Oni Hunter''s Garb, Shifter''s Shield, Stone of Binding,
    Midgardian Mail, Helm of Darkness, Screeching Gargoyle, Spear of Desolation, Magi''s
    Cloak, Mantle Of Discord, Leviathan''s Hide, Helm of Radiance, Hide of the Nemean
    Lion, Blood-Bound Book, Nimble Ring, Ancile, Gladiator''s Shield, Void Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.55
      pick: 0.16
      fit: 0.31
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.67
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.49
      pick: 0.35
      fit: 0.51
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.11
      fit: 0.57
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
---
