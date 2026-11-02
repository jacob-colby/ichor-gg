---
type: smite-build
god: Chaac
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fulmination
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.35
  slot_order:
  - name: Bancroft's Talon
    pick_rate: 0.21
    win_rate: 0.44
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.17
      win_rate: 0.36
    - name: Regrowth Striders
      pick_rate: 0.07
      win_rate: 0.56
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.4
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.35
  - name: Freya's Tears
    pick_rate: 0.21
    win_rate: 0.46
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.44
    - name: Breastplate of Valor
      pick_rate: 0.06
      win_rate: 0.42
  - name: Genji's Guard
    pick_rate: 0.1
    win_rate: 0.57
    alternates:
    - name: Gem of Focus
      pick_rate: 0.1
      win_rate: 0.45
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.4
  - name: Shell of Rebuke
    pick_rate: 0.04
    win_rate: 0.71
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.52
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.5
  - name: Soul Reaver
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Sundering Echo
      pick_rate: 0.05
      win_rate: 0.43
    - name: Engraved Guard
      pick_rate: 0.05
      win_rate: 0.43
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.44
    win_rate: 0.48
  - name: Bluestone Pendant
    pick_rate: 0.29
    win_rate: 0.3
  - name: Bumba's Cudgel
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-11-02'
  god_win_rate: 0.43555555555555553
  god_matches_won: 98
  god_matches_played: 225
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
  - Book of Thoth
  - Jotunn's Revenge
  - Genji's Guard
  - Transcendence
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shell of Rebuke — physical protection
    swap_item: Shell of Rebuke
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Berserker''s
    Shield, Shield Splitter, Gluttonous Grimoire, Obsidian Shard, Spear of Desolation,
    Soul Gem, Runeforged Hammer, Titan''s Bane, Helm of Radiance, Helm of Darkness,
    Erosion, Spear of the Magus, Hydra''s Lament, Eye of Providence, Oni Hunter''s
    Garb, Draconic Scale, Shield of the Phoenix, Stone of Binding, Midgardian Mail,
    Magi''s Cloak, Screeching Gargoyle, Death Metal, Doom Orb, Heartseeker, Mantle
    Of Discord, The World Stone, The Crusher, Leviathan''s Hide, Jade Scepter, Chronos''
    Pendant, Avenging Blade, The Reaper, Wyrmskin Hide, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.48
      win: 0.45
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.24
    Transcendence:
      total: 0.4
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.17
    Freya's Tears:
      total: 0.48
      efficiency: 0.55
      win: 0.46
      pick: 0.33
      fit: 0.4
    Amanita Charm:
      total: 0.48
      efficiency: 0.62
      win: 0.45
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Genji's Guard
  - Transcendence
  - Soul Reaver
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Berserker''s Shield, Shield Splitter,
    Gluttonous Grimoire, Kinetic Cuirass, Obsidian Shard, Spear of Desolation, Soul
    Gem, Hydra''s Lament, Helm of Radiance, Runeforged Hammer, Titan''s Bane, Helm
    of Darkness, Oni Hunter''s Garb, Spear of the Magus, Doom Orb, The World Stone,
    Death Metal, Heartseeker, Erosion, Chronos'' Pendant, Shield of the Phoenix, Screeching
    Gargoyle, Eye of Providence, Stone of Binding, Jade Scepter, Draconic Scale, The
    Crusher, Midgardian Mail, Wish-Granting Pearl, Heartwood Charm, Ancient Signet,
    Magi''s Cloak, Polynomicon, Avenging Blade, Arondight.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.48
      win: 0.45
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.29
    Transcendence:
      total: 0.41
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.25
    Soul Reaver:
      total: 0.48
      efficiency: 0.39
      win: 0.6
      pick: 0.22
      fit: 0.45
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.81
      win: 0.45
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Soul Reaver
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Genji's Guard
  - Transcendence
  - Freya's Tears
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Spear of Desolation, Gluttonous
    Grimoire, Soul Gem, Obsidian Shard, Berserker''s Shield, Kinetic Cuirass, Shield
    Splitter, Titan''s Bane, Spear of the Magus, Hydra''s Lament, Helm of Radiance,
    Runeforged Hammer, Helm of Darkness, Shield of the Phoenix, Doom Orb, Screeching
    Gargoyle, The World Stone, Heartseeker, Erosion, Oni Hunter''s Garb, The Crusher,
    Chronos'' Pendant, Eye of Providence, Draconic Scale, Stone of Binding, Midgardian
    Mail, The Reaper, Magi''s Cloak, Death Metal, Leviathan''s Hide, Mantle Of Discord,
    Dreamer''s Idol, Arondight, Jade Scepter, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.48
      win: 0.45
      pick: 0.0
      fit: 0.14
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.27
    Transcendence:
      total: 0.39
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.14
    Freya's Tears:
      total: 0.48
      efficiency: 0.55
      win: 0.46
      pick: 0.33
      fit: 0.41
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.81
      win: 0.45
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Transcendence
  - Genji's Guard
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Soul Gem, Jotunn''s Revenge, Regrowth
    Striders, Shield of the Phoenix, Gluttonous Grimoire, Berserker''s Shield, Kinetic
    Cuirass, Ethereal Staff, The Reaper, Obsidian Shard, Shield Splitter, Spear of
    Desolation, Yogi''s Necklace, Phoenix Feather, Runeforged Hammer, Blood-Bound
    Book, Titan''s Bane, Chandra''s Grace, Rod of Asclepius, Sphere of Negation, Helm
    of Radiance, Spear of the Magus, Hydra''s Lament, Oni Hunter''s Garb, Erosion,
    Helm of Darkness, Eye of Providence, Draconic Scale, Midgardian Mail, Death Metal,
    Doom Orb, Jade Scepter, Heartseeker, Glorious Pridwen, The Crusher, The World
    Stone.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.48
      win: 0.45
      pick: 0.0
      fit: 0.16
    Transcendence:
      total: 0.4
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.17
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.22
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.81
      win: 0.45
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.53
      efficiency: 0.62
      win: 0.45
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.49
      efficiency: 0.5
      win: 0.45
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Genji's Guard
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Obsidian Shard, Stone of Binding, Spear of Desolation, Screeching Gargoyle, Soul
    Gem, Berserker''s Shield, Kinetic Cuirass, Titan''s Bane, Avenging Blade, Shield
    Splitter, Void Stone, Spear of the Magus, Void Shield, Doom Orb, Heartseeker,
    The World Stone, The Crusher, Runeforged Hammer, Helm of Radiance, Helm of Darkness,
    The Reaper, Hydra''s Lament, Erosion, Oni Hunter''s Garb, Dreamer''s Idol, Eye
    of Providence, Draconic Scale, Shield of the Phoenix, Midgardian Mail, Tekko-Kagi,
    Magi''s Cloak, Death Metal, Leviathan''s Hide, Mantle Of Discord.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.48
      win: 0.45
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.21
    Transcendence:
      total: 0.39
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.14
    Rod of Tahuti:
      total: 0.54
      efficiency: 0.81
      win: 0.45
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.47
      efficiency: 0.62
      win: 0.45
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Genji's Guard
  - Nimble Ring
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Nimble Ring
  - Golden Blade
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Gluttonous Grimoire, Jotunn''s Revenge,
    Amanita Charm, Nimble Ring, Soul Gem, Kinetic Cuirass, Obsidian Shard, Golden
    Blade, Shield Splitter, Spear of Desolation, Tekko-Kagi, Silverbranch Bow, Toxic
    Blade, Tyrfing, Eros'' Bow, Helm of Radiance, Pharaoh''s Curse, Runeforged Hammer,
    Riptalon, Titan''s Bane, The Reaper, Spear of the Magus, Blood-Bound Book, Helm
    of Darkness, Oni Hunter''s Garb, Lernaean Bow, Hydra''s Lament, Shogun''s Ofuda,
    Erosion, Stone of Binding, Screeching Gargoyle, Midgardian Mail, Shield of the
    Phoenix, Eye of Providence, Bragi''s Harp, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.44
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.5
      efficiency: 0.7
      win: 0.45
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.17
    Nimble Ring:
      total: 0.46
      efficiency: 0.61
      win: 0.45
      pick: 0.0
      fit: 0.33
    Gluttonous Grimoire:
      total: 0.47
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.52
      efficiency: 0.81
      win: 0.45
      pick: 0.0
      fit: 0.21
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Genji's Guard
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shell of Rebuke — magical protection
    swap_item: Shell of Rebuke
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Spear of Desolation, Regrowth Striders, Soul Gem, Kinetic Cuirass,
    Berserker''s Shield, Shield of the Phoenix, Hydra''s Lament, Screeching Gargoyle,
    Shield Splitter, Gluttonous Grimoire, Obsidian Shard, Chronos'' Pendant, Prophetic
    Cloak, Erosion, Helm of Radiance, Arondight, Oni Hunter''s Garb, Runeforged Hammer,
    Titan''s Bane, Gladiator''s Shield, Helm of Darkness, Eye of Providence, Draconic
    Scale, Stone of Binding, Heartwood Charm, Spear of the Magus, Midgardian Mail,
    Chandra''s Grace, Magi''s Cloak, Mantle Of Discord, Leviathan''s Hide, Glorious
    Pridwen, Pendulum Blade, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.61
      win: 0.44
      pick: 0.26
      fit: 0.43
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.43
    Freya's Tears:
      total: 0.5
      efficiency: 0.55
      win: 0.46
      pick: 0.33
      fit: 0.58
    Spear of Desolation:
      total: 0.47
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.48
      efficiency: 0.62
      win: 0.45
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Rod of Tahuti
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic
    Cuirass, Berserker''s Shield, Shield Splitter, Gluttonous Grimoire, Obsidian Shard,
    Spear of Desolation, Soul Gem, Runeforged Hammer, Titan''s Bane, Helm of Radiance,
    Helm of Darkness, Erosion, Spear of the Magus, Hydra''s Lament, Eye of Providence,
    Oni Hunter''s Garb, Draconic Scale, Shield of the Phoenix, Stone of Binding, Midgardian
    Mail, Magi''s Cloak, Screeching Gargoyle, Death Metal, Doom Orb, Heartseeker,
    Shifter''s Shield, Mantle Of Discord, The World Stone, The Crusher, Leviathan''s
    Hide, Jade Scepter, Chronos'' Pendant, Avenging Blade, The Reaper, Wyrmskin Hide.'
  slot_scores:
    Berserker's Shield:
      total: 0.46
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.57
      pick: 0.17
      fit: 0.24
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.53
      efficiency: 0.81
      win: 0.45
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.48
      efficiency: 0.62
      win: 0.45
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  starter: *id001
---
