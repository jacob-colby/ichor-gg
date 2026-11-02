---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.27
  aspect_win_rate: 0.48
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.27
    win_rate: 0.63
    alternates:
    - name: Stampede
      pick_rate: 0.17
      win_rate: 0.54
    - name: Mystical Mail
      pick_rate: 0.13
      win_rate: 0.54
  - name: Stampede
    pick_rate: 0.19
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.65
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.64
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.54
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.57
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.66
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.65
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.66
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.59
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.62
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.61
    - name: Engraved Guard
      pick_rate: 0.06
      win_rate: 0.74
  community_starters:
  - name: Selflessness
    pick_rate: 0.24
    win_rate: 0.56
  - name: Heroism
    pick_rate: 0.18
    win_rate: 0.66
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-11-02'
  god_win_rate: 0.5472
  god_matches_won: 342
  god_matches_played: 625
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
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield Splitter
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Draconic Scale, Berserker''s
    Shield, Shield Splitter, Breastplate of Valor, Erosion, Jotunn''s Revenge, Eye
    of Providence, Shield of the Phoenix, Shifter''s Shield, Oni Hunter''s Garb, Stone
    of Binding, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Mantle Of Discord,
    Screeching Gargoyle, Leviathan''s Hide, Gluttonous Grimoire, Prophetic Cloak,
    Helm of Radiance, Runeforged Hammer, Ancile, Spear of Desolation, Hide of the
    Nemean Lion, Void Stone, Void Shield, Xibalban Effigy, Gladiator''s Shield, Soul
    Gem, Obsidian Shard, Hydra''s Lament, Hussar''s Wings, Spectral Armor, Brawler’s
    Beat Stick, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.38
    Berserker's Shield:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.77
    Shield Splitter:
      total: 0.55
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.54
    Draconic Scale:
      total: 0.56
      efficiency: 0.47
      win: 0.65
      pick: 0.11
      fit: 0.67
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Berserker''s Shield, Draconic Scale, Soul Gem, Phoenix Feather, Jotunn''s Revenge,
    Erosion, Breastplate of Valor, Chandra''s Grace, Yogi''s Necklace, Eye of Providence,
    Ethereal Staff, Shield Splitter, Oni Hunter''s Garb, Glorious Pridwen, Shifter''s
    Shield, Gluttonous Grimoire, Midgardian Mail, Leviathan''s Hide, Regrowth Striders,
    Runeforged Hammer, Stone of Binding, Rod of Asclepius, Helm of Darkness, Screeching
    Gargoyle, Ancile, Hide of the Nemean Lion, Spear of Desolation, Magi''s Cloak,
    Sphere of Negation, Void Stone, Void Shield, Gladiator''s Shield, Helm of Radiance,
    Mantle Of Discord, Blood-Bound Book.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.35
    Berserker's Shield:
      total: 0.57
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.9
    Draconic Scale:
      total: 0.56
      efficiency: 0.47
      win: 0.65
      pick: 0.11
      fit: 0.65
    Amanita Charm:
      total: 0.64
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Genji's Guard
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Screeching Gargoyle, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation,
    Berserker''s Shield, Obsidian Shard, Soul Gem, Void Stone, Void Shield, Draconic
    Scale, Breastplate of Valor, Titan''s Bane, Shield Splitter, Spear of the Magus,
    Avenging Blade, Erosion, Eye of Providence, Doom Orb, Oni Hunter''s Garb, Shield
    of the Phoenix, The World Stone, Heartseeker, The Crusher, Midgardian Mail, Helm
    of Darkness, Magi''s Cloak, Shifter''s Shield, Helm of Radiance, Mantle Of Discord,
    Runeforged Hammer, The Reaper, Leviathan''s Hide, Dreamer''s Idol, Hydra''s Lament,
    Ancile, Hide of the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.55
      efficiency: 0.47
      win: 0.61
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.27
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Shield Splitter, Draconic Scale, Tyrfing, Soul Gem, Pharaoh''s Curse, Tekko-Kagi,
    Toxic Blade, Runeforged Hammer, Silverbranch Bow, Shogun''s Ofuda, Lernaean Bow,
    Oni Hunter''s Garb, Erosion, Hydra''s Lament, Eros'' Bow, Riptalon, Shield of
    the Phoenix, Eye of Providence, Stone of Binding, Obsidian Shard, Helm of Radiance,
    Screeching Gargoyle, Midgardian Mail, Spear of Desolation, Magi''s Cloak, Sundering
    Echo, The Reaper, Helm of Darkness, Titan''s Bane, Leviathan''s Hide, Mantle Of
    Discord.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.49
      win: 0.61
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.21
    Berserker's Shield:
      total: 0.59
      efficiency: 0.7
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.53
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.55
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Berserker''s
    Shield, Spear of Desolation, Screeching Gargoyle, Hydra''s Lament, Soul Gem, Draconic
    Scale, Shield Splitter, Chronos'' Pendant, Prophetic Cloak, Erosion, Gladiator''s
    Shield, Arondight, Gluttonous Grimoire, Eye of Providence, Helm of Radiance, Helm
    of Darkness, Oni Hunter''s Garb, Runeforged Hammer, Obsidian Shard, Stone of Binding,
    Heartwood Charm, Gem of Focus, Chandra''s Grace, Midgardian Mail, Magi''s Cloak,
    Sundering Echo, Shifter''s Shield, Glorious Pridwen, Mantle Of Discord, Leviathan''s
    Hide, Regrowth Striders, Eye of Erebus, Ancile, Titan''s Bane.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.61
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.22
      fit: 0.64
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.56
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Shield Splitter
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Breastplate of Valor, Erosion, Jotunn''s Revenge, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Shifter''s Shield, Oni Hunter''s
    Garb, Stone of Binding, Helm of Darkness, Magi''s Cloak, Midgardian Mail, Mantle
    Of Discord, Screeching Gargoyle, Leviathan''s Hide, Gluttonous Grimoire, Prophetic
    Cloak, Helm of Radiance, Runeforged Hammer, Ancile, Spear of Desolation, Hide
    of the Nemean Lion, Void Stone, Void Shield, Xibalban Effigy, Gladiator''s Shield,
    Soul Gem, Obsidian Shard, Hydra''s Lament, Hussar''s Wings, Spectral Armor, Brawler’s
    Beat Stick, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.38
    Berserker's Shield:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.22
      fit: 0.62
    Shield Splitter:
      total: 0.55
      efficiency: 0.54
      win: 0.61
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Gauntlet of Thebes
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Gauntlet of Thebes
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Berserker''s Shield, Shield Splitter, Breastplate of Valor, Erosion,
    Jotunn''s Revenge, Eye of Providence, Draconic Scale, Shield of the Phoenix, Shifter''s
    Shield, Oni Hunter''s Garb, Stone of Binding, Helm of Darkness, Magi''s Cloak,
    Midgardian Mail, Mantle Of Discord, Screeching Gargoyle, Leviathan''s Hide, Gluttonous
    Grimoire, Prophetic Cloak, Helm of Radiance, Runeforged Hammer, Ancile, Spear
    of Desolation, Hide of the Nemean Lion, Void Stone, Void Shield, Xibalban Effigy,
    Gladiator''s Shield, Soul Gem, Obsidian Shard, Hydra''s Lament, Hussar''s Wings,
    Spectral Armor, Brawler’s Beat Stick, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Gauntlet of Thebes:
      total: 0.41
      efficiency: 0.23
      win: 0.63
      pick: 0.27
      fit: 0.19
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.61
      pick: 0.2
      fit: 0.38
    Berserker's Shield:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.54
      efficiency: 0.55
      win: 0.54
      pick: 0.22
      fit: 0.62
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.59
      efficiency: 0.62
      win: 0.61
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Gauntlet of Thebes
  - Genji's Guard
  - Freya's Tears
  swaps:
  - added: Gauntlet of Thebes
    removed: Shield Splitter
    reason: community 63% win over 169 matches (vs 55% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
