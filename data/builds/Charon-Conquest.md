---
type: smite-build
god: Charon
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Tollkeeper
  aspect_pick_rate: 0.11
  aspect_win_rate: 0.52
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.2
    win_rate: 0.5
    alternates:
    - name: Lifebinder
      pick_rate: 0.15
      win_rate: 0.53
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.53
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.47
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.56
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.6
  - name: Breastplate of Valor
    pick_rate: 0.13
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.19
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.54
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.31
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.66
    - name: Ethereal Staff
      pick_rate: 0.06
      win_rate: 0.6
  - name: Ethereal Staff
    pick_rate: 0.07
    win_rate: 0.66
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.47
    - name: Hide of the Nemean Lion
      pick_rate: 0.05
      win_rate: 0.52
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.67
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.47
    - name: Medallion
      pick_rate: 0.04
      win_rate: 0.36
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.41
    win_rate: 0.48
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.59
  - name: Bumba's Cudgel
    pick_rate: 0.07
    win_rate: 0.25
  source_url: https://smitebrain.com/gods/charon/
  last_verified: '2026-08-10'
  god_win_rate: 0.5272727272727272
  god_matches_won: 319
  god_matches_played: 605
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-10'
  god_matches_analyzed: 17490
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
    this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Gluttonous Grimoire,
    Erosion, Oni Hunter''s Garb, Shield of the Phoenix, Eye of Providence, Draconic
    Scale, Spectral Armor, Soul Gem, Mantle Of Discord, Leviathan''s Hide, Stone of
    Binding, Midgardian Mail, Prophetic Cloak, Helm of Radiance, Magi''s Cloak, Hide
    of the Nemean Lion, Gladiator''s Shield, Ancile, Xibalban Effigy, Void Shield,
    Screeching Gargoyle.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.47
      pick: 0.23
      fit: 0.39
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.81
    Ethereal Staff:
      total: 0.53
      efficiency: 0.52
      win: 0.66
      pick: 0.15
      fit: 0.3
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.64
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.52
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
  - Oni Hunter's Garb
  - Ethereal Staff
  - Amanita Charm
  flex_slots:
  - Ethereal Staff
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Gluttonous
    Grimoire, Rod of Asclepius, Oni Hunter''s Garb, Freya''s Tears, Chandra''s Grace,
    Erosion, Eye of Providence, Draconic Scale, Phoenix Feather, Spectral Armor, Lifebinder,
    Leviathan''s Hide, Blood-Bound Book, Bancroft''s Talon, Midgardian Mail, Glorious
    Pridwen, Gladiator''s Shield, Ancile, Jade Scepter, Void Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.92
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.48
    Ethereal Staff:
      total: 0.54
      efficiency: 0.52
      win: 0.66
      pick: 0.15
      fit: 0.36
    Amanita Charm:
      total: 0.6
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 1.0
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  flex_slots:
  - Stone of Binding
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Soul Gem, Kinetic Cuirass, Amanita Charm, Stone
    of Binding, Spear of the Magus, Freya''s Tears, Screeching Gargoyle, Void Shield,
    The Cosmic Horror, Oni Hunter''s Garb, Void Stone, Shield of the Phoenix, Spear
    of Desolation, Erosion, Obsidian Shard, Eye of Providence, Spectral Armor, Draconic
    Scale, Leviathan''s Hide, Helm of Radiance, Mantle Of Discord, Midgardian Mail,
    The World Stone.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.48
      win: 0.52
      pick: 0.0
      fit: 0.75
    Genji's Guard:
      total: 0.51
      efficiency: 0.71
      win: 0.47
      pick: 0.23
      fit: 0.27
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.27
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.59
    Ethereal Staff:
      total: 0.52
      efficiency: 0.52
      win: 0.66
      pick: 0.15
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Gluttonous Grimoire, Kinetic Cuirass, Amanita Charm, Freya''s Tears,
    Oni Hunter''s Garb, Soul Gem, Shield of the Phoenix, Spectral Armor, Erosion,
    Bracer of The Abyss, Eye of Providence, Helm of Radiance, Draconic Scale, Leviathan''s
    Hide, Death Metal, Midgardian Mail, Yogi''s Necklace, Mantle Of Discord, Stone
    of Binding, Spear of the Magus, Rod of Asclepius, Blood-Bound Book, Bragi''s Harp,
    Bancroft''s Talon.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.2
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.47
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.45
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.52
      pick: 0.0
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.35
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
  - Shield of the Phoenix
  - Ethereal Staff
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
    of the Phoenix, Soul Gem, Amanita Charm, Gluttonous Grimoire, Oni Hunter''s Garb,
    Screeching Gargoyle, Chronos'' Pendant, Prophetic Cloak, Spear of Desolation,
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
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.48
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.61
    Ethereal Staff:
      total: 0.52
      efficiency: 0.52
      win: 0.66
      pick: 0.15
      fit: 0.22
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, The Crusher, Kinetic Cuirass, Amanita Charm, Soul Gem, Hydra''s Lament,
    Freya''s Tears, Oni Hunter''s Garb, Runeforged Hammer, Shield Splitter, Pharaoh''s
    Curse, Golden Blade, Shield of the Phoenix, Lernaean Bow, Eye of the Storm, Erosion,
    Spectral Armor, Death Metal, Spear of the Magus, Eye of Providence, Shogun''s
    Ofuda, The Reaper, Draconic Scale, Damaru, The Cosmic Horror, Avenging Blade,
    Helm of Radiance, Riptalon, Leviathan''s Hide, Midgardian Mail, Mantle Of Discord,
    Stone of Binding, Heartseeker, Silverbranch Bow, Yogi''s Necklace.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.35
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.42
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.47
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Ethereal Staff
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
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
    + fit + win/pick). Underrated for this god: Gluttonous Grimoire, Jotunn''s Revenge,
    Kinetic Cuirass, The Crusher, Amanita Charm, Soul Gem, Berserker''s Shield, Freya''s
    Tears, Spear of the Magus, Oni Hunter''s Garb, Hydra''s Lament, Death Metal, The
    Cosmic Horror, Runeforged Hammer, Shield Splitter, Helm of Radiance, Shield of
    the Phoenix, Spear of Desolation, Erosion, Spectral Armor, Eye of the Storm, Rod
    of Asclepius, Eye of Providence, Pharaoh''s Curse, Obsidian Shard, Jade Scepter,
    Draconic Scale, Chronos'' Pendant, Golden Blade, Leviathan''s Hide, Blood-Bound
    Book, Lernaean Bow, The Reaper, Damaru, Bancroft''s Talon, Midgardian Mail, Mantle
    Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.52
    Ethereal Staff:
      total: 0.53
      efficiency: 0.52
      win: 0.66
      pick: 0.15
      fit: 0.3
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.43
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
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.81
    Freya's Tears:
      total: 0.54
      efficiency: 0.59
      win: 0.52
      pick: 0.0
      fit: 0.64
    Shifter's Shield:
      total: 0.52
      efficiency: 0.52
      win: 0.5
      pick: 0.2
      fit: 0.71
    Amanita Charm:
      total: 0.56
      efficiency: 0.63
      win: 0.52
      pick: 0.0
      fit: 0.71
  starter: *id001
---
