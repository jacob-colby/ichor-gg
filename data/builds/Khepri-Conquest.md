---
type: smite-build
god: Khepri
mode: Conquest
builds:
- source: community
  aspect: Aspect of Laceration
  aspect_pick_rate: 0.71
  aspect_win_rate: 0.7
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.45
    win_rate: 0.59
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.21
      win_rate: 0.75
    - name: The Cosmic Horror
      pick_rate: 0.16
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.78
    alternates:
    - name: Stampede
      pick_rate: 0.21
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.33
  - name: Freya's Tears
    pick_rate: 0.26
    win_rate: 0.7
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.6
    - name: Damaru
      pick_rate: 0.08
      win_rate: 0.0
  - name: Stampede
    pick_rate: 0.16
    win_rate: 0.5
    alternates:
    - name: Totem of Death
      pick_rate: 0.14
      win_rate: 0.2
    - name: Omen Drum
      pick_rate: 0.08
      win_rate: 0.67
  - name: Stone of Binding
    pick_rate: 0.12
    win_rate: 0.75
    alternates:
    - name: Evil Eye
      pick_rate: 0.12
      win_rate: 0.75
    - name: Shield
      pick_rate: 0.06
      win_rate: 1.0
  - name: Veve Charm
    pick_rate: 0.13
    win_rate: 1.0
    alternates:
    - name: Void Shard
      pick_rate: 0.09
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.09
      win_rate: 0.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.29
    win_rate: 0.73
  - name: Heroism
    pick_rate: 0.24
    win_rate: 0.78
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/khepri/
  last_verified: '2026-10-22'
  god_win_rate: 0.6052631578947368
  god_matches_won: 23
  god_matches_played: 38
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-22'
  god_matches_analyzed: 1760
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Shifter's Shield
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Magi''s Cloak, Helm
    of Radiance, Gluttonous Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian
    Mail, Prophetic Cloak, Leviathan''s Hide, Helm of Darkness, Void Shield, Spear
    of Desolation, Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Xibalban Effigy,
    Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.62
      efficiency: 0.51
      win: 0.75
      pick: 0.26
      fit: 0.6
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.4
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.7
      pick: 0.4
      fit: 0.65
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Stone of Binding
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
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Eye of Providence, Draconic
    Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Chandra''s Grace,
    Glorious Pridwen, Lifebinder, Midgardian Mail, Helm of Radiance, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Ancile, Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.61
      efficiency: 0.51
      win: 0.75
      pick: 0.26
      fit: 0.52
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.37
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.7
      pick: 0.4
      fit: 0.58
    Amanita Charm:
      total: 0.68
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.98
  community_ordered:
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
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
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass,
    Screeching Gargoyle, Spear of Desolation, Soul Gem, Spear of the Magus, Void Shield,
    Obsidian Shard, Void Stone, Shifter''s Shield, Erosion, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Doom Orb, Helm of Radiance, The World Stone, Magi''s
    Cloak, Dreamer''s Idol, Mantle Of Discord, Midgardian Mail, Rod of Asclepius,
    Breastplate of Valor.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.58
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.68
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.28
    Stone of Binding:
      total: 0.64
      efficiency: 0.51
      win: 0.75
      pick: 0.26
      fit: 0.75
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.7
      pick: 0.4
      fit: 0.45
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Genji's Guard
  - Stone of Binding
  - Freya's Tears
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
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Shifter''s Shield, Soul Gem, Helm of Radiance, Erosion, Shield of the
    Phoenix, Eye of Providence, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Spear of Desolation, Spear of the Magus, Daybreak Gavel, Bragi''s Harp, Rod of
    Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard,
    Leviathan''s Hide, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.21
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
      fit: 0.3
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.4
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
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Spear of Desolation
  flex_slots:
  - Shield of the Phoenix
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Gem
    of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus,
    Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Breastplate
    of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.26
      fit: 0.42
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.7
      pick: 0.4
      fit: 0.64
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.46
  community_ordered:
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged
    Hammer, Shifter''s Shield, Gluttonous Grimoire, Eye of the Storm, Tyrfing, Hydra''s
    Lament, Heartseeker, Spear of Desolation, Lernaean Bow, Spear of the Magus, Erosion,
    Silverbranch Bow, Tekko-Kagi, Eye of Providence, Soul Gem, Shield of the Phoenix,
    Avenging Blade, Helm of Radiance, Draconic Scale, Toxic Blade, Obsidian Shard,
    Titan''s Bane, The Crusher, Pharaoh''s Curse, Nimble Ring, Magi''s Cloak, The
    Reaper, Screeching Gargoyle, Shogun''s Ofuda, Mantle Of Discord, Midgardian Mail,
    Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.26
      fit: 0.39
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.78
      pick: 0.33
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
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.4
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Spear of the Magus, Soul Gem, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament,
    Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix,
    Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging
    Blade, Chronos'' Pendant, Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s
    Bane, Screeching Gargoyle, Ancient Signet, The Crusher, Mantle Of Discord, Dreamer''s
    Idol, Midgardian Mail, Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.75
      pick: 0.26
      fit: 0.39
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.24
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.4
      fit: 0.38
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Stone of Binding
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
    of the Phoenix, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of
    Discord, Screeching Gargoyle, Midgardian Mail, Prophetic Cloak, Leviathan''s Hide,
    Helm of Darkness, Void Shield, Spear of Desolation, Ancile, Oni Hunter''s Garb,
    Gladiator''s Shield, Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.66
      efficiency: 0.66
      win: 0.78
      pick: 0.33
      fit: 0.4
    Breastplate of Valor:
      total: 0.44
      efficiency: 0.65
      win: 0.33
      pick: 0.11
      fit: 0.4
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.7
      pick: 0.4
      fit: 0.65
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
---
