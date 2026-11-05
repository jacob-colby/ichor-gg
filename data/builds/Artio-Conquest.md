---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.5
  aspect_win_rate: 0.59
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.18
    win_rate: 0.51
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.57
    - name: Gauntlet of Thebes
      pick_rate: 0.14
      win_rate: 0.47
  - name: Breastplate of Valor
    pick_rate: 0.09
    win_rate: 0.48
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.52
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.52
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.51
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.46
    - name: Genji's Guard
      pick_rate: 0.05
      win_rate: 0.35
  - name: Hide of the Nemean Lion
    pick_rate: 0.04
    win_rate: 0.39
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.68
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.57
  - name: Olmec Blue
    pick_rate: 0.06
    win_rate: 0.6
    alternates:
    - name: Medal of Defense
      pick_rate: 0.05
      win_rate: 0.71
    - name: Mote of Chaos
      pick_rate: 0.04
      win_rate: 0.58
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.54
  - name: Bumba's Cudgel
    pick_rate: 0.14
    win_rate: 0.35
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-11-04'
  god_win_rate: 0.5281553398058253
  god_matches_won: 272
  god_matches_played: 515
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
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shield Splitter, Jotunn''s
    Revenge, Berserker''s Shield, Gluttonous Grimoire, Soul Gem, Shield of the Phoenix,
    Draconic Scale, Runeforged Hammer, Oni Hunter''s Garb, Erosion, Hydra''s Lament,
    Eye of Providence, Breastplate of Valor, The Reaper, Midgardian Mail, Spear of
    Desolation, Screeching Gargoyle, Stone of Binding, Leviathan''s Hide, Lotus Sickle,
    Helm of Darkness, Helm of Radiance, Blood-Bound Book, Magi''s Cloak, Mantle Of
    Discord, Death Metal, Wyrmskin Hide, Avenging Blade, Tyrfing, Ancile, Arondight,
    The Crusher, Gladiator''s Shield, Void Stone, Phoenix Feather, Hide of the Nemean
    Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.27
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.45
    Shield Splitter:
      total: 0.52
      efficiency: 0.58
      win: 0.52
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Kinetic Cuirass, Rod
    of Tahuti, The Reaper, Berserker''s Shield, Blood-Bound Book, Jotunn''s Revenge,
    Shield Splitter, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace, Runeforged
    Hammer, Ethereal Staff, Draconic Scale, Chandra''s Grace, Oni Hunter''s Garb,
    Erosion, Hydra''s Lament, Eye of Providence, Bloodforge, Bancroft''s Talon, Breastplate
    of Valor, Regrowth Striders, Midgardian Mail, Rod of Asclepius, Leviathan''s Hide,
    Soul Locket, Spear of Desolation, Glorious Pridwen, Avenging Blade, Screeching
    Gargoyle, Lotus Sickle, Wyrmskin Hide, Death Metal, Stone of Binding, Ancile,
    Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.26
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.52
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.41
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.75
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, Kinetic Cuirass, The Reaper, Screeching Gargoyle, Stone of Binding,
    Spear of Desolation, Berserker''s Shield, Avenging Blade, Shield Splitter, Void
    Stone, The Crusher, Void Shield, Heartseeker, Obsidian Shard, Titan''s Bane, Shield
    of the Phoenix, Runeforged Hammer, Spear of the Magus, Oni Hunter''s Garb, Draconic
    Scale, Hydra''s Lament, Breastplate of Valor, Dreamer''s Idol, Erosion, Eye of
    Providence, Lotus Sickle, Midgardian Mail, Blood-Bound Book, Helm of Radiance,
    Doom Orb, Leviathan''s Hide, Avatar''s Parashu, Death Metal, Magi''s Cloak, Hide
    of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.61
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.21
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.33
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Kinetic Cuirass,
    Tyrfing, Jotunn''s Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s Garb, Breastplate
    of Valor, Runeforged Hammer, Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse,
    Hydra''s Lament, Toxic Blade, Spear of Desolation, Bragi''s Harp, Erosion, Eye
    of Providence, Lotus Sickle, The Reaper, Blood-Bound Book, Screeching Gargoyle,
    Midgardian Mail, Eros'' Bow, Lernaean Bow, Dominance, Helm of Radiance, Silverbranch
    Bow, Stone of Binding, Leviathan''s Hide, Tekko-Kagi, Riptalon, Hide of the Nemean
    Lion.'
  slot_scores:
    Golden Blade:
      total: 0.49
      efficiency: 0.51
      win: 0.52
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.19
    Berserker's Shield:
      total: 0.55
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.31
    Tyrfing:
      total: 0.5
      efficiency: 0.53
      win: 0.52
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
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
    Breastplate of Valor, Lotus Sickle, Berserker''s Shield, Hydra''s Lament, Screeching
    Gargoyle, Gluttonous Grimoire, Shield Splitter, Chronos'' Pendant, Gladiator''s
    Shield, Oni Hunter''s Garb, Draconic Scale, Arondight, Prophetic Cloak, Blood-Bound
    Book, Erosion, Runeforged Hammer, Helm of Radiance, Eye of Providence, Gem of
    Focus, Heartwood Charm, Chandra''s Grace, Midgardian Mail, Helm of Darkness, The
    Reaper, Stone of Binding, Ancient Signet, Regrowth Striders, Leviathan''s Hide,
    Eye of Erebus, Magi''s Cloak, Mantle Of Discord, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.44
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.58
    Spear of Desolation:
      total: 0.51
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.43
    Soul Gem:
      total: 0.53
      efficiency: 0.58
      win: 0.52
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Kinetic Cuirass, Shield Splitter, Gluttonous Grimoire,
    Soul Gem, The Reaper, Runeforged Hammer, Tyrfing, Hydra''s Lament, Spear of Desolation,
    Shield of the Phoenix, Golden Blade, The Crusher, Oni Hunter''s Garb, Heartseeker,
    Draconic Scale, Breastplate of Valor, Tekko-Kagi, Titan''s Bane, Erosion, Death
    Metal, Eye of Providence, Lotus Sickle, Bragi''s Harp, Blood-Bound Book, Midgardian
    Mail, Screeching Gargoyle, Avenging Blade, Obsidian Shard, Helm of Radiance, Arondight,
    Nimble Ring, Stone of Binding, Leviathan''s Hide, Lernaean Bow, Dominance.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.2
    Berserker's Shield:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.33
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Kinetic Cuirass, Spear of Desolation, Berserker''s
    Shield, Shield Splitter, The Reaper, Lotus Sickle, Blood-Bound Book, Runeforged
    Hammer, Obsidian Shard, Death Metal, Helm of Radiance, Shield of the Phoenix,
    Hydra''s Lament, Oni Hunter''s Garb, Spear of the Magus, Draconic Scale, Ancient
    Signet, Helm of Darkness, Breastplate of Valor, The Crusher, Polynomicon, Heartseeker,
    Dreamer''s Idol, Erosion, Chronos'' Pendant, Eye of Providence, Jade Scepter,
    Midgardian Mail, Screeching Gargoyle, Titan''s Bane, Triton''s Conch, Stone of
    Binding, Leviathan''s Hide, Doom Orb.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.2
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.33
    Spear of Desolation:
      total: 0.5
      efficiency: 0.6
      win: 0.52
      pick: 0.0
      fit: 0.39
    Amanita Charm:
      total: 0.53
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Freya's Tears
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Shield
    Splitter, Jotunn''s Revenge, Berserker''s Shield, Gluttonous Grimoire, Soul Gem,
    Shield of the Phoenix, Breastplate of Valor, Draconic Scale, Runeforged Hammer,
    Oni Hunter''s Garb, Erosion, Hydra''s Lament, Eye of Providence, The Reaper, Midgardian
    Mail, Spear of Desolation, Screeching Gargoyle, Stone of Binding, Leviathan''s
    Hide, Lotus Sickle, Hide of the Nemean Lion, Helm of Darkness, Helm of Radiance,
    Blood-Bound Book, Magi''s Cloak, Mantle Of Discord, Death Metal, Wyrmskin Hide,
    Avenging Blade, Tyrfing, Ancile, Arondight, The Crusher, Gladiator''s Shield,
    Void Stone, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.71
      win: 0.52
      pick: 0.19
      fit: 0.27
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.61
      win: 0.52
      pick: 0.0
      fit: 0.6
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.6
      pick: 0.23
      fit: 0.45
    Shield Splitter:
      total: 0.52
      efficiency: 0.58
      win: 0.52
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
---
