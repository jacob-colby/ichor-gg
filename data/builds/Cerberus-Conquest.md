---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.57
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.25
    win_rate: 0.58
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.23
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.46
  - name: Genji's Guard
    pick_rate: 0.23
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.57
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.63
  - name: Shell of Rebuke
    pick_rate: 0.15
    win_rate: 0.54
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.6
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.52
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 0.58
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.48
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.58
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.71
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.68
  - name: Sage's Ring
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.58
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.44
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.49
  - name: Bluestone Brooch
    pick_rate: 0.22
    win_rate: 0.65
  - name: Conduit Gem
    pick_rate: 0.15
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-08-21'
  god_win_rate: 0.5441640378548895
  god_matches_won: 345
  god_matches_played: 634
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-21'
  god_matches_analyzed: 12786
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Freya''s Tears, Draconic
    Scale, Shield of the Phoenix, Gluttonous Grimoire, Mantle Of Discord, Stone of
    Binding, Erosion, Eye of Providence, Spectral Armor, Nimble Ring, Helm of Radiance,
    Soul Gem, Leviathan''s Hide, Magi''s Cloak, Stampede, Midgardian Mail, Screeching
    Gargoyle, Hide of the Nemean Lion, Ethereal Staff, Spear of Desolation, Doublet
    of Binding, Rod of Asclepius, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.15
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.13
      fit: 0.51
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.25
      fit: 0.56
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.58
      pick: 0.13
      fit: 0.56
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.56
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Ethereal Staff, Rod of Asclepius, Gluttonous Grimoire, Draconic Scale,
    Phoenix Feather, Freya''s Tears, Chandra''s Grace, Erosion, Eye of Providence,
    Yogi''s Necklace, Spectral Armor, Mantle Of Discord, Stone of Binding, Nimble
    Ring, Leviathan''s Hide, Lifebinder, Glorious Pridwen, Helm of Radiance, Blood-Bound
    Book, Midgardian Mail, Sphere of Negation.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.15
      fit: 0.28
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.79
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.25
      fit: 0.54
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.58
      pick: 0.13
      fit: 0.54
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Shifter's Shield
  - Rod of Tahuti
  flex_slots:
  - Screeching Gargoyle
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Stone of Binding, Amanita Charm,
    Kinetic Cuirass, Soul Gem, Screeching Gargoyle, Spear of Desolation, Void Shield,
    Spear of the Magus, Void Stone, Obsidian Shard, Freya''s Tears, Shield of the
    Phoenix, Mantle Of Discord, Draconic Scale, Nimble Ring, Erosion, Spectral Armor,
    Eye of Providence, Helm of Radiance, Doom Orb, The Cosmic Horror, The World Stone,
    Leviathan''s Hide, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.63
    Stone of Binding:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.7
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.57
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.25
      fit: 0.41
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
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
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Nimble Ring, Gluttonous
    Grimoire, Freya''s Tears, Soul Gem, Shield of the Phoenix, Mantle Of Discord,
    Stone of Binding, Draconic Scale, Death Metal, Spectral Armor, Helm of Radiance,
    Erosion, Eye of Providence, Leviathan''s Hide, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, Spear of the Magus, Spear of Desolation, Ethereal Staff, Bragi''s
    Harp, Rod of Asclepius, Midgardian Mail.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.15
      fit: 0.2
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.57
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Freya''s Tears, Shield of the Phoenix, Soul Gem, Spear of Desolation,
    Gluttonous Grimoire, Screeching Gargoyle, Nimble Ring, Mantle Of Discord, Stone
    of Binding, Chronos'' Pendant, Draconic Scale, Helm of Radiance, Death Metal,
    Spectral Armor, Erosion, Prophetic Cloak, Eye of Providence, Gladiator''s Shield,
    Leviathan''s Hide, Chandra''s Grace, Ethereal Staff, Gem of Focus, Spear of the
    Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.31
      fit: 0.41
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.15
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.48
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.13
      fit: 0.55
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.58
      pick: 0.25
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, The Crusher, Shield
    Splitter, Runeforged Hammer, Golden Blade, Soul Gem, Death Metal, Freya''s Tears,
    Eye of the Storm, Nimble Ring, Shield of the Phoenix, Hydra''s Lament, Mantle
    Of Discord, Stone of Binding, Heartseeker, Draconic Scale, The Reaper, Pharaoh''s
    Curse, Spear of Desolation, Spear of the Magus, Lernaean Bow, Tyrfing, Spectral
    Armor, Erosion, Helm of Radiance, Shogun''s Ofuda, Avenging Blade, Eye of Providence,
    Tekko-Kagi, Obsidian Shard, Titan''s Bane, Leviathan''s Hide, Silverbranch Bow,
    Magi''s Cloak.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.15
      fit: 0.21
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.58
      pick: 0.25
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Gluttonous Grimoire, Kinetic Cuirass, Soul
    Gem, Death Metal, Nimble Ring, The Crusher, Shield Splitter, Spear of the Magus,
    Spear of Desolation, Runeforged Hammer, Helm of Radiance, Obsidian Shard, Freya''s
    Tears, Shield of the Phoenix, Mantle Of Discord, Stone of Binding, Golden Blade,
    Draconic Scale, Hydra''s Lament, Ethereal Staff, Eye of the Storm, Rod of Asclepius,
    Pharaoh''s Curse, Heartseeker, Spectral Armor, The Reaper, Erosion, Eye of Providence,
    Shogun''s Ofuda, Lernaean Bow, Leviathan''s Hide, Tyrfing, Jade Scepter, Doom
    Orb, The Cosmic Horror.'
  slot_scores:
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.57
      pick: 0.15
      fit: 0.2
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.46
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.58
      pick: 0.25
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.36
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
  - Genji's Guard
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Freya''s
    Tears, Shield of the Phoenix, Gluttonous Grimoire, Mantle Of Discord, Stone of
    Binding, Erosion, Eye of Providence, Draconic Scale, Spectral Armor, Nimble Ring,
    Helm of Radiance, Soul Gem, Leviathan''s Hide, Magi''s Cloak, Midgardian Mail,
    Screeching Gargoyle, Hide of the Nemean Lion, Ethereal Staff, Spear of Desolation,
    Doublet of Binding, Rod of Asclepius, Void Shield, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.31
      fit: 0.31
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.15
      fit: 0.31
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.6
      win: 0.57
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.52
      pick: 0.13
      fit: 0.51
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.25
      fit: 0.56
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.56
  starter: *id001
---
