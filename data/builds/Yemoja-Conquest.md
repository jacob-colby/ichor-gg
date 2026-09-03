---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.19
  aspect_win_rate: 0.56
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.17
    win_rate: 0.65
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.62
    - name: Chandra's Grace
      pick_rate: 0.11
      win_rate: 0.55
  - name: Stampede
    pick_rate: 0.1
    win_rate: 0.72
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.22
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.53
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.52
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.54
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.6
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.56
  - name: Rod of Tahuti
    pick_rate: 0.04
    win_rate: 0.44
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.39
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.71
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.75
    alternates:
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.71
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.33
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.4
    win_rate: 0.55
  - name: Bluestone Brooch
    pick_rate: 0.35
    win_rate: 0.53
  - name: Heroism
    pick_rate: 0.06
    win_rate: 0.73
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-09-02'
  god_win_rate: 0.5399239543726235
  god_matches_won: 142
  god_matches_played: 263
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-01'
  god_matches_analyzed: 8200
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Stampede, Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shifter''s
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm
    of Radiance, Gluttonous Grimoire, Stone of Binding, Magi''s Cloak, Screeching
    Gargoyle, Soul Gem, Mantle Of Discord, Helm of Darkness, Rod of Asclepius, Prophetic
    Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus, Leviathan''s
    Hide, Void Shield, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.17
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.73
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.65
      pick: 0.17
      fit: 0.37
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.62
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.63
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Spear of Desolation
  - Freya's Tears
  - Stampede
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Soul Gem, Rod of Tahuti, Shifter''s Shield, Ethereal Staff, Chandra''s Grace,
    Gluttonous Grimoire, Erosion, Eye of Providence, Draconic Scale, Lifebinder, Phoenix
    Feather, Yogi''s Necklace, Glorious Pridwen, Helm of Radiance, Sphere of Negation,
    Stone of Binding, Midgardian Mail, Screeching Gargoyle, Jade Scepter, Wish-Granting
    Pearl, Hide of the Nemean Lion.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.54
      pick: 0.0
      fit: 0.9
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.65
      pick: 0.17
      fit: 0.38
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.55
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.92
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.43
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Stone of Binding
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Stone of Binding,
    Screeching Gargoyle, Kinetic Cuirass, Soul Gem, Spear of the Magus, Obsidian Shard,
    Void Shield, Void Stone, Shifter''s Shield, Doom Orb, Helm of Radiance, Erosion,
    Shield of the Phoenix, Eye of Providence, The World Stone, Draconic Scale, Dreamer''s
    Idol, Magi''s Cloak, Rod of Asclepius, Mantle Of Discord, Midgardian Mail, Chronos''
    Pendant.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.53
      efficiency: 0.51
      win: 0.54
      pick: 0.0
      fit: 0.72
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.65
      pick: 0.17
      fit: 0.55
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.45
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.29
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Spear of Desolation
  - Bragi's Harp
  - Rod of Tahuti
  - Stampede
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Nimble Ring, Rod of Tahuti, Gluttonous Grimoire, Kinetic
    Cuirass, Soul Gem, Shifter''s Shield, Helm of Radiance, Shield of the Phoenix,
    Erosion, Stone of Binding, Eye of Providence, Spear of the Magus, Draconic Scale,
    Screeching Gargoyle, Rod of Asclepius, Bragi''s Harp, Magi''s Cloak, Daybreak
    Gavel, Obsidian Shard, Bracer of The Abyss, Midgardian Mail, Mantle Of Discord,
    Chronos'' Pendant, Jade Scepter.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.54
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.32
    Spear of Desolation:
      total: 0.53
      efficiency: 0.57
      win: 0.65
      pick: 0.17
      fit: 0.2
    Bragi's Harp:
      total: 0.47
      efficiency: 0.44
      win: 0.54
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.86
      win: 0.44
      pick: 0.09
      fit: 0.11
    Stampede:
      total: 0.54
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.22
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Stampede
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod
    of Tahuti, Shield of the Phoenix, Screeching Gargoyle, Soul Gem, Shifter''s Shield,
    Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire,
    Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding, Gem
    of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.52
      pick: 0.17
      fit: 0.48
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.48
      pick: 0.16
      fit: 0.48
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.65
      pick: 0.17
      fit: 0.46
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.45
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Spear of Desolation
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Gluttonous
    Grimoire, Golden Blade, Hydra''s Lament, Shifter''s Shield, Eye of the Storm,
    Heartseeker, Spear of the Magus, Soul Gem, Helm of Radiance, Obsidian Shard, Lernaean
    Bow, Tyrfing, Shield of the Phoenix, Erosion, Eye of Providence, Avenging Blade,
    Nimble Ring, Tekko-Kagi, Stone of Binding, Draconic Scale, Titan''s Bane, The
    Crusher, Screeching Gargoyle, Pharaoh''s Curse, Rod of Asclepius, Magi''s Cloak,
    Silverbranch Bow, Bragi''s Harp, The Reaper, Daybreak Gavel, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.54
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.45
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.65
      pick: 0.17
      fit: 0.33
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.38
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.38
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.25
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Spear of Desolation
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Soul Gem,
    Spear of the Magus, Runeforged Hammer, Helm of Radiance, Shifter''s Shield, Obsidian
    Shard, Berserker''s Shield, Hydra''s Lament, Eye of the Storm, Rod of Asclepius,
    Heartseeker, Shield of the Phoenix, Erosion, Eye of Providence, Stone of Binding,
    Draconic Scale, Chronos'' Pendant, Jade Scepter, Doom Orb, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Screeching Gargoyle, Magi''s Cloak, The World Stone, Titan''s
    Bane, Helm of Darkness, Ancient Signet, The Crusher, Mantle Of Discord, Daybreak
    Gavel, Dreamer''s Idol.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.54
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.5
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.65
      pick: 0.17
      fit: 0.42
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.39
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.4
    Stampede:
      total: 0.55
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.26
  community_ordered:
  - Spear of Desolation
  - Freya's Tears
  - Stampede
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Shifter''s
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm
    of Radiance, Gluttonous Grimoire, Stone of Binding, Magi''s Cloak, Screeching
    Gargoyle, Soul Gem, Mantle Of Discord, Helm of Darkness, Rod of Asclepius, Prophetic
    Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear of the Magus, Leviathan''s
    Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.17
      fit: 0.39
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.48
      pick: 0.16
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.54
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.17
      fit: 0.62
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.54
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.54
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
---
