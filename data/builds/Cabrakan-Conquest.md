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
      win_rate: 0.63
  - name: Breastplate of Valor
    pick_rate: 0.15
    win_rate: 0.67
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.74
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.61
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.56
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.65
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.62
  - name: Kinetic Cuirass
    pick_rate: 0.07
    win_rate: 0.65
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
    win_rate: 0.62
  - name: Bumba's Cudgel
    pick_rate: 0.3
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.09
    win_rate: 0.62
  source_url: https://smitebrain.com/gods/cabrakan/
  last_verified: '2026-11-02'
  god_win_rate: 0.570694087403599
  god_matches_won: 222
  god_matches_played: 389
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
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Draconic Scale
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Jotunn''s Revenge, Berserker''s
    Shield, Erosion, Eye of Providence, Shield of the Phoenix, Hydra''s Lament, Oni
    Hunter''s Garb, Stone of Binding, Helm of Darkness, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Gluttonous Grimoire, Sundering Echo, Screeching Gargoyle,
    Titan''s Bane, Wyrmskin Hide, Leviathan''s Hide, Helm of Radiance, Avenging Blade,
    Spear of Desolation, Ancile, Hide of the Nemean Lion, Prophetic Cloak, Obsidian
    Shard, Void Stone, Stampede, Void Shield, Arondight, Xibalban Effigy, Soul Gem,
    Spectral Armor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.67
    Shield Splitter:
      total: 0.58
      efficiency: 0.54
      win: 0.65
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.59
      efficiency: 0.55
      win: 0.69
      pick: 0.22
      fit: 0.52
    Shifter's Shield:
      total: 0.58
      efficiency: 0.44
      win: 0.74
      pick: 0.16
      fit: 0.57
    Draconic Scale:
      total: 0.58
      efficiency: 0.47
      win: 0.71
      pick: 0.18
      fit: 0.57
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.57
  community_ordered:
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Jotunn''s Revenge,
    Berserker''s Shield, Shield Splitter, Soul Gem, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Ethereal Staff, The Reaper, Erosion, Eye of Providence, Hydra''s
    Lament, Oni Hunter''s Garb, Gluttonous Grimoire, Midgardian Mail, Glorious Pridwen,
    Avenging Blade, Wyrmskin Hide, Sundering Echo, Leviathan''s Hide, Regrowth Striders,
    Titan''s Bane, Rod of Asclepius, Stone of Binding, Blood-Bound Book, Sphere of
    Negation, Screeching Gargoyle, Helm of Darkness, Ancile, Spear of Desolation,
    Helm of Radiance, Magi''s Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.66
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.49
      win: 0.65
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.58
      efficiency: 0.55
      win: 0.69
      pick: 0.22
      fit: 0.46
    Shifter's Shield:
      total: 0.58
      efficiency: 0.44
      win: 0.74
      pick: 0.16
      fit: 0.56
    Amanita Charm:
      total: 0.64
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.86
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Shifter's Shield
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Screeching Gargoyle, Gluttonous Grimoire, Titan''s Bane, Berserker''s Shield,
    Obsidian Shard, Shield Splitter, Avenging Blade, Spear of Desolation, Void Stone,
    Void Shield, Soul Gem, Heartseeker, The Crusher, Spear of the Magus, The Reaper,
    Erosion, Hydra''s Lament, Oni Hunter''s Garb, Doom Orb, Eye of Providence, The
    World Stone, Shield of the Phoenix, Tekko-Kagi, Sundering Echo, Midgardian Mail,
    Helm of Radiance, Magi''s Cloak, Helm of Darkness, Mantle Of Discord, Leviathan''s
    Hide, Pendulum Blade.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.47
      win: 0.65
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.54
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.69
      pick: 0.22
      fit: 0.38
    Shifter's Shield:
      total: 0.56
      efficiency: 0.44
      win: 0.74
      pick: 0.16
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Golden Blade, Gluttonous Grimoire, Shield Splitter, Tyrfing, Soul
    Gem, Pharaoh''s Curse, Tekko-Kagi, Toxic Blade, Silverbranch Bow, Shogun''s Ofuda,
    Lernaean Bow, Oni Hunter''s Garb, Erosion, Eros'' Bow, Hydra''s Lament, Riptalon,
    Eye of Providence, Stone of Binding, Shield of the Phoenix, Obsidian Shard, Helm
    of Radiance, Midgardian Mail, Screeching Gargoyle, Magi''s Cloak, Spear of Desolation,
    Sundering Echo, The Reaper, Helm of Darkness, Titan''s Bane, Leviathan''s Hide,
    Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.49
      win: 0.65
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.6
      efficiency: 0.7
      win: 0.65
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.47
    Nimble Ring:
      total: 0.55
      efficiency: 0.61
      win: 0.65
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.56
      efficiency: 0.55
      win: 0.69
      pick: 0.22
      fit: 0.33
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.65
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Shield of the Phoenix, Berserker''s Shield, Spear of Desolation,
    Screeching Gargoyle, Hydra''s Lament, Soul Gem, Shield Splitter, Chronos'' Pendant,
    Prophetic Cloak, Erosion, Gladiator''s Shield, Arondight, Gluttonous Grimoire,
    Eye of Providence, Helm of Radiance, Helm of Darkness, Oni Hunter''s Garb, Obsidian
    Shard, Stone of Binding, Heartwood Charm, Gem of Focus, Chandra''s Grace, Midgardian
    Mail, Magi''s Cloak, Sundering Echo, Glorious Pridwen, Mantle Of Discord, Leviathan''s
    Hide, Regrowth Striders, Eye of Erebus, Ancile, Titan''s Bane.'
  slot_scores:
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.48
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.23
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.55
    Freya's Tears:
      total: 0.61
      efficiency: 0.55
      win: 0.69
      pick: 0.22
      fit: 0.64
    Amanita Charm:
      total: 0.58
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
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
    win/pick). Underrated for this god: Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Tekko-Kagi, Titan''s Bane, Golden Blade,
    Hydra''s Lament, Gluttonous Grimoire, Obsidian Shard, Spear of Desolation, Sundering
    Echo, Erosion, Heartseeker, Tyrfing, Oni Hunter''s Garb, The Crusher, Soul Gem,
    Eye of Providence, Lernaean Bow, Stone of Binding, Shield of the Phoenix, Toxic
    Blade, Avenging Blade, Pharaoh''s Curse, Midgardian Mail, The Reaper, Helm of
    Radiance, Magi''s Cloak, Screeching Gargoyle, Helm of Darkness, Wyrmskin Hide,
    Silverbranch Bow, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.7
      win: 0.65
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.52
    Shield Splitter:
      total: 0.56
      efficiency: 0.54
      win: 0.65
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.69
      pick: 0.22
      fit: 0.38
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Breastplate of Valor
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Berserker''s Shield, Shield Splitter, Obsidian
    Shard, Spear of Desolation, Soul Gem, Sundering Echo, Helm of Radiance, Titan''s
    Bane, Helm of Darkness, Spear of the Magus, Hydra''s Lament, Erosion, Oni Hunter''s
    Garb, Death Metal, Eye of Providence, Doom Orb, Stone of Binding, Shield of the
    Phoenix, The World Stone, Heartseeker, Midgardian Mail, The Crusher, Screeching
    Gargoyle, Magi''s Cloak, Jade Scepter, Chronos'' Pendant, Mantle Of Discord, Leviathan''s
    Hide, Avenging Blade, The Reaper, Triton''s Conch.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.61
      win: 0.67
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.55
      win: 0.69
      pick: 0.22
      fit: 0.38
    Shifter's Shield:
      total: 0.56
      efficiency: 0.44
      win: 0.74
      pick: 0.16
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Genji's Guard
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Shield Splitter, Jotunn''s
    Revenge, Berserker''s Shield, Erosion, Eye of Providence, Shield of the Phoenix,
    Hydra''s Lament, Oni Hunter''s Garb, Stone of Binding, Helm of Darkness, Magi''s
    Cloak, Midgardian Mail, Mantle Of Discord, Gluttonous Grimoire, Sundering Echo,
    Screeching Gargoyle, Titan''s Bane, Wyrmskin Hide, Leviathan''s Hide, Helm of
    Radiance, Avenging Blade, Spear of Desolation, Ancile, Hide of the Nemean Lion,
    Prophetic Cloak, Obsidian Shard, Void Stone, Stampede, Void Shield, Arondight,
    Xibalban Effigy, Soul Gem, Spectral Armor.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.63
      win: 0.65
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.61
      pick: 0.23
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.53
      win: 0.65
      pick: 0.15
      fit: 0.67
    Shield Splitter:
      total: 0.58
      efficiency: 0.54
      win: 0.65
      pick: 0.0
      fit: 0.63
    Amanita Charm:
      total: 0.6
      efficiency: 0.62
      win: 0.65
      pick: 0.0
      fit: 0.57
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
---
