---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.46
  slot_order:
  - name: Eye of Erebus
    pick_rate: 0.47
    win_rate: 0.61
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.12
      win_rate: 0.61
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.41
  - name: Shifter's Shield
    pick_rate: 0.27
    win_rate: 0.6
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.13
      win_rate: 0.59
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
    - name: Ethereal Staff
      pick_rate: 0.09
      win_rate: 0.54
    - name: Soul Reaver
      pick_rate: 0.09
      win_rate: 0.6
  - name: Soul Reaver
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.69
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
    pick_rate: 0.23
    win_rate: 0.55
  - name: Sundering Axe
    pick_rate: 0.06
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-11-04'
  god_win_rate: 0.5753424657534246
  god_matches_won: 168
  god_matches_played: 292
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-03'
  god_matches_analyzed: 14667
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
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Shield Splitter,
    Jotunn''s Revenge, Kinetic Cuirass, Genji''s Guard, Gluttonous Grimoire, Nimble
    Ring, Breastplate of Valor, Runeforged Hammer, Golden Blade, Soul Gem, Tekko-Kagi,
    Hydra''s Lament, Erosion, Oni Hunter''s Garb, Pharaoh''s Curse, Eye of Providence,
    Tyrfing, Lernaean Bow, Draconic Scale, The Reaper, Helm of Radiance, Stone of
    Binding, Shield of the Phoenix, Shogun''s Ofuda, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Magi''s Cloak, Spear of Desolation, Avenging Blade, Screeching
    Gargoyle, Mantle Of Discord, Obsidian Shard, Leviathan''s Hide, Dominance, Blood-Bound
    Book.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.54
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.48
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.28
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.44
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
  - Hide of the Nemean Lion
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
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
    this god: Amanita Charm, Berserker''s Shield, Rod of Tahuti, Soul Gem, The Reaper,
    Shield of the Phoenix, Jotunn''s Revenge, Kinetic Cuirass, Genji''s Guard, Blood-Bound
    Book, Shield Splitter, Gluttonous Grimoire, Nimble Ring, Golden Blade, Runeforged
    Hammer, Yogi''s Necklace, Phoenix Feather, Bloodforge, Riptalon, Breastplate of
    Valor, Tekko-Kagi, Hydra''s Lament, Oni Hunter''s Garb, Chandra''s Grace, Pharaoh''s
    Curse, Tyrfing, Lernaean Bow, Bancroft''s Talon, Erosion, Eye of Providence, Shogun''s
    Ofuda, Avenging Blade, Midgardian Mail, Draconic Scale, Regrowth Striders, Titan''s
    Bane, Helm of Radiance, Sphere of Negation, Spear of Desolation.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.29
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.52
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.29
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.72
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.61
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Hide of the Nemean Lion
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Stone of Binding
  - Hide of the Nemean Lion
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Amanita Charm, Soul Gem, Stone of Binding, Genji''s Guard, Screeching
    Gargoyle, Tekko-Kagi, Avenging Blade, Shield Splitter, Kinetic Cuirass, The Reaper,
    Obsidian Shard, Titan''s Bane, Spear of Desolation, Void Stone, Nimble Ring, Void
    Shield, Breastplate of Valor, Runeforged Hammer, The Crusher, Spear of the Magus,
    Toxic Blade, Silverbranch Bow, Golden Blade, Hydra''s Lament, Heartseeker, Oni
    Hunter''s Garb, Helm of Radiance, Lernaean Bow, Tyrfing, Erosion, Riptalon, Pharaoh''s
    Curse, Doom Orb, Eye of Providence, Midgardian Mail, The World Stone.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.44
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.22
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.54
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.61
      pick: 0.0
      fit: 0.28
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble
    Ring, Kinetic Cuirass, Jotunn''s Revenge, Golden Blade, Shield Splitter, Gluttonous
    Grimoire, Tyrfing, Breastplate of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Oni Hunter''s Garb, Hydra''s Lament,
    Shogun''s Ofuda, Silverbranch Bow, Helm of Radiance, Erosion, Eye of Providence,
    Stone of Binding, Draconic Scale, Obsidian Shard, Midgardian Mail, Shield of the
    Phoenix, Spear of Desolation, Helm of Darkness, The Reaper, Magi''s Cloak, Screeching
    Gargoyle, Titan''s Bane, Riptalon, Leviathan''s Hide, Dominance, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.2
    Berserker's Shield:
      total: 0.6
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.54
      efficiency: 0.63
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
    Genji''s Guard, Jotunn''s Revenge, Amanita Charm, Soul Gem, Breastplate of Valor,
    Kinetic Cuirass, Gluttonous Grimoire, Nimble Ring, Spear of Desolation, Hydra''s
    Lament, Shield Splitter, Shield of the Phoenix, Screeching Gargoyle, Chronos''
    Pendant, Helm of Radiance, Runeforged Hammer, Arondight, Oni Hunter''s Garb, Obsidian
    Shard, Golden Blade, Helm of Darkness, Erosion, Pharaoh''s Curse, Eye of Providence,
    Stone of Binding, Tekko-Kagi, Blood-Bound Book, Midgardian Mail, Gladiator''s
    Shield, Draconic Scale, Gem of Focus, Magi''s Cloak, Shogun''s Ofuda, Lernaean
    Bow, Heartwood Charm, Tyrfing, Ancient Signet.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.39
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.37
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.27
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.36
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
    Revenge, Amanita Charm, Shield Splitter, Gluttonous Grimoire, Genji''s Guard,
    Kinetic Cuirass, Soul Gem, Runeforged Hammer, The Reaper, Tekko-Kagi, Titan''s
    Bane, Breastplate of Valor, Hydra''s Lament, Nimble Ring, Golden Blade, Obsidian
    Shard, Spear of Desolation, The Crusher, Oni Hunter''s Garb, Lernaean Bow, Tyrfing,
    Erosion, Avenging Blade, Helm of Radiance, Eye of Providence, Heartseeker, Stone
    of Binding, Draconic Scale, Shield of the Phoenix, Midgardian Mail, Arondight,
    Helm of Darkness, Magi''s Cloak, Spear of the Magus, Death Metal, Screeching Gargoyle,
    Pharaoh''s Curse, Leviathan''s Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.21
    Berserker's Shield:
      total: 0.58
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.42
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.49
    Hide of the Nemean Lion:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.25
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.39
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
  - Gluttonous Grimoire
  flex_slots:
  - Genji's Guard
  - Shield Splitter
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield,
    Gluttonous Grimoire, Jotunn''s Revenge, Amanita Charm, Soul Gem, Nimble Ring,
    Genji''s Guard, Shield Splitter, Kinetic Cuirass, Obsidian Shard, Spear of Desolation,
    Tekko-Kagi, Helm of Radiance, Runeforged Hammer, Breastplate of Valor, The Reaper,
    Titan''s Bane, Spear of the Magus, Golden Blade, Hydra''s Lament, Helm of Darkness,
    Blood-Bound Book, Death Metal, Oni Hunter''s Garb, Ancient Signet, Lernaean Bow,
    Bragi''s Harp, Tyrfing, Erosion, The Crusher, Pharaoh''s Curse, Eye of Providence,
    Jade Scepter, Stone of Binding, Doom Orb, Midgardian Mail, Shield of the Phoenix,
    Draconic Scale, Avenging Blade.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.19
    Berserker's Shield:
      total: 0.59
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.33
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.39
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.25
      fit: 0.22
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.53
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
    Underrated for this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Shield
    Splitter, Jotunn''s Revenge, Kinetic Cuirass, Genji''s Guard, Gluttonous Grimoire,
    Nimble Ring, Breastplate of Valor, Runeforged Hammer, Golden Blade, Soul Gem,
    Tekko-Kagi, Hydra''s Lament, Erosion, Oni Hunter''s Garb, Pharaoh''s Curse, Eye
    of Providence, Tyrfing, Lernaean Bow, Draconic Scale, The Reaper, Helm of Radiance,
    Stone of Binding, Shield of the Phoenix, Shogun''s Ofuda, Helm of Darkness, Midgardian
    Mail, Titan''s Bane, Magi''s Cloak, Spear of Desolation, Avenging Blade, Screeching
    Gargoyle, Mantle Of Discord, Obsidian Shard, Leviathan''s Hide, Dominance, Blood-Bound
    Book.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.61
      pick: 0.0
      fit: 0.24
    Berserker's Shield:
      total: 0.6
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.54
    Shield Splitter:
      total: 0.55
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.44
  starter: *id001
---
