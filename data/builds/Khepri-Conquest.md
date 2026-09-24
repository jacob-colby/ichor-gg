---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.7
  aspect_win_rate: 0.67
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.38
    win_rate: 0.61
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.44
    - name: The Cosmic Horror
      pick_rate: 0.09
      win_rate: 0.75
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.33
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.67
    - name: Stampede
      pick_rate: 0.13
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.17
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.67
    - name: Erosion
      pick_rate: 0.09
      win_rate: 0.75
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
  - name: Spirit Robe
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.0
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.5
  - name: Captain's Ring
    pick_rate: 0.16
    win_rate: 0.33
    alternates:
    - name: Plated Metal
      pick_rate: 0.11
      win_rate: 1.0
    - name: Evil Eye
      pick_rate: 0.11
      win_rate: 0.5
  community_starters:
  - name: Selflessness
    pick_rate: 0.32
    win_rate: 0.6
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.4
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-09-24'
  god_win_rate: 0.6382978723404256
  god_matches_won: 30
  god_matches_played: 47
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Erosion, Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield,
    Breastplate of Valor, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Hide of the Nemean Lion, Leviathan''s Hide, Helm of
    Darkness, Void Shield, Spear of Desolation, Ancile, Oni Hunter''s Garb, Gladiator''s
    Shield, Xibalban Effigy, Draconic Scale.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.8
    Shell of Rebuke:
      total: 0.64
      efficiency: 0.28
      win: 1.0
      pick: 0.23
      fit: 0.5
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.65
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.75
      pick: 0.14
      fit: 0.7
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Erosion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Spirit Robe — physical protection
    swap_item: Spirit Robe
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Erosion, Shield of the Phoenix, Rod of Tahuti, Kinetic
    Cuirass, Rod of Asclepius, Shifter''s Shield, Soul Gem, Breastplate of Valor,
    Eye of Providence, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Chandra''s
    Grace, Yogi''s Necklace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone
    of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void
    Shield, Magi''s Cloak, Ancile, Draconic Scale.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.93
    Shell of Rebuke:
      total: 0.62
      efficiency: 0.28
      win: 1.0
      pick: 0.23
      fit: 0.42
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.58
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.98
    Erosion:
      total: 0.63
      efficiency: 0.51
      win: 0.75
      pick: 0.14
      fit: 0.68
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Erosion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Rod of Tahuti, Erosion, Amanita Charm, Stone of Binding, Gluttonous
    Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Soul Gem,
    Spear of the Magus, Void Shield, Breastplate of Valor, Obsidian Shard, Void Stone,
    Shifter''s Shield, Eye of Providence, Shield of the Phoenix, Doom Orb, Helm of
    Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius, Hide of the Nemean Lion, Draconic Scale.'
  slot_scores:
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.59
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.23
      fit: 0.35
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.45
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.49
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.75
      pick: 0.14
      fit: 0.49
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Erosion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Amanita Charm
  - Erosion
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
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Erosion, Amanita Charm, Nimble Ring, Kinetic Cuirass,
    Gluttonous Grimoire, Breastplate of Valor, Shifter''s Shield, Soul Gem, Helm of
    Radiance, Shield of the Phoenix, Stone of Binding, Eye of Providence, Magi''s
    Cloak, Screeching Gargoyle, Spear of Desolation, Spear of the Magus, Daybreak
    Gavel, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer
    of The Abyss, Obsidian Shard, Hide of the Nemean Lion, Leviathan''s Hide, Draconic
    Scale.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.5
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.3
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.23
      fit: 0.26
    Bragi's Harp:
      total: 0.51
      efficiency: 0.44
      win: 0.63
      pick: 0.0
      fit: 0.44
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.36
    Erosion:
      total: 0.58
      efficiency: 0.51
      win: 0.75
      pick: 0.14
      fit: 0.36
  community_ordered:
  - Shell of Rebuke
  - Erosion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Amanita Charm
  - Prophetic Cloak
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Erosion, Breastplate
    of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Screeching Gargoyle, Soul Gem, Shifter''s Shield, Chronos'' Pendant, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Draconic
    Scale.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.48
    Prophetic Cloak:
      total: 0.56
      efficiency: 0.44
      win: 0.67
      pick: 0.18
      fit: 0.64
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.23
      fit: 0.32
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.45
    Erosion:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.14
      fit: 0.45
  community_ordered:
  - Prophetic Cloak
  - Shell of Rebuke
  - Freya's Tears
  - Erosion
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Erosion
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Erosion,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Golden Blade,
    Breastplate of Valor, Runeforged Hammer, Shifter''s Shield, Gluttonous Grimoire,
    Eye of the Storm, Tyrfing, Hydra''s Lament, Heartseeker, Spear of Desolation,
    Lernaean Bow, Spear of the Magus, Silverbranch Bow, Tekko-Kagi, Eye of Providence,
    Soul Gem, Shield of the Phoenix, Avenging Blade, Helm of Radiance, Stone of Binding,
    Toxic Blade, Obsidian Shard, Titan''s Bane, The Crusher, Pharaoh''s Curse, Nimble
    Ring, Magi''s Cloak, The Reaper, Screeching Gargoyle, Shogun''s Ofuda, Mantle
    Of Discord, Midgardian Mail, Draconic Scale.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.45
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.23
      fit: 0.29
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.41
    Erosion:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.14
      fit: 0.41
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Erosion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Freya's Tears
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Erosion, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Breastplate of Valor,
    Spear of Desolation, Shield Splitter, Spear of the Magus, Soul Gem, Runeforged
    Hammer, Helm of Radiance, Shifter''s Shield, Obsidian Shard, Berserker''s Shield,
    Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Eye of Providence,
    Shield of the Phoenix, Stone of Binding, Doom Orb, Jade Scepter, Death Metal,
    Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant, Magi''s Cloak, The World
    Stone, Helm of Darkness, Titan''s Bane, Screeching Gargoyle, Ancient Signet, The
    Crusher, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail, Draconic Scale.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.51
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.23
      fit: 0.29
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.41
    Erosion:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.14
      fit: 0.41
  community_ordered:
  - Shell of Rebuke
  - Freya's Tears
  - Erosion
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
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Gluttonous
    Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Hide of the
    Nemean Lion, Leviathan''s Hide, Helm of Darkness, Void Shield, Spear of Desolation,
    Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Xibalban Effigy.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.45
      efficiency: 0.66
      win: 0.33
      pick: 0.18
      fit: 0.4
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.63
      pick: 0.26
      fit: 0.65
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.63
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
