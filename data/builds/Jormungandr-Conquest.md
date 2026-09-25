---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.56
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.44
    win_rate: 0.58
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.16
      win_rate: 0.56
    - name: Golden Blade
      pick_rate: 0.07
      win_rate: 1.0
  - name: Ethereal Staff
    pick_rate: 0.15
    win_rate: 0.75
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.57
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.71
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.11
      win_rate: 0.83
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.75
    - name: Soul Reaver
      pick_rate: 0.08
      win_rate: 0.75
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Soul Reaver
      pick_rate: 0.07
      win_rate: 0.33
    - name: Gladiator's Shield
      pick_rate: 0.07
      win_rate: 0.67
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 1.0
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
    - name: Mantle Of Discord
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.38
    win_rate: 0.76
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.64
  - name: Death's Toll
    pick_rate: 0.11
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-09-25'
  god_win_rate: 0.6363636363636364
  god_matches_won: 35
  god_matches_played: 55
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
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
    this god: Golden Blade, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Freya''s Tears, Shield Splitter, Runeforged Hammer,
    Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean Bow,
    Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix, Stone
    of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous Grimoire, Magi''s
    Cloak, Avenging Blade, Screeching Gargoyle, Midgardian Mail, Bragi''s Harp, Tekko-Kagi,
    Daybreak Gavel, Spear of Desolation, Hide of the Nemean Lion, Heartseeker, Rod
    of Asclepius, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Golden Blade:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.52
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.27
      fit: 0.26
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.71
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Golden Blade
  - Genji's Guard
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Freya''s Tears,
    Soul Gem, Runeforged Hammer, Shield Splitter, Eye of the Storm, Pharaoh''s Curse,
    The Reaper, Yogi''s Necklace, Lernaean Bow, Erosion, Shogun''s Ofuda, Hydra''s
    Lament, Gluttonous Grimoire, Eye of Providence, Phoenix Feather, Tyrfing, Chandra''s
    Grace, Riptalon, Draconic Scale, Nimble Ring, Avenging Blade, Lifebinder, Helm
    of Radiance, Stone of Binding, Glorious Pridwen, Daybreak Gavel, Midgardian Mail,
    Bragi''s Harp, Tekko-Kagi, Sphere of Negation.'
  slot_scores:
    Golden Blade:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.58
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.75
      pick: 0.27
      fit: 0.23
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.32
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.53
      win: 0.71
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.66
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Golden Blade
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Golden Blade
  - Stone of Binding
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Golden Blade, Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Stone of Binding, Avenging Blade, Screeching Gargoyle, Kinetic
    Cuirass, Gluttonous Grimoire, Freya''s Tears, Void Shield, Spear of Desolation,
    Spear of the Magus, Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi,
    Obsidian Shard, Runeforged Hammer, Silverbranch Bow, Toxic Blade, Titan''s Bane,
    The Crusher, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Erosion, Nimble
    Ring, Pharaoh''s Curse, The Reaper, Helm of Radiance, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.4
    Stone of Binding:
      total: 0.6
      efficiency: 0.51
      win: 0.71
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.27
      fit: 0.2
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.37
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Golden Blade
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
  - Jotunn's Revenge
  - Nimble Ring
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Golden Blade, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Nimble Ring, Kinetic Cuirass, Freya''s Tears, Gluttonous Grimoire, Tyrfing,
    Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse, Riptalon, Lernaean
    Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence,
    Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The
    Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian Mail,
    Tekko-Kagi, Rod of Asclepius, Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.72
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.54
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.27
      fit: 0.2
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.59
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Golden Blade
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Golden Blade, Rod of Tahuti, Jotunn''s
    Revenge, Freya''s Tears, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Shield of the Phoenix, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle,
    Soul Gem, Chronos'' Pendant, Shield Splitter, Nimble Ring, Runeforged Hammer,
    Helm of Radiance, Gluttonous Grimoire, Erosion, Prophetic Cloak, Pharaoh''s Curse,
    Eye of Providence, Stone of Binding, Draconic Scale, Shogun''s Ofuda, Eye of the
    Storm, Arondight, Gem of Focus, Lernaean Bow, Spear of the Magus, Magi''s Cloak,
    Rod of Asclepius, Daybreak Gavel, Obsidian Shard, Midgardian Mail, Eye of Erebus,
    Tyrfing.'
  slot_scores:
    Golden Blade:
      total: 0.69
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.36
    Genji's Guard:
      total: 0.64
      efficiency: 0.66
      win: 0.75
      pick: 0.27
      fit: 0.41
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.71
      pick: 0.2
      fit: 0.41
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.71
      pick: 0.0
      fit: 0.55
  community_ordered:
  - Golden Blade
  - Genji's Guard
  - Breastplate of Valor
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Golden Blade, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Freya''s Tears, Shield Splitter,
    Runeforged Hammer, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker,
    Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence, Spear
    of the Magus, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Helm of Radiance, Tyrfing, Titan''s Bane, Soul Gem, The Crusher, Obsidian
    Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Nimble Ring, Shogun''s Ofuda,
    Screeching Gargoyle, Midgardian Mail, Daybreak Gavel, Silverbranch Bow.'
  slot_scores:
    Golden Blade:
      total: 0.71
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.47
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.27
      fit: 0.23
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.64
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.71
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Golden Blade
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Golden Blade
  - Book of Thoth
  - Genji's Guard
  - Berserker's Shield
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Golden Blade, Rod of Tahuti, Jotunn''s
    Revenge, Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire,
    Freya''s Tears, Shield Splitter, Spear of the Magus, Spear of Desolation, Nimble
    Ring, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Eye of the
    Storm, Hydra''s Lament, Lernaean Bow, Rod of Asclepius, Bragi''s Harp, Heartseeker,
    Erosion, Pharaoh''s Curse, Tekko-Kagi, Stone of Binding, Eye of Providence, Tyrfing,
    Shield of the Phoenix, Draconic Scale, Shogun''s Ofuda, Jade Scepter, Doom Orb,
    Silverbranch Bow, Wish-Granting Pearl, Avenging Blade, Death Metal, Chronos''
    Pendant, Magi''s Cloak.'
  slot_scores:
    Golden Blade:
      total: 0.7
      efficiency: 0.52
      win: 1.0
      pick: 0.07
      fit: 0.42
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.71
      pick: 0.0
      fit: 0.16
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.75
      pick: 0.27
      fit: 0.2
    Berserker's Shield:
      total: 0.61
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.35
    Transcendence:
      total: 0.53
      efficiency: 0.53
      win: 0.71
      pick: 0.0
      fit: 0.16
  community_ordered:
  - Golden Blade
  - Genji's Guard
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
    Revenge, Kinetic Cuirass, Freya''s Tears, Shield Splitter, Golden Blade, Runeforged
    Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean
    Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix,
    Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous Grimoire,
    Magi''s Cloak, Avenging Blade, Screeching Gargoyle, Midgardian Mail, Bragi''s
    Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation, Hide of the Nemean Lion,
    Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.63
      efficiency: 0.68
      win: 0.71
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.71
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.71
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.59
      efficiency: 0.55
      win: 0.71
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.71
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.71
      pick: 0.0
      fit: 0.48
  starter: *id001
---
