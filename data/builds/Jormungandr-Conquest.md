---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.38
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.5
    win_rate: 0.5
    alternates:
    - name: Eye of Erebus
      pick_rate: 0.09
      win_rate: 0.59
    - name: Avenging Blade
      pick_rate: 0.05
      win_rate: 0.41
  - name: Ethereal Staff
    pick_rate: 0.19
    win_rate: 0.55
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.16
      win_rate: 0.46
    - name: Shifter's Shield
      pick_rate: 0.15
      win_rate: 0.45
  - name: Gladiator's Shield
    pick_rate: 0.12
    win_rate: 0.42
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.17
      win_rate: 0.49
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.48
  - name: Soul Reaver
    pick_rate: 0.17
    win_rate: 0.45
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.46
    alternates:
    - name: Soul Reaver
      pick_rate: 0.11
      win_rate: 0.43
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.48
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.45
    - name: Draconic Scale
      pick_rate: 0.05
      win_rate: 0.6
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.51
    win_rate: 0.54
  - name: Bluestone Pendant
    pick_rate: 0.23
    win_rate: 0.42
  - name: Vampiric Shroud
    pick_rate: 0.08
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-09-08'
  god_win_rate: 0.47733333333333333
  god_matches_won: 179
  god_matches_played: 375
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-08'
  god_matches_analyzed: 17639
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - Draconic Scale
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Genji''s Guard, Shield Splitter, Breastplate of Valor, Golden
    Blade, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of
    Providence, Lernaean Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix,
    Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous Grimoire,
    Magi''s Cloak, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Bragi''s
    Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation, Hide of the Nemean Lion,
    Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede, Ancile,
    Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.31
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.5
      fit: 0.48
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.58
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.6
      pick: 0.15
      fit: 0.48
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Shifter's Shield
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Ethereal Staff
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Genji''s Guard, Golden
    Blade, Soul Gem, Runeforged Hammer, Breastplate of Valor, Shield Splitter, Eye
    of the Storm, Pharaoh''s Curse, The Reaper, Yogi''s Necklace, Lernaean Bow, Erosion,
    Shogun''s Ofuda, Hydra''s Lament, Gluttonous Grimoire, Eye of Providence, Phoenix
    Feather, Tyrfing, Chandra''s Grace, Riptalon, Nimble Ring, Lifebinder, Helm of
    Radiance, Stone of Binding, Glorious Pridwen, Daybreak Gavel, Midgardian Mail,
    Bragi''s Harp, Tekko-Kagi, Sphere of Negation, Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.32
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.5
      fit: 0.46
    Ethereal Staff:
      total: 0.52
      efficiency: 0.46
      win: 0.55
      pick: 0.26
      fit: 0.62
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.6
      pick: 0.15
      fit: 0.46
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Shifter's Shield
  - Ethereal Staff
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Shifter's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Stone of Binding
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Genji''s Guard, Screeching Gargoyle, Kinetic Cuirass, Gluttonous
    Grimoire, Void Shield, Breastplate of Valor, Spear of Desolation, Spear of the
    Magus, Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi, Obsidian
    Shard, Runeforged Hammer, Silverbranch Bow, Avenging Blade, Golden Blade, Toxic
    Blade, Titan''s Bane, The Crusher, Eye of the Storm, Hydra''s Lament, Lernaean
    Bow, Erosion, Nimble Ring, Pharaoh''s Curse, The Reaper, Helm of Radiance, Eye
    of Providence, Shield of the Phoenix, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.49
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.66
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.37
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.5
      fit: 0.37
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.47
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.15
      fit: 0.37
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Shifter's Shield
  - Nimble Ring
  - Draconic Scale
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
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Genji''s Guard, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire,
    Breastplate of Valor, Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm
    of Radiance, Eye of Providence, Stone of Binding, Eye of the Storm, Shield of
    the Phoenix, Hydra''s Lament, Toxic Blade, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s
    Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.47
      efficiency: 0.52
      win: 0.47
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.43
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.5
      fit: 0.37
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.3
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.15
      fit: 0.37
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Draconic Scale
  flex_slots:
  - Berserker's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Genji''s Guard, Berserker''s Shield, Breastplate of Valor, Amanita Charm, Eye
    of Erebus, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Hydra''s
    Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter, Nimble
    Ring, Runeforged Hammer, Helm of Radiance, Gluttonous Grimoire, Erosion, Pharaoh''s
    Curse, Golden Blade, Eye of Providence, Stone of Binding, Shogun''s Ofuda, Eye
    of the Storm, Arondight, Gem of Focus, Lernaean Bow, Spear of the Magus, Magi''s
    Cloak, Rod of Asclepius, Daybreak Gavel, Mantle Of Discord, Obsidian Shard, Midgardian
    Mail, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.12
      fit: 0.41
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.46
      pick: 0.15
      fit: 0.55
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.15
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Genji''s Guard, Shield Splitter, Runeforged
    Hammer, Breastplate of Valor, Eye of the Storm, Gluttonous Grimoire, Golden Blade,
    Hydra''s Lament, Heartseeker, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi,
    Eye of Providence, Spear of the Magus, Shield of the Phoenix, Stone of Binding,
    Helm of Radiance, Tyrfing, Titan''s Bane, Soul Gem, The Crusher, Obsidian Shard,
    Pharaoh''s Curse, Magi''s Cloak, The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching
    Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Silverbranch Bow,
    Avenging Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.45
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.5
      fit: 0.42
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.52
    Draconic Scale:
      total: 0.52
      efficiency: 0.5
      win: 0.6
      pick: 0.15
      fit: 0.42
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Shifter's Shield
  - Jotunn's Revenge
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Genji''s Guard, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Shield Splitter, Spear of the Magus, Spear of
    Desolation, Nimble Ring, Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian
    Shard, Golden Blade, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Rod of Asclepius,
    Bragi''s Harp, Heartseeker, Erosion, Pharaoh''s Curse, Tekko-Kagi, Stone of Binding,
    Eye of Providence, Tyrfing, Shield of the Phoenix, Shogun''s Ofuda, Jade Scepter,
    Doom Orb, Silverbranch Bow, Wish-Granting Pearl, Death Metal, Chronos'' Pendant,
    Magi''s Cloak, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.48
      pick: 0.12
      fit: 0.2
    Berserker's Shield:
      total: 0.5
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.36
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.5
      fit: 0.36
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.35
    Draconic Scale:
      total: 0.51
      efficiency: 0.5
      win: 0.6
      pick: 0.15
      fit: 0.36
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Shifter's Shield
  - Draconic Scale
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
    Revenge, Kinetic Cuirass, Shield Splitter, Genji''s Guard, Breastplate of Valor,
    Golden Blade, Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse,
    Eye of Providence, Lernaean Bow, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous
    Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation,
    Hide of the Nemean Lion, Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void
    Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.47
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.47
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.47
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.48
      efficiency: 0.55
      win: 0.47
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.46
      pick: 0.15
      fit: 0.43
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
  starter: *id001
---
