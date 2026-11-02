---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.43
  slot_order:
  - name: Eye of Erebus
    pick_rate: 0.47
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.41
  - name: Shifter's Shield
    pick_rate: 0.28
    win_rate: 0.6
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.58
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.61
  - name: Ethereal Staff
    pick_rate: 0.21
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.52
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.57
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Soul Reaver
      pick_rate: 0.09
      win_rate: 0.6
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.52
  - name: Soul Reaver
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.68
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.71
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.58
    - name: Soul Reaver
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.48
    win_rate: 0.61
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.54
  - name: Sundering Axe
    pick_rate: 0.06
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-11-02'
  god_win_rate: 0.5724137931034483
  god_matches_won: 166
  god_matches_played: 290
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Hide of the Nemean Lion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Shield Splitter, Kinetic Cuirass, Genji''s Guard, Breastplate of Valor, Golden
    Blade, Runeforged Hammer, Tekko-Kagi, Hydra''s Lament, Erosion, Pharaoh''s Curse,
    Eye of Providence, Tyrfing, Lernaean Bow, Draconic Scale, Stone of Binding, Shogun''s
    Ofuda, Oni Hunter''s Garb, Shield of the Phoenix, Helm of Radiance, Helm of Darkness,
    Magi''s Cloak, Midgardian Mail, Nimble Ring, Titan''s Bane, Gluttonous Grimoire,
    Mantle Of Discord, Screeching Gargoyle, Avenging Blade, Eros'' Bow, Leviathan''s
    Hide, Spear of Desolation, Obsidian Shard, Bragi''s Harp, Arondight, Dominance,
    Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.31
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Ethereal Staff
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Jotunn''s Revenge,
    Shield of the Phoenix, Kinetic Cuirass, Shield Splitter, Genji''s Guard, Soul
    Gem, Golden Blade, Runeforged Hammer, Phoenix Feather, Yogi''s Necklace, Breastplate
    of Valor, The Reaper, Tekko-Kagi, Hydra''s Lament, Pharaoh''s Curse, Chandra''s
    Grace, Tyrfing, Lernaean Bow, Erosion, Eye of Providence, Shogun''s Ofuda, Oni
    Hunter''s Garb, Gluttonous Grimoire, Avenging Blade, Draconic Scale, Blood-Bound
    Book, Eros'' Bow, Midgardian Mail, Nimble Ring, Titan''s Bane, Helm of Radiance,
    Sphere of Negation, Rod of Asclepius, Regrowth Striders, Leviathan''s Hide, Glorious
    Pridwen, Spear of Desolation.'
  slot_scores:
    Berserker's Shield:
      total: 0.61
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.56
    Ethereal Staff:
      total: 0.57
      efficiency: 0.47
      win: 0.65
      pick: 0.33
      fit: 0.62
    Hide of the Nemean Lion:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.32
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Ethereal Staff
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Tekko-Kagi
  - Amanita Charm
  flex_slots:
  - Tekko-Kagi
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Stone of Binding, Tekko-Kagi, Screeching Gargoyle, Genji''s Guard, Avenging Blade,
    Shield Splitter, Kinetic Cuirass, Titan''s Bane, Gluttonous Grimoire, Obsidian
    Shard, Spear of Desolation, Void Stone, Void Shield, Soul Gem, Breastplate of
    Valor, Runeforged Hammer, The Crusher, Toxic Blade, Spear of the Magus, Heartseeker,
    Silverbranch Bow, Golden Blade, Hydra''s Lament, The Reaper, Lernaean Bow, Helm
    of Radiance, Tyrfing, Erosion, Doom Orb, Pharaoh''s Curse, Oni Hunter''s Garb,
    Eye of Providence, Nimble Ring, The World Stone, Draconic Scale, Midgardian Mail,
    Shield of the Phoenix.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.6
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.59
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.47
    Tekko-Kagi:
      total: 0.55
      efficiency: 0.55
      win: 0.61
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Genji''s Guard, Nimble Ring, Kinetic Cuirass, Golden Blade, Shield Splitter, Gluttonous
    Grimoire, Tyrfing, Breastplate of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Hydra''s Lament, Shogun''s Ofuda,
    Silverbranch Bow, Helm of Radiance, Erosion, Eros'' Bow, Oni Hunter''s Garb, Eye
    of Providence, Stone of Binding, Draconic Scale, Obsidian Shard, Midgardian Mail,
    Shield of the Phoenix, Helm of Darkness, Spear of Desolation, Magi''s Cloak, Screeching
    Gargoyle, The Reaper, Riptalon, Titan''s Bane, Mantle Of Discord, Leviathan''s
    Hide, Blood-Bound Book.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.6
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.54
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.24
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Genji''s Guard, Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Kinetic
    Cuirass, Spear of Desolation, Hydra''s Lament, Shield Splitter, Shield of the
    Phoenix, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Arondight, Helm of
    Radiance, Runeforged Hammer, Nimble Ring, Golden Blade, Gluttonous Grimoire, Helm
    of Darkness, Erosion, Obsidian Shard, Pharaoh''s Curse, Eye of Providence, Oni
    Hunter''s Garb, Stone of Binding, Gladiator''s Shield, Eros'' Bow, Tekko-Kagi,
    Draconic Scale, Gem of Focus, Midgardian Mail, Shogun''s Ofuda, Magi''s Cloak,
    Heartwood Charm, Lernaean Bow, Tyrfing, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.59
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.61
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.27
      fit: 0.55
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Genji''s Guard, Kinetic Cuirass, Runeforged
    Hammer, Tekko-Kagi, Titan''s Bane, Breastplate of Valor, Hydra''s Lament, Golden
    Blade, Gluttonous Grimoire, Spear of Desolation, Obsidian Shard, The Crusher,
    Heartseeker, Lernaean Bow, Tyrfing, Erosion, Avenging Blade, Eye of Providence,
    Soul Gem, Helm of Radiance, Oni Hunter''s Garb, Stone of Binding, Draconic Scale,
    Arondight, The Reaper, Shield of the Phoenix, Helm of Darkness, Midgardian Mail,
    Magi''s Cloak, Screeching Gargoyle, Pharaoh''s Curse, Death Metal, Spear of the
    Magus, Wyrmskin Hide, Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.23
    Berserker's Shield:
      total: 0.59
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.27
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield Splitter
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Shield Splitter, Kinetic Cuirass,
    Gluttonous Grimoire, Obsidian Shard, Spear of Desolation, Tekko-Kagi, Breastplate
    of Valor, Soul Gem, Helm of Radiance, Runeforged Hammer, Nimble Ring, Titan''s
    Bane, Golden Blade, Helm of Darkness, Spear of the Magus, Hydra''s Lament, Eros''
    Bow, Bragi''s Harp, Death Metal, Lernaean Bow, Tyrfing, Erosion, Oni Hunter''s
    Garb, Pharaoh''s Curse, Eye of Providence, Stone of Binding, Doom Orb, The Crusher,
    Jade Scepter, Heartseeker, Draconic Scale, Midgardian Mail, The World Stone, Shield
    of the Phoenix, Avenging Blade, Chronos'' Pendant.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.59
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.35
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.41
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.23
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Shield Splitter, Kinetic Cuirass, Genji''s Guard, Breastplate of Valor,
    Golden Blade, Runeforged Hammer, Tekko-Kagi, Hydra''s Lament, Erosion, Pharaoh''s
    Curse, Eye of Providence, Tyrfing, Lernaean Bow, Draconic Scale, Stone of Binding,
    Shogun''s Ofuda, Oni Hunter''s Garb, Shield of the Phoenix, Helm of Radiance,
    Helm of Darkness, Magi''s Cloak, Midgardian Mail, Nimble Ring, Titan''s Bane,
    Gluttonous Grimoire, Mantle Of Discord, Screeching Gargoyle, Avenging Blade, Eros''
    Bow, Leviathan''s Hide, Spear of Desolation, Obsidian Shard, Bragi''s Harp, Arondight,
    Dominance, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.26
    Berserker's Shield:
      total: 0.61
      efficiency: 0.75
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
  starter: *id001
---
