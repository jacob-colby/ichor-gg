---
type: smite-build
god: Cerberus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Souls
  aspect_pick_rate: 0.07
  aspect_win_rate: 0.63
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.32
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.24
      win_rate: 0.62
    - name: Shifter's Shield
      pick_rate: 0.05
      win_rate: 0.69
  - name: Stampede
    pick_rate: 0.17
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.54
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.7
  - name: Shell of Rebuke
    pick_rate: 0.21
    win_rate: 0.49
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.72
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.64
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.66
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.69
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.43
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.73
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.54
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.09
    win_rate: 0.83
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.29
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.28
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.56
  - name: Bluestone Brooch
    pick_rate: 0.15
    win_rate: 0.75
  source_url: https://smitebrain.com/gods/cerberus/
  last_verified: '2026-09-26'
  god_win_rate: 0.6068702290076335
  god_matches_won: 159
  god_matches_played: 262
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-26'
  god_matches_analyzed: 4198
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Draconic Scale, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Shield of the Phoenix,
    Stone of Binding, Helm of Radiance, Magi''s Cloak, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Prophetic
    Cloak, Void Shield, Ancile, Spear of Desolation, Nimble Ring, Helm of Darkness,
    Oni Hunter''s Garb, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.35
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.57
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.69
      pick: 0.05
      fit: 0.63
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.63
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
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
  - Freya's Tears
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Draconic Scale, Shifter''s Shield, Rod of Asclepius, Soul Gem, Breastplate of
    Valor, Erosion, Eye of Providence, Ethereal Staff, Gluttonous Grimoire, Phoenix
    Feather, Yogi''s Necklace, Chandra''s Grace, Lifebinder, Glorious Pridwen, Stone
    of Binding, Midgardian Mail, Helm of Radiance, Sphere of Negation, Leviathan''s
    Hide, Magi''s Cloak, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.71
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.85
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.5
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.61
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.91
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
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Draconic Scale, Screeching Gargoyle, Shifter''s Shield, Spear
    of Desolation, Spear of the Magus, Void Shield, Soul Gem, Breastplate of Valor,
    Obsidian Shard, Void Stone, Erosion, Eye of Providence, Shield of the Phoenix,
    Doom Orb, Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Nimble
    Ring, Mantle Of Discord, Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.41
    Draconic Scale:
      total: 0.58
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Draconic
    Scale, Gluttonous Grimoire, Shifter''s Shield, Breastplate of Valor, Soul Gem,
    Helm of Radiance, Erosion, Stone of Binding, Eye of Providence, Shield of the
    Phoenix, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Spear of the Magus,
    Spear of Desolation, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle
    Of Discord, Bracer of The Abyss, Obsidian Shard, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.2
    Bracer of The Abyss:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Kinetic Cuirass, Draconic Scale, Shield of the Phoenix, Shifter''s
    Shield, Spear of Desolation, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Helm of Radiance, Prophetic Cloak, Gluttonous Grimoire, Erosion, Eye of Providence,
    Stone of Binding, Gladiator''s Shield, Nimble Ring, Gem of Focus, Magi''s Cloak,
    Spear of the Magus, Rod of Asclepius, Eye of Erebus, Mantle Of Discord, Midgardian
    Mail, Daybreak Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.45
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.59
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.11
      fit: 0.42
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.42
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Draconic Scale, Shield Splitter, Shifter''s
    Shield, Runeforged Hammer, Breastplate of Valor, Golden Blade, Gluttonous Grimoire,
    Eye of the Storm, Hydra''s Lament, Heartseeker, Tyrfing, Spear of Desolation,
    Lernaean Bow, Erosion, Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging
    Blade, Helm of Radiance, Soul Gem, Stone of Binding, Shield of the Phoenix, Obsidian
    Shard, Titan''s Bane, The Crusher, Pharaoh''s Curse, Silverbranch Bow, Magi''s
    Cloak, Nimble Ring, The Reaper, Toxic Blade, Shogun''s Ofuda, Screeching Gargoyle,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.23
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.37
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
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
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Kinetic Cuirass, Gluttonous Grimoire, Draconic
    Scale, Shifter''s Shield, Breastplate of Valor, Shield Splitter, Spear of Desolation,
    Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard,
    Golden Blade, Nimble Ring, Eye of the Storm, Hydra''s Lament, Rod of Asclepius,
    Heartseeker, Erosion, Eye of Providence, Stone of Binding, Shield of the Phoenix,
    Tyrfing, Lernaean Bow, Bragi''s Harp, Jade Scepter, Doom Orb, Wish-Granting Pearl,
    Avenging Blade, Death Metal, Magi''s Cloak, Chronos'' Pendant, Tekko-Kagi, Pharaoh''s
    Curse, The World Stone, Silverbranch Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.21
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.32
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.35
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
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
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Helm of Radiance, Magi''s Cloak, Gluttonous
    Grimoire, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Leviathan''s
    Hide, Prophetic Cloak, Void Shield, Ancile, Spear of Desolation, Nimble Ring,
    Helm of Darkness, Oni Hunter''s Garb, Rod of Asclepius.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.72
      pick: 0.19
      fit: 0.35
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.61
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.73
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.66
      pick: 0.28
      fit: 0.57
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.69
      pick: 0.05
      fit: 0.63
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
