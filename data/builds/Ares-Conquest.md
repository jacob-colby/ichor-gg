---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.28
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
    pick_rate: 0.12
    win_rate: 0.66
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.53
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
      win_rate: 0.57
  - name: Sage's Ring
    pick_rate: 0.08
    win_rate: 0.62
    alternates:
    - name: Medal of Defense
      pick_rate: 0.07
      win_rate: 0.61
    - name: Engraved Guard
      pick_rate: 0.05
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
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-11-03'
  god_win_rate: 0.546031746031746
  god_matches_won: 344
  god_matches_played: 630
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
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
  - Draconic Scale
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
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Berserker''s Shield,
    Draconic Scale, Shield Splitter, Erosion, Breastplate of Valor, Eye of Providence,
    Jotunn''s Revenge, Shield of the Phoenix, Oni Hunter''s Garb, Shifter''s Shield,
    Helm of Darkness, Stone of Binding, Magi''s Cloak, Midgardian Mail, Mantle Of
    Discord, Helm of Radiance, Screeching Gargoyle, Leviathan''s Hide, Runeforged
    Hammer, Gluttonous Grimoire, Prophetic Cloak, Spear of Desolation, Ancile, Hide
    of the Nemean Lion, Void Stone, Hydra''s Lament, Void Shield, Brawler’s Beat Stick,
    Soul Gem, Obsidian Shard, Xibalban Effigy, Gladiator''s Shield, Spectral Armor,
    Hussar''s Wings, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.38
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.77
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.54
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.65
      pick: 0.11
      fit: 0.67
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
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
  - Genji's Guard
  - Draconic Scale
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Kinetic Cuirass,
    Berserker''s Shield, Draconic Scale, Soul Gem, Phoenix Feather, Shield Splitter,
    Jotunn''s Revenge, Erosion, Eye of Providence, Breastplate of Valor, Yogi''s Necklace,
    Ethereal Staff, Oni Hunter''s Garb, Chandra''s Grace, Shifter''s Shield, Midgardian
    Mail, Glorious Pridwen, Runeforged Hammer, Gluttonous Grimoire, Regrowth Striders,
    Leviathan''s Hide, Helm of Darkness, Rod of Asclepius, Stone of Binding, Helm
    of Radiance, Spear of Desolation, Screeching Gargoyle, Ancile, Magi''s Cloak,
    Sphere of Negation, Soul Locket, Hide of the Nemean Lion, Blood-Bound Book, Void
    Stone, Mantle Of Discord, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.35
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.9
    Draconic Scale:
      total: 0.57
      efficiency: 0.5
      win: 0.65
      pick: 0.11
      fit: 0.65
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
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
  - Kinetic Cuirass
  - Screeching Gargoyle
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
    Kinetic Cuirass, Gluttonous Grimoire, Screeching Gargoyle, Spear of Desolation,
    Berserker''s Shield, Obsidian Shard, Soul Gem, Void Stone, Void Shield, Draconic
    Scale, Shield Splitter, Titan''s Bane, Breastplate of Valor, Avenging Blade, Spear
    of the Magus, Erosion, Eye of Providence, Oni Hunter''s Garb, The Crusher, Doom
    Orb, Shield of the Phoenix, The World Stone, Helm of Radiance, Helm of Darkness,
    Heartseeker, Runeforged Hammer, Midgardian Mail, Magi''s Cloak, The Reaper, Shifter''s
    Shield, Mantle Of Discord, Dreamer''s Idol, Leviathan''s Hide, Hydra''s Lament,
    Ancile, Tekko-Kagi.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.56
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.27
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.57
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
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
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Shield Splitter, Gluttonous Grimoire,
    Tyrfing, Breastplate of Valor, Draconic Scale, Soul Gem, Runeforged Hammer, Tekko-Kagi,
    Pharaoh''s Curse, Lernaean Bow, Toxic Blade, Hydra''s Lament, Oni Hunter''s Garb,
    Shogun''s Ofuda, Eros'' Bow, Silverbranch Bow, Helm of Radiance, Erosion, Eye
    of Providence, Stone of Binding, Shield of the Phoenix, Spear of Desolation, Obsidian
    Shard, Midgardian Mail, Screeching Gargoyle, Helm of Darkness, The Reaper, Magi''s
    Cloak, Titan''s Bane, Riptalon, Leviathan''s Hide, Dominance, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.61
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.21
    Berserker's Shield:
      total: 0.6
      efficiency: 0.74
      win: 0.61
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.54
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
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
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Breastplate of Valor, Kinetic Cuirass, Berserker''s Shield, Spear
    of Desolation, Shield of the Phoenix, Hydra''s Lament, Shield Splitter, Screeching
    Gargoyle, Soul Gem, Draconic Scale, Lotus Sickle, Chronos'' Pendant, Arondight,
    Prophetic Cloak, Helm of Radiance, Runeforged Hammer, Erosion, Helm of Darkness,
    Oni Hunter''s Garb, Eye of Providence, Gluttonous Grimoire, Gladiator''s Shield,
    Obsidian Shard, Stone of Binding, Gem of Focus, Midgardian Mail, Heartwood Charm,
    Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Shifter''s Shield, Regrowth
    Striders, Chandra''s Grace, Eye of Erebus, Glorious Pridwen, Ancient Signet, Jade
    Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.48
    Berserker's Shield:
      total: 0.55
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.29
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
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
  - Freya's Tears
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
    Shield, Shield Splitter, Erosion, Breastplate of Valor, Eye of Providence, Jotunn''s
    Revenge, Draconic Scale, Shield of the Phoenix, Oni Hunter''s Garb, Shifter''s
    Shield, Helm of Darkness, Stone of Binding, Magi''s Cloak, Midgardian Mail, Mantle
    Of Discord, Helm of Radiance, Screeching Gargoyle, Leviathan''s Hide, Runeforged
    Hammer, Gluttonous Grimoire, Prophetic Cloak, Spear of Desolation, Ancile, Hide
    of the Nemean Lion, Void Stone, Hydra''s Lament, Void Shield, Brawler’s Beat Stick,
    Soul Gem, Obsidian Shard, Xibalban Effigy, Gladiator''s Shield, Spectral Armor,
    Hussar''s Wings, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.38
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.54
      pick: 0.22
      fit: 0.62
    Shield Splitter:
      total: 0.56
      efficiency: 0.59
      win: 0.61
      pick: 0.0
      fit: 0.54
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
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
  - Freya's Tears
  - Gauntlet of Thebes
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Berserker''s Shield, Shield Splitter, Erosion, Breastplate of Valor,
    Eye of Providence, Jotunn''s Revenge, Draconic Scale, Shield of the Phoenix, Oni
    Hunter''s Garb, Shifter''s Shield, Helm of Darkness, Stone of Binding, Magi''s
    Cloak, Midgardian Mail, Mantle Of Discord, Helm of Radiance, Screeching Gargoyle,
    Leviathan''s Hide, Runeforged Hammer, Gluttonous Grimoire, Prophetic Cloak, Spear
    of Desolation, Ancile, Hide of the Nemean Lion, Void Stone, Hydra''s Lament, Void
    Shield, Brawler’s Beat Stick, Soul Gem, Obsidian Shard, Xibalban Effigy, Gladiator''s
    Shield, Spectral Armor, Hussar''s Wings, Phoenix Feather, Doublet of Binding.'
  slot_scores:
    Gauntlet of Thebes:
      total: 0.41
      efficiency: 0.23
      win: 0.63
      pick: 0.27
      fit: 0.19
    Genji's Guard:
      total: 0.58
      efficiency: 0.69
      win: 0.61
      pick: 0.2
      fit: 0.38
    Berserker's Shield:
      total: 0.57
      efficiency: 0.67
      win: 0.61
      pick: 0.0
      fit: 0.43
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.54
      pick: 0.22
      fit: 0.62
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.61
      pick: 0.0
      fit: 0.77
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
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
    reason: community 63% win over 170 matches (vs 55% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
