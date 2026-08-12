---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.54
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.19
    win_rate: 0.5
    alternates:
    - name: Lifebinder
      pick_rate: 0.15
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.47
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.55
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.57
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.3
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.64
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.65
  - name: Ethereal Staff
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.44
    - name: Freya's Tears
      pick_rate: 0.05
      win_rate: 0.67
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.63
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.5
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.42
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.41
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.58
  - name: War Banner
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-11'
  god_win_rate: 0.5214067278287462
  god_matches_won: 341
  god_matches_played: 654
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-11'
  god_matches_analyzed: 18835
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Ethereal Staff
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire,
    Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence, Draconic
    Scale, Spectral Armor, Prophetic Cloak, Soul Gem, Mantle Of Discord, Leviathan''s
    Hide, Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Void Shield, Hide of the Nemean Lion, Screeching
    Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.47
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.81
    Ethereal Staff:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.3
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.64
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Ethereal Staff
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Gluttonous Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Chandra''s
    Grace, Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Spectral Armor,
    Lifebinder, Leviathan''s Hide, Blood-Bound Book, Bancroft''s Talon, Midgardian
    Mail, Glorious Pridwen, Gladiator''s Shield, Ancile, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.92
    Ethereal Staff:
      total: 0.55
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.36
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Stone of Binding, Spear of the Magus, Screeching Gargoyle, Void
    Shield, The Cosmic Horror, Oni Hunter''s Garb, Void Stone, Shield of the Phoenix,
    Spear of Desolation, Erosion, Obsidian Shard, Eye of Providence, Spectral Armor,
    Draconic Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.47
      pick: 0.23
      fit: 0.27
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.2
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral Armor, Erosion,
    Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic Scale, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Yogi''s Necklace, Mantle Of Discord, Stone
    of Binding, Spear of the Magus, Rod of Asclepius, Blood-Bound Book, Bragi''s Harp,
    Bancroft''s Talon.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.2
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.44
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.44
    Ethereal Staff:
      total: 0.51
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.15
    Freya's Tears:
      total: 0.56
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.33
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Ethereal Staff
  - Freya's Tears
  flex_slots:
  - Kinetic Cuirass
  - Shield of the Phoenix
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Kinetic Cuirass, Shield
    of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Prophetic Cloak,
    Oni Hunter''s Garb, Screeching Gargoyle, Chronos'' Pendant, Spear of Desolation,
    Chandra''s Grace, Gladiator''s Shield, Erosion, Spectral Armor, Eye of Providence,
    Draconic Scale, Helm of Radiance, Gem of Focus, Leviathan''s Hide, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius, Stone of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.47
      pick: 0.23
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.61
    Ethereal Staff:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.22
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Ethereal Staff
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Ethereal Staff
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Soul
    Gem, Hydra''s Lament, Oni Hunter''s Garb, Runeforged Hammer, Shield Splitter,
    Pharaoh''s Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow, Eye of the
    Storm, Erosion, Spectral Armor, Death Metal, Spear of the Magus, Eye of Providence,
    Shogun''s Ofuda, The Reaper, Draconic Scale, Damaru, The Cosmic Horror, Avenging
    Blade, Helm of Radiance, Riptalon, Leviathan''s Hide, Midgardian Mail, Mantle
    Of Discord, Stone of Binding, Heartseeker, Silverbranch Bow, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.45
    Ethereal Staff:
      total: 0.52
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.17
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Ethereal Staff
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Jotunn''s Revenge, Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s
    Shield, Spear of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death Metal,
    The Cosmic Horror, Runeforged Hammer, Shield Splitter, Helm of Radiance, Shield
    of the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Eye of the Storm,
    Rod of Asclepius, Eye of Providence, Pharaoh''s Curse, Obsidian Shard, Jade Scepter,
    Draconic Scale, Chronos'' Pendant, Golden Blade, Leviathan''s Hide, Blood-Bound
    Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.52
    Ethereal Staff:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.13
      fit: 0.3
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.38
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous
    Grimoire, Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence,
    Draconic Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s Hide,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Magi''s Cloak, Gladiator''s
    Shield, Ancile, Xibalban Effigy, Prophetic Cloak, Void Shield, Hide of the Nemean
    Lion, Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.47
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.67
      pick: 0.11
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.19
      fit: 0.71
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.71
  starter: *id001
---
