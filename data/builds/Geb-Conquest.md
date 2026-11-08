---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.01
  aspect_win_rate: 0.25
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.41
    win_rate: 0.55
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.73
    - name: Chandra's Grace
      pick_rate: 0.13
      win_rate: 0.64
  - name: Stampede
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.62
    - name: Chandra's Grace
      pick_rate: 0.15
      win_rate: 0.65
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.66
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.7
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.18
      win_rate: 0.64
    - name: Stampede
      pick_rate: 0.08
      win_rate: 0.4
  - name: Glorious Pridwen
    pick_rate: 0.07
    win_rate: 0.71
    alternates:
    - name: Freya's Tears
      pick_rate: 0.16
      win_rate: 0.74
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.46
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.13
    - name: Legionnaire Armor
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Selflessness
    pick_rate: 0.43
    win_rate: 0.57
  - name: Heroism
    pick_rate: 0.32
    win_rate: 0.7
  - name: Archmage's Gem
    pick_rate: 0.07
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-11-08'
  god_win_rate: 0.6037037037037037
  god_matches_won: 163
  god_matches_played: 270
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
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
    this god: Amanita Charm, Kinetic Cuirass, Draconic Scale, Shield of the Phoenix,
    Breastplate of Valor, Erosion, Eye of Providence, Oni Hunter''s Garb, Shifter''s
    Shield, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide,
    Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion, Ancile, Gladiator''s
    Shield, Void Stone, Phoenix Feather, Prophetic Cloak, Void Shield, Spectral Armor,
    Doublet of Binding, Hussar''s Wings, Xibalban Effigy, Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.49
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Amanita Charm, Soul Gem, Gluttonous Grimoire, Kinetic Cuirass, Spear
    of Desolation, Breastplate of Valor, Lotus Sickle, Nimble Ring, Ancient Signet,
    Bragi''s Harp, Blood-Bound Book, Oni Hunter''s Garb, Death Metal, Helm of Radiance,
    Polynomicon, Shield of the Phoenix, Obsidian Shard, Eros'' Bow, Spear of the Magus,
    Helm of Darkness, Chronos'' Pendant, Draconic Scale, Screeching Gargoyle, Bracer
    of The Abyss, Dreamer''s Idol, Erosion, Doom Orb.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.64
      pick: 0.0
      fit: 0.2
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.23
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.28
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.64
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
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
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Phoenix Feather,
    Yogi''s Necklace, Draconic Scale, Oni Hunter''s Garb, Breastplate of Valor, Erosion,
    Eye of Providence, Shifter''s Shield, Midgardian Mail, Regrowth Striders, Leviathan''s
    Hide, Hide of the Nemean Lion, Screeching Gargoyle, Stone of Binding, Ancile,
    Gladiator''s Shield, Void Stone, Magi''s Cloak, Mantle Of Discord, Umbral Link,
    Void Shield, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.27
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.63
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.43
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.65
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.83
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Amanita Charm, Kinetic Cuirass, Screeching Gargoyle, Stone of Binding,
    Void Stone, Void Shield, Breastplate of Valor, Shield of the Phoenix, Draconic
    Scale, Oni Hunter''s Garb, Erosion, Eye of Providence, Shifter''s Shield, Gluttonous
    Grimoire, Midgardian Mail, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord,
    Hide of the Nemean Lion, Soul Gem, Ancile, Phoenix Feather, Gladiator''s Shield,
    Spectral Armor, Yogi''s Necklace, Prophetic Cloak, Doublet of Binding.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.61
    Stone of Binding:
      total: 0.56
      efficiency: 0.49
      win: 0.64
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.21
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.35
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Breastplate of Valor, Shield of the
    Phoenix, Draconic Scale, Oni Hunter''s Garb, Erosion, Eye of Providence, Shifter''s
    Shield, Midgardian Mail, Screeching Gargoyle, Stone of Binding, Leviathan''s Hide,
    Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion, Ancile, Void Stone,
    Phoenix Feather, Void Shield, Gladiator''s Shield, Spectral Armor, Yogi''s Necklace,
    Prophetic Cloak, Doublet of Binding, Nimble Ring, Bragi''s Harp.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.49
    Nimble Ring:
      total: 0.49
      efficiency: 0.47
      win: 0.64
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.49
      efficiency: 0.4
      win: 0.64
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.35
    Eros' Bow:
      total: 0.48
      efficiency: 0.41
      win: 0.64
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Lotus Sickle
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Lotus Sickle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod
    of Tahuti, Breastplate of Valor, Shield of the Phoenix, Soul Gem, Lotus Sickle,
    Screeching Gargoyle, Chronos'' Pendant, Nimble Ring, Oni Hunter''s Garb, Draconic
    Scale, Gladiator''s Shield, Blood-Bound Book, Helm of Radiance, Prophetic Cloak,
    Erosion, Spear of Desolation, Eye of Providence, Midgardian Mail, Shifter''s Shield,
    Eros'' Bow, Bragi''s Harp, Gem of Focus, Heartwood Charm, Helm of Darkness, Ancient
    Signet, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.38
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.51
    Lotus Sickle:
      total: 0.55
      efficiency: 0.57
      win: 0.64
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.36
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
  - Genji's Guard
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
    win/pick). Underrated for this god: Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Tyrfing, The Reaper, Golden Blade,
    Runeforged Hammer, Breastplate of Valor, Hydra''s Lament, Shield of the Phoenix,
    The Crusher, Draconic Scale, Oni Hunter''s Garb, Heartseeker, Erosion, Eye of
    Providence, Tekko-Kagi, Toxic Blade, Titan''s Bane, Shifter''s Shield, Midgardian
    Mail, Screeching Gargoyle, Stone of Binding, Avenging Blade, Leviathan''s Hide,
    Silverbranch Bow, Arondight, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean
    Lion, Lernaean Bow, Dominance, Wyrmskin Hide, Riptalon, Shogun''s Ofuda, Pharaoh''s
    Curse, Ancile, Sanguine Lash.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.22
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.36
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Jotunn''s Revenge, Soul Gem,
    Tyrfing, Spear of Desolation, Shield Splitter, Golden Blade, Nimble Ring, Breastplate
    of Valor, The Reaper, Bragi''s Harp, Lotus Sickle, Blood-Bound Book, Helm of Radiance,
    Runeforged Hammer, Obsidian Shard, Shield of the Phoenix, Death Metal, Oni Hunter''s
    Garb, Hydra''s Lament, Ancient Signet, Toxic Blade, Draconic Scale, Eros'' Bow,
    Spear of the Magus, Helm of Darkness, Tekko-Kagi, The Crusher, Polynomicon, Silverbranch
    Bow, Erosion, Bracer of The Abyss, Heartseeker, Dreamer''s Idol, Eye of Providence,
    Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.18
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.64
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.64
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.29
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.33
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Draconic Scale, Shield
    of the Phoenix, Breastplate of Valor, Erosion, Eye of Providence, Oni Hunter''s
    Garb, Shifter''s Shield, Midgardian Mail, Stone of Binding, Screeching Gargoyle,
    Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion,
    Ancile, Gladiator''s Shield, Void Stone, Phoenix Feather, Prophetic Cloak, Void
    Shield, Spectral Armor, Doublet of Binding, Hussar''s Wings, Xibalban Effigy,
    Yogi''s Necklace.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.71
      win: 0.62
      pick: 0.23
      fit: 0.29
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.64
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.64
      pick: 0.0
      fit: 0.65
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.32
      fit: 0.49
    Draconic Scale:
      total: 0.55
      efficiency: 0.53
      win: 0.64
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.64
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
  - aspect: Aspect of Calamity
    status: below minimum
    matches_by_window:
      ob47: 4
      ob46: 13
      ob45: 6
      ob44: 5
---
