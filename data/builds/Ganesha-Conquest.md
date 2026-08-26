---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.17
  slot_order:
  - name: Stampede
    pick_rate: 0.29
    win_rate: 0.58
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.24
      win_rate: 0.4
    - name: Amanita Charm
      pick_rate: 0.1
      win_rate: 0.25
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Stampede
      pick_rate: 0.2
      win_rate: 0.5
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.25
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 1.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.21
      win_rate: 0.38
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.67
  - name: Gauntlet of Thebes
    pick_rate: 0.07
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.67
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.0
  - name: Veve Charm
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Sash
      pick_rate: 0.05
      win_rate: 1.0
    - name: Medallion
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.46
    win_rate: 0.42
  - name: Heroism
    pick_rate: 0.2
    win_rate: 0.38
  - name: Conduit Gem
    pick_rate: 0.15
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-08-26'
  god_win_rate: 0.43902439024390244
  god_matches_won: 18
  god_matches_played: 41
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Freya''s Tears, Kinetic Cuirass, Shifter''s Shield, Erosion,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Prophetic Cloak, Hide of the Nemean Lion, Leviathan''s Hide,
    Helm of Darkness, Void Shield, Spear of Desolation, Ancile, Oni Hunter''s Garb,
    Gladiator''s Shield, Xibalban Effigy, Amanita Charm, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.4
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.8
    Shell of Rebuke:
      total: 0.63
      efficiency: 0.28
      win: 1.0
      pick: 0.16
      fit: 0.5
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.65
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.7
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
  - Shifter's Shield
  - Rod of Asclepius
  flex_slots:
  - Rod of Asclepius
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass, Freya''s Tears,
    Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Eye of Providence, Draconic
    Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Chandra''s Grace,
    Yogi''s Necklace, Glorious Pridwen, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Amanita Charm, Breastplate of Valor.'
  slot_scores:
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
    Shell of Rebuke:
      total: 0.62
      efficiency: 0.28
      win: 1.0
      pick: 0.16
      fit: 0.42
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.58
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.68
    Rod of Asclepius:
      total: 0.6
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Stone of Binding, Freya''s Tears, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Soul Gem, Spear of
    the Magus, Void Shield, Void Stone, Shifter''s Shield, Erosion, Eye of Providence,
    Shield of the Phoenix, Draconic Scale, Doom Orb, Helm of Radiance, The World Stone,
    Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord, Midgardian Mail, Rod of Asclepius,
    Hide of the Nemean Lion, Amanita Charm, Breastplate of Valor.'
  slot_scores:
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.59
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.16
      fit: 0.35
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.45
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.65
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.0
      fit: 0.41
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Freya's Tears
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Nimble Ring, Freya''s Tears, Kinetic Cuirass, Gluttonous
    Grimoire, Shifter''s Shield, Soul Gem, Helm of Radiance, Erosion, Shield of the
    Phoenix, Stone of Binding, Eye of Providence, Draconic Scale, Magi''s Cloak, Screeching
    Gargoyle, Spear of Desolation, Spear of the Magus, Daybreak Gavel, Bragi''s Harp,
    Rod of Asclepius, Midgardian Mail, Mantle Of Discord, Bracer of The Abyss, Hide
    of the Nemean Lion, Leviathan''s Hide, Amanita Charm, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.2
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
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.16
      fit: 0.26
    Bragi's Harp:
      total: 0.52
      efficiency: 0.44
      win: 0.67
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shell of Rebuke
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
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Kinetic
    Cuirass, Shield of the Phoenix, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance,
    Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone
    of Binding, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear
    of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Breastplate of Valor, Amanita Charm.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.2
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
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.16
      fit: 0.32
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.64
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.67
      pick: 0.0
      fit: 0.46
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Freya''s Tears, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged
    Hammer, Shifter''s Shield, Gluttonous Grimoire, Eye of the Storm, Hydra''s Lament,
    Tyrfing, Heartseeker, Spear of Desolation, Lernaean Bow, Spear of the Magus, Erosion,
    Tekko-Kagi, Eye of Providence, Soul Gem, Shield of the Phoenix, Avenging Blade,
    Helm of Radiance, Silverbranch Bow, Stone of Binding, Draconic Scale, Titan''s
    Bane, The Crusher, Toxic Blade, Pharaoh''s Curse, Nimble Ring, Magi''s Cloak,
    The Reaper, Screeching Gargoyle, Shogun''s Ofuda, Mantle Of Discord, Midgardian
    Mail, Amanita Charm, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.2
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
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.51
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.16
      fit: 0.29
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.38
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Gluttonous Grimoire
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
    Freya''s Tears, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Spear of the Magus, Soul Gem, Runeforged Hammer, Helm of Radiance, Shifter''s
    Shield, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius,
    Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Stone of Binding,
    Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging
    Blade, Chronos'' Pendant, Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s
    Bane, Screeching Gargoyle, Ancient Signet, The Crusher, Mantle Of Discord, Dreamer''s
    Idol, Midgardian Mail, Amanita Charm, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.2
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
    Shell of Rebuke:
      total: 0.6
      efficiency: 0.28
      win: 1.0
      pick: 0.16
      fit: 0.29
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.54
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Shifter''s Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Gluttonous Grimoire, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail,
    Prophetic Cloak, Hide of the Nemean Lion, Leviathan''s Hide, Helm of Darkness,
    Void Shield, Spear of Desolation, Ancile, Oni Hunter''s Garb, Gladiator''s Shield,
    Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.2
      fit: 0.4
    Breastplate of Valor:
      total: 0.41
      efficiency: 0.65
      win: 0.25
      pick: 0.14
      fit: 0.4
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.67
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.67
      pick: 0.13
      fit: 0.65
    Shifter's Shield:
      total: 0.6
      efficiency: 0.55
      win: 0.67
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.45
      efficiency: 0.65
      win: 0.25
      pick: 0.1
      fit: 0.7
  starter: *id001
---
