---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.57
  aspect_win_rate: 0.45
  slot_order:
  - name: Chandra's Grace
    pick_rate: 0.15
    win_rate: 0.25
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.7
    - name: Daybreak Gavel
      pick_rate: 0.1
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Regrowth Striders
      pick_rate: 0.09
      win_rate: 0.71
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.12
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.56
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.42
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.4
  - name: Mote of Chaos
    pick_rate: 0.07
    win_rate: 0.2
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.57
  - name: Mana Tome
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.67
    - name: Spectral Armor
      pick_rate: 0.07
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.2
    win_rate: 0.44
  - name: Bumba's Cudgel
    pick_rate: 0.15
    win_rate: 0.58
  - name: Bumba's Hammer
    pick_rate: 0.15
    win_rate: 0.83
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-09-24'
  god_win_rate: 0.5121951219512195
  god_matches_won: 42
  god_matches_played: 82
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
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
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
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Shifter''s Shield, Runeforged Hammer, Eye of the Storm, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s
    Lament, Stone of Binding, Gluttonous Grimoire, Avenging Blade, Helm of Radiance,
    Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Screeching Gargoyle, Hide of
    the Nemean Lion, Heartseeker, Leviathan''s Hide, Spear of Desolation, Void Shield,
    Stampede, Ancile, Rod of Asclepius, Oni Hunter''s Garb, Prophetic Cloak, Soul
    Gem, Void Stone, Spear of the Magus, Arondight, Xibalban Effigy, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.06
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.17
      fit: 0.31
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.2
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.39
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.22
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Rod of Asclepius, Shifter''s Shield, Runeforged Hammer, Shield
    Splitter, Soul Gem, Eye of the Storm, Berserker''s Shield, Erosion, Ethereal Staff,
    Eye of Providence, The Reaper, Draconic Scale, Yogi''s Necklace, Phoenix Feather,
    Hydra''s Lament, Gluttonous Grimoire, Avenging Blade, Glorious Pridwen, Lifebinder,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Hide of the Nemean Lion,
    Magi''s Cloak, Leviathan''s Hide, Sphere of Negation, Void Shield, Stampede, Ancile,
    Screeching Gargoyle, Oni Hunter''s Garb, Heartseeker, Daybreak Gavel, Chandra''s
    Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.17
      fit: 0.28
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.2
      fit: 0.28
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.8
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Kinetic Cuirass, Screeching Gargoyle, Spear
    of Desolation, Heartseeker, Spear of the Magus, Void Shield, Soul Gem, Shifter''s
    Shield, Void Stone, Obsidian Shard, Shield Splitter, Runeforged Hammer, Titan''s
    Bane, The Crusher, Berserker''s Shield, Eye of the Storm, The Reaper, Hydra''s
    Lament, Erosion, Eye of Providence, Shield of the Phoenix, Doom Orb, Draconic
    Scale, Helm of Radiance, The World Stone, Pendulum Blade, Dreamer''s Idol, Avatar''s
    Parashu, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Rod of Asclepius,
    Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.04
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.17
      fit: 0.22
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.56
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.16
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Nimble Ring
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Shifter''s Shield,
    Tyrfing, Runeforged Hammer, Soul Gem, Shield Splitter, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Silverbranch Bow, Shogun''s Ofuda, Toxic Blade, Hydra''s Lament,
    Erosion, Helm of Radiance, Eye of the Storm, Shield of the Phoenix, Eye of Providence,
    Stone of Binding, Draconic Scale, Magi''s Cloak, The Reaper, Bragi''s Harp, Tekko-Kagi,
    Screeching Gargoyle, Spear of Desolation, Spear of the Magus, Rod of Asclepius,
    Avenging Blade, Midgardian Mail, Mantle Of Discord, Daybreak Gavel.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.17
      fit: 0.19
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.2
      fit: 0.19
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.3
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Spear of Desolation, Hydra''s
    Lament, Soul Gem, Screeching Gargoyle, Shifter''s Shield, Chronos'' Pendant, Berserker''s
    Shield, Shield Splitter, Prophetic Cloak, Runeforged Hammer, Gluttonous Grimoire,
    Helm of Radiance, Gladiator''s Shield, Erosion, Eye of Providence, Arondight,
    Gem of Focus, Draconic Scale, Eye of the Storm, Stone of Binding, Eye of Erebus,
    Rod of Asclepius, Spear of the Magus, Magi''s Cloak, Midgardian Mail, Glorious
    Pridwen, Obsidian Shard, Mantle Of Discord, Jade Scepter, Hide of the Nemean Lion,
    Wish-Granting Pearl, Avenging Blade, Daybreak Gavel, Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.17
      fit: 0.48
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.2
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.63
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Shifter''s
    Shield, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Lernaean Bow, Tekko-Kagi, Spear of Desolation, Tyrfing, Avenging
    Blade, Spear of the Magus, Erosion, Titan''s Bane, Eye of Providence, Shield of
    the Phoenix, Soul Gem, The Crusher, Helm of Radiance, Draconic Scale, Obsidian
    Shard, Stone of Binding, Pharaoh''s Curse, The Reaper, Nimble Ring, Silverbranch
    Bow, Magi''s Cloak, Shogun''s Ofuda, Screeching Gargoyle, Bragi''s Harp, Toxic
    Blade, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.04
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.17
      fit: 0.22
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.47
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.23
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
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
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Spear
    of the Magus, Shield Splitter, Shifter''s Shield, Runeforged Hammer, Soul Gem,
    Helm of Radiance, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Doom Orb, Jade Scepter, Draconic Scale, Death Metal, Stone of Binding,
    Wish-Granting Pearl, Avenging Blade, Chronos'' Pendant, The World Stone, Titan''s
    Bane, The Crusher, Ancient Signet, Magi''s Cloak, Triton''s Conch, Dreamer''s
    Idol, Helm of Darkness, Screeching Gargoyle, Daybreak Gavel.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.17
      fit: 0.22
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.67
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.42
    Transcendence:
      total: 0.47
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.18
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Shifter''s Shield, Runeforged Hammer, Eye of the Storm,
    Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the
    Phoenix, Hydra''s Lament, Stone of Binding, Gluttonous Grimoire, Avenging Blade,
    Helm of Radiance, Magi''s Cloak, Midgardian Mail, Mantle Of Discord, Screeching
    Gargoyle, Hide of the Nemean Lion, Heartseeker, Leviathan''s Hide, Spear of Desolation,
    Void Shield, Stampede, Daybreak Gavel, Ancile, Rod of Asclepius, Oni Hunter''s
    Garb, Prophetic Cloak, Soul Gem, Void Stone, Spear of the Magus, Arondight, Xibalban
    Effigy.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.57
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.19
      fit: 0.5
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.12
      fit: 0.56
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
