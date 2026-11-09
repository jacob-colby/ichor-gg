---
type: smite-build
god: Cabrakan
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Rotund Jotunn
  aspect_pick_rate: 0.1
  aspect_win_rate: 0.3
  slot_order:
  - name: Runeforged Hammer
    pick_rate: 0.43
    win_rate: 0.51
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.18
      win_rate: 0.39
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.62
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.33
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.46
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.54
  - name: Freya's Tears
    pick_rate: 0.19
    win_rate: 0.32
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.54
    - name: Breastplate of Valor
      pick_rate: 0.12
      win_rate: 0.58
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.17
    alternates:
    - name: Freya's Tears
      pick_rate: 0.2
      win_rate: 0.37
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.67
  - name: Draconic Scale
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.57
    - name: Sundering Echo
      pick_rate: 0.06
      win_rate: 0.4
  - name: Veve Charm
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Draconic Scale
      pick_rate: 0.1
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.67
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.34
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.4
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.45
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-11-08'
  god_win_rate: 0.45544554455445546
  god_matches_won: 46
  god_matches_played: 101
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shield Splitter, Berserker''s
    Shield, Jotunn''s Revenge, Gluttonous Grimoire, Shield of the Phoenix, Soul Gem,
    Erosion, Oni Hunter''s Garb, Eye of Providence, Hydra''s Lament, The Reaper, Midgardian
    Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Spear of Desolation,
    Helm of Darkness, Magi''s Cloak, Mantle Of Discord, Helm of Radiance, Hide of
    the Nemean Lion, Lotus Sickle, Blood-Bound Book, Wyrmskin Hide, Death Metal, Ancile,
    Tyrfing, Avenging Blade, Gladiator''s Shield, Void Stone, The Crusher, Arondight,
    Phoenix Feather.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.58
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.62
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.55
      win: 0.51
      pick: 0.43
      fit: 0.44
    Shifter's Shield:
      total: 0.5
      efficiency: 0.5
      win: 0.54
      pick: 0.18
      fit: 0.52
    Draconic Scale:
      total: 0.5
      efficiency: 0.53
      win: 0.5
      pick: 0.17
      fit: 0.52
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Runeforged Hammer
  - Shield of the Phoenix
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Rod
    of Tahuti, The Reaper, Berserker''s Shield, Jotunn''s Revenge, Blood-Bound Book,
    Shield Splitter, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace, Ethereal
    Staff, Chandra''s Grace, Oni Hunter''s Garb, Erosion, Hydra''s Lament, Eye of
    Providence, Bloodforge, Bancroft''s Talon, Regrowth Striders, Midgardian Mail,
    Rod of Asclepius, Leviathan''s Hide, Soul Locket, Spear of Desolation, Glorious
    Pridwen, Hide of the Nemean Lion, Avenging Blade, Screeching Gargoyle, Wyrmskin
    Hide, Lotus Sickle, Death Metal, Stone of Binding, Ancile.'
  slot_scores:
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.63
      win: 0.58
      pick: 0.19
      fit: 0.26
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.6
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.55
      win: 0.51
      pick: 0.43
      fit: 0.5
    Shield of the Phoenix:
      total: 0.51
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.75
    Shifter's Shield:
      total: 0.5
      efficiency: 0.5
      win: 0.54
      pick: 0.18
      fit: 0.5
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Kinetic Cuirass, Screeching Gargoyle, Stone of Binding, The Reaper,
    Spear of Desolation, Berserker''s Shield, Shield Splitter, Avenging Blade, Void
    Stone, Void Shield, The Crusher, Heartseeker, Obsidian Shard, Shield of the Phoenix,
    Titan''s Bane, Oni Hunter''s Garb, Spear of the Magus, Hydra''s Lament, Erosion,
    Eye of Providence, Dreamer''s Idol, Midgardian Mail, Lotus Sickle, Blood-Bound
    Book, Helm of Radiance, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord, Doom
    Orb, Hide of the Nemean Lion, Avatar''s Parashu.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.58
      pick: 0.19
      fit: 0.21
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.55
      win: 0.51
      pick: 0.43
      fit: 0.36
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.49
      efficiency: 0.5
      win: 0.54
      pick: 0.18
      fit: 0.39
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Runeforged Hammer
  - Tyrfing
  - Amanita Charm
  flex_slots:
  - Tyrfing
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic Cuirass,
    Tyrfing, Jotunn''s Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, Shield of the Phoenix, Oni Hunter''s Garb, Nimble Ring, Shogun''s Ofuda,
    Pharaoh''s Curse, Erosion, Hydra''s Lament, Eye of Providence, Toxic Blade, Spear
    of Desolation, Bragi''s Harp, Screeching Gargoyle, Lotus Sickle, Midgardian Mail,
    The Reaper, Blood-Bound Book, Helm of Radiance, Stone of Binding, Eros'' Bow,
    Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch Bow, Magi''s Cloak, Mantle
    Of Discord, Hide of the Nemean Lion.'
  slot_scores:
    Golden Blade:
      total: 0.46
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.52
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.58
      pick: 0.19
      fit: 0.2
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.55
      win: 0.51
      pick: 0.43
      fit: 0.31
    Tyrfing:
      total: 0.47
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.53
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Kinetic Cuirass
  - Shifter's Shield
  - Soul Gem
  flex_slots:
  - Shifter's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Soul
    Gem, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation,
    Lotus Sickle, Berserker''s Shield, Screeching Gargoyle, Hydra''s Lament, Gluttonous
    Grimoire, Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Oni Hunter''s
    Garb, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Blood-Bound Book,
    Helm of Radiance, Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian
    Mail, Stone of Binding, Chandra''s Grace, Leviathan''s Hide, Regrowth Striders,
    The Reaper, Ancient Signet, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean
    Lion, Eye of Erebus.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.58
      pick: 0.19
      fit: 0.44
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.49
      efficiency: 0.55
      win: 0.51
      pick: 0.43
      fit: 0.31
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.51
    Shifter's Shield:
      total: 0.49
      efficiency: 0.5
      win: 0.54
      pick: 0.18
      fit: 0.41
    Soul Gem:
      total: 0.5
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, The Reaper, Tyrfing, Hydra''s Lament, Spear of Desolation, Shield of
    the Phoenix, Golden Blade, The Crusher, Oni Hunter''s Garb, Heartseeker, Erosion,
    Eye of Providence, Tekko-Kagi, Titan''s Bane, Death Metal, Midgardian Mail, Screeching
    Gargoyle, Lotus Sickle, Blood-Bound Book, Stone of Binding, Bragi''s Harp, Helm
    of Radiance, Obsidian Shard, Avenging Blade, Leviathan''s Hide, Arondight, Nimble
    Ring, Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.5
      efficiency: 0.72
      win: 0.45
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.58
      pick: 0.19
      fit: 0.21
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.42
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.55
      win: 0.51
      pick: 0.43
      fit: 0.42
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Breastplate of Valor
  - Runeforged Hammer
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Kinetic Cuirass, Jotunn''s Revenge, Shield Splitter, Spear
    of Desolation, Berserker''s Shield, The Reaper, Lotus Sickle, Blood-Bound Book,
    Helm of Radiance, Shield of the Phoenix, Obsidian Shard, Death Metal, Oni Hunter''s
    Garb, Helm of Darkness, Hydra''s Lament, Spear of the Magus, Ancient Signet, The
    Crusher, Erosion, Eye of Providence, Polynomicon, Heartseeker, Dreamer''s Idol,
    Chronos'' Pendant, Screeching Gargoyle, Midgardian Mail, Stone of Binding, Jade
    Scepter, Titan''s Bane, Leviathan''s Hide, Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.63
      win: 0.58
      pick: 0.19
      fit: 0.21
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.38
    Runeforged Hammer:
      total: 0.5
      efficiency: 0.55
      win: 0.51
      pick: 0.43
      fit: 0.38
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.49
    Shifter's Shield:
      total: 0.48
      efficiency: 0.5
      win: 0.54
      pick: 0.18
      fit: 0.39
    Amanita Charm:
      total: 0.5
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Breastplate of Valor
  - Runeforged Hammer
  - Shifter's Shield
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shield
    Splitter, Berserker''s Shield, Jotunn''s Revenge, Gluttonous Grimoire, Shield
    of the Phoenix, Soul Gem, Erosion, Oni Hunter''s Garb, Eye of Providence, Hydra''s
    Lament, The Reaper, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Spear of Desolation, Helm of Darkness, Magi''s Cloak, Mantle Of Discord,
    Helm of Radiance, Hide of the Nemean Lion, Lotus Sickle, Blood-Bound Book, Wyrmskin
    Hide, Death Metal, Ancile, Tyrfing, Avenging Blade, Gladiator''s Shield, Void
    Stone, The Crusher, Arondight, Phoenix Feather.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.66
      win: 0.45
      pick: 0.0
      fit: 0.33
    Genji's Guard:
      total: 0.45
      efficiency: 0.71
      win: 0.33
      pick: 0.2
      fit: 0.28
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.62
    Shield Splitter:
      total: 0.49
      efficiency: 0.58
      win: 0.45
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.44
      efficiency: 0.61
      win: 0.32
      pick: 0.3
      fit: 0.47
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.52
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
community_aspects:
  source: SmiteBrain per-match feed, obsidian+ (data/Analysis/aspect_matches)
  complete_from: '2026-09-24'
  partial_windows:
    ob44: '2026-09-24'
  minimum_matches: 30
  window_rule: the newest patch window, or the last closed one when the newest holds
    fewer than minimum_matches of the aspect's matches
  aspects:
  - aspect: Aspect of the Rotund Jotunn
    status: shown
    window: ob46
    window_rule: last closed
    window_start: '2026-10-20'
    window_end: '2026-11-03'
    matches: 31
    wins: 10
    win_share: 0.32
    aggregate:
      aspect_matches: 40
      aspect_win_rate: 0.275
      no_aspect_matches: 376
      no_aspect_win_rate: 0.598
    roles:
    - role: Mid
      matches: 17
      share: 0.55
    - role: Solo
      matches: 11
      share: 0.35
    - role: Jungle
      matches: 3
      share: 0.1
    base_role: Solo Support
    base_role_share: 0.35
    role_shift: null
    items:
    - name: Rod of Tahuti
      share: 0.58
    - name: Chronos' Pendant
      share: 0.48
    - name: The Cosmic Horror
      share: 0.48
    - name: Totem of Death
      share: 0.42
    - name: Ancient Signet
      share: 0.29
    - name: Spear of Desolation
      share: 0.26
    - name: Spear of the Magus
      share: 0.26
    - name: Damaru
      share: 0.23
    starters:
    - name: Archmage's Gem
      share: 0.39
    - name: Bluestone Brooch
      share: 0.29
    - name: Bluestone Pendant
      share: 0.16
    relics:
    - name: aegis-of-acceleration
      share: 0.52
    - name: purification-beads
      share: 0.32
    - name: sundering-arc
      share: 0.16
    matches_by_window:
      ob47: 10
      ob46: 31
      ob45: 53
      ob44: 61
    unmapped_slugs:
    - aegis-of-acceleration
    - purification-beads
    - sundering-arc
---
