---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.4
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.28
    win_rate: 0.5
    alternates:
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.55
    - name: Devourer's Gauntlet
      pick_rate: 0.13
      win_rate: 0.6
  - name: Stone of Binding
    pick_rate: 0.15
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.57
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.67
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.55
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.67
    - name: Brawler’s Beat Stick
      pick_rate: 0.08
      win_rate: 0.67
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.75
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.29
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.6
  - name: Sage's Ring
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.83
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 1.0
  - name: Spectral Armor
    pick_rate: 0.06
    win_rate: 0.5
    alternates:
    - name: Sage's Ring
      pick_rate: 0.08
      win_rate: 0.67
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bumba's Cudgel
    pick_rate: 0.37
    win_rate: 0.45
  - name: Bumba's Hammer
    pick_rate: 0.15
    win_rate: 0.67
  - name: Bluestone Brooch
    pick_rate: 0.1
    win_rate: 0.88
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-10-10'
  god_win_rate: 0.5512820512820513
  god_matches_won: 43
  god_matches_played: 78
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-10'
  god_matches_analyzed: 4063
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Transcendence
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Breastplate of Valor,
    Kinetic Cuirass, Shield Splitter, Shifter''s Shield, Eye of the Storm, Berserker''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s
    Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire, Avenging Blade,
    Mantle Of Discord, Stampede, Midgardian Mail, Screeching Gargoyle, Hide of the
    Nemean Lion, Leviathan''s Hide, Void Shield, Ancile, Heartseeker, Oni Hunter''s
    Garb, Spear of Desolation, Prophetic Cloak, Daybreak Gavel, Rod of Asclepius,
    Void Stone, Xibalban Effigy, Helm of Darkness, Soul Gem, Spear of the Magus.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.67
      pick: 0.19
      fit: 0.31
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.37
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.22
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.55
      pick: 0.23
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
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
  - Breastplate of Valor
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Shield of the Phoenix,
    Breastplate of Valor, Kinetic Cuirass, Rod of Asclepius, Shield Splitter, Shifter''s
    Shield, Soul Gem, Eye of the Storm, Berserker''s Shield, Erosion, Ethereal Staff,
    Eye of Providence, The Reaper, Draconic Scale, Yogi''s Necklace, Hydra''s Lament,
    Phoenix Feather, Gluttonous Grimoire, Avenging Blade, Chandra''s Grace, Glorious
    Pridwen, Lifebinder, Stampede, Midgardian Mail, Helm of Radiance, Daybreak Gavel,
    Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s Hide, Void Shield, Sphere
    of Negation, Ancile, Screeching Gargoyle, Heartseeker, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.19
      fit: 0.28
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.8
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Breastplate of
    Valor, Kinetic Cuirass, Gluttonous Grimoire, Avenging Blade, Screeching Gargoyle,
    Void Shield, Spear of Desolation, Heartseeker, Spear of the Magus, Shield Splitter,
    Void Stone, Soul Gem, Obsidian Shard, Shifter''s Shield, Berserker''s Shield,
    Titan''s Bane, The Crusher, Eye of the Storm, Erosion, The Reaper, Hydra''s Lament,
    Eye of Providence, Shield of the Phoenix, Draconic Scale, Helm of Radiance, Doom
    Orb, The World Stone, Magi''s Cloak, Pendulum Blade, Dreamer''s Idol, Avatar''s
    Parashu, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Rod of Asclepius.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.04
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.19
      fit: 0.23
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.54
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.16
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Breastplate of Valor, Amanita Charm,
    Jotunn''s Revenge, Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire,
    Tyrfing, Shifter''s Shield, Shield Splitter, Pharaoh''s Curse, Soul Gem, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye
    of Providence, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The
    Reaper, Midgardian Mail, Mantle Of Discord, Spear of Desolation, Bragi''s Harp,
    Spear of the Magus, Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.19
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.2
    Nimble Ring:
      total: 0.52
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.37
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
  - Amanita Charm
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Rod of Tahuti,
    Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear
    of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Shifter''s Shield,
    Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion,
    Helm of Radiance, Gluttonous Grimoire, Eye of Providence, Gladiator''s Shield,
    Draconic Scale, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod
    of Asclepius, Eye of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Hide of the
    Nemean Lion, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.19
      fit: 0.48
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.55
      pick: 0.23
      fit: 0.64
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Shield Splitter,
    Shifter''s Shield, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s
    Lament, Heartseeker, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye
    of Providence, Tyrfing, Avenging Blade, Spear of the Magus, Shield of the Phoenix,
    Draconic Scale, Helm of Radiance, Titan''s Bane, Soul Gem, The Crusher, Obsidian
    Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Silverbranch Bow, Nimble Ring,
    Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak
    Gavel.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.19
      fit: 0.23
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.55
      pick: 0.23
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Gluttonous Grimoire, Shield
    Splitter, Spear of Desolation, Spear of the Magus, Helm of Radiance, Soul Gem,
    Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the
    Phoenix, Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting Pearl,
    Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm of Darkness,
    Titan''s Bane, The Crusher, Ancient Signet, Screeching Gargoyle, Mantle Of Discord,
    Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.45
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.19
      fit: 0.23
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.18
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Shifter''s Shield, Breastplate of Valor, Eye of the
    Storm, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Hydra''s Lament, Magi''s Cloak, Helm of Radiance, Gluttonous Grimoire,
    Avenging Blade, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Hide
    of the Nemean Lion, Leviathan''s Hide, Void Shield, Stampede, Ancile, Heartseeker,
    Oni Hunter''s Garb, Spear of Desolation, Prophetic Cloak, Daybreak Gavel, Rod
    of Asclepius, Void Stone, Xibalban Effigy, Helm of Darkness, Soul Gem, Spear of
    the Magus.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.67
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.55
      pick: 0.23
      fit: 0.52
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Freya's Tears
  starter: *id001
---
