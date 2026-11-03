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
    win_rate: 0.43
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
      pick_rate: 0.05
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
    pick_rate: 0.3
    win_rate: 0.3
  - name: Bumba's Cudgel
    pick_rate: 0.09
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/chaac/
  last_verified: '2026-11-03'
  god_win_rate: 0.4336283185840708
  god_matches_won: 98
  god_matches_played: 226
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
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield Splitter, Kinetic
    Cuirass, Berserker''s Shield, Gluttonous Grimoire, Spear of Desolation, Obsidian
    Shard, Soul Gem, Runeforged Hammer, Helm of Radiance, Helm of Darkness, Titan''s
    Bane, Hydra''s Lament, Spear of the Magus, Erosion, Oni Hunter''s Garb, Eye of
    Providence, Draconic Scale, Stone of Binding, Death Metal, Shield of the Phoenix,
    Midgardian Mail, The Crusher, Magi''s Cloak, Ancient Signet, Lotus Sickle, Jade
    Scepter, Avenging Blade, Screeching Gargoyle, Doom Orb, Mantle Of Discord, Leviathan''s
    Hide, Heartseeker, The World Stone, Chronos'' Pendant, The Reaper, Shifter''s
    Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.15
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.24
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.17
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
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
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Shield Splitter, Berserker''s Shield,
    Spear of Desolation, Kinetic Cuirass, Gluttonous Grimoire, Obsidian Shard, Hydra''s
    Lament, Soul Gem, Helm of Radiance, Runeforged Hammer, Lotus Sickle, Ancient Signet,
    Titan''s Bane, Helm of Darkness, Spear of the Magus, Oni Hunter''s Garb, Death
    Metal, Doom Orb, The World Stone, Heartseeker, Jade Scepter, Chronos'' Pendant,
    The Crusher, Erosion, Eye of Providence, Shield of the Phoenix, Avenging Blade,
    Stone of Binding, Arondight, Screeching Gargoyle, Draconic Scale, Midgardian Mail,
    Wish-Granting Pearl, Magi''s Cloak, Polynomicon, Triton''s Conch.'
  slot_scores:
    Book of Thoth:
      total: 0.41
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.29
    Transcendence:
      total: 0.42
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.25
    Soul Reaver:
      total: 0.49
      efficiency: 0.42
      win: 0.6
      pick: 0.22
      fit: 0.45
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
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
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Spear of Desolation, Gluttonous
    Grimoire, Soul Gem, Berserker''s Shield, Obsidian Shard, Kinetic Cuirass, Shield
    Splitter, Titan''s Bane, Spear of the Magus, Hydra''s Lament, Helm of Radiance,
    Runeforged Hammer, Helm of Darkness, Lotus Sickle, Shield of the Phoenix, The
    Crusher, Oni Hunter''s Garb, Doom Orb, Screeching Gargoyle, Erosion, The World
    Stone, Eye of Providence, Chronos'' Pendant, Heartseeker, Ancient Signet, Stone
    of Binding, Death Metal, Draconic Scale, The Reaper, Midgardian Mail, Arondight,
    Magi''s Cloak, Dreamer''s Idol, Jade Scepter, Leviathan''s Hide, Avenging Blade.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.14
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.27
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.14
    Freya's Tears:
      total: 0.49
      efficiency: 0.58
      win: 0.46
      pick: 0.33
      fit: 0.41
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
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
    Striders, Shield of the Phoenix, Berserker''s Shield, Kinetic Cuirass, Gluttonous
    Grimoire, The Reaper, Shield Splitter, Ethereal Staff, Spear of Desolation, Obsidian
    Shard, Runeforged Hammer, Yogi''s Necklace, Phoenix Feather, Blood-Bound Book,
    Titan''s Bane, Rod of Asclepius, Helm of Radiance, Sphere of Negation, Hydra''s
    Lament, Spear of the Magus, Oni Hunter''s Garb, Chandra''s Grace, Helm of Darkness,
    Erosion, Eye of Providence, Death Metal, Jade Scepter, Avenging Blade, Draconic
    Scale, Midgardian Mail, The Crusher, Lotus Sickle, Ancient Signet, Doom Orb, Leviathan''s
    Hide.'
  slot_scores:
    Book of Thoth:
      total: 0.4
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.16
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.17
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.22
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.31
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.73
    Soul Gem:
      total: 0.5
      efficiency: 0.53
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Obsidian Shard, Spear of Desolation, Stone of Binding, Screeching Gargoyle, Avenging
    Blade, Soul Gem, Berserker''s Shield, Shield Splitter, Kinetic Cuirass, Titan''s
    Bane, Spear of the Magus, Void Stone, Void Shield, The Crusher, Runeforged Hammer,
    Helm of Radiance, Doom Orb, Heartseeker, The World Stone, Helm of Darkness, Hydra''s
    Lament, The Reaper, Oni Hunter''s Garb, Dreamer''s Idol, Erosion, Eye of Providence,
    Death Metal, Ancient Signet, Draconic Scale, Midgardian Mail, Shield of the Phoenix,
    Tekko-Kagi, Lotus Sickle, Magi''s Cloak, Jade Scepter.'
  slot_scores:
    Book of Thoth:
      total: 0.39
      efficiency: 0.49
      win: 0.45
      pick: 0.0
      fit: 0.13
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.21
    Transcendence:
      total: 0.41
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.14
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.4
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
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
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Gluttonous Grimoire,
    Jotunn''s Revenge, Nimble Ring, Soul Gem, Kinetic Cuirass, Shield Splitter, Golden
    Blade, Obsidian Shard, Spear of Desolation, Tekko-Kagi, Tyrfing, Helm of Radiance,
    Eros'' Bow, Runeforged Hammer, Silverbranch Bow, Toxic Blade, The Reaper, Spear
    of the Magus, Titan''s Bane, Pharaoh''s Curse, Hydra''s Lament, Lernaean Bow,
    Helm of Darkness, Oni Hunter''s Garb, Blood-Bound Book, Ancient Signet, Riptalon,
    Shogun''s Ofuda, Bragi''s Harp, Erosion, Stone of Binding, Lotus Sickle, Eye of
    Providence, Midgardian Mail, Bracer of The Abyss, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.45
    Berserker's Shield:
      total: 0.51
      efficiency: 0.74
      win: 0.45
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.53
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.17
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.47
      efficiency: 0.63
      win: 0.45
      pick: 0.0
      fit: 0.33
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.31
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
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Regrowth Striders — physical protection
    swap_item: Regrowth Striders
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Spear of Desolation, Regrowth Striders, Soul Gem, Berserker''s
    Shield, Kinetic Cuirass, Hydra''s Lament, Shield of the Phoenix, Shield Splitter,
    Screeching Gargoyle, Lotus Sickle, Gluttonous Grimoire, Obsidian Shard, Chronos''
    Pendant, Arondight, Helm of Radiance, Runeforged Hammer, Prophetic Cloak, Oni
    Hunter''s Garb, Erosion, Helm of Darkness, Titan''s Bane, Eye of Providence, Spear
    of the Magus, Draconic Scale, Stone of Binding, Gladiator''s Shield, Midgardian
    Mail, Magi''s Cloak, Heartwood Charm, Mantle Of Discord, Leviathan''s Hide, Ancient
    Signet, Chandra''s Grace, Eye of Erebus, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.49
      efficiency: 0.63
      win: 0.43
      pick: 0.26
      fit: 0.43
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.51
    Genji's Guard:
      total: 0.57
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.43
    Freya's Tears:
      total: 0.51
      efficiency: 0.58
      win: 0.46
      pick: 0.33
      fit: 0.58
    Spear of Desolation:
      total: 0.48
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.51
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
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
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Genji's Guard
  - Shield Splitter
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Shield
    Splitter, Kinetic Cuirass, Berserker''s Shield, Gluttonous Grimoire, Spear of
    Desolation, Obsidian Shard, Soul Gem, Runeforged Hammer, Helm of Radiance, Helm
    of Darkness, Titan''s Bane, Hydra''s Lament, Spear of the Magus, Erosion, Oni
    Hunter''s Garb, Eye of Providence, Draconic Scale, Stone of Binding, Death Metal,
    Shield of the Phoenix, Midgardian Mail, The Crusher, Magi''s Cloak, Ancient Signet,
    Lotus Sickle, Jade Scepter, Avenging Blade, Screeching Gargoyle, Doom Orb, Mantle
    Of Discord, Leviathan''s Hide, Shifter''s Shield, Heartseeker, The World Stone,
    Chronos'' Pendant, The Reaper.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.67
      win: 0.45
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.56
      win: 0.45
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.17
      fit: 0.24
    Shield Splitter:
      total: 0.48
      efficiency: 0.59
      win: 0.45
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.45
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  starter: *id001
---
