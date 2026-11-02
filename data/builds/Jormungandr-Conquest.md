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
    pick_rate: 0.46
    win_rate: 0.6
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.41
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.61
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.58
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.61
  - name: Ethereal Staff
    pick_rate: 0.21
    win_rate: 0.66
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
    win_rate: 0.63
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
  god_win_rate: 0.5743944636678201
  god_matches_won: 166
  god_matches_played: 289
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Genji''s Guard, Shield Splitter, Breastplate of Valor, Golden
    Blade, Runeforged Hammer, Pharaoh''s Curse, Erosion, Tekko-Kagi, Eye of Providence,
    Hydra''s Lament, Draconic Scale, Oni Hunter''s Garb, Shogun''s Ofuda, Tyrfing,
    Shield of the Phoenix, Lernaean Bow, Stone of Binding, Midgardian Mail, Gluttonous
    Grimoire, Nimble Ring, Helm of Darkness, Sundering Echo, Magi''s Cloak, Titan''s
    Bane, Helm of Radiance, Screeching Gargoyle, Eros'' Bow, Mantle Of Discord, Leviathan''s
    Hide, Obsidian Shard, Spear of Desolation, Toxic Blade, Avenging Blade, Wyrmskin
    Hide, Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.58
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.61
      pick: 0.27
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.48
      win: 0.71
      pick: 0.25
      fit: 0.31
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Shield of the Phoenix,
    Jotunn''s Revenge, Kinetic Cuirass, Genji''s Guard, Soul Gem, Shield Splitter,
    Golden Blade, Yogi''s Necklace, Phoenix Feather, Runeforged Hammer, Breastplate
    of Valor, The Reaper, Chandra''s Grace, Pharaoh''s Curse, Tekko-Kagi, Hydra''s
    Lament, Erosion, Shogun''s Ofuda, Oni Hunter''s Garb, Tyrfing, Gluttonous Grimoire,
    Lernaean Bow, Eye of Providence, Draconic Scale, Eros'' Bow, Midgardian Mail,
    Blood-Bound Book, Nimble Ring, Sundering Echo, Regrowth Striders, Glorious Pridwen,
    Titan''s Bane, Rod of Asclepius, Toxic Blade, Leviathan''s Hide, Avenging Blade,
    Sphere of Negation.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.32
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.56
    Ethereal Staff:
      total: 0.56
      efficiency: 0.44
      win: 0.66
      pick: 0.33
      fit: 0.62
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.48
      win: 0.71
      pick: 0.25
      fit: 0.32
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
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
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Screeching Gargoyle
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
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm,
    Stone of Binding, Screeching Gargoyle, Tekko-Kagi, Genji''s Guard, Kinetic Cuirass,
    Gluttonous Grimoire, Obsidian Shard, Titan''s Bane, Avenging Blade, Spear of Desolation,
    Shield Splitter, Void Stone, Void Shield, Soul Gem, Breastplate of Valor, Toxic
    Blade, Silverbranch Bow, Heartseeker, Spear of the Magus, Runeforged Hammer, The
    Crusher, Golden Blade, Hydra''s Lament, The Reaper, Oni Hunter''s Garb, Pharaoh''s
    Curse, Erosion, Doom Orb, Lernaean Bow, Nimble Ring, Eye of Providence, The World
    Stone, Sundering Echo, Tyrfing, Draconic Scale, Shield of the Phoenix, Helm of
    Radiance.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.6
    Stone of Binding:
      total: 0.54
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.58
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.47
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.48
      win: 0.71
      pick: 0.25
      fit: 0.24
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble
    Ring, Jotunn''s Revenge, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Shield
    Splitter, Breastplate of Valor, Tyrfing, Soul Gem, Pharaoh''s Curse, Tekko-Kagi,
    Toxic Blade, Runeforged Hammer, Silverbranch Bow, Shogun''s Ofuda, Lernaean Bow,
    Oni Hunter''s Garb, Erosion, Eros'' Bow, Hydra''s Lament, Riptalon, Eye of Providence,
    Stone of Binding, Draconic Scale, Obsidian Shard, Shield of the Phoenix, Helm
    of Radiance, Midgardian Mail, Screeching Gargoyle, Magi''s Cloak, Spear of Desolation,
    Sundering Echo, The Reaper, Helm of Darkness, Titan''s Bane, Leviathan''s Hide,
    Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.59
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.48
      win: 0.71
      pick: 0.25
      fit: 0.24
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
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
  - Breastplate of Valor
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Berserker''s Shield, Rod of Tahuti,
    Genji''s Guard, Jotunn''s Revenge, Breastplate of Valor, Amanita Charm, Kinetic
    Cuirass, Spear of Desolation, Shield of the Phoenix, Hydra''s Lament, Screeching
    Gargoyle, Soul Gem, Shield Splitter, Chronos'' Pendant, Gluttonous Grimoire, Nimble
    Ring, Helm of Radiance, Pharaoh''s Curse, Gladiator''s Shield, Erosion, Obsidian
    Shard, Arondight, Oni Hunter''s Garb, Runeforged Hammer, Golden Blade, Helm of
    Darkness, Eye of Providence, Eros'' Bow, Draconic Scale, Stone of Binding, Shogun''s
    Ofuda, Heartwood Charm, Midgardian Mail, Gem of Focus, Sundering Echo, Tekko-Kagi,
    Magi''s Cloak, Chandra''s Grace, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.41
    Berserker's Shield:
      total: 0.58
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.61
      pick: 0.27
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Genji''s Guard, Kinetic Cuirass, Tekko-Kagi,
    Titan''s Bane, Runeforged Hammer, Breastplate of Valor, Golden Blade, Hydra''s
    Lament, Gluttonous Grimoire, Obsidian Shard, Spear of Desolation, Sundering Echo,
    Erosion, Heartseeker, Soul Gem, Oni Hunter''s Garb, The Crusher, Eye of Providence,
    Lernaean Bow, Tyrfing, Draconic Scale, Stone of Binding, Shield of the Phoenix,
    Avenging Blade, Pharaoh''s Curse, Midgardian Mail, Helm of Radiance, The Reaper,
    Magi''s Cloak, Screeching Gargoyle, Helm of Darkness, Toxic Blade, Wyrmskin Hide,
    Mantle Of Discord, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.23
    Berserker's Shield:
      total: 0.58
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
    Shield Splitter:
      total: 0.54
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.48
      win: 0.71
      pick: 0.25
      fit: 0.27
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
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
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Obsidian Shard, Shield Splitter, Spear of Desolation, Tekko-Kagi, Breastplate
    of Valor, Soul Gem, Sundering Echo, Nimble Ring, Helm of Radiance, Titan''s Bane,
    Runeforged Hammer, Golden Blade, Helm of Darkness, Spear of the Magus, Eros''
    Bow, Hydra''s Lament, Oni Hunter''s Garb, Bragi''s Harp, Pharaoh''s Curse, Erosion,
    Lernaean Bow, Tyrfing, Death Metal, Doom Orb, Eye of Providence, Stone of Binding,
    Toxic Blade, Draconic Scale, Shield of the Phoenix, The World Stone, Heartseeker,
    Silverbranch Bow, Midgardian Mail, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.58
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.35
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.61
      pick: 0.27
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.48
      win: 0.71
      pick: 0.25
      fit: 0.23
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Freya's Tears
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Genji''s Guard, Shield Splitter, Breastplate of Valor,
    Golden Blade, Runeforged Hammer, Pharaoh''s Curse, Erosion, Tekko-Kagi, Eye of
    Providence, Hydra''s Lament, Draconic Scale, Oni Hunter''s Garb, Shogun''s Ofuda,
    Tyrfing, Shield of the Phoenix, Lernaean Bow, Stone of Binding, Midgardian Mail,
    Gluttonous Grimoire, Nimble Ring, Helm of Darkness, Sundering Echo, Magi''s Cloak,
    Titan''s Bane, Helm of Radiance, Screeching Gargoyle, Eros'' Bow, Mantle Of Discord,
    Leviathan''s Hide, Obsidian Shard, Spear of Desolation, Toxic Blade, Avenging
    Blade, Wyrmskin Hide, Dominance.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.61
      pick: 0.0
      fit: 0.26
    Berserker's Shield:
      total: 0.59
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.54
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.48
  starter: *id001
---
