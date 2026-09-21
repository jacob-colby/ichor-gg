---
type: smite-build
god: Sylvanus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Grover's Wrath
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.56
  slot_order:
  - name: Stampede
    pick_rate: 0.17
    win_rate: 0.5
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.17
      win_rate: 0.54
    - name: Tyrfing
      pick_rate: 0.12
      win_rate: 0.55
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.48
    alternates:
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.51
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.42
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.59
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.44
  - name: Spirit Robe
    pick_rate: 0.05
    win_rate: 0.74
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.58
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.49
  - name: Sage's Ring
    pick_rate: 0.06
    win_rate: 0.52
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.59
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.4
  community_starters:
  - name: Selflessness
    pick_rate: 0.32
    win_rate: 0.45
  - name: Heroism
    pick_rate: 0.15
    win_rate: 0.62
  - name: Conduit Gem
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/sylvanus/
  last_verified: '2026-09-21'
  god_win_rate: 0.5126050420168067
  god_matches_won: 488
  god_matches_played: 952
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-21'
  god_matches_analyzed: 15551
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm
    of Radiance, Gluttonous Grimoire, Stone of Binding, Spear of Desolation, Magi''s
    Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord, Helm of Darkness, Rod
    of Asclepius, Prophetic Cloak, Midgardian Mail, Hide of the Nemean Lion, Spear
    of the Magus, Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.11
      fit: 0.39
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.22
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.62
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
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
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Rod of Asclepius, Soul Gem, Shifter''s Shield, Ethereal Staff, Breastplate of
    Valor, Gluttonous Grimoire, Erosion, Eye of Providence, Draconic Scale, Lifebinder,
    Phoenix Feather, Yogi''s Necklace, Glorious Pridwen, Helm of Radiance, Spear of
    Desolation, Sphere of Negation, Stone of Binding, Midgardian Mail, Screeching
    Gargoyle, Jade Scepter, Wish-Granting Pearl, Hide of the Nemean Lion.'
  slot_scores:
    Breastplate of Valor:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.11
      fit: 0.36
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.55
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.92
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Spear of Desolation
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
    Spear of Desolation, Screeching Gargoyle, Kinetic Cuirass, Soul Gem, Spear of
    the Magus, Obsidian Shard, Void Shield, Void Stone, Breastplate of Valor, Shifter''s
    Shield, Doom Orb, Helm of Radiance, Erosion, Shield of the Phoenix, Eye of Providence,
    The World Stone, Draconic Scale, Dreamer''s Idol, Magi''s Cloak, Rod of Asclepius,
    Mantle Of Discord, Midgardian Mail, Chronos'' Pendant.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.52
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.53
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.72
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.44
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Gluttonous Grimoire, Kinetic
    Cuirass, Soul Gem, Breastplate of Valor, Shifter''s Shield, Helm of Radiance,
    Shield of the Phoenix, Erosion, Spear of Desolation, Stone of Binding, Eye of
    Providence, Spear of the Magus, Draconic Scale, Screeching Gargoyle, Rod of Asclepius,
    Bragi''s Harp, Magi''s Cloak, Daybreak Gavel, Obsidian Shard, Bracer of The Abyss,
    Midgardian Mail, Mantle Of Discord, Chronos'' Pendant, Jade Scepter.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.44
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.46
      efficiency: 0.44
      win: 0.53
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.33
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Breastplate
    of Valor, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching
    Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion,
    Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.11
      fit: 0.48
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.22
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.64
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.53
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Tyrfing, Golden Blade,
    Runeforged Hammer, Gluttonous Grimoire, Breastplate of Valor, Hydra''s Lament,
    Shifter''s Shield, Spear of Desolation, Eye of the Storm, Heartseeker, Spear of
    the Magus, Soul Gem, Helm of Radiance, Obsidian Shard, Lernaean Bow, Shield of
    the Phoenix, Erosion, Silverbranch Bow, Eye of Providence, Avenging Blade, Nimble
    Ring, Tekko-Kagi, Stone of Binding, Draconic Scale, Titan''s Bane, Toxic Blade,
    The Crusher, Screeching Gargoyle, Pharaoh''s Curse, Rod of Asclepius, Magi''s
    Cloak, Bragi''s Harp, The Reaper, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.48
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.38
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Soul Gem, Spear of the Magus, Breastplate of Valor, Runeforged Hammer,
    Helm of Radiance, Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Hydra''s
    Lament, Eye of the Storm, Rod of Asclepius, Heartseeker, Shield of the Phoenix,
    Erosion, Eye of Providence, Stone of Binding, Draconic Scale, Chronos'' Pendant,
    Jade Scepter, Doom Orb, Death Metal, Wish-Granting Pearl, Avenging Blade, Screeching
    Gargoyle, Magi''s Cloak, The World Stone, Titan''s Bane, Helm of Darkness, Ancient
    Signet, The Crusher, Mantle Of Discord, Daybreak Gavel, Dreamer''s Idol.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.17
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.17
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.39
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
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
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Helm of Radiance, Gluttonous Grimoire, Stone of Binding, Spear
    of Desolation, Magi''s Cloak, Screeching Gargoyle, Soul Gem, Mantle Of Discord,
    Helm of Darkness, Rod of Asclepius, Prophetic Cloak, Midgardian Mail, Hide of
    the Nemean Lion, Spear of the Magus, Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.11
      fit: 0.39
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.22
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.62
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Shifter's Shield
  - Spirit Robe
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Helm of Radiance, Gluttonous Grimoire,
    Stone of Binding, Spear of Desolation, Magi''s Cloak, Screeching Gargoyle, Soul
    Gem, Mantle Of Discord, Helm of Darkness, Rod of Asclepius, Prophetic Cloak, Midgardian
    Mail, Hide of the Nemean Lion, Spear of the Magus, Leviathan''s Hide, Void Shield,
    Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.53
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.22
      fit: 0.39
    Spirit Robe:
      total: 0.53
      efficiency: 0.34
      win: 0.74
      pick: 0.11
      fit: 0.45
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.18
      fit: 0.62
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.53
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.86
      win: 0.53
      pick: 0.0
      fit: 0.2
  community_ordered:
  - Genji's Guard
  - Spirit Robe
  - Freya's Tears
  swaps:
  - added: Spirit Robe
    removed: Breastplate of Valor
    reason: community 74% win over 48 matches (vs 51% on this god), taking the model's
      weakest slot from Breastplate of Valor
  starter: *id001
---
