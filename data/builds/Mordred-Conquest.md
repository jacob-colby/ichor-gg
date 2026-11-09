---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.8
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.23
    win_rate: 0.62
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.2
      win_rate: 0.59
    - name: Bragi's Harp
      pick_rate: 0.14
      win_rate: 0.61
  - name: Genji's Guard
    pick_rate: 0.09
    win_rate: 0.72
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.53
    - name: Typhon’s Heart
      pick_rate: 0.09
      win_rate: 0.47
  - name: Nimble Ring
    pick_rate: 0.11
    win_rate: 0.59
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.7
    - name: Bracer of The Abyss
      pick_rate: 0.1
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.13
    win_rate: 0.52
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.08
      win_rate: 0.8
    - name: Magi's Cloak
      pick_rate: 0.08
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.08
    win_rate: 0.64
    alternates:
    - name: Contagion
      pick_rate: 0.06
      win_rate: 0.5
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.8
  - name: Shell of Rebuke
    pick_rate: 0.06
    win_rate: 0.83
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.67
    - name: Evil Eye
      pick_rate: 0.04
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.7
  - name: Hunter's Cowl
    pick_rate: 0.26
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.19
    win_rate: 0.53
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-11-08'
  god_win_rate: 0.6180904522613065
  god_matches_won: 123
  god_matches_played: 199
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-08'
  god_matches_analyzed: 5119
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Genji''s Guard, Amanita Charm, Jotunn''s Revenge, Shield
    Splitter, Gluttonous Grimoire, Berserker''s Shield, Soul Gem, Magi''s Cloak, Breastplate
    of Valor, The Reaper, Shield of the Phoenix, Draconic Scale, Runeforged Hammer,
    Oni Hunter''s Garb, Spear of Desolation, Erosion, Eye of Providence, Hydra''s
    Lament, The Crusher, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Heartseeker, Helm of Radiance, Mantle Of Discord, Helm of Darkness, Blood-Bound
    Book, Death Metal, Titan''s Bane, Obsidian Shard, Ancile, Avenging Blade, Wyrmskin
    Hide, Tyrfing, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.57
    Shield Splitter:
      total: 0.56
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.51
    Shell of Rebuke:
      total: 0.57
      efficiency: 0.41
      win: 0.83
      pick: 0.18
      fit: 0.34
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Kinetic
    Cuirass, Genji''s Guard, Jotunn''s Revenge, Amanita Charm, Soul Gem, Gluttonous
    Grimoire, Spear of Desolation, Shield Splitter, Berserker''s Shield, Breastplate
    of Valor, Hydra''s Lament, The Reaper, Ancient Signet, Oni Hunter''s Garb, Blood-Bound
    Book, Death Metal, Helm of Radiance, Runeforged Hammer, Shield of the Phoenix,
    Polynomicon, Obsidian Shard, Heartseeker, Helm of Darkness, Spear of the Magus,
    Draconic Scale, Chronos'' Pendant, The Crusher, Screeching Gargoyle, Erosion,
    Dreamer''s Idol, Doom Orb, Eye of Providence, Jade Scepter, Bancroft''s Talon,
    Midgardian Mail, Soul Reaver, Heartwood Charm, Stone of Binding.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.61
      pick: 0.0
      fit: 0.23
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.27
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.44
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.61
      pick: 0.0
      fit: 0.23
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.64
      pick: 0.17
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Spear of Desolation
  - Soul Gem
  flex_slots:
  - Shell of Rebuke
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Kinetic Cuirass, Genji''s Guard, Soul Gem, Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Spear of Desolation, Berserker''s Shield, Breastplate of
    Valor, Shield Splitter, The Reaper, Shield of the Phoenix, Obsidian Shard, Hydra''s
    Lament, Spear of the Magus, Blood-Bound Book, Oni Hunter''s Garb, Helm of Radiance,
    Runeforged Hammer, The Crusher, Draconic Scale, Screeching Gargoyle, Heartseeker,
    Dreamer''s Idol, Death Metal, Chronos'' Pendant, Helm of Darkness, Ancient Signet,
    Erosion, Eye of Providence, Titan''s Bane, Polynomicon, Midgardian Mail, Doom
    Orb, Stone of Binding, Leviathan''s Hide, Arondight, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.46
    Shell of Rebuke:
      total: 0.56
      efficiency: 0.41
      win: 0.83
      pick: 0.18
      fit: 0.26
    Spear of Desolation:
      total: 0.56
      efficiency: 0.6
      win: 0.61
      pick: 0.0
      fit: 0.45
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Shell of Rebuke
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Genji''s Guard, Soul Gem, The Reaper,
    Shield of the Phoenix, Jotunn''s Revenge, Gluttonous Grimoire, Blood-Bound Book,
    Berserker''s Shield, Shield Splitter, Phoenix Feather, Yogi''s Necklace, Runeforged
    Hammer, Ethereal Staff, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Draconic Scale, Spear of Desolation, Hydra''s Lament, Bancroft''s Talon,
    Erosion, Bloodforge, Eye of Providence, Regrowth Striders, The Crusher, Midgardian
    Mail, Leviathan''s Hide, Heartseeker, Glorious Pridwen, Screeching Gargoyle, Avenging
    Blade, Death Metal, Titan''s Bane, Helm of Radiance, Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.66
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.55
    Shell of Rebuke:
      total: 0.57
      efficiency: 0.41
      win: 0.83
      pick: 0.18
      fit: 0.28
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Kinetic Cuirass, Genji''s Guard, Jotunn''s Revenge, Amanita Charm,
    Gluttonous Grimoire, Soul Gem, Screeching Gargoyle, Stone of Binding, The Reaper,
    Spear of Desolation, Berserker''s Shield, Shield Splitter, Avenging Blade, Void
    Stone, Void Shield, Magi''s Cloak, The Crusher, Breastplate of Valor, Heartseeker,
    Obsidian Shard, Shield of the Phoenix, Titan''s Bane, Runeforged Hammer, Draconic
    Scale, Oni Hunter''s Garb, Spear of the Magus, Hydra''s Lament, Erosion, Eye of
    Providence, Dreamer''s Idol, Midgardian Mail, Blood-Bound Book, Helm of Radiance,
    Leviathan''s Hide, Mantle Of Discord, Doom Orb, Death Metal.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.61
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.21
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.49
    Shell of Rebuke:
      total: 0.57
      efficiency: 0.41
      win: 0.83
      pick: 0.18
      fit: 0.28
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
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
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Genji''s Guard, Berserker''s Shield, Amanita Charm,
    Jotunn''s Revenge, Tyrfing, Gluttonous Grimoire, Soul Gem, Shield Splitter, Golden
    Blade, Breastplate of Valor, Shield of the Phoenix, Spear of Desolation, Oni Hunter''s
    Garb, The Reaper, Draconic Scale, Toxic Blade, Runeforged Hammer, Bragi''s Harp,
    Hydra''s Lament, Shogun''s Ofuda, Erosion, Silverbranch Bow, Pharaoh''s Curse,
    Eye of Providence, Tekko-Kagi, Screeching Gargoyle, Blood-Bound Book, Midgardian
    Mail, Helm of Radiance, Riptalon, Stone of Binding, Lernaean Bow, Leviathan''s
    Hide, Dominance, The Crusher, Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.51
      win: 0.61
      pick: 0.0
      fit: 0.5
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.19
    Berserker's Shield:
      total: 0.59
      efficiency: 0.72
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.44
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.61
      pick: 0.0
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Soul Gem
  flex_slots:
  - Shell of Rebuke
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Genji''s Guard, Soul
    Gem, Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Spear of Desolation,
    Shield of the Phoenix, Gluttonous Grimoire, Berserker''s Shield, Screeching Gargoyle,
    Hydra''s Lament, Magi''s Cloak, Shield Splitter, Chronos'' Pendant, Oni Hunter''s
    Garb, Draconic Scale, Gladiator''s Shield, Prophetic Cloak, The Reaper, Arondight,
    Erosion, Blood-Bound Book, Helm of Radiance, Eye of Providence, Runeforged Hammer,
    Midgardian Mail, Gem of Focus, Obsidian Shard, Heartwood Charm, Helm of Darkness,
    Stone of Binding, Ancient Signet, Chandra''s Grace, Leviathan''s Hide, Mantle
    Of Discord, Regrowth Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.41
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.63
      win: 0.61
      pick: 0.0
      fit: 0.41
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.48
    Shell of Rebuke:
      total: 0.57
      efficiency: 0.41
      win: 0.83
      pick: 0.18
      fit: 0.27
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Shell of Rebuke
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Kinetic Cuirass, Genji''s Guard, Soul Gem,
    Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge, Spear of Desolation, Berserker''s
    Shield, Shield Splitter, Breastplate of Valor, Blood-Bound Book, Helm of Radiance,
    Obsidian Shard, Shield of the Phoenix, The Reaper, Death Metal, Helm of Darkness,
    Ancient Signet, Spear of the Magus, Hydra''s Lament, Runeforged Hammer, Oni Hunter''s
    Garb, Chronos'' Pendant, Draconic Scale, Polynomicon, Dreamer''s Idol, Screeching
    Gargoyle, Erosion, The Crusher, Jade Scepter, Eye of Providence, Midgardian Mail,
    Heartseeker, Doom Orb, Stone of Binding, Ethereal Staff, Leviathan''s Hide, Triton''s
    Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.46
    Shell of Rebuke:
      total: 0.56
      efficiency: 0.41
      win: 0.83
      pick: 0.18
      fit: 0.26
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.82
      win: 0.64
      pick: 0.17
      fit: 0.33
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Genji''s Guard, Amanita
    Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, Shield Splitter, Spear
    of Desolation, Berserker''s Shield, Magi''s Cloak, The Reaper, Breastplate of
    Valor, Blood-Bound Book, Helm of Radiance, Runeforged Hammer, Shield of the Phoenix,
    Obsidian Shard, Death Metal, Oni Hunter''s Garb, Draconic Scale, Helm of Darkness,
    Hydra''s Lament, Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye
    of Providence, Polynomicon, Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Screeching
    Gargoyle, Midgardian Mail, Stone of Binding, Jade Scepter, Titan''s Bane, Leviathan''s
    Hide, Mantle Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.61
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.21
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.65
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.49
    Shield Splitter:
      total: 0.55
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.44
    Shell of Rebuke:
      total: 0.57
      efficiency: 0.41
      win: 0.83
      pick: 0.18
      fit: 0.28
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
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
  - Shield Splitter
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Jotunn''s Revenge, Genji''s
    Guard, Shield Splitter, Gluttonous Grimoire, Berserker''s Shield, Soul Gem, Breastplate
    of Valor, The Reaper, Shield of the Phoenix, Draconic Scale, Runeforged Hammer,
    Oni Hunter''s Garb, Spear of Desolation, Erosion, Eye of Providence, Hydra''s
    Lament, The Crusher, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Heartseeker, Helm of Radiance, Magi''s Cloak, Mantle Of Discord, Helm of
    Darkness, Blood-Bound Book, Death Metal, Titan''s Bane, Obsidian Shard, Ancile,
    Avenging Blade, Wyrmskin Hide, Tyrfing, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.71
      win: 0.72
      pick: 0.12
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.61
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.67
      efficiency: 0.61
      win: 0.8
      pick: 0.13
      fit: 0.57
    Shield Splitter:
      total: 0.56
      efficiency: 0.58
      win: 0.61
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.52
      pick: 0.22
      fit: 0.42
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.61
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
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
  - aspect: Aspect of Rage
    status: below minimum
    matches_by_window:
      ob47: 6
      ob46: 23
      ob45: 45
      ob44: 53
---
