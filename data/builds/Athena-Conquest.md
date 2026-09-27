---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.55
  slot_order:
  - name: Stampede
    pick_rate: 0.24
    win_rate: 0.57
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.2
      win_rate: 0.66
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.38
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.65
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.49
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.58
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.62
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.62
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.4
  - name: Deathbringer
    pick_rate: 0.08
    win_rate: 0.79
    alternates:
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.88
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.7
    alternates:
    - name: Freya's Tears
      pick_rate: 0.04
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.04
      win_rate: 0.63
  community_starters:
  - name: Selflessness
    pick_rate: 0.18
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.37
  - name: Bumba's Hammer
    pick_rate: 0.15
    win_rate: 0.56
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-09-27'
  god_win_rate: 0.5602240896358543
  god_matches_won: 200
  god_matches_played: 357
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-27'
  god_matches_analyzed: 5610
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Jotunn's Revenge
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Jotunn''s
    Revenge, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield, Shield
    Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Hide of the
    Nemean Lion, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of
    Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Leviathan''s
    Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy,
    Void Stone, Spear of Desolation, Spectral Armor, Hussar''s Wings, Rod of Asclepius,
    Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament,
    Breastplate of Valor, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.25
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.62
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Shifter''s Shield, Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather,
    Gluttonous Grimoire, Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Hide
    of the Nemean Lion, Runeforged Hammer, Glorious Pridwen, Eye of the Storm, Lifebinder,
    Midgardian Mail, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Void Shield,
    Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Sphere of Negation,
    Screeching Gargoyle, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield, Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.26
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.34
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.9
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.66
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Shifter''s Shield, Void Shield, Spear of the Magus, Soul Gem, Void Stone, Obsidian
    Shard, Avenging Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter,
    Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance,
    Runeforged Hammer, The World Stone, Hide of the Nemean Lion, Titan''s Bane, Magi''s
    Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, Midgardian
    Mail, The Reaper, Daybreak Gavel, Rod of Asclepius, Leviathan''s Hide, Hydra''s
    Lament, Breastplate of Valor.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.66
    Stone of Binding:
      total: 0.57
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.26
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Shifter''s Shield,
    Tyrfing, Shield Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye
    of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s
    Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak
    Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian
    Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade, Breastplate
    of Valor.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.2
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.2
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Hydra''s
    Lament, Shifter''s Shield, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield
    Splitter, Berserker''s Shield, Breastplate of Valor, Erosion, Helm of Radiance,
    Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of Focus, Hide
    of the Nemean Lion, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the
    Magus, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s
    Grace, Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield, Prophetic
    Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.46
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.64
    Spear of Desolation:
      total: 0.55
      efficiency: 0.57
      win: 0.62
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Golden
    Blade, Shifter''s Shield, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Spear of the Magus, Eye of Providence, Avenging Blade, Shield of the Phoenix,
    Stone of Binding, Draconic Scale, Helm of Radiance, Soul Gem, Titan''s Bane, Silverbranch
    Bow, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak, Toxic Blade,
    The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord,
    Midgardian Mail, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.23
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Shifter''s Shield, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal,
    Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World
    Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching
    Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail, Breastplate of
    Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.62
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.23
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.18
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Hide of the
    Nemean Lion, Prophetic Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Spectral
    Armor, Hussar''s Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel,
    Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.25
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.65
      pick: 0.22
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.22
      fit: 0.62
    Shifter's Shield:
      total: 0.58
      efficiency: 0.55
      win: 0.62
      pick: 0.12
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
