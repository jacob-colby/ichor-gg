---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.6
    win_rate: 0.67
    alternates:
    - name: The World Stone
      pick_rate: 0.2
      win_rate: 0.0
    - name: Chronos' Pendant
      pick_rate: 0.2
      win_rate: 1.0
  - name: Genji's Guard
    pick_rate: 0.4
    win_rate: 0.0
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.4
      win_rate: 1.0
    - name: Soul Reaver
      pick_rate: 0.2
      win_rate: 1.0
  - name: Sphere of Negation
    pick_rate: 0.2
    win_rate: 0.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.6
      win_rate: 1.0
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.0
  - name: Spectral Armor
    pick_rate: 0.4
    win_rate: 0.5
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.2
      win_rate: 1.0
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.0
  - name: Gem of Focus
    pick_rate: 0.25
    win_rate: 1.0
    alternates:
    - name: Spectral Armor
      pick_rate: 0.25
      win_rate: 1.0
    - name: Sphere of Negation
      pick_rate: 0.25
      win_rate: 0.0
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.0
    alternates:
    - name: Gem of Focus
      pick_rate: 0.33
      win_rate: 1.0
    - name: Gem
      pick_rate: 0.33
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.8
    win_rate: 0.75
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-11-04'
  god_win_rate: 0.6
  god_matches_won: 3
  god_matches_played: 5
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-04'
  god_matches_analyzed: 149
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  flex_slots:
  - Soul Reaver
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield
    Splitter, Berserker''s Shield, Kinetic Cuirass, Obsidian Shard, Runeforged Hammer,
    Helm of Radiance, The Reaper, Titan''s Bane, Helm of Darkness, Hydra''s Lament,
    Spear of the Magus, Oni Hunter''s Garb, Erosion, Blood-Bound Book, Eye of Providence,
    Draconic Scale, Stone of Binding, Death Metal, Shield of the Phoenix, Ancient
    Signet, Midgardian Mail, The Crusher, Magi''s Cloak, Jade Scepter, Screeching
    Gargoyle, Avenging Blade, Doom Orb, Mantle Of Discord, Leviathan''s Hide, Heartseeker,
    Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.63
      win: 1.0
      pick: 0.55
      fit: 0.23
    Chronos' Pendant:
      total: 0.68
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.22
    Spear of Desolation:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.6
      fit: 0.36
    Ethereal Staff:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.33
      fit: 0.36
    Soul Reaver:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.27
      fit: 0.34
    Gem of Focus:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.54
      fit: 0.22
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Transcendence
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  flex_slots:
  - Soul Reaver
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Gluttonous Grimoire, Soul Gem, Amanita Charm, Shield Splitter, Berserker''s
    Shield, Kinetic Cuirass, Obsidian Shard, Hydra''s Lament, Helm of Radiance, Runeforged
    Hammer, The Reaper, Ancient Signet, Titan''s Bane, Helm of Darkness, Spear of
    the Magus, Oni Hunter''s Garb, Blood-Bound Book, Death Metal, Doom Orb, Heartseeker,
    Jade Scepter, The Crusher, Erosion, Avenging Blade, Eye of Providence, Shield
    of the Phoenix, Stone of Binding, Arondight, Screeching Gargoyle, Midgardian Mail,
    Draconic Scale, Magi''s Cloak, Polynomicon.'
  slot_scores:
    Breastplate of Valor:
      total: 0.74
      efficiency: 0.63
      win: 1.0
      pick: 0.55
      fit: 0.27
    Chronos' Pendant:
      total: 0.69
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.26
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.23
    Ethereal Staff:
      total: 0.69
      efficiency: 0.47
      win: 1.0
      pick: 0.33
      fit: 0.37
    Soul Reaver:
      total: 0.67
      efficiency: 0.42
      win: 1.0
      pick: 0.27
      fit: 0.43
    Gem of Focus:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.54
      fit: 0.26
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  flex_slots:
  - Soul Reaver
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem, Amanita Charm, Berserker''s
    Shield, Obsidian Shard, Kinetic Cuirass, Shield Splitter, The Reaper, Titan''s
    Bane, Spear of the Magus, Hydra''s Lament, Helm of Radiance, Runeforged Hammer,
    Helm of Darkness, Blood-Bound Book, The Crusher, Shield of the Phoenix, Oni Hunter''s
    Garb, Doom Orb, Screeching Gargoyle, Erosion, Ancient Signet, Eye of Providence,
    Heartseeker, Stone of Binding, Death Metal, Midgardian Mail, Draconic Scale, Arondight,
    Magi''s Cloak, Jade Scepter, Dreamer''s Idol, Leviathan''s Hide.'
  slot_scores:
    Breastplate of Valor:
      total: 0.74
      efficiency: 0.63
      win: 1.0
      pick: 0.55
      fit: 0.26
    Chronos' Pendant:
      total: 0.69
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.26
    Spear of Desolation:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.6
      fit: 0.45
    Ethereal Staff:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.33
      fit: 0.33
    Soul Reaver:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.27
      fit: 0.33
    Gem of Focus:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.54
      fit: 0.26
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  - Amanita Charm
  flex_slots:
  - Soul Reaver
  - Amanita Charm
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, The Reaper, Gluttonous Grimoire, Jotunn''s
    Revenge, Blood-Bound Book, Shield of the Phoenix, Berserker''s Shield, Kinetic
    Cuirass, Shield Splitter, Obsidian Shard, Runeforged Hammer, Yogi''s Necklace,
    Bancroft''s Talon, Phoenix Feather, Bloodforge, Titan''s Bane, Helm of Radiance,
    Hydra''s Lament, Spear of the Magus, Chandra''s Grace, Oni Hunter''s Garb, Helm
    of Darkness, Erosion, Death Metal, Eye of Providence, Jade Scepter, Avenging Blade,
    Midgardian Mail, Regrowth Striders, Ancient Signet, The Crusher, Draconic Scale,
    Doom Orb.'
  slot_scores:
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.63
      win: 1.0
      pick: 0.55
      fit: 0.2
    Chronos' Pendant:
      total: 0.69
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.22
    Ethereal Staff:
      total: 0.73
      efficiency: 0.47
      win: 1.0
      pick: 0.33
      fit: 0.7
    Soul Reaver:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.27
      fit: 0.34
    Gem of Focus:
      total: 0.69
      efficiency: 0.5
      win: 1.0
      pick: 0.54
      fit: 0.22
    Amanita Charm:
      total: 0.63
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.69
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  flex_slots:
  - Soul Reaver
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Gluttonous Grimoire, Soul Gem, Amanita Charm,
    Obsidian Shard, Stone of Binding, Screeching Gargoyle, Avenging Blade, Berserker''s
    Shield, Shield Splitter, The Reaper, Kinetic Cuirass, Titan''s Bane, Spear of
    the Magus, Void Stone, Void Shield, Runeforged Hammer, The Crusher, Helm of Radiance,
    Doom Orb, Heartseeker, Hydra''s Lament, Helm of Darkness, Oni Hunter''s Garb,
    Blood-Bound Book, Dreamer''s Idol, Erosion, Ancient Signet, Eye of Providence,
    Death Metal, Midgardian Mail, Draconic Scale, Shield of the Phoenix, Tekko-Kagi,
    Magi''s Cloak.'
  slot_scores:
    Breastplate of Valor:
      total: 0.73
      efficiency: 0.63
      win: 1.0
      pick: 0.55
      fit: 0.19
    Chronos' Pendant:
      total: 0.68
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.19
    Spear of Desolation:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.6
      fit: 0.44
    Ethereal Staff:
      total: 0.68
      efficiency: 0.47
      win: 1.0
      pick: 0.33
      fit: 0.32
    Soul Reaver:
      total: 0.66
      efficiency: 0.42
      win: 1.0
      pick: 0.27
      fit: 0.32
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.54
      fit: 0.19
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Chronos' Pendant
  - Nimble Ring
  - Gem of Focus
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
    this god: Berserker''s Shield, Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge,
    Nimble Ring, Soul Gem, Kinetic Cuirass, Shield Splitter, Golden Blade, Obsidian
    Shard, Tekko-Kagi, Tyrfing, Helm of Radiance, Runeforged Hammer, Silverbranch
    Bow, Toxic Blade, The Reaper, Spear of the Magus, Titan''s Bane, Pharaoh''s Curse,
    Hydra''s Lament, Lernaean Bow, Helm of Darkness, Oni Hunter''s Garb, Blood-Bound
    Book, Ancient Signet, Riptalon, Shogun''s Ofuda, Bragi''s Harp, Erosion, Stone
    of Binding, Eye of Providence, Midgardian Mail, Bracer of The Abyss, Shield of
    the Phoenix, Screeching Gargoyle.'
  slot_scores:
    Golden Blade:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.67
      pick: 0.0
      fit: 0.37
    Breastplate of Valor:
      total: 0.72
      efficiency: 0.63
      win: 1.0
      pick: 0.55
      fit: 0.17
    Chronos' Pendant:
      total: 0.68
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.16
    Nimble Ring:
      total: 0.57
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.33
    Gem of Focus:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.54
      fit: 0.16
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  flex_slots:
  - Soul Reaver
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Amanita
    Charm, Gluttonous Grimoire, Berserker''s Shield, Kinetic Cuirass, Hydra''s Lament,
    Shield Splitter, Shield of the Phoenix, Screeching Gargoyle, Obsidian Shard, Helm
    of Radiance, Arondight, Runeforged Hammer, The Reaper, Oni Hunter''s Garb, Titan''s
    Bane, Prophetic Cloak, Helm of Darkness, Erosion, Eye of Providence, Spear of
    the Magus, Stone of Binding, Draconic Scale, Blood-Bound Book, Midgardian Mail,
    Magi''s Cloak, Gladiator''s Shield, Heartwood Charm, Leviathan''s Hide, Ancient
    Signet, Mantle Of Discord, Shifter''s Shield, Chandra''s Grace.'
  slot_scores:
    Breastplate of Valor:
      total: 0.76
      efficiency: 0.63
      win: 1.0
      pick: 0.55
      fit: 0.4
    Chronos' Pendant:
      total: 0.7
      efficiency: 0.55
      win: 1.0
      pick: 0.2
      fit: 0.35
    Spear of Desolation:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.6
      fit: 0.47
    Ethereal Staff:
      total: 0.67
      efficiency: 0.47
      win: 1.0
      pick: 0.33
      fit: 0.29
    Soul Reaver:
      total: 0.65
      efficiency: 0.42
      win: 1.0
      pick: 0.27
      fit: 0.28
    Gem of Focus:
      total: 0.71
      efficiency: 0.5
      win: 1.0
      pick: 0.54
      fit: 0.35
  community_ordered:
  - Breastplate of Valor
  - Chronos' Pendant
  - Spear of Desolation
  - Ethereal Staff
  - Soul Reaver
  - Gem of Focus
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - Rod of Tahuti
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge, Amanita Charm,
    Soul Gem, Shield Splitter, Berserker''s Shield, Kinetic Cuirass, Obsidian Shard,
    Runeforged Hammer, Helm of Radiance, The Reaper, Titan''s Bane, Helm of Darkness,
    Hydra''s Lament, Spear of the Magus, Oni Hunter''s Garb, Erosion, Blood-Bound
    Book, Eye of Providence, Draconic Scale, Stone of Binding, Death Metal, Shield
    of the Phoenix, Ancient Signet, Midgardian Mail, The Crusher, Magi''s Cloak, Jade
    Scepter, Screeching Gargoyle, Avenging Blade, Doom Orb, Mantle Of Discord, Leviathan''s
    Hide, Heartseeker, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.49
      win: 0.67
      pick: 0.0
      fit: 0.14
    Genji's Guard:
      total: 0.3
      efficiency: 0.69
      win: 0.0
      pick: 0.55
      fit: 0.23
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.67
      win: 0.67
      pick: 0.0
      fit: 0.37
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.16
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.59
      win: 0.67
      pick: 0.0
      fit: 0.57
    Rod of Tahuti:
      total: 0.39
      efficiency: 0.86
      win: 0.0
      pick: 1.0
      fit: 0.28
  community_ordered:
  - Genji's Guard
  - Rod of Tahuti
  starter: *id001
---
