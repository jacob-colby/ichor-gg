---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.58
    win_rate: 0.57
    alternates:
    - name: Ring of Dispel
      pick_rate: 0.08
      win_rate: 0.0
    - name: Helm of Radiance
      pick_rate: 0.08
      win_rate: 0.0
  - name: Ethereal Staff
    pick_rate: 0.33
    win_rate: 0.75
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.25
      win_rate: 0.67
    - name: Shifter's Shield
      pick_rate: 0.17
      win_rate: 0.5
  - name: Soul Reaver
    pick_rate: 0.27
    win_rate: 0.67
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.27
      win_rate: 1.0
    - name: Gladiator's Shield
      pick_rate: 0.18
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.3
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.5
    - name: Ethereal Staff
      pick_rate: 0.2
      win_rate: 0.0
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.33
      win_rate: 0.67
    - name: Flaming Pearl
      pick_rate: 0.11
      win_rate: 0.0
  - name: Shield of the Phoenix
    pick_rate: 0.33
    win_rate: 0.0
    alternates:
    - name: Spirit Robe
      pick_rate: 0.33
      win_rate: 0.0
    - name: Hide of the Nemean Lion
      pick_rate: 0.33
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.42
    win_rate: 0.4
  - name: Bluestone Pendant
    pick_rate: 0.42
    win_rate: 0.8
  - name: Aegis of Acceleration
    pick_rate: 0.08
    win_rate: 1.0
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-09-10'
  god_win_rate: 0.5833333333333334
  god_matches_won: 7
  god_matches_played: 12
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Shield Splitter, Genji''s Guard, Golden Blade, Runeforged Hammer,
    Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean Bow,
    Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Stone of Binding, Tyrfing, Nimble
    Ring, Gluttonous Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of
    Desolation, Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede,
    Ancile, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.34
      fit: 0.26
    Prophetic Cloak:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.42
      fit: 0.43
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.43
    Hide of the Nemean Lion:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.31
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Prophetic Cloak
  - Ethereal Staff
  - Freya's Tears
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Ethereal Staff
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Kinetic Cuirass, Rod of Asclepius, Golden Blade, Soul Gem, Runeforged Hammer,
    Genji''s Guard, Shield Splitter, Eye of the Storm, Pharaoh''s Curse, The Reaper,
    Yogi''s Necklace, Lernaean Bow, Erosion, Shogun''s Ofuda, Hydra''s Lament, Gluttonous
    Grimoire, Eye of Providence, Phoenix Feather, Tyrfing, Chandra''s Grace, Riptalon,
    Draconic Scale, Nimble Ring, Avenging Blade, Lifebinder, Stone of Binding, Glorious
    Pridwen, Daybreak Gavel, Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Sphere of
    Negation, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.49
    Prophetic Cloak:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.42
      fit: 0.37
    Ethereal Staff:
      total: 0.61
      efficiency: 0.46
      win: 0.75
      pick: 0.45
      fit: 0.62
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.37
    Hide of the Nemean Lion:
      total: 0.73
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.32
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Prophetic Cloak
  - Ethereal Staff
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Avenging Blade, Screeching Gargoyle, Kinetic Cuirass, Gluttonous
    Grimoire, Genji''s Guard, Void Shield, Spear of Desolation, Spear of the Magus,
    Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi, Obsidian Shard,
    Runeforged Hammer, Silverbranch Bow, Golden Blade, Toxic Blade, Titan''s Bane,
    The Crusher, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Erosion, Nimble
    Ring, Pharaoh''s Curse, The Reaper, Eye of Providence, Draconic Scale, Doom Orb,
    Shogun''s Ofuda, Tyrfing, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.37
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.34
      fit: 0.2
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.47
    Prophetic Cloak:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.42
      fit: 0.33
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.24
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Prophetic Cloak
  - Nimble Ring
  - Freya's Tears
  - Hide of the Nemean Lion
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Genji''s Guard,
    Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse, Riptalon,
    Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Eye of Providence, Stone
    of Binding, Eye of the Storm, Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s
    Cloak, Screeching Gargoyle, Daybreak Gavel, The Reaper, Spear of Desolation, Spear
    of the Magus, Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod
    of Asclepius, Avenging Blade, Helm of Radiance.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.62
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.43
    Prophetic Cloak:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.42
      fit: 0.33
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.24
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Genji''s Guard, Amanita Charm, Kinetic Cuirass, Spear of
    Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant,
    Shield Splitter, Nimble Ring, Runeforged Hammer, Gluttonous Grimoire, Erosion,
    Pharaoh''s Curse, Golden Blade, Eye of Providence, Stone of Binding, Draconic
    Scale, Shogun''s Ofuda, Eye of the Storm, Arondight, Gem of Focus, Lernaean Bow,
    Spear of the Magus, Magi''s Cloak, Rod of Asclepius, Daybreak Gavel, Mantle Of
    Discord, Obsidian Shard, Midgardian Mail, Eye of Erebus, Tyrfing, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.34
      fit: 0.41
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.39
    Prophetic Cloak:
      total: 0.71
      efficiency: 0.44
      win: 1.0
      pick: 0.42
      fit: 0.55
    Freya's Tears:
      total: 0.76
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.55
    Hide of the Nemean Lion:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.25
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Berserker's Shield
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
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Genji''s
    Guard, Eye of the Storm, Gluttonous Grimoire, Golden Blade, Hydra''s Lament, Heartseeker,
    Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence, Spear
    of the Magus, Avenging Blade, Stone of Binding, Draconic Scale, Tyrfing, Titan''s
    Bane, Soul Gem, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak,
    The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord,
    Midgardian Mail, Daybreak Gavel, Silverbranch Bow, Helm of Radiance.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.34
      fit: 0.23
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.45
    Prophetic Cloak:
      total: 0.68
      efficiency: 0.44
      win: 1.0
      pick: 0.42
      fit: 0.38
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.38
    Hide of the Nemean Lion:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.27
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Prophetic Cloak
  - Ethereal Staff
  - Freya's Tears
  - Hide of the Nemean Lion
  flex_slots:
  - Breastplate of Valor
  - Ethereal Staff
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Genji''s
    Guard, Shield Splitter, Spear of the Magus, Spear of Desolation, Nimble Ring,
    Runeforged Hammer, Soul Gem, Obsidian Shard, Golden Blade, Eye of the Storm, Hydra''s
    Lament, Lernaean Bow, Rod of Asclepius, Bragi''s Harp, Heartseeker, Erosion, Pharaoh''s
    Curse, Tekko-Kagi, Stone of Binding, Eye of Providence, Tyrfing, Draconic Scale,
    Shogun''s Ofuda, Jade Scepter, Doom Orb, Silverbranch Bow, Wish-Granting Pearl,
    Avenging Blade, Death Metal, Chronos'' Pendant, Magi''s Cloak, Helm of Radiance.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.34
      fit: 0.2
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.35
    Prophetic Cloak:
      total: 0.67
      efficiency: 0.44
      win: 1.0
      pick: 0.42
      fit: 0.33
    Ethereal Staff:
      total: 0.58
      efficiency: 0.46
      win: 0.75
      pick: 0.45
      fit: 0.36
    Freya's Tears:
      total: 0.73
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.33
    Hide of the Nemean Lion:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 1.0
      fit: 0.23
  community_ordered:
  - Breastplate of Valor
  - Prophetic Cloak
  - Ethereal Staff
  - Freya's Tears
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Genji''s Guard, Golden Blade, Runeforged
    Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean
    Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Stone of Binding, Tyrfing,
    Nimble Ring, Helm of Radiance, Gluttonous Grimoire, Magi''s Cloak, Avenging Blade,
    Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Bragi''s Harp, Tekko-Kagi,
    Daybreak Gavel, Spear of Desolation, Heartseeker, Rod of Asclepius, Leviathan''s
    Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.62
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.62
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.55
      efficiency: 0.55
      win: 0.62
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.74
      efficiency: 0.61
      win: 1.0
      pick: 0.24
      fit: 0.43
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
  starter: *id001
---
