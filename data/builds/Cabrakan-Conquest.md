---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.28
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.41
    win_rate: 0.61
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.57
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.65
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.73
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.68
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.62
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.66
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.55
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.89
    alternates:
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 0.61
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.71
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.32
    win_rate: 0.61
  - name: Bumba's Cudgel
    pick_rate: 0.31
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.09
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-11-04'
  god_win_rate: 0.5674300254452926
  god_matches_won: 223
  god_matches_played: 393
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
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Berserker''s Shield,
    Jotunn''s Revenge, Gluttonous Grimoire, Shield of the Phoenix, Soul Gem, Erosion,
    Oni Hunter''s Garb, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian
    Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Spear of Desolation,
    Helm of Darkness, Magi''s Cloak, Mantle Of Discord, Helm of Radiance, Hide of
    the Nemean Lion, Lotus Sickle, Blood-Bound Book, Wyrmskin Hide, Death Metal, Ancile,
    Tyrfing, Avenging Blade, Gladiator''s Shield, Void Stone, The Crusher, Arondight,
    Phoenix Feather.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.63
      win: 0.67
      pick: 0.2
      fit: 0.28
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.62
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.47
    Shifter's Shield:
      total: 0.59
      efficiency: 0.5
      win: 0.73
      pick: 0.16
      fit: 0.52
    Draconic Scale:
      total: 0.59
      efficiency: 0.53
      win: 0.71
      pick: 0.18
      fit: 0.52
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Rod of Tahuti, The Reaper,
    Berserker''s Shield, Jotunn''s Revenge, Blood-Bound Book, Shield Splitter, Phoenix
    Feather, Gluttonous Grimoire, Yogi''s Necklace, Ethereal Staff, Chandra''s Grace,
    Oni Hunter''s Garb, Erosion, Hydra''s Lament, Eye of Providence, Bloodforge, Bancroft''s
    Talon, Regrowth Striders, Midgardian Mail, Rod of Asclepius, Leviathan''s Hide,
    Soul Locket, Spear of Desolation, Glorious Pridwen, Hide of the Nemean Lion, Avenging
    Blade, Screeching Gargoyle, Wyrmskin Hide, Lotus Sickle, Death Metal, Stone of
    Binding, Ancile.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.6
    Shield of the Phoenix:
      total: 0.6
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.75
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.41
    Shifter's Shield:
      total: 0.59
      efficiency: 0.5
      win: 0.73
      pick: 0.16
      fit: 0.5
    Draconic Scale:
      total: 0.59
      efficiency: 0.53
      win: 0.71
      pick: 0.18
      fit: 0.5
    Amanita Charm:
      total: 0.64
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Screeching Gargoyle, Stone of Binding, The Reaper, Spear of Desolation,
    Berserker''s Shield, Shield Splitter, Avenging Blade, Void Stone, Void Shield,
    The Crusher, Heartseeker, Obsidian Shard, Shield of the Phoenix, Titan''s Bane,
    Oni Hunter''s Garb, Spear of the Magus, Hydra''s Lament, Erosion, Eye of Providence,
    Dreamer''s Idol, Midgardian Mail, Lotus Sickle, Blood-Bound Book, Helm of Radiance,
    Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Doom Orb, Hide of the Nemean
    Lion, Avatar''s Parashu.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.35
    Shifter's Shield:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.16
      fit: 0.39
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.71
      pick: 0.18
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Tyrfing
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Tyrfing, Jotunn''s
    Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire, Soul Gem, Shield
    of the Phoenix, Oni Hunter''s Garb, Nimble Ring, Shogun''s Ofuda, Pharaoh''s Curse,
    Erosion, Hydra''s Lament, Eye of Providence, Toxic Blade, Spear of Desolation,
    Bragi''s Harp, Screeching Gargoyle, Lotus Sickle, Midgardian Mail, The Reaper,
    Blood-Bound Book, Helm of Radiance, Stone of Binding, Eros'' Bow, Lernaean Bow,
    Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Mantle Of Discord,
    Hide of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.47
    Tyrfing:
      total: 0.55
      efficiency: 0.53
      win: 0.63
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Jotunn''s Revenge, Shield of the Phoenix, Spear of Desolation, Lotus Sickle,
    Berserker''s Shield, Screeching Gargoyle, Hydra''s Lament, Gluttonous Grimoire,
    Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s Garb, Prophetic
    Cloak, Arondight, Erosion, Eye of Providence, Blood-Bound Book, Helm of Radiance,
    Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian Mail, Stone of Binding,
    Chandra''s Grace, Leviathan''s Hide, Regrowth Striders, The Reaper, Ancient Signet,
    Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion, Eye of Erebus.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.63
      win: 0.67
      pick: 0.2
      fit: 0.44
    Genji's Guard:
      total: 0.6
      efficiency: 0.71
      win: 0.6
      pick: 0.23
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.51
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.59
    Draconic Scale:
      total: 0.58
      efficiency: 0.53
      win: 0.71
      pick: 0.18
      fit: 0.41
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Shield Splitter, Gluttonous Grimoire, Soul Gem, The
    Reaper, Tyrfing, Hydra''s Lament, Spear of Desolation, Shield of the Phoenix,
    Golden Blade, The Crusher, Oni Hunter''s Garb, Heartseeker, Erosion, Eye of Providence,
    Tekko-Kagi, Titan''s Bane, Death Metal, Midgardian Mail, Screeching Gargoyle,
    Lotus Sickle, Blood-Bound Book, Stone of Binding, Bragi''s Harp, Helm of Radiance,
    Obsidian Shard, Avenging Blade, Leviathan''s Hide, Arondight, Nimble Ring, Magi''s
    Cloak, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.35
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.71
      pick: 0.18
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Shield Splitter, Spear of Desolation, Berserker''s
    Shield, The Reaper, Lotus Sickle, Blood-Bound Book, Helm of Radiance, Shield of
    the Phoenix, Obsidian Shard, Death Metal, Oni Hunter''s Garb, Helm of Darkness,
    Hydra''s Lament, Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye
    of Providence, Polynomicon, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Screeching
    Gargoyle, Midgardian Mail, Stone of Binding, Jade Scepter, Titan''s Bane, Leviathan''s
    Hide, Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.49
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.35
    Shifter's Shield:
      total: 0.57
      efficiency: 0.5
      win: 0.73
      pick: 0.16
      fit: 0.39
    Draconic Scale:
      total: 0.57
      efficiency: 0.53
      win: 0.71
      pick: 0.18
      fit: 0.39
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Berserker''s
    Shield, Jotunn''s Revenge, Gluttonous Grimoire, Shield of the Phoenix, Soul Gem,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian
    Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Spear of Desolation,
    Helm of Darkness, Magi''s Cloak, Mantle Of Discord, Helm of Radiance, Hide of
    the Nemean Lion, Lotus Sickle, Blood-Bound Book, Wyrmskin Hide, Death Metal, Ancile,
    Tyrfing, Avenging Blade, Gladiator''s Shield, Void Stone, The Crusher, Arondight,
    Phoenix Feather.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.66
      win: 0.63
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.23
      fit: 0.28
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.15
      fit: 0.62
    Shield Splitter:
      total: 0.57
      efficiency: 0.58
      win: 0.63
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.68
      pick: 0.22
      fit: 0.47
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
