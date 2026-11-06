---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.34
  aspect_win_rate: 0.68
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.38
    win_rate: 0.64
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.31
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.67
  - name: Regrowth Striders
    pick_rate: 0.13
    win_rate: 0.8
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.43
    - name: Prophetic Cloak
      pick_rate: 0.1
      win_rate: 0.83
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.67
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.12
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.83
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.33
  - name: Contagion
    pick_rate: 0.06
    win_rate: 0.8
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.1
      win_rate: 0.67
    - name: Captain's Ring
      pick_rate: 0.06
      win_rate: 0.4
  - name: Sage's Ring
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Medal of Defense
      pick_rate: 0.1
      win_rate: 0.67
    - name: Veve Charm
      pick_rate: 0.08
      win_rate: 0.8
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.23
    win_rate: 0.7
  - name: Bumba's Cudgel
    pick_rate: 0.17
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.16
    win_rate: 0.39
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-11-06'
  god_win_rate: 0.6120689655172413
  god_matches_won: 71
  god_matches_played: 116
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Jotunn''s Revenge, Berserker''s
    Shield, Gluttonous Grimoire, Soul Gem, Shield of the Phoenix, Breastplate of Valor,
    Draconic Scale, Runeforged Hammer, Oni Hunter''s Garb, Erosion, Hydra''s Lament,
    Eye of Providence, The Reaper, Midgardian Mail, Spear of Desolation, Screeching
    Gargoyle, Stone of Binding, Leviathan''s Hide, Lotus Sickle, Hide of the Nemean
    Lion, Helm of Darkness, Helm of Radiance, Blood-Bound Book, Magi''s Cloak, Mantle
    Of Discord, Death Metal, Wyrmskin Hide, Avenging Blade, Tyrfing, Ancile, Arondight,
    The Crusher, Gladiator''s Shield, Void Stone, Phoenix Feather.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.35
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.45
      win: 0.83
      pick: 0.14
      fit: 0.45
    Shield Splitter:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.45
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
  - Regrowth Striders
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Rod of Tahuti, The Reaper,
    Berserker''s Shield, Blood-Bound Book, Jotunn''s Revenge, Shield Splitter, Phoenix
    Feather, Gluttonous Grimoire, Yogi''s Necklace, Runeforged Hammer, Chandra''s
    Grace, Ethereal Staff, Draconic Scale, Breastplate of Valor, Oni Hunter''s Garb,
    Erosion, Hydra''s Lament, Eye of Providence, Bloodforge, Bancroft''s Talon, Midgardian
    Mail, Rod of Asclepius, Leviathan''s Hide, Soul Locket, Spear of Desolation, Glorious
    Pridwen, Hide of the Nemean Lion, Avenging Blade, Screeching Gargoyle, Lotus Sickle,
    Wyrmskin Hide, Death Metal, Stone of Binding, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.35
    Prophetic Cloak:
      total: 0.6
      efficiency: 0.45
      win: 0.83
      pick: 0.14
      fit: 0.41
    Regrowth Striders:
      total: 0.62
      efficiency: 0.47
      win: 0.8
      pick: 0.18
      fit: 0.56
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.41
    Amanita Charm:
      total: 0.66
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Prophetic Cloak
  - Regrowth Striders
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Stone of Binding
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Soul Gem, The Reaper, Screeching Gargoyle, Stone of Binding, Spear of Desolation,
    Berserker''s Shield, Avenging Blade, Shield Splitter, Void Stone, The Crusher,
    Void Shield, Heartseeker, Breastplate of Valor, Obsidian Shard, Titan''s Bane,
    Shield of the Phoenix, Runeforged Hammer, Spear of the Magus, Oni Hunter''s Garb,
    Draconic Scale, Hydra''s Lament, Dreamer''s Idol, Erosion, Eye of Providence,
    Lotus Sickle, Midgardian Mail, Blood-Bound Book, Helm of Radiance, Doom Orb, Leviathan''s
    Hide, Avatar''s Parashu, Death Metal, Hide of the Nemean Lion, Magi''s Cloak.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.58
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.61
    Stone of Binding:
      total: 0.57
      efficiency: 0.49
      win: 0.67
      pick: 0.0
      fit: 0.66
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.51
    Prophetic Cloak:
      total: 0.59
      efficiency: 0.45
      win: 0.83
      pick: 0.14
      fit: 0.33
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.33
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Prophetic Cloak
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Tyrfing, Jotunn''s
    Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor,
    Soul Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s Garb, Runeforged Hammer,
    Draconic Scale, Shogun''s Ofuda, Pharaoh''s Curse, Hydra''s Lament, Toxic Blade,
    Spear of Desolation, Bragi''s Harp, Erosion, Eye of Providence, Lotus Sickle,
    The Reaper, Blood-Bound Book, Screeching Gargoyle, Midgardian Mail, Eros'' Bow,
    Lernaean Bow, Dominance, Helm of Radiance, Silverbranch Bow, Stone of Binding,
    Leviathan''s Hide, Tekko-Kagi, Hide of the Nemean Lion, Riptalon.'
  slot_scores:
    Golden Blade:
      total: 0.56
      efficiency: 0.51
      win: 0.67
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.62
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.43
    Prophetic Cloak:
      total: 0.58
      efficiency: 0.45
      win: 0.83
      pick: 0.14
      fit: 0.31
    Tyrfing:
      total: 0.57
      efficiency: 0.53
      win: 0.67
      pick: 0.0
      fit: 0.54
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.31
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Prophetic Cloak
  - Regrowth Striders
  - Freya's Tears
  - Spear of Desolation
  flex_slots:
  - Breastplate of Valor
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Prophetic Cloak, Rod of Tahuti, Amanita
    Charm, Soul Gem, Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Lotus Sickle, Berserker''s Shield, Hydra''s Lament, Screeching
    Gargoyle, Gluttonous Grimoire, Shield Splitter, Chronos'' Pendant, Gladiator''s
    Shield, Oni Hunter''s Garb, Draconic Scale, Arondight, Blood-Bound Book, Chandra''s
    Grace, Erosion, Runeforged Hammer, Helm of Radiance, Eye of Providence, Gem of
    Focus, Heartwood Charm, Midgardian Mail, Helm of Darkness, The Reaper, Stone of
    Binding, Ancient Signet, Leviathan''s Hide, Eye of Erebus, Hide of the Nemean
    Lion, Magi''s Cloak, Mantle Of Discord.'
  slot_scores:
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.63
      win: 0.67
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.43
    Prophetic Cloak:
      total: 0.62
      efficiency: 0.45
      win: 0.83
      pick: 0.14
      fit: 0.58
    Regrowth Striders:
      total: 0.6
      efficiency: 0.47
      win: 0.8
      pick: 0.18
      fit: 0.44
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.58
    Spear of Desolation:
      total: 0.58
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Prophetic Cloak
  - Regrowth Striders
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Prophetic Cloak
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
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita
    Charm, Jotunn''s Revenge, Shield Splitter, Gluttonous Grimoire, Soul Gem, The
    Reaper, Runeforged Hammer, Tyrfing, Breastplate of Valor, Hydra''s Lament, Spear
    of Desolation, Shield of the Phoenix, Golden Blade, The Crusher, Oni Hunter''s
    Garb, Heartseeker, Draconic Scale, Tekko-Kagi, Titan''s Bane, Erosion, Death Metal,
    Eye of Providence, Lotus Sickle, Bragi''s Harp, Blood-Bound Book, Midgardian Mail,
    Screeching Gargoyle, Avenging Blade, Obsidian Shard, Helm of Radiance, Arondight,
    Nimble Ring, Stone of Binding, Leviathan''s Hide, Lernaean Bow, Dominance.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.72
      win: 0.67
      pick: 0.0
      fit: 0.33
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.43
    Prophetic Cloak:
      total: 0.59
      efficiency: 0.45
      win: 0.83
      pick: 0.14
      fit: 0.33
    Shield Splitter:
      total: 0.57
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.33
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Freya's Tears
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Spear of Desolation, Berserker''s Shield,
    Shield Splitter, The Reaper, Breastplate of Valor, Lotus Sickle, Blood-Bound Book,
    Runeforged Hammer, Obsidian Shard, Death Metal, Helm of Radiance, Shield of the
    Phoenix, Hydra''s Lament, Oni Hunter''s Garb, Spear of the Magus, Draconic Scale,
    Ancient Signet, Helm of Darkness, The Crusher, Polynomicon, Heartseeker, Dreamer''s
    Idol, Erosion, Chronos'' Pendant, Eye of Providence, Jade Scepter, Midgardian
    Mail, Screeching Gargoyle, Titan''s Bane, Triton''s Conch, Stone of Binding, Leviathan''s
    Hide, Doom Orb.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.39
    Prophetic Cloak:
      total: 0.59
      efficiency: 0.45
      win: 0.83
      pick: 0.14
      fit: 0.33
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.33
    Spear of Desolation:
      total: 0.57
      efficiency: 0.6
      win: 0.67
      pick: 0.0
      fit: 0.39
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.67
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Jotunn''s
    Revenge, Berserker''s Shield, Gluttonous Grimoire, Soul Gem, Shield of the Phoenix,
    Breastplate of Valor, Draconic Scale, Runeforged Hammer, Oni Hunter''s Garb, Erosion,
    Hydra''s Lament, Eye of Providence, The Reaper, Midgardian Mail, Spear of Desolation,
    Screeching Gargoyle, Stone of Binding, Leviathan''s Hide, Lotus Sickle, Hide of
    the Nemean Lion, Helm of Darkness, Helm of Radiance, Blood-Bound Book, Magi''s
    Cloak, Mantle Of Discord, Death Metal, Wyrmskin Hide, Avenging Blade, Tyrfing,
    Ancile, Arondight, The Crusher, Gladiator''s Shield, Void Stone, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.71
      win: 0.5
      pick: 0.17
      fit: 0.28
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.67
      pick: 0.0
      fit: 0.35
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.61
      win: 0.54
      pick: 0.19
      fit: 0.6
    Shield Splitter:
      total: 0.59
      efficiency: 0.58
      win: 0.67
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.67
      pick: 0.22
      fit: 0.45
    Amanita Charm:
      total: 0.61
      efficiency: 0.68
      win: 0.67
      pick: 0.0
      fit: 0.5
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
