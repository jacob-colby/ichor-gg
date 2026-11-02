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
    pick_rate: 0.08
    win_rate: 0.47
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.5
    - name: Prophetic Cloak
      pick_rate: 0.08
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.53
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.52
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
  last_verified: '2026-11-02'
  god_win_rate: 0.5295275590551181
  god_matches_won: 269
  god_matches_played: 508
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14397
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic Cuirass, Shield
    Splitter, Berserker''s Shield, Runeforged Hammer, Erosion, Prophetic Cloak, Eye
    of Providence, Draconic Scale, Hydra''s Lament, Shield of the Phoenix, Oni Hunter''s
    Garb, Stone of Binding, Midgardian Mail, Gluttonous Grimoire, Sundering Echo,
    Helm of Darkness, Titan''s Bane, Magi''s Cloak, Wyrmskin Hide, Screeching Gargoyle,
    Leviathan''s Hide, Mantle Of Discord, Helm of Radiance, Avenging Blade, Spear
    of Desolation, Breastplate of Valor, Obsidian Shard, Ancile, Arondight, Void Stone,
    Stampede, Soul Gem, Void Shield, Death Metal, Xibalban Effigy, Hide of the Nemean
    Lion.'
  slot_scores:
    Berserker's Shield:
      total: 0.52
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.55
      efficiency: 0.55
      win: 0.6
      pick: 0.23
      fit: 0.5
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Jotunn''s Revenge,
    Kinetic Cuirass, Berserker''s Shield, Shield Splitter, Soul Gem, Phoenix Feather,
    Runeforged Hammer, Yogi''s Necklace, Chandra''s Grace, Ethereal Staff, The Reaper,
    Erosion, Eye of Providence, Draconic Scale, Oni Hunter''s Garb, Hydra''s Lament,
    Gluttonous Grimoire, Midgardian Mail, Glorious Pridwen, Avenging Blade, Wyrmskin
    Hide, Sundering Echo, Leviathan''s Hide, Regrowth Striders, Titan''s Bane, Rod
    of Asclepius, Stone of Binding, Blood-Bound Book, Sphere of Negation, Helm of
    Darkness, Screeching Gargoyle, Ancile, Spear of Desolation, Helm of Radiance,
    Magi''s Cloak, Breastplate of Valor.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.38
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.23
      fit: 0.46
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Jotunn's Revenge
  - Freya's Tears
  - Titan's Bane
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Titan's Bane
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Screeching Gargoyle, Titan''s Bane, Obsidian Shard, Kinetic
    Cuirass, Berserker''s Shield, Spear of Desolation, Avenging Blade, Shield Splitter,
    Soul Gem, Void Stone, Void Shield, Heartseeker, The Crusher, Spear of the Magus,
    Runeforged Hammer, The Reaper, Hydra''s Lament, Doom Orb, Erosion, The World Stone,
    Oni Hunter''s Garb, Tekko-Kagi, Eye of Providence, Shield of the Phoenix, Draconic
    Scale, Sundering Echo, Midgardian Mail, Helm of Radiance, Pendulum Blade, Magi''s
    Cloak, Helm of Darkness, Leviathan''s Hide, Dreamer''s Idol, Breastplate of Valor.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.51
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.62
    Stone of Binding:
      total: 0.51
      efficiency: 0.47
      win: 0.55
      pick: 0.0
      fit: 0.68
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.23
      fit: 0.36
    Titan's Bane:
      total: 0.51
      efficiency: 0.51
      win: 0.55
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Nimble Ring, Jotunn''s
    Revenge, Golden Blade, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter,
    Tyrfing, Soul Gem, Pharaoh''s Curse, Toxic Blade, Tekko-Kagi, Silverbranch Bow,
    Runeforged Hammer, Shogun''s Ofuda, Lernaean Bow, Eros'' Bow, Oni Hunter''s Garb,
    Riptalon, Hydra''s Lament, Erosion, Obsidian Shard, Shield of the Phoenix, Eye
    of Providence, Helm of Radiance, Stone of Binding, Draconic Scale, Midgardian
    Mail, Spear of Desolation, Screeching Gargoyle, Sundering Echo, The Reaper, Titan''s
    Bane, Magi''s Cloak, Leviathan''s Hide, Dominance, Helm of Darkness, Breastplate
    of Valor.'
  slot_scores:
    Golden Blade:
      total: 0.5
      efficiency: 0.49
      win: 0.55
      pick: 0.0
      fit: 0.55
    Berserker's Shield:
      total: 0.56
      efficiency: 0.7
      win: 0.55
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.51
      efficiency: 0.61
      win: 0.55
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.52
      efficiency: 0.55
      win: 0.6
      pick: 0.23
      fit: 0.31
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Prophetic Cloak
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Spear of Desolation
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Prophetic Cloak, Spear of Desolation, Shield of the Phoenix, Kinetic
    Cuirass, Berserker''s Shield, Hydra''s Lament, Soul Gem, Screeching Gargoyle,
    Breastplate of Valor, Shield Splitter, Chronos'' Pendant, Arondight, Gladiator''s
    Shield, Gluttonous Grimoire, Erosion, Runeforged Hammer, Helm of Radiance, Oni
    Hunter''s Garb, Heartwood Charm, Obsidian Shard, Gem of Focus, Eye of Providence,
    Helm of Darkness, Chandra''s Grace, Draconic Scale, Stone of Binding, Midgardian
    Mail, Sundering Echo, Magi''s Cloak, Glorious Pridwen, Leviathan''s Hide, Regrowth
    Striders, Eye of Erebus, Mantle Of Discord, Titan''s Bane, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.47
    Prophetic Cloak:
      total: 0.52
      efficiency: 0.42
      win: 0.6
      pick: 0.11
      fit: 0.63
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.23
      fit: 0.63
    Spear of Desolation:
      total: 0.51
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Kinetic Cuirass, Tekko-Kagi, Titan''s
    Bane, Runeforged Hammer, Golden Blade, Hydra''s Lament, Gluttonous Grimoire, Obsidian
    Shard, Spear of Desolation, Sundering Echo, Heartseeker, Tyrfing, The Crusher,
    Soul Gem, Lernaean Bow, Erosion, Oni Hunter''s Garb, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Avenging Blade, Toxic Blade, The Reaper, Stone
    of Binding, Pharaoh''s Curse, Midgardian Mail, Helm of Radiance, Screeching Gargoyle,
    Wyrmskin Hide, Silverbranch Bow, Arondight, Spear of the Magus, Magi''s Cloak,
    Helm of Darkness, Breastplate of Valor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.22
    Berserker's Shield:
      total: 0.55
      efficiency: 0.7
      win: 0.55
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.47
    Shield Splitter:
      total: 0.51
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Berserker''s Shield, Kinetic Cuirass, Obsidian
    Shard, Shield Splitter, Spear of Desolation, Soul Gem, Sundering Echo, Titan''s
    Bane, Runeforged Hammer, Helm of Radiance, Spear of the Magus, Helm of Darkness,
    Hydra''s Lament, Death Metal, Doom Orb, Erosion, Oni Hunter''s Garb, The World
    Stone, Heartseeker, Eye of Providence, Shield of the Phoenix, Draconic Scale,
    The Crusher, Jade Scepter, Stone of Binding, Chronos'' Pendant, Midgardian Mail,
    Screeching Gargoyle, Magi''s Cloak, Avenging Blade, Leviathan''s Hide, The Reaper,
    Breastplate of Valor, Triton''s Conch, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.22
    Berserker's Shield:
      total: 0.51
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.5
    Freya's Tears:
      total: 0.53
      efficiency: 0.55
      win: 0.6
      pick: 0.23
      fit: 0.36
    Amanita Charm:
      total: 0.52
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
  - Berserker's Shield
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Jotunn''s Revenge, Kinetic
    Cuirass, Shield Splitter, Berserker''s Shield, Breastplate of Valor, Runeforged
    Hammer, Erosion, Eye of Providence, Draconic Scale, Hydra''s Lament, Shield of
    the Phoenix, Oni Hunter''s Garb, Stone of Binding, Midgardian Mail, Gluttonous
    Grimoire, Sundering Echo, Helm of Darkness, Titan''s Bane, Magi''s Cloak, Wyrmskin
    Hide, Screeching Gargoyle, Leviathan''s Hide, Mantle Of Discord, Helm of Radiance,
    Avenging Blade, Spear of Desolation, Obsidian Shard, Ancile, Hide of the Nemean
    Lion, Arondight, Void Stone, Stampede, Soul Gem, Void Shield, Prophetic Cloak,
    Death Metal, Xibalban Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.17
      fit: 0.31
    Berserker's Shield:
      total: 0.52
      efficiency: 0.63
      win: 0.55
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.53
      win: 0.55
      pick: 0.0
      fit: 0.66
    Shield Splitter:
      total: 0.53
      efficiency: 0.54
      win: 0.55
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.55
      pick: 0.0
      fit: 0.56
  community_ordered:
  - Genji's Guard
  starter: *id001
---
