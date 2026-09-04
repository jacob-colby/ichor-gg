---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.49
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.57
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.26
      win_rate: 0.45
    - name: Chronos' Pendant
      pick_rate: 0.06
      win_rate: 0.63
  - name: Breastplate of Valor
    pick_rate: 0.17
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.19
      win_rate: 0.45
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.24
    win_rate: 0.52
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.68
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.64
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.65
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.55
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.65
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.47
  - name: Engraved Guard
    pick_rate: 0.07
    win_rate: 0.58
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.58
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.6
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.3
    win_rate: 0.43
  - name: Bumba's Hammer
    pick_rate: 0.23
    win_rate: 0.58
  - name: Bluestone Brooch
    pick_rate: 0.08
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-09-04'
  god_win_rate: 0.5089514066496164
  god_matches_won: 199
  god_matches_played: 391
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-04'
  god_matches_analyzed: 11911
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Shield Splitter
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield Splitter, Eye
    of the Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Kinetic Cuirass, Shield of the Phoenix, Stone of Binding, Hydra''s Lament, Magi''s
    Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Heartseeker, Oni Hunter''s Garb, Spear of Desolation, Prophetic Cloak,
    Daybreak Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy, Spectral Armor,
    Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.37
      fit: 0.31
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.57
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.52
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Shield of the Phoenix
  - Shifter's Shield
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Rod of Asclepius, Shield Splitter, Soul Gem, Eye of the Storm, Berserker''s Shield,
    Erosion, Ethereal Staff, Eye of Providence, The Reaper, Draconic Scale, Yogi''s
    Necklace, Kinetic Cuirass, Hydra''s Lament, Phoenix Feather, Gluttonous Grimoire,
    Avenging Blade, Chandra''s Grace, Glorious Pridwen, Lifebinder, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Daybreak Gavel, Magi''s Cloak, Leviathan''s
    Hide, Void Shield, Sphere of Negation, Stampede, Ancile, Screeching Gargoyle,
    Heartseeker, Oni Hunter''s Garb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.39
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.57
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.8
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.56
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.46
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Avenging Blade
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Avenging Blade
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle, Void Shield, Spear of
    Desolation, Heartseeker, Spear of the Magus, Shield Splitter, Void Stone, Soul
    Gem, Obsidian Shard, Berserker''s Shield, Titan''s Bane, The Crusher, Eye of the
    Storm, Erosion, The Reaper, Hydra''s Lament, Eye of Providence, Shield of the
    Phoenix, Draconic Scale, Kinetic Cuirass, Helm of Radiance, Doom Orb, The World
    Stone, Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Avatar''s Parashu, Mantle
    Of Discord, Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.53
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.63
    Stone of Binding:
      total: 0.54
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.7
    Avenging Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.57
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield Splitter, Pharaoh''s
    Curse, Soul Gem, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion,
    Helm of Radiance, Eye of Providence, Stone of Binding, Eye of the Storm, Shield
    of the Phoenix, Hydra''s Lament, Toxic Blade, Draconic Scale, Kinetic Cuirass,
    Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Midgardian Mail,
    Mantle Of Discord, Spear of Desolation, Bragi''s Harp, Spear of the Magus, Tekko-Kagi,
    Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.43
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
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Chronos' Pendant
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Chronos' Pendant
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
    Amanita Charm, Chronos'' Pendant, Shield of the Phoenix, Spear of Desolation,
    Hydra''s Lament, Screeching Gargoyle, Soul Gem, Shield Splitter, Berserker''s
    Shield, Prophetic Cloak, Erosion, Helm of Radiance, Gluttonous Grimoire, Eye of
    Providence, Gladiator''s Shield, Draconic Scale, Kinetic Cuirass, Stone of Binding,
    Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye
    of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Leviathan''s Hide, Jade
    Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.53
      pick: 0.23
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.52
      pick: 0.37
      fit: 0.48
    Chronos' Pendant:
      total: 0.54
      efficiency: 0.55
      win: 0.63
      pick: 0.06
      fit: 0.42
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.64
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Chronos' Pendant
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Shifter's Shield
  - Freya's Tears
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Shield Splitter, Golden Blade, Eye of the Storm, Gluttonous
    Grimoire, Hydra''s Lament, Heartseeker, Lernaean Bow, Erosion, Spear of Desolation,
    Tekko-Kagi, Eye of Providence, Tyrfing, Avenging Blade, Spear of the Magus, Shield
    of the Phoenix, Stone of Binding, Draconic Scale, Kinetic Cuirass, Helm of Radiance,
    Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s
    Cloak, The Reaper, Silverbranch Bow, Nimble Ring, Shogun''s Ofuda, Screeching
    Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.42
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.38
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Shield Splitter
  - Shifter's Shield
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Shield Splitter, Spear of Desolation, Chronos''
    Pendant, Spear of the Magus, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s
    Shield, Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Erosion,
    Eye of Providence, Shield of the Phoenix, Stone of Binding, Draconic Scale, Kinetic
    Cuirass, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl, Avenging Blade,
    Magi''s Cloak, The World Stone, Helm of Darkness, Titan''s Bane, The Crusher,
    Ancient Signet, Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian
    Mail.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.41
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.42
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.38
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Eye of the Storm, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding, Hydra''s
    Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Leviathan''s Hide, Void
    Shield, Stampede, Ancile, Heartseeker, Oni Hunter''s Garb, Spear of Desolation,
    Prophetic Cloak, Daybreak Gavel, Rod of Asclepius, Void Stone, Xibalban Effigy,
    Spectral Armor, Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.56
      win: 0.47
      pick: 0.13
      fit: 0.67
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.57
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.57
      pick: 0.27
      fit: 0.57
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.15
      fit: 0.52
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Freya's Tears
  starter: *id001
---
