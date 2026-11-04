---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.59
  aspect_win_rate: 0.59
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.4
    win_rate: 0.63
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.16
      win_rate: 0.51
    - name: Stampede
      pick_rate: 0.11
      win_rate: 0.47
  - name: Berserker's Shield
    pick_rate: 0.31
    win_rate: 0.64
    alternates:
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.56
  - name: Kinetic Cuirass
    pick_rate: 0.14
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.56
    - name: Berserker's Shield
      pick_rate: 0.1
      win_rate: 0.55
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.59
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.13
      win_rate: 0.61
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.55
  - name: Hide of the Nemean Lion
    pick_rate: 0.05
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.68
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.65
  - name: Medal of Defense
    pick_rate: 0.07
    win_rate: 0.61
    alternates:
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.54
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.55
  community_starters:
  - name: Hunter's Cowl
    pick_rate: 0.29
    win_rate: 0.65
  - name: Leather Cowl
    pick_rate: 0.18
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.11
    win_rate: 0.4
  source_url: https://smitebrain.com/gods/bacchus/
  last_verified: '2026-11-03'
  god_win_rate: 0.5610412926391383
  god_matches_won: 625
  god_matches_played: 1114
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
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
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
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Shield Splitter, Gluttonous
    Grimoire, Breastplate of Valor, Erosion, Jotunn''s Revenge, Eye of Providence,
    Soul Gem, Draconic Scale, Oni Hunter''s Garb, Shield of the Phoenix, Helm of Darkness,
    Stone of Binding, Shifter''s Shield, Magi''s Cloak, Midgardian Mail, Helm of Radiance,
    Hide of the Nemean Lion, Mantle Of Discord, Runeforged Hammer, Leviathan''s Hide,
    Screeching Gargoyle, Spear of Desolation, Ancile, Prophetic Cloak, Void Stone,
    Hydra''s Lament, Obsidian Shard, Void Shield, Brawler’s Beat Stick, Blood-Bound
    Book, Xibalban Effigy, Spectral Armor, The Reaper, Phoenix Feather, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.39
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.71
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
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
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Phoenix Feather — magical protection
    swap_item: Phoenix Feather
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Shield of the Phoenix, Gluttonous
    Grimoire, Genji''s Guard, Blood-Bound Book, Phoenix Feather, The Reaper, Shield
    Splitter, Jotunn''s Revenge, Yogi''s Necklace, Erosion, Ethereal Staff, Breastplate
    of Valor, Eye of Providence, Oni Hunter''s Garb, Draconic Scale, Chandra''s Grace,
    Runeforged Hammer, Midgardian Mail, Shifter''s Shield, Hide of the Nemean Lion,
    Glorious Pridwen, Leviathan''s Hide, Regrowth Striders, Bancroft''s Talon, Helm
    of Darkness, Helm of Radiance, Stone of Binding, Sphere of Negation, Spear of
    Desolation, Magi''s Cloak, Bloodforge, Ancile, Screeching Gargoyle, Mantle Of
    Discord, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.3
    Berserker's Shield:
      total: 0.6
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.41
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.69
    Freya's Tears:
      total: 0.55
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.89
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.75
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Jotunn''s Revenge, Amanita Charm,
    Soul Gem, Stone of Binding, Screeching Gargoyle, Genji''s Guard, Spear of Desolation,
    Obsidian Shard, Void Stone, Void Shield, The Reaper, Shield Splitter, Avenging
    Blade, Titan''s Bane, Breastplate of Valor, Spear of the Magus, Erosion, Oni Hunter''s
    Garb, Eye of Providence, The Crusher, Doom Orb, Draconic Scale, Helm of Radiance,
    The World Stone, Runeforged Hammer, Shield of the Phoenix, Helm of Darkness, Midgardian
    Mail, Heartseeker, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Dreamer''s
    Idol, Shifter''s Shield, Hydra''s Lament, Blood-Bound Book.'
  slot_scores:
    Stone of Binding:
      total: 0.54
      efficiency: 0.5
      win: 0.57
      pick: 0.0
      fit: 0.72
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.28
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.54
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.66
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Nimble Ring, Jotunn''s
    Revenge, Golden Blade, Shield Splitter, Gluttonous Grimoire, Tyrfing, Breastplate
    of Valor, Soul Gem, Runeforged Hammer, Tekko-Kagi, Pharaoh''s Curse, Lernaean
    Bow, Toxic Blade, Oni Hunter''s Garb, Hydra''s Lament, Shogun''s Ofuda, Silverbranch
    Bow, Helm of Radiance, Erosion, Eye of Providence, Stone of Binding, Obsidian
    Shard, Draconic Scale, Midgardian Mail, Shield of the Phoenix, Spear of Desolation,
    Helm of Darkness, The Reaper, Magi''s Cloak, Screeching Gargoyle, Titan''s Bane,
    Riptalon, Leviathan''s Hide, Dominance, Mantle Of Discord.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.52
      win: 0.57
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.63
      efficiency: 0.74
      win: 0.64
      pick: 0.42
      fit: 0.43
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.47
    Nimble Ring:
      total: 0.52
      efficiency: 0.63
      win: 0.57
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.33
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Amanita Charm
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Genji''s Guard, Jotunn''s
    Revenge, Amanita Charm, Soul Gem, Breastplate of Valor, Spear of Desolation, Gluttonous
    Grimoire, Hydra''s Lament, Shield of the Phoenix, Shield Splitter, Screeching
    Gargoyle, Chronos'' Pendant, Arondight, Helm of Radiance, Prophetic Cloak, Runeforged
    Hammer, Oni Hunter''s Garb, Erosion, Helm of Darkness, Eye of Providence, Obsidian
    Shard, Draconic Scale, Stone of Binding, Gladiator''s Shield, Gem of Focus, Midgardian
    Mail, Heartwood Charm, Magi''s Cloak, Blood-Bound Book, Mantle Of Discord, Leviathan''s
    Hide, Shifter''s Shield, Regrowth Striders, The Reaper, Ancient Signet, Chandra''s
    Grace, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.45
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.27
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.52
    Freya's Tears:
      total: 0.57
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.6
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
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
  - Shield Splitter
  - Freya's Tears
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Shield Splitter, Gluttonous Grimoire, Genji''s Guard, Soul Gem, Runeforged
    Hammer, The Reaper, Tekko-Kagi, Titan''s Bane, Golden Blade, Breastplate of Valor,
    Hydra''s Lament, Nimble Ring, Obsidian Shard, Spear of Desolation, Tyrfing, The
    Crusher, Oni Hunter''s Garb, Lernaean Bow, Erosion, Avenging Blade, Helm of Radiance,
    Eye of Providence, Heartseeker, Stone of Binding, Draconic Scale, Shield of the
    Phoenix, Midgardian Mail, Arondight, Toxic Blade, Helm of Darkness, Magi''s Cloak,
    Spear of the Magus, Death Metal, Screeching Gargoyle, Pharaoh''s Curse.'
  slot_scores:
    Berserker's Shield:
      total: 0.62
      efficiency: 0.74
      win: 0.64
      pick: 0.42
      fit: 0.33
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.49
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.35
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Gluttonous Grimoire
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, Amanita Charm, Soul Gem, Shield Splitter, Genji''s Guard, Obsidian
    Shard, Spear of Desolation, Helm of Radiance, Runeforged Hammer, Breastplate of
    Valor, The Reaper, Titan''s Bane, Helm of Darkness, Spear of the Magus, Hydra''s
    Lament, Blood-Bound Book, Death Metal, Oni Hunter''s Garb, Ancient Signet, Erosion,
    Eye of Providence, The Crusher, Doom Orb, Jade Scepter, Stone of Binding, Draconic
    Scale, Shield of the Phoenix, Midgardian Mail, Avenging Blade, The World Stone,
    Magi''s Cloak, Chronos'' Pendant, Heartseeker, Screeching Gargoyle, Leviathan''s
    Hide, Mantle Of Discord.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.25
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.67
      win: 0.57
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.49
    Shield Splitter:
      total: 0.53
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.53
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.35
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.58
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
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
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Shield
    Splitter, Gluttonous Grimoire, Breastplate of Valor, Erosion, Jotunn''s Revenge,
    Eye of Providence, Soul Gem, Draconic Scale, Oni Hunter''s Garb, Shield of the
    Phoenix, Helm of Darkness, Stone of Binding, Shifter''s Shield, Magi''s Cloak,
    Midgardian Mail, Helm of Radiance, Mantle Of Discord, Runeforged Hammer, Leviathan''s
    Hide, Screeching Gargoyle, Spear of Desolation, Ancile, Prophetic Cloak, Hide
    of the Nemean Lion, Stampede, Void Stone, Hydra''s Lament, Obsidian Shard, Void
    Shield, Brawler’s Beat Stick, Blood-Bound Book, Xibalban Effigy, Spectral Armor,
    The Reaper, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.39
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.71
    Shield Splitter:
      total: 0.54
      efficiency: 0.59
      win: 0.57
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.55
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Devourer's Gauntlet
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  flex_slots:
  - Freya's Tears
  - Devourer's Gauntlet
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s
    Guard, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor, Erosion, Jotunn''s
    Revenge, Eye of Providence, Soul Gem, Draconic Scale, Oni Hunter''s Garb, Shield
    of the Phoenix, Helm of Darkness, Stone of Binding, Shifter''s Shield, Magi''s
    Cloak, Midgardian Mail, Helm of Radiance, Mantle Of Discord, Runeforged Hammer,
    Leviathan''s Hide, Screeching Gargoyle, Spear of Desolation, Ancile, Prophetic
    Cloak, Hide of the Nemean Lion, Stampede, Void Stone, Hydra''s Lament, Obsidian
    Shard, Void Shield, Brawler’s Beat Stick, Blood-Bound Book, Xibalban Effigy, Spectral
    Armor, The Reaper, Phoenix Feather.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.56
      pick: 0.08
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.67
      win: 0.64
      pick: 0.42
      fit: 0.39
    Devourer's Gauntlet:
      total: 0.44
      efficiency: 0.33
      win: 0.63
      pick: 0.4
      fit: 0.16
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.64
      pick: 0.22
      fit: 0.71
    Freya's Tears:
      total: 0.56
      efficiency: 0.58
      win: 0.59
      pick: 0.25
      fit: 0.55
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.57
      pick: 0.0
      fit: 0.11
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Devourer's Gauntlet
  - Kinetic Cuirass
  - Freya's Tears
  swaps:
  - added: Devourer's Gauntlet
    removed: Shield Splitter
    reason: community 63% win over 446 matches (vs 56% on this god), taking the model's
      weakest slot from Shield Splitter
  starter: *id001
---
