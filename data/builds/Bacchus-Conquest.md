---
type: smite-build
god: Bacchus
mode: Conquest
builds:
- source: community
  aspect: Aspect of Revelry
  aspect_pick_rate: 0.6
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
      pick_rate: 0.1
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
      win_rate: 0.54
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
      win_rate: 0.66
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
  last_verified: '2026-11-04'
  god_win_rate: 0.5613249776186213
  god_matches_won: 627
  god_matches_played: 1117
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
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Draconic Scale, Shield
    Splitter, Shield of the Phoenix, Gluttonous Grimoire, Breastplate of Valor, Erosion,
    Eye of Providence, Soul Gem, Shifter''s Shield, Oni Hunter''s Garb, Jotunn''s
    Revenge, Hide of the Nemean Lion, Stone of Binding, Midgardian Mail, Helm of Darkness,
    Screeching Gargoyle, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Spear
    of Desolation, Helm of Radiance, Gladiator''s Shield, Runeforged Hammer, Ancile,
    Prophetic Cloak, Blood-Bound Book, Void Stone, Phoenix Feather, Void Shield, Spectral
    Armor, Hydra''s Lament, The Reaper, Doublet of Binding, Hussar''s Wings, Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.42
      fit: 0.39
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.71
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.55
    Draconic Scale:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
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
  - Shield of the Phoenix
  - Freya's Tears
  - Amanita Charm
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
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Soul Gem, Rod of Tahuti, Genji''s
    Guard, Phoenix Feather, Gluttonous Grimoire, Blood-Bound Book, The Reaper, Draconic
    Scale, Yogi''s Necklace, Ethereal Staff, Oni Hunter''s Garb, Erosion, Chandra''s
    Grace, Breastplate of Valor, Eye of Providence, Shield Splitter, Jotunn''s Revenge,
    Shifter''s Shield, Hide of the Nemean Lion, Midgardian Mail, Bancroft''s Talon,
    Regrowth Striders, Glorious Pridwen, Leviathan''s Hide, Runeforged Hammer, Spear
    of Desolation, Screeching Gargoyle, Gladiator''s Shield, Ancile, Stone of Binding,
    Helm of Darkness, Void Stone, Helm of Radiance, Sphere of Negation, Magi''s Cloak,
    Stampede.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.3
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.42
      fit: 0.41
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.69
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.57
      win: 0.57
      pick: 0.0
      fit: 0.83
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.49
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.89
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s
    Revenge, Genji''s Guard, Screeching Gargoyle, Stone of Binding, Spear of Desolation,
    Void Stone, Void Shield, The Reaper, Breastplate of Valor, Shield Splitter, Obsidian
    Shard, Shield of the Phoenix, Draconic Scale, Avenging Blade, Oni Hunter''s Garb,
    Spear of the Magus, The Crusher, Erosion, Eye of Providence, Hide of the Nemean
    Lion, Dreamer''s Idol, Heartseeker, Shifter''s Shield, Midgardian Mail, Titan''s
    Bane, Helm of Radiance, Leviathan''s Hide, Doom Orb, Runeforged Hammer, Magi''s
    Cloak, Blood-Bound Book, Mantle Of Discord, Helm of Darkness, The World Stone.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.24
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.42
      fit: 0.28
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.54
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.4
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
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
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Genji''s Guard, Tyrfing, Jotunn''s Revenge,
    Golden Blade, Shield Splitter, Gluttonous Grimoire, Breastplate of Valor, Soul
    Gem, Shield of the Phoenix, Nimble Ring, Oni Hunter''s Garb, Draconic Scale, Runeforged
    Hammer, Shogun''s Ofuda, Hide of the Nemean Lion, Pharaoh''s Curse, Erosion, Hydra''s
    Lament, Eye of Providence, Spear of Desolation, Toxic Blade, Bragi''s Harp, Screeching
    Gargoyle, Shifter''s Shield, Midgardian Mail, The Reaper, Blood-Bound Book, Helm
    of Radiance, Stone of Binding, Lernaean Bow, Dominance, Leviathan''s Hide, Silverbranch
    Bow, Magi''s Cloak, Mantle Of Discord, Helm of Darkness.'
  slot_scores:
    Golden Blade:
      total: 0.52
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.54
    Berserker's Shield:
      total: 0.63
      efficiency: 0.72
      win: 0.64
      pick: 0.42
      fit: 0.43
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.47
    Tyrfing:
      total: 0.53
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.68
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
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Amanita
    Charm, Soul Gem, Jotunn''s Revenge, Breastplate of Valor, Shield of the Phoenix,
    Spear of Desolation, Screeching Gargoyle, Hydra''s Lament, Gluttonous Grimoire,
    Shield Splitter, Chronos'' Pendant, Gladiator''s Shield, Draconic Scale, Oni Hunter''s
    Garb, Prophetic Cloak, Arondight, Erosion, Eye of Providence, Hide of the Nemean
    Lion, Helm of Radiance, Runeforged Hammer, Blood-Bound Book, Shifter''s Shield,
    Gem of Focus, Heartwood Charm, Helm of Darkness, Midgardian Mail, Chandra''s Grace,
    Stone of Binding, Leviathan''s Hide, Regrowth Striders, Ancient Signet, Magi''s
    Cloak, Mantle Of Discord, The Reaper, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.45
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.42
      fit: 0.27
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.52
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.6
    Soul Gem:
      total: 0.55
      efficiency: 0.58
      win: 0.57
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge,
    Genji''s Guard, Shield Splitter, Gluttonous Grimoire, Soul Gem, The Reaper, Tyrfing,
    Runeforged Hammer, Breastplate of Valor, Hydra''s Lament, Golden Blade, Spear
    of Desolation, Shield of the Phoenix, The Crusher, Oni Hunter''s Garb, Draconic
    Scale, Heartseeker, Erosion, Eye of Providence, Tekko-Kagi, Titan''s Bane, Death
    Metal, Shifter''s Shield, Midgardian Mail, Screeching Gargoyle, Bragi''s Harp,
    Stone of Binding, Helm of Radiance, Blood-Bound Book, Obsidian Shard, Avenging
    Blade, Leviathan''s Hide, Arondight, Magi''s Cloak, Mantle Of Discord, Nimble
    Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.21
    Berserker's Shield:
      total: 0.61
      efficiency: 0.72
      win: 0.64
      pick: 0.42
      fit: 0.33
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.49
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.35
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
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
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Gluttonous
    Grimoire, Soul Gem, Jotunn''s Revenge, Genji''s Guard, Shield Splitter, Spear
    of Desolation, The Reaper, Breastplate of Valor, Helm of Radiance, Blood-Bound
    Book, Runeforged Hammer, Shield of the Phoenix, Obsidian Shard, Death Metal, Oni
    Hunter''s Garb, Draconic Scale, Helm of Darkness, Hydra''s Lament, Spear of the
    Magus, Ancient Signet, The Crusher, Erosion, Eye of Providence, Polynomicon, Heartseeker,
    Dreamer''s Idol, Chronos'' Pendant, Shifter''s Shield, Midgardian Mail, Screeching
    Gargoyle, Stone of Binding, Jade Scepter, Tyrfing, Titan''s Bane, Leviathan''s
    Hide, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.21
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.64
      pick: 0.42
      fit: 0.25
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.49
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.35
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
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
  - Freya's Tears
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
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s Guard, Draconic
    Scale, Shield Splitter, Shield of the Phoenix, Gluttonous Grimoire, Breastplate
    of Valor, Erosion, Eye of Providence, Soul Gem, Shifter''s Shield, Oni Hunter''s
    Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail, Helm of Darkness,
    Screeching Gargoyle, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Hide
    of the Nemean Lion, Spear of Desolation, Helm of Radiance, Gladiator''s Shield,
    Runeforged Hammer, Ancile, Prophetic Cloak, Blood-Bound Book, Void Stone, Phoenix
    Feather, Stampede, Void Shield, Spectral Armor, Hydra''s Lament, The Reaper, Doublet
    of Binding, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.42
      fit: 0.39
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.71
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.55
    Draconic Scale:
      total: 0.54
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.61
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
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
  - Berserker's Shield
  - Devourer's Gauntlet
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Genji''s
    Guard, Draconic Scale, Shield Splitter, Shield of the Phoenix, Gluttonous Grimoire,
    Breastplate of Valor, Erosion, Eye of Providence, Soul Gem, Shifter''s Shield,
    Oni Hunter''s Garb, Jotunn''s Revenge, Stone of Binding, Midgardian Mail, Helm
    of Darkness, Screeching Gargoyle, Magi''s Cloak, Mantle Of Discord, Leviathan''s
    Hide, Hide of the Nemean Lion, Spear of Desolation, Helm of Radiance, Gladiator''s
    Shield, Runeforged Hammer, Ancile, Prophetic Cloak, Blood-Bound Book, Void Stone,
    Phoenix Feather, Stampede, Void Shield, Spectral Armor, Hydra''s Lament, The Reaper,
    Doublet of Binding, Hussar''s Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.71
      win: 0.56
      pick: 0.08
      fit: 0.33
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.42
      fit: 0.39
    Devourer's Gauntlet:
      total: 0.47
      efficiency: 0.4
      win: 0.63
      pick: 0.4
      fit: 0.16
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.61
      win: 0.64
      pick: 0.22
      fit: 0.71
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.59
      pick: 0.25
      fit: 0.55
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.82
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
    removed: Draconic Scale
    reason: community 63% win over 447 matches (vs 56% on this god), taking the model's
      weakest slot from Draconic Scale
  starter: *id001
---
